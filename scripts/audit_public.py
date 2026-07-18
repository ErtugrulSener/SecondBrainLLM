#!/usr/bin/env python3
"""Prüft veröffentlichte Textdateien auf offensichtliche private Inhalte."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git", "plugins", "cache", "logs", "Drafts"}
SKIP_FILES = {"workspace.json", "audit_public.py"}
TEXT_SUFFIXES = {".md", ".json", ".jsonl", ".py", ".sh", ".txt", ""}
PATTERNS = {
    "privater Schlüssel": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "offensichtliches Geheimnis": re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"][^'\"]{8,}"),
    "lokaler Windows-Benutzerpfad": re.compile(r"(?i)[A-Z]:[\\/]Users[\\/][^\\/\s]+"),
    "lokaler Unix-Benutzerpfad": re.compile(r"/(?:home|Users)/[^/\s]+"),
}


def candidates():
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.name in SKIP_FILES:
            continue
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.is_relative_to(ROOT / "Raw" / "Files"):
            continue
        if path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def main() -> int:
    errors = []
    tracked_state = subprocess.run(
        ["git", "ls-files", "--", ".obsidian/plugins", ".obsidian/cache", ".obsidian/logs"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if tracked_state.returncode == 0:
        errors.extend(
            f"Plugin-/Cache-Zustand von Git erfasst: {path}"
            for path in tracked_state.stdout.splitlines()
            if path
        )
    for path in candidates():
        try:
            text = path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError):
            continue
        for label, pattern in PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{path.relative_to(ROOT).as_posix()}: {label}")
    if errors:
        print("Öffentlicher Audit fehlgeschlagen:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Öffentlicher Audit bestanden.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
