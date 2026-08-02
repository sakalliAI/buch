#!/usr/bin/env python3
"""
Konsolidiert die Quellennummern.

Beim parallelen Ausbau haben mehrere Kapitel-Bearbeitungen unabhängig
voneinander „die nächste freie Nummer ab 119" vergeben. Dadurch sind
119–127 mehrfach belegt, und Kapitel 1 ist auf den Bereich 200–218
ausgewichen.

Dieses Skript vergibt ab 119 eindeutige, kapitelweise gruppierte Nummern
und zieht die Verweise („→ QUELLEN.md Nr. N") in den Kapiteldateien mit.
Es ist einmalig gedacht und dokumentiert den Eingriff.
"""

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
QUELLEN = ROOT / "QUELLEN.md"
KAP = ROOT / "02_kapitel"

# Zeilenbereiche (1-basiert, inklusiv) der Nachtragsblöcke und ihr Kapitel.
# Ermittelt durch Auszählen der aktuellen QUELLEN.md.
BLOECKE = [
    ("01", 174, 192),   # 200–218  Buchdruck
    ("02", 194, 196),   # 120–122  Elektrizität
    ("03", 199, 207),   # 119–127  Telefon/Auto/Kaffee/Radio/TV
    ("04", 193, 193),   # 119      Behavioral Scientist
    ("05", 159, 162),   # 128–131  Rechner/Internet
    ("07", 197, 198),   # 123–124  Bloom, Verwertungsgesellschaften
    ("08", 167, 168),   # 119–120  Rechenbeispiel, Northpointe
    ("09", 153, 157),   # 119–123  AlphaFold-Umfeld
    ("10", 158, 158),   # 119      Turing 1950
]

KAPITELDATEI = {p.name[:2]: p for p in KAP.glob("*.md")}

TITEL = {
    "01": "Kapitel 1 — Die Angst ist älter als die Maschine",
    "02": "Kapitel 2 — Tempo, Strom und der Tod des Abendlands",
    "03": 'Kapitel 3 — „Das Telefon wird die Familie zerstören"',
    "04": "Kapitel 4 — Warum wir nie aus der Geschichte lernen",
    "05": "Kapitel 5 — Der Taschenrechner-Moment",
    "07": "Kapitel 7 — Werden wir dümmer?",
    "08": "Kapitel 8 — Die echten Risiken",
    "09": "Kapitel 9 — Die Stimmen der Propheten",
    "10": "Kapitel 10 — Was vom Menschen bleibt",
}


def main():
    zeilen = QUELLEN.read_text(encoding="utf-8").split("\n")

    # 1) Einträge einsammeln und neue Nummern vergeben
    naechste = 119
    neue_bloecke = []          # (kap, [(alt, neu, resttext), ...])
    verbrauchte_zeilen = set()

    for kap, von, bis in BLOECKE:
        eintraege = []
        for ln in range(von, bis + 1):
            zeile = zeilen[ln - 1]
            m = re.match(r"^(\d+)\.\s+(.*)$", zeile)
            if not m:
                raise SystemExit(f"Zeile {ln} ist kein Quelleneintrag: {zeile[:60]!r}")
            alt, rest = int(m.group(1)), m.group(2)
            eintraege.append((alt, naechste, rest))
            naechste += 1
            verbrauchte_zeilen.add(ln)
        neue_bloecke.append((kap, eintraege))

    # 2) Kapitelverweise umschreiben — pro Kapitel eigene Zuordnung,
    #    absteigend ersetzen, damit sich Nummern nicht überschreiben.
    for kap, eintraege in neue_bloecke:
        pfad = KAPITELDATEI[kap]
        text = pfad.read_text(encoding="utf-8")
        for alt, neu, _ in sorted(eintraege, key=lambda e: -e[0]):
            text = re.sub(rf"(QUELLEN\.md Nr\.\s*){alt}\b", rf"\g<1>{neu}", text)
        pfad.write_text(text, encoding="utf-8")
        print(f"Kapitel {kap}: {len(eintraege)} Verweise umgestellt "
              f"({eintraege[0][0]}… → {eintraege[0][1]}…)")

    # 3) QUELLEN.md neu schreiben: alte Blockzeilen raus, sauberer Anhang rein
    kopf_ende = 162           # letzte Zeile vor dem ersten Block-Header
    behalten = [z for i, z in enumerate(zeilen[:kopf_ende], start=1)
                if i not in verbrauchte_zeilen]

    raus = list(behalten)
    raus.append("")
    raus.append("## Nachträge aus Phase 5 (Ausbau)")
    raus.append("")
    raus.append("*Beim parallelen Ausbau vergaben mehrere Kapitelbearbeitungen "
                "unabhängig voneinander Nummern ab 119; Kapitel 1 wich auf 200+ "
                "aus. Die Nummern sind hier einmalig konsolidiert und die "
                "Verweise in den Kapiteln wurden mitgezogen "
                "(`04_produktion/konsolidiere_quellen.py`).*")
    raus.append("")
    for kap, eintraege in neue_bloecke:
        raus.append(f"### {TITEL[kap]}")
        raus.append("")
        for _, neu, rest in eintraege:
            raus.append(f"{neu}. {rest}")
        raus.append("")

    QUELLEN.write_text("\n".join(raus).rstrip() + "\n", encoding="utf-8")
    print(f"\nQUELLEN.md neu geschrieben. Höchste Nummer: {naechste - 1}")


if __name__ == "__main__":
    main()
