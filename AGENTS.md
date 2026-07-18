# LLM Wiki Agent Rules

## Schichten

- Behandle `Raw/Sources/` als unverändertes Quellenmaterial, nicht als kompiliertes Wissen.
- Schreibe wiederverwendbares Wissen ausschließlich unter `Wiki/`.
- Verknüpfe jede kompilierte Notiz über `sources` mit mindestens einer existierenden Quelle unter `Raw/Sources/`.
- Suche zuerst in `Wiki/catalog.jsonl`, bevor du breite Raw-Kontexte öffnest.

## Arbeitsablauf

1. Suche im Katalog nach bereits kompiliertem Wissen.
2. Öffne nur relevante Wiki-Notizen und anschließend bei Bedarf deren Quellen.
3. Erstelle oder aktualisiere fokussierte Wiki-Notizen gemäß `Schema/frontmatter-schema.md`.
4. Halte `source_count` synchron mit `sources`.
5. Führe vor Commits `build`, `lint` und die Quellenprüfungen aus.

## Integrität

- Erfinde keine Zitate, Quellen oder unbelegten Behauptungen.
- Bewahre die Rückverfolgbarkeit jeder Aussage zu den angegebenen Raw-Quellen.
- Nutze nur die in `Schema/frontmatter-schema.md` erlaubten Typ-Tags.
- Ändere Raw-Quellen nicht stillschweigend beim Kompilieren.

## Wartungsprüfung

```bash
python scripts/wiki_tool.py doctor
python scripts/wiki_tool.py build
python scripts/wiki_tool.py lint
python scripts/wiki_tool.py source-lint
python scripts/audit_public.py
```

