# Workflow-Beispiele

## Quelle aufnehmen

1. Lege bereinigtes Markdown in `Raw/Sources/` ab.
2. Suche mit `python scripts/wiki_tool.py search-catalog --query "Begriff"` nach vorhandenem Wissen.
3. Erstelle kleine, fokussierte Notizen in den passenden `Wiki/`-Ordnern.
4. Trage die Quelle unter `sources` ein und aktualisiere `source_count`.
5. Baue Katalog und Indizes neu und führe alle Prüfungen aus.
6. Aktualisiere das Quellenmanifest mit `source-scan --update --accept-covered`.

## Frage beantworten

1. Beginne bei `Wiki/index.md`.
2. Suche den Katalog.
3. Lies die relevantesten Wiki-Notizen.
4. Öffne Raw-Quellen nur, wenn Details oder eine Quellenprüfung erforderlich sind.
5. Verweise auf Wiki-Notiz und Raw-Quelle.

