---
tags:
  - "concept"
topics:
  - "Retrieval-Augmented Generation"
status: seed
created: 2026-07-18
updated: 2026-07-18
sources:
  - "Raw/Sources/Retrieval Augmented Generation (RAG) Was wirklich wichtig ist  INSIDE AI 21.md"
source_count: 1
aliases:
  - "RAG"
---

# RAG-Grundprinzip

Retrieval-Augmented Generation nimmt Informationen aus externen Quellen und stellt sie einem Sprachmodell innerhalb seines Kontextfensters zur Verfügung. Dadurch kann das Modell Informationen verwenden, die nicht in seinen Trainingsdaten enthalten waren oder für eine konkrete Anfrage gezielt ausgewählt werden müssen.

Bei kleinen Quellen kann bereits das vollständige Bereitstellen eines Textes genügen. Bei großen Wissensbeständen ist dagegen ein Retrieval-Mechanismus nötig, der nur relevante Ausschnitte auswählt.

RAG ist nicht mit Embeddings gleichzusetzen. Embeddings sind lediglich eine mögliche Technik zur Identifikation relevanter Informationen. Auch Websuche oder der Zugriff auf Werkzeuge über Schnittstellen wie MCP erfüllen eine Retrieval-Funktion.

Siehe auch [[Wiki/Topics/retrieval-augmented-generation|Retrieval-Augmented Generation]].
