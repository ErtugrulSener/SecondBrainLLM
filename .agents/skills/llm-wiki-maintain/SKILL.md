---
name: llm-wiki-maintain
description: Baut Katalog, Indizes und Quellenmanifest reproduzierbar neu auf.
---

# LLM Wiki Maintain

1. Führe `doctor` aus.
2. Erzeuge mit `build` Katalog und Indizes neu.
3. Aktualisiere nach Ingests das Manifest mit `source-scan --update --accept-covered`.
4. Führe `lint`, `source-lint` und den öffentlichen Audit aus.
5. Committe generierte Artefakte zusammen mit der auslösenden Wissensänderung.

