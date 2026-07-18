# Befehlsreferenz

Alle Befehle werden vom Vault-Stamm ausgeführt.

| Befehl | Wirkung |
| --- | --- |
| `python scripts/wiki_tool.py doctor` | Prüft Umgebung, Ordner, Artefakte und Notizzahlen ohne Änderungen. |
| `python scripts/wiki_tool.py build` | Erzeugt Katalog sowie Haupt- und Ordnerindizes neu. |
| `python scripts/wiki_tool.py lint` | Prüft kompilierte Wiki-Notizen und Quellenverweise. |
| `python scripts/wiki_tool.py source-scan` | Listet Raw-Quellen und ihren Abdeckungszustand. |
| `python scripts/wiki_tool.py source-scan --update --accept-covered` | Schreibt das Manifest und akzeptiert belegte Abdeckung. |
| `python scripts/wiki_tool.py source-lint` | Prüft Quellen-Frontmatter und Verarbeitungszustand. |
| `python scripts/wiki_tool.py source-delta` | Listet Quellen, die im Manifest fehlen. |
| `python scripts/wiki_tool.py source-coverage` | Zeigt Wiki-Abdeckung je Raw-Quelle. |
| `python scripts/wiki_tool.py search-catalog --query "text"` | Durchsucht den kompilierten Katalog. |
| `python scripts/wiki_tool.py log --title "Titel" --details "Details"` | Ergänzt `Wiki/log.md`. |

Der öffentliche Audit läuft mit `python scripts/audit_public.py`. Der Hook wird mit `sh scripts/install_hooks.sh` aktiviert.
