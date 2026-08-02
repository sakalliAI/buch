#!/usr/bin/env python3
"""
Baut aus den Markdown-Kapiteln das satzfertige Word-Manuskript.

Zielformat: Amazon KDP Taschenbuch, Trim 6 × 9" (15,24 × 22,86 cm),
Schwarz auf cremefarbenem Papier, gespiegelte Ränder mit Bundsteg.

Aufruf:  python3 04_produktion/build_docx.py
Ergebnis: 04_produktion/Erst_kam_die_Angst_Manuskript.docx
"""

import re
import pathlib

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt

ROOT = pathlib.Path(__file__).resolve().parent.parent
KAP = ROOT / "02_kapitel"
OUT = ROOT / "04_produktion" / "Erst_kam_die_Angst_Manuskript.docx"

TITEL = "Erst kam die Angst, dann kam der Alltag"
UNTERTITEL = ("Was Buchdruck, Dampflok und Smartphone über unsere Furcht "
              "vor künstlicher Intelligenz verraten")
AUTOR = "Emre Sakalli"

# Trim 6 × 9". Bundsteg 0,625" (15,88 mm) für 301–500 Seiten — bei finaler
# Seitenzahl gegen die KDP-Tabelle prüfen (siehe 01_konzept/p2_kdp_format.md).
SEITE_B, SEITE_H = Cm(15.24), Cm(22.86)
RAND_OBEN, RAND_UNTEN = Cm(1.9), Cm(1.9)
RAND_INNEN, RAND_AUSSEN = Cm(1.7), Cm(1.5)
BUNDSTEG = Cm(1.59)

SCHRIFT = "Georgia"          # Serifenschrift, gut lesbar im Druck
SCHRIFT_GRAD = Pt(10.5)
ZEILENABSTAND = Pt(15)

# Teil-Zuordnung: Kapitelnummer -> Teilüberschrift
TEILE = {
    1: ("TEIL I", "Das Muster: Warum wir uns immer fürchten"),
    5: ("TEIL II", "Die ehrliche Bilanz: Was KI wirklich kann (und kostet)"),
    9: ("TEIL III", "Vom Fürchten zum Vertrauen: Wie wir mit KI leben"),
}


# ---------------------------------------------------------------- Hilfsmittel

def seitenzahl_feld(paragraph):
    """Fügt ein automatisches Seitenzahl-Feld ein."""
    run = paragraph.add_run()
    for instr, typ in (("begin", "fldCharType"), (None, None), ("end", "fldCharType")):
        if instr == "begin":
            el = OxmlElement("w:fldChar"); el.set(qn("w:fldCharType"), "begin")
        elif instr == "end":
            el = OxmlElement("w:fldChar"); el.set(qn("w:fldCharType"), "end")
        else:
            el = OxmlElement("w:instrText"); el.set(qn("xml:space"), "preserve")
            el.text = "PAGE"
        run._r.append(el)


def setze_inline(paragraph, text, basis_kursiv=False):
    """Wandelt **fett**, *kursiv* und „Anführungen" in Word-Runs."""
    teile = re.split(r"(\*\*[^*]+\*\*|\*[^*]+\*)", text)
    for teil in teile:
        if not teil:
            continue
        if teil.startswith("**") and teil.endswith("**"):
            run = paragraph.add_run(teil[2:-2]); run.bold = True
        elif teil.startswith("*") and teil.endswith("*"):
            run = paragraph.add_run(teil[1:-1]); run.italic = True
        else:
            run = paragraph.add_run(teil)
        if basis_kursiv:
            run.italic = True


def absatz(doc, text, stil="Fliesstext", einzug=True):
    p = doc.add_paragraph(style=stil)
    if einzug and stil == "Fliesstext":
        p.paragraph_format.first_line_indent = Cm(0.5)
    setze_inline(p, text)
    return p


# ---------------------------------------------------------------- Stile

