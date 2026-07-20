---
tags:
  - "topic"
topics:
  - "Internal Developer Platforms"
status: seed
created: 2026-07-20
updated: 2026-07-20
sources:
  - "Raw/Sources/Notiz zu Internal Developer Portals.md"
  - "Raw/Sources/Korrektur zu Internal Developer Platform.md"
  - "Raw/Sources/What is an Internal Developer Platform.md"
  - "Raw/Sources/Backstage Non-technical FAQ.md"
  - "Raw/Sources/Backstage Strategies for Adopting.md"
  - "Raw/Sources/Harness Pricing.md"
  - "Raw/Sources/Atlassian Compass Pricing and Licensing.md"
  - "Raw/Sources/Port Pricing.md"
  - "Raw/Sources/Cortex Pricing.md"
  - "Raw/Sources/Cortex Internal Developer Portal Strategy.md"
  - "Raw/Sources/OpsLevel Pricing.md"
  - "Raw/Sources/Introducing OpsLevel.md"
source_count: 12
aliases:
  - "IDP"
  - "Internal Developer Platform"
---

# Internal Developer Platforms

IDP steht hier für **Internal Developer Platform**. Eine solche Plattform verbindet Werkzeuge und Technologien zu standardisierten Entwicklungswegen („Golden Paths“) und ermöglicht Self-Service für Entwicklungsteams. Sie wird von einem Plattformteam als internes Produkt betrieben und kontinuierlich anhand des Nutzerfeedbacks weiterentwickelt.

## Abgrenzung zum Internal Developer Portal

Ein Internal Developer Portal ist eine mögliche Benutzeroberfläche auf einer Internal Developer Platform. Die Plattform umfasst dagegen die gesamte zugrunde liegende Plattformschicht und kann zusätzlich über CLI, API oder deklarative Spezifikationen zugänglich sein.

Die Begriffe werden am Markt nicht einheitlich verwendet. Mehrere Anbieter kürzen auch „Internal Developer Portal“ mit IDP ab. Bei Produktvergleichen muss deshalb geprüft werden, ob ein Angebot nur Portal und Softwarekatalog oder auch Orchestrierung, Self-Service und weitere Plattformfähigkeiten umfasst.

## Verbreitete Lösungen

Eine belastbare, herstellerunabhängige Rangliste nach aktiven Installationen oder Nutzern liegt in den geprüften Quellen nicht vor. Die folgende Auswahl ist daher keine Nutzungsrangliste, sondern umfasst etablierte und häufig evaluierte Lösungen. Preisstand: 2026-07-20.

| Lösung | Einordnung und Kosten | Vorteile | Nachteile |
| --- | --- | --- | --- |
| **Backstage** | Open-Source-Framework für Developer Portals; Apache 2.0 und ohne Lizenzkosten. Betrieb, Entwicklung und Wartung verursachen interne Kosten. | Sehr flexibel, großes Plugin-Modell, selbst betreibbar und ohne Bindung an einen SaaS-Anbieter. | Kein fertiges Produkt: Eine zentrale Mannschaft muss Anpassung, Infrastruktur, CI/CD, Support und Bereitschaft übernehmen. |
| **Harness Internal Developer Portal** | Kommerzielles, von Backstage angetriebenes Portal. Preise auf Anfrage; Harness nennt eine Mindestabnahme von 20 Developer-Lizenzen. | Backstage-Basis mit Softwarekatalog, Self-Service, Scorecards und enger Einbindung in die Harness-Plattform. | Kein transparenter Listenpreis, Mindestabnahme und stärkster Nutzen innerhalb des Harness-Ökosystems. |
| **Atlassian Compass** | Cloud-basiertes kommerzielles Produkt. Free-Tarif mit bis zu drei Full Users und unbegrenzt vielen Basic Users; größere Funktionsumfänge sind kostenpflichtig. | Schnell einsetzbar, Softwarekatalog und Scorecards sowie naheliegende Integration mit Atlassian-Produkten. | Nur als Cloud-Produkt verfügbar; der Free-Tarif begrenzt voll berechtigte Nutzer stark und die Bindung an das Atlassian-Ökosystem ist hoch. |
| **Port** | Kommerzielles SaaS-Portal. Free-Tarif bis 15 Seats; Basic ab 30 US-Dollar und Standard ab 40 US-Dollar pro Seat und Monat. | Flexibles Datenmodell, Katalog, Aktionen, Workflows und Scorecards; relativ großzügiger Einstiegstarif. | Sitzbasierte Kosten steigen mit dem Team; SSO und weitere Sicherheitsfunktionen beginnen erst in höheren Tarifen. |
| **Cortex** | Kommerzielles Portal mit individuellem Angebot; keine öffentliche Preisliste. | Vorgefertigte Katalogmodelle, Scorecards, Workflows und Engineering-Intelligence reduzieren den Startaufwand. | Kosten sind ohne Vertriebsgespräch nicht vergleichbar; der breite Funktionsumfang kann für einen einfachen Katalog überdimensioniert sein. |
| **OpsLevel** | Kommerzielles Portal mit nutzerbasierter, individuell angebotener Preisgestaltung. | Automatische Katalogerkennung, Scorecards und Checks sowie Self-Service-Aktionen sind als integriertes Produkt verfügbar. | Kein öffentlicher Listenpreis und kein frei zugänglicher Self-Service-Tarif; Evaluierung läuft über Demo beziehungsweise Anbietertermin. |

## Erste Einordnung

- **Maximale Kontrolle und Anpassbarkeit:** Backstage, wenn ein dauerhaft verantwortliches Plattformteam vorhanden ist.
- **Backstage ohne vollständigen Eigenbetrieb:** Harness, besonders bei bereits starker Nutzung der Harness-Plattform.
- **Atlassian-zentrierte Organisation:** Compass.
- **Schneller SaaS-Einstieg mit transparentem Free-Tarif:** Port.
- **Starker Fokus auf Standards und Engineering Excellence:** Cortex oder OpsLevel.

Vor einer Auswahl sollten mindestens Toolchain-Integrationen, Self-Service-Tiefe, Datenhaltung, Berechtigungsmodell, Betriebsaufwand und Gesamtkosten mit einem eigenen Proof of Concept geprüft werden.
