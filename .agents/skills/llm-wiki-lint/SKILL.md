---
name: llm-wiki-lint
description: Prüft Wiki-Frontmatter, Quellenlinks, Zählwerte und Quellenzustand.
---

# LLM Wiki Lint

Führe der Reihe nach aus:

```bash
python scripts/wiki_tool.py build
python scripts/wiki_tool.py lint
python scripts/wiki_tool.py source-lint
python scripts/audit_public.py
```

Behebe nur konkrete Befunde. Erfinde keine Quellen, um eine Prüfung zu erfüllen.