def baue_stile(doc):
    normal = doc.styles["Normal"]
    normal.font.name = SCHRIFT
    normal.font.size = SCHRIFT_GRAD
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), SCHRIFT)

    def neu(name, groesse, fett=False, vor=0, nach=0, ausricht=WD_ALIGN_PARAGRAPH.JUSTIFY,
            kursiv=False, abstand=ZEILENABSTAND):
        st = doc.styles.add_style(name, 1)  # 1 = WD_STYLE_TYPE.PARAGRAPH
        st.font.name = SCHRIFT
        st.font.size = groesse
        st.font.bold = fett
        st.font.italic = kursiv
        pf = st.paragraph_format
        pf.space_before = Pt(vor)
        pf.space_after = Pt(nach)
        pf.alignment = ausricht
        pf.line_spacing = abstand
        pf.widow_control = True
        return st

    neu("Fliesstext", SCHRIFT_GRAD, nach=0)
    neu("FliesstextErst", SCHRIFT_GRAD, nach=0)          # erster Absatz, kein Einzug
    neu("KapitelNummer", Pt(11), ausricht=WD_ALIGN_PARAGRAPH.LEFT, nach=6,
        abstand=Pt(13))
    neu("KapitelTitel", Pt(20), fett=True, ausricht=WD_ALIGN_PARAGRAPH.LEFT,
        nach=24, abstand=Pt(24))
    neu("Zwischen", Pt(13), fett=True, ausricht=WD_ALIGN_PARAGRAPH.LEFT,
        vor=18, nach=6, abstand=Pt(16))
    neu("TeilLabel", Pt(12), ausricht=WD_ALIGN_PARAGRAPH.CENTER, nach=10, abstand=Pt(14))
    neu("TeilTitel", Pt(18), fett=True, ausricht=WD_ALIGN_PARAGRAPH.CENTER,
        nach=0, abstand=Pt(22))
    neu("TitelHaupt", Pt(26), fett=True, ausricht=WD_ALIGN_PARAGRAPH.CENTER,
        nach=14, abstand=Pt(30))
    neu("TitelUnter", Pt(13), ausricht=WD_ALIGN_PARAGRAPH.CENTER, nach=40,
        kursiv=True, abstand=Pt(17))
    neu("TitelAutor", Pt(15), ausricht=WD_ALIGN_PARAGRAPH.CENTER, abstand=Pt(18))
    neu("Klein", Pt(9), ausricht=WD_ALIGN_PARAGRAPH.LEFT, nach=4, abstand=Pt(12))
    neu("Anmerkung", Pt(9), ausricht=WD_ALIGN_PARAGRAPH.LEFT, nach=4, abstand=Pt(12))
    neu("InhaltEintrag", Pt(10.5), ausricht=WD_ALIGN_PARAGRAPH.LEFT, nach=5,
        abstand=Pt(14))


def richte_seite_ein(section, mit_kopfzeile=True, kopftext=""):
    section.page_width, section.page_height = SEITE_B, SEITE_H
    section.top_margin, section.bottom_margin = RAND_OBEN, RAND_UNTEN
    section.left_margin, section.right_margin = RAND_INNEN, RAND_AUSSEN
    section.gutter = BUNDSTEG
    section.different_first_page_header_footer = True

    fuss = section.footer.paragraphs[0]
    fuss.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fuss.style = section.part.document.styles["Klein"]
    seitenzahl_feld(fuss)

    if mit_kopfzeile and kopftext:
        kopf = section.header.paragraphs[0]
        kopf.alignment = WD_ALIGN_PARAGRAPH.CENTER
        kopf.style = section.part.document.styles["Klein"]
        kopf.add_run(kopftext).italic = True


# ---------------------------------------------------------------- Kapitel

def lies_kapitel(pfad):
    """Zerlegt eine Kapiteldatei in Titel, Fließtext-Blöcke und Endnoten."""
    text = pfad.read_text(encoding="utf-8")

    # Quellenapparat abtrennen
    teile = re.split(r"^## Quellen zu .*$", text, maxsplit=1, flags=re.M)
    koerper = teile[0]
    noten = teile[1].strip() if len(teile) > 1 else ""

    # Redaktionsnotizen entfernen (nicht Teil des Buchtexts)
    koerper = re.sub(r"^\*\*Redaktionsnotiz.*?(?=\n#|\Z)", "", koerper,
                     flags=re.M | re.S)

    zeilen = koerper.split("\n")
    titel = ""
    bloecke = []
    for z in zeilen:
        z = z.rstrip()
        if z.startswith("# "):
            titel = z[2:].strip()
        elif z.startswith("## "):
            bloecke.append(("h2", z[3:].strip()))
        elif z.startswith("### "):
            bloecke.append(("h3", z[4:].strip()))
        elif z.strip() in ("", "---"):
            continue
        elif z.startswith("> "):
            bloecke.append(("zitat", z[2:].strip()))
        else:
            bloecke.append(("p", z.strip()))

    notenzeilen = [n.strip() for n in noten.split("\n")
                   if n.strip() and not n.strip().startswith("*(")]
    return titel, bloecke, notenzeilen


