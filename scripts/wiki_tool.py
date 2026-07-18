#!/usr/bin/env python3
"""Deterministische Wartungswerkzeuge für das LLM Wiki."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "Wiki"
RAW_SOURCES = ROOT / "Raw" / "Sources"
SCHEMA = ROOT / "Schema"
CATALOG = WIKI / "catalog.jsonl"
MANIFEST = SCHEMA / "source-manifest.jsonl"
WIKI_FOLDERS = ("Topics", "Concepts", "Entities", "Projects", "Logs")
ALLOWED_TAGS = {"topic", "concept", "entity", "project", "log"}
REQUIRED_SOURCE_FIELDS = {"Title", "Reference", "Created", "Processed", "tags"}


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def scalar(value: str):
    value = value.strip()
    if not value:
        return ""
    if value == "[]":
        return []
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        return [] if not inner else [scalar(part) for part in inner.split(",")]
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def read_note(path: Path) -> tuple[dict, str, list[str]]:
    errors: list[str] = []
    try:
        text = path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as error:
        return {}, "", [f"Datei nicht lesbar: {error}"]
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text, ["Frontmatter fehlt"]
    try:
        end = next(index for index in range(1, len(lines)) if lines[index].strip() == "---")
    except StopIteration:
        return {}, text, ["Frontmatter ist nicht geschlossen"]

    data: dict = {}
    current_key: str | None = None
    for line_number, line in enumerate(lines[1:end], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        list_match = re.match(r"^\s+-\s+(.+?)\s*$", line)
        if list_match and current_key:
            if not isinstance(data.get(current_key), list):
                data[current_key] = []
            data[current_key].append(scalar(list_match.group(1)))
            continue
        key_match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$", line)
        if not key_match:
            errors.append(f"Ungültiges Frontmatter in Zeile {line_number}")
            continue
        current_key, raw_value = key_match.groups()
        data[current_key] = [] if raw_value == "" else scalar(raw_value)
    return data, "\n".join(lines[end + 1 :]), errors


def note_title(path: Path, metadata: dict, body: str) -> str:
    if metadata.get("Title"):
        return str(metadata["Title"])
    heading = re.search(r"^#\s+(.+?)\s*$", body, re.MULTILINE)
    return heading.group(1) if heading else path.stem.replace("-", " ").title()


def compiled_notes() -> list[Path]:
    notes: list[Path] = []
    for folder in WIKI_FOLDERS:
        directory = WIKI / folder
        if directory.exists():
            notes.extend(path for path in directory.glob("*.md") if path.name != "index.md")
    return sorted(notes, key=lambda path: relative(path).lower())


def raw_notes() -> list[Path]:
    return sorted(RAW_SOURCES.glob("*.md"), key=lambda path: relative(path).lower())


def source_values(metadata: dict) -> list[str]:
    value = metadata.get("sources", [])
    return [str(item).replace("\\", "/") for item in value] if isinstance(value, list) else []


def catalog_records() -> list[dict]:
    records = []
    for path in compiled_notes():
        metadata, body, _ = read_note(path)
        tags = metadata.get("tags", [])
        tag = tags[0] if isinstance(tags, list) and tags else ""
        topics = metadata.get("topics", [])
        records.append(
            {
                "path": relative(path),
                "title": note_title(path, metadata, body),
                "tag": tag,
                "topics": topics if isinstance(topics, list) else [],
                "sources": source_values(metadata),
                "updated": str(metadata.get("updated", "")),
            }
        )
    return records


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records)
    path.write_text(content, encoding="utf-8", newline="\n")


def command_build(_args: argparse.Namespace) -> int:
    records = catalog_records()
    write_jsonl(CATALOG, records)
    by_folder = {folder: [] for folder in WIKI_FOLDERS}
    for record in records:
        by_folder[Path(record["path"]).parent.name].append(record)

    root_lines = ["# Wiki-Index", "", f"Kompilierte Notizen: {len(records)}", ""]
    for folder in WIKI_FOLDERS:
        root_lines.append(f"- [[Wiki/{folder}/index|{folder}]] ({len(by_folder[folder])})")
        folder_lines = [f"# {folder}", ""]
        if by_folder[folder]:
            for record in by_folder[folder]:
                target = record["path"][:-3]
                folder_lines.append(f"- [[{target}|{record['title']}]]")
        else:
            folder_lines.append("Noch keine Notizen.")
        (WIKI / folder / "index.md").write_text("\n".join(folder_lines) + "\n", encoding="utf-8", newline="\n")
    WIKI.joinpath("index.md").write_text("\n".join(root_lines) + "\n", encoding="utf-8", newline="\n")
    print(f"Build abgeschlossen: {len(records)} Notiz(en).")
    return 0


def command_lint(_args: argparse.Namespace) -> int:
    errors: list[str] = []
    for path in compiled_notes():
        metadata, _body, parse_errors = read_note(path)
        prefix = relative(path)
        errors.extend(f"{prefix}: {error}" for error in parse_errors)
        tags = metadata.get("tags")
        valid_tags = [tag for tag in tags if tag in ALLOWED_TAGS] if isinstance(tags, list) else []
        if len(valid_tags) != 1 or len(tags or []) != 1:
            errors.append(f"{prefix}: genau ein erlaubtes Typ-Tag erforderlich")
        for field in ("topics", "status", "created", "updated", "sources", "source_count", "aliases"):
            if field not in metadata:
                errors.append(f"{prefix}: Pflichtfeld '{field}' fehlt")
        sources = source_values(metadata)
        if metadata.get("source_count") != len(sources):
            errors.append(f"{prefix}: source_count stimmt nicht mit sources überein")
        if not sources:
            errors.append(f"{prefix}: mindestens eine Raw-Quelle erforderlich")
        for source in sources:
            source_path = ROOT / source
            try:
                is_raw = source_path.resolve().is_relative_to(RAW_SOURCES.resolve())
            except OSError:
                is_raw = False
            if not is_raw or not source_path.is_file():
                errors.append(f"{prefix}: ungültige oder fehlende Quelle '{source}'")
    if errors:
        print("Wiki-Lint fehlgeschlagen:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Wiki-Lint bestanden: {len(compiled_notes())} Notiz(en).")
    return 0


def coverage_map() -> dict[str, list[str]]:
    coverage: dict[str, list[str]] = {}
    for path in compiled_notes():
        metadata, _body, _errors = read_note(path)
        for source in source_values(metadata):
            coverage.setdefault(source, []).append(relative(path))
    return {key: sorted(value) for key, value in sorted(coverage.items())}


def source_records(accept_covered: bool = False) -> list[dict]:
    coverage = coverage_map()
    records = []
    for path in raw_notes():
        metadata, body, _errors = read_note(path)
        source_path = relative(path)
        covered_by = coverage.get(source_path, [])
        processed = bool(metadata.get("Processed"))
        if accept_covered and covered_by:
            processed = True
        records.append(
            {
                "path": source_path,
                "title": note_title(path, metadata, body),
                "processed": processed,
                "covered_by": covered_by,
                "updated": date.today().isoformat(),
            }
        )
    return records


def command_source_scan(args: argparse.Namespace) -> int:
    records = source_records(args.accept_covered)
    for record in records:
        state = "abgedeckt" if record["covered_by"] else "offen"
        print(f"{record['path']}: {state}")
    if args.update:
        write_jsonl(MANIFEST, records)
        print(f"Manifest aktualisiert: {len(records)} Quelle(n).")
    return 0


def command_source_lint(_args: argparse.Namespace) -> int:
    errors: list[str] = []
    coverage = coverage_map()
    for path in raw_notes():
        metadata, _body, parse_errors = read_note(path)
        prefix = relative(path)
        errors.extend(f"{prefix}: {error}" for error in parse_errors)
        for field in REQUIRED_SOURCE_FIELDS:
            if field not in metadata or metadata[field] in ("", None, []):
                errors.append(f"{prefix}: Pflichtfeld '{field}' fehlt oder ist leer")
        tags = metadata.get("tags", [])
        if not isinstance(tags, list) or "source" not in tags:
            errors.append(f"{prefix}: Tag 'source' fehlt")
        if metadata.get("Processed") is True and not coverage.get(prefix):
            errors.append(f"{prefix}: verarbeitet, aber ohne Wiki-Abdeckung")
    if MANIFEST.exists():
        manifest_paths = set()
        for line_number, line in enumerate(MANIFEST.read_text(encoding="utf-8-sig").splitlines(), start=1):
            try:
                record = json.loads(line)
                manifest_paths.add(record["path"])
                if record.get("processed") and not record.get("covered_by"):
                    errors.append(f"Manifest Zeile {line_number}: verarbeitet, aber nicht abgedeckt")
            except (json.JSONDecodeError, KeyError):
                errors.append(f"Manifest Zeile {line_number}: ungültiger Datensatz")
        missing = {relative(path) for path in raw_notes()} - manifest_paths
        errors.extend(f"Manifest: Quelle fehlt '{path}'" for path in sorted(missing))
    if errors:
        print("Source-Lint fehlgeschlagen:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Source-Lint bestanden: {len(raw_notes())} Quelle(n).")
    return 0


def command_source_delta(_args: argparse.Namespace) -> int:
    known = set()
    if MANIFEST.exists():
        for line in MANIFEST.read_text(encoding="utf-8-sig").splitlines():
            if line.strip():
                try:
                    known.add(json.loads(line)["path"])
                except (json.JSONDecodeError, KeyError):
                    pass
    delta = [relative(path) for path in raw_notes() if relative(path) not in known]
    for path in delta:
        print(path)
    print(f"Nicht im Manifest: {len(delta)}")
    return 0


def command_source_coverage(_args: argparse.Namespace) -> int:
    coverage = coverage_map()
    for path in raw_notes():
        source = relative(path)
        targets = coverage.get(source, [])
        print(f"{source}: {', '.join(targets) if targets else 'nicht abgedeckt'}")
    return 0


def command_search_catalog(args: argparse.Namespace) -> int:
    if not CATALOG.exists():
        print("Katalog fehlt. Zuerst 'build' ausführen.", file=sys.stderr)
        return 1
    terms = args.query.casefold().split()
    matches = []
    for line in CATALOG.read_text(encoding="utf-8-sig").splitlines():
        record = json.loads(line)
        haystack = json.dumps(record, ensure_ascii=False).casefold()
        if all(term in haystack for term in terms):
            matches.append(record)
    for record in matches:
        print(f"{record['title']}\t{record['path']}")
    print(f"Treffer: {len(matches)}")
    return 0


def command_log(args: argparse.Namespace) -> int:
    path = WIKI / "log.md"
    timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
    existing = path.read_text(encoding="utf-8-sig") if path.exists() else "# Wiki-Log\n"
    entry = f"\n## {timestamp} — {args.title}\n\n{args.details}\n"
    path.write_text(existing.rstrip() + "\n" + entry, encoding="utf-8", newline="\n")
    print(f"Logeintrag ergänzt: {args.title}")
    return 0


def command_doctor(_args: argparse.Namespace) -> int:
    errors: list[str] = []
    required = [RAW_SOURCES, WIKI, SCHEMA, ROOT / "_templates", ROOT / ".agents" / "skills", ROOT / "scripts"]
    for path in required:
        if not path.is_dir():
            errors.append(f"Ordner fehlt: {relative(path)}")
    if sys.version_info < (3, 9):
        errors.append("Python 3.9 oder neuer ist erforderlich")
    for path in (CATALOG, MANIFEST):
        if not path.is_file():
            errors.append(f"Artefakt fehlt: {relative(path)}")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Raw-Quellen: {len(raw_notes())}")
    print(f"Wiki-Notizen: {len(compiled_notes())}")
    if errors:
        print("Doctor fehlgeschlagen:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Doctor bestanden.")
    return 0


def parser() -> argparse.ArgumentParser:
    main = argparse.ArgumentParser(description=__doc__)
    commands = main.add_subparsers(dest="command", required=True)
    for name, handler in (
        ("doctor", command_doctor),
        ("build", command_build),
        ("lint", command_lint),
        ("source-lint", command_source_lint),
        ("source-delta", command_source_delta),
        ("source-coverage", command_source_coverage),
    ):
        command = commands.add_parser(name)
        command.set_defaults(handler=handler)
    scan = commands.add_parser("source-scan")
    scan.add_argument("--update", action="store_true")
    scan.add_argument("--accept-covered", action="store_true")
    scan.set_defaults(handler=command_source_scan)
    search = commands.add_parser("search-catalog")
    search.add_argument("--query", required=True)
    search.set_defaults(handler=command_search_catalog)
    log = commands.add_parser("log")
    log.add_argument("--title", required=True)
    log.add_argument("--details", required=True)
    log.set_defaults(handler=command_log)
    return main


def main() -> int:
    args = parser().parse_args()
    return args.handler(args)


if __name__ == "__main__":
    raise SystemExit(main())
