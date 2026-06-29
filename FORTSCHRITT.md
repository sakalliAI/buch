# FORTSCHRITT — Sachbuch „Vertrauen statt Angst vor KI"

Autor/Herausgeber: Emre Sakalli
Stand: 2026-06-28

## Phasen-Status

| Phase | Beschreibung | Status | Gate |
|-------|--------------|--------|------|
| 0 | Projektstruktur anlegen | ✅ erledigt | — |
| 1 | Tiefenrecherche Inhalt | ✅ freigegeben | 🚦 GATE 1 ✅ |
| 2 | Markt- & Formatrecherche | ✅ (Zielmarke als Arbeitsbasis übernommen) | 🚦 GATE 2 ✅* |
| 3 | Konzept, Titel & Struktur | ✅ fertig — wartet auf Freigabe | 🚦 GATE 3 (offen) |
| 4 | Schreiben (Kapitel für Kapitel) | ⬜ offen | — |
| 5 | Quellenapparat & Humanisierungs-Pass | ⬜ offen | — |
| 6 | Word-Dokument bauen | ⬜ offen | — |
| 7 | KDP-Paket + Verlags-Exposé | ⬜ offen | 🚦 GATE 4 |

## Phase 1 — Recherche-Stränge

| Strang | Inhalt | Datei | Status |
|--------|--------|-------|--------|
| a1 | Buchdruck, Eisenbahn, Elektrizität | 00_recherche/a1_buchdruck_eisenbahn_elektrizitaet.md | ✅ |
| a2 | Telefon, Auto, Kaffee, Radio, TV | 00_recherche/a2_telefon_auto_kaffee_radio_tv.md | ✅ |
| a3 | Rechner, Computer, Walkman, Internet, Smartphone, Kamera | 00_recherche/a3_rechner_computer_internet_smartphone.md | ✅ |
| a4 | Theorie: Luddismus, Moral Panic, Technikgeschichte | 00_recherche/a4_theorie_luddismus_moralpanik.md | ✅ |
| b1 | KI heute: Arbeitsmarkt, Bildung, Kreativität | 00_recherche/b1_ki_arbeit_bildung_kreativitaet.md | ✅ |
| b2 | KI heute: Sicherheit, Bias, Datenschutz, Energie | 00_recherche/b2_ki_sicherheit_bias_datenschutz_energie.md | ✅ |
| c1 | Zukunft: Hot Takes, Szenarien | 00_recherche/c1_zukunft_hottakes.md | ✅ |

**GATE-1-Deliverables:** `00_recherche/RECHERCHE_ZUSAMMENFASSUNG.md` (max. 2 S.) · `QUELLEN.md` (110 Quellen, konsolidiert). → freigegeben.

## Phase 2 — Markt- & Formatrecherche

| Strang | Inhalt | Datei | Status |
|--------|--------|-------|--------|
| p2-1 | Vergleichstitel + Umfangs-Ableitung | 01_konzept/p2_vergleichstitel.md | ✅ |
| p2-2 | Amazon-KDP-Formatvorgaben | 01_konzept/p2_kdp_format.md | ✅ |
| p2-3 | Deutsches Sachbuch-Exposé | 01_konzept/p2_expose_konventionen.md | ✅ |

**GATE-2-Deliverable:** `01_konzept/GATE2_MARKT_UMFANG.md` — Empfehlung **288 S. / ~80–85k Wörter / 12 Kapitel in 3 Teilen** + Vergleichstitel-Tabelle (16). *(\*als Arbeitsbasis übernommen, an GATE 3 noch änderbar.)*

## Phase 3 — Konzept, Titel & Struktur

**GATE-3-Deliverable:** `01_konzept/GATE3_KONZEPT_STRUKTUR.md` — 12 Titel-Kandidaten (Empfehlung „Erst kam die Angst, dann kam der Alltag"), Stimme/Ansprache (Empfehlung „Du"), vollständiges Inhaltsverzeichnis (3 Teile, 12 Kapitel + Einl./Schluss, ~82.500 W), Dramaturgie. → Warten auf: Titel + Ansprache + Struktur-Freigabe + `{{AUTOR_BIO}}`.

## Notizen
- Repo ist dem Buchprojekt gewidmet; Ordnerstruktur liegt im Repo-Root (statt in einem Unterordner `buch-ki-angst/`), um Verschachtelung zu vermeiden.
- Abrufdatum aller Quellen: 2026-06-28 (sofern nicht anders vermerkt).
- **Infrastruktur-Blocker (zu klären):** (1) Remote-Push blockiert — `git push` → 403 (Egress-Policy) UND GitHub-API-Schreiben → 403 „Resource not accessible by integration". Alle Arbeit ist lokal committet. (2) WebFetch für externe Hosts blockiert → Recherche via WebSearch-Triangulation; ▲/[PRÜFEN]-Belege vor Druck final verifizieren.