def schreibe_kapitel(doc, titel, bloecke, kapnummer=None):
    if kapnummer is not None:
        p = doc.add_paragraph(style="KapitelNummer")
        p.add_run(f"Kapitel {kapnummer}").italic = True
        klartitel = re.sub(r"^Kapitel\s+\d+\s*[—–-]\s*", "", titel)
    else:
        klartitel = re.sub(r"^(Einleitung|Schluss)\s*[—–-]\s*", "", titel)
        p = doc.add_paragraph(style="KapitelNummer")
        p.add_run("Einleitung" if "Einleitung" in titel else "Schluss").italic = True

    p = doc.add_paragraph(style="KapitelTitel")
    setze_inline(p, klartitel)

    erster = True
    for art, inhalt in bloecke:
        if art == "h2":
            p = doc.add_paragraph(style="Zwischen"); setze_inline(p, inhalt)
            erster = True
        elif art == "h3":
            p = doc.add_paragraph(style="Zwischen"); setze_inline(p, inhalt)
            erster = True
        elif art == "zitat":
            p = doc.add_paragraph(style="Fliesstext")
            p.paragraph_format.left_indent = Cm(0.8)
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(6)
            setze_inline(p, inhalt, basis_kursiv=True)
            erster = True
        else:
            p = doc.add_paragraph(style="Fliesstext")
            if not erster:
                p.paragraph_format.first_line_indent = Cm(0.5)
            setze_inline(p, inhalt)
            erster = False


# ---------------------------------------------------------------- Hauptlauf

def main():
    doc = Document()
    baue_stile(doc)
    richte_seite_ein(doc.sections[0], mit_kopfzeile=False)

    # --- Titelseite
    for _ in range(4):
        doc.add_paragraph(style="Fliesstext")
    doc.add_paragraph(TITEL, style="TitelHaupt")
    doc.add_paragraph(UNTERTITEL, style="TitelUnter")
    doc.add_paragraph(AUTOR, style="TitelAutor")
    doc.add_page_break()

    # --- Impressum
    doc.add_paragraph("Impressum", style="Zwischen")
    for zeile in [
        f"{TITEL}",
        f"{UNTERTITEL}",
        "",
        f"© {AUTOR}",
        "Alle Rechte vorbehalten.",
        "",
        "Kontakt und Verlagsangaben: [vor Veröffentlichung ergänzen]",
        "",
        "Hinweis zu Quellen: Alle Tatsachenbehauptungen sind mit Endnoten belegt; "
        "der vollständige Nachweis steht im Anhang. Einschätzungen und Prognosen "
        "sind im Text als solche gekennzeichnet.",
        "",
        "Offenlegung: Der Autor arbeitet beruflich mit Automatisierungs- und "
        "KI-Technologie. Diese Befangenheit ist in der Einleitung offengelegt.",
    ]:
        doc.add_paragraph(zeile, style="Klein")
    doc.add_page_break()

    # --- Kapitel einsammeln
    dateien = sorted(KAP.glob("*.md"))
    alle_noten = []

    # --- Inhaltsverzeichnis
    doc.add_paragraph("Inhalt", style="KapitelTitel")
    for pfad in dateien:
        titel, _, _ = lies_kapitel(pfad)
        num = int(pfad.name[:2])
        if num in TEILE:
            label, teiltitel = TEILE[num]
            p = doc.add_paragraph(style="InhaltEintrag")
            p.add_run(f"{label} — {teiltitel}").bold = True
        p = doc.add_paragraph(style="InhaltEintrag")
        p.paragraph_format.left_indent = Cm(0.4)
        setze_inline(p, titel)
    doc.add_page_break()

    # --- Fließtext
    for pfad in dateien:
        num = int(pfad.name[:2])
        titel, bloecke, noten = lies_kapitel(pfad)

        if num in TEILE:
            label, teiltitel = TEILE[num]
            for _ in range(6):
                doc.add_paragraph(style="Fliesstext")
            doc.add_paragraph(label, style="TeilLabel")
            doc.add_paragraph(teiltitel, style="TeilTitel")
            doc.add_page_break()

        kapnummer = num if 1 <= num <= 12 else None
        schreibe_kapitel(doc, titel, bloecke, kapnummer)
        doc.add_page_break()

        if noten:
            alle_noten.append((titel, noten))

    # --- Anhang: Anmerkungen
    doc.add_paragraph("Anmerkungen", style="KapitelTitel")
    p = doc.add_paragraph(style="Klein")
    p.add_run(
        "Die Nummerierung läuft kapitelweise. Mit ▲ markierte Belege sind vor "
        "Drucklegung am Volltext gegenzulesen; die vollständige Prüfliste liegt "
        "in der Projektdokumentation."
    ).italic = True
    for titel, noten in alle_noten:
        p = doc.add_paragraph(style="Zwischen")
        setze_inline(p, titel)
        for note in noten:
            p = doc.add_paragraph(style="Anmerkung")
            setze_inline(p, note)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.save(OUT)

    woerter = sum(len(p.text.split()) for p in doc.paragraphs)
    print(f"Geschrieben: {OUT}")
    print(f"Absätze: {len(doc.paragraphs)},  Wörter im Dokument: {woerter}")
    print(f"Trim: 6 × 9 Zoll,  Bundsteg: {BUNDSTEG.cm:.2f} cm,  Schrift: {SCHRIFT} {SCHRIFT_GRAD.pt} pt")


if __name__ == "__main__":
    main()
