# Frontmatter-Schema

## Raw-Quellen

Erforderliche Eigenschaften:

- `Title`: nicht leerer Titel
- `Author`: Urheber, sofern bekannt
- `Reference`: Herkunft oder stabile Referenz
- `ContentType`: Liste der Inhaltsformate
- `Created`: Datum im Format `YYYY-MM-DD`
- `Processed`: boolescher Wert
- `tags`: enthält `source`

## Kompilierte Wiki-Notizen

Erforderliche Eigenschaften:

- `tags`: genau ein Typ aus `topic`, `concept`, `entity`, `project`, `log`
- `topics`: Liste zugehöriger Themen
- `status`: Reifegrad, anfänglich `seed`
- `created`: Erstellungsdatum im Format `YYYY-MM-DD`
- `updated`: Änderungsdatum im Format `YYYY-MM-DD`
- `sources`: Liste existierender Pfade unter `Raw/Sources/`
- `source_count`: Anzahl der Einträge in `sources`
- `aliases`: Liste alternativer Namen

Die Pfade in `sources` werden relativ zum Vault-Stamm angegeben, etwa `Raw/Sources/example.md`.

