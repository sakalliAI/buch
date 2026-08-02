# KDP-Veröffentlichungspaket

**Buch:** „Erst kam die Angst, dann kam der Alltag" · **Autor:** Emre Sakalli
**Erstellt:** 2026-08-02 · **Status:** Arbeitsdokument für Phase 7 (GATE 4)

---

## Vorbemerkung zur Belegbasis

Sämtliche KDP-Regeln, Grenzwerte und Formatangaben in diesem Dokument stammen aus dem Recherche-Dossier `01_konzept/p2_kdp_format.md` (Abruf 2026-06-28). Dessen Vorbehalte gelten hier unverändert weiter:

> **Der direkte Abruf von `kdp.amazon.com` war im Recherche-Setup blockiert (HTTP 403).** Alle Werte wurden über den Suchindex aus offiziellen KDP-Hilfeseiten extrahiert. Mit ⚠️ markierte Zahlen stammen aus Suchergebnis-Snippets oder Sekundärquellen. **Trim-Size-Tabelle, Margin-Tabelle, Max.-Seitenzahlen, Druckkosten und Royalty-Sätze sind vor dem Upload im eingeloggten KDP-Konto gegenzuprüfen** — KDP ändert Spezifikationen und Druckkosten regelmäßig.

Werte, die **nicht** im Dossier belegt sind (insbesondere konkrete Druckkosten in Euro, die Rückenbreiten-Formel und die exakten deutschen Kategoriepfade), sind in diesem Dokument **nicht** durch plausible Zahlen ersetzt worden, sondern ausdrücklich als **[im KDP-Konto verifizieren]** gekennzeichnet. Diese Lücken sind vor dem Upload zu füllen, nicht zu überspringen.

---

## 1. Metadaten-Datenblatt

Feldweise zum Übertragen in das KDP-Formular (Reihenfolge nach KDP „Metadata Guidelines for Books").

| KDP-Feld | Eintrag | Anmerkung |
|---|---|---|
| **Book Title / Buchtitel** | `Erst kam die Angst, dann kam der Alltag` | Freigegebener Titel (GATE 3). Kein Untertitel-Anteil, keine Reihenangabe, keine Werbezusätze im Titelfeld. |
| **Subtitle / Untertitel** | `Was Buchdruck, Dampflok und Smartphone über unsere Furcht vor künstlicher Intelligenz verraten` | Freigegebener Untertitel (GATE 3). Er liefert zugleich die wichtigsten Suchbegriffe, die deshalb **nicht** in den Keyword-Slots wiederholt werden (siehe Abschnitt 4). |
| **Series / Reihe** | *leer* | Kein Reihentitel. |
| **Edition Number / Ausgabe** | `1` | Erstausgabe. Feld nur füllen, wenn KDP es für Erstausgaben zulässt — sonst leer lassen. |
| **Author / Autor** | Vorname `Emre` · Nachname `Sakalli` | Namensform laut `01_konzept/autor_bio.md`. Über alle Ausgaben und im Author-Central-Profil identisch halten. |
| **Contributors / Mitwirkende** | *leer bzw. nach Bedarf* | Falls Lektorat/Cover extern vergeben wird und genannt werden soll: als „Illustrator"/„Editor" ergänzen. Sonst leer. |
| **Description / Buchbeschreibung** | siehe Abschnitt 2 | Limit ca. 4.000 Zeichen inkl. Leerzeichen, Satzzeichen und HTML-Tags. ⚠️ Der 4.000er-Wert ist nur über Sekundärquellen belegt — **im KDP-Editor verifizieren** (der Editor zeigt den Zähler an). |
| **Publishing Rights / Veröffentlichungsrechte** | „Ich besitze das Urheberrecht und die notwendigen Veröffentlichungsrechte." | Eigenes Werk. Voraussetzung: alle Zitate/Paraphrasen sind rechtlich sauber (siehe Abschnitt 7). |
| **Primary Audience / Erwachseneninhalte** | **Nein** | Das Buch enthält keine expliziten Inhalte. Ein „Ja" schränkt Auffindbarkeit und Werbemöglichkeiten ein und wäre hier sachlich falsch. |
| **Reading Age / Lesealter** | *optional, leer lassen* | Allgemeines Sachbuch für Erwachsene; eine enge Altersangabe schadet der Auffindbarkeit mehr, als sie nützt. |
| **Categories / Kategorien** | bis zu 3, siehe Abschnitt 3 | Bis zu 3 bei der Einrichtung wählbar. ⚠️ Nachträglich bis zu 10 über den KDP-Support anforderbar (nur über Sekundärquellen belegt). |
| **Keywords** | genau 7, siehe Abschnitt 4 | KDP stellt genau 7 Felder bereit. |
| **Language / Sprache** | `Deutsch` | Buch- **und** Metadatensprache. KDP unterstützt Deutsch (eigene de_DE-Hilfe, Marketplace Amazon.de). |
| **Publication Date / Veröffentlichungsdatum** | **leer lassen** | Feld nur ausfüllen, wenn das Werk zuvor bereits anderswo veröffentlicht war. Für eine Erstveröffentlichung setzt KDP das Datum selbst. Das gewünschte Erscheinungsdatum wird stattdessen über den Upload-Zeitpunkt bzw. die Vorbestellfunktion gesteuert. **Im KDP-Konto prüfen, ob die Vorbestellfunktion für Taschenbücher verfügbar ist — das Dossier belegt das nicht.** |
| **Imprint** | abhängig von der ISBN-Wahl (s. u.) | Bei KDP-Gratis-ISBN automatisch „Independently published". |
| **ISBN** | Entscheidung erforderlich, s. u. | **Für das Taschenbuch ist eine ISBN Pflicht** (Gratis-ISBN von KDP oder eigene). |

### 1.1 ISBN — Gratis-ISBN vs. eigene ISBN

Belegt im Dossier (KDP „What is an ISBN and Imprint?", „Get an ISBN"):

| | **KDP-Gratis-ISBN** | **Eigene ISBN** (DE: ISBN-Agentur/MVB) |
|---|---|---|
| Kosten | keine | Kaufpreis; im Einzelkauf pro Nummer deutlich teurer als im Block |
| Imprint | zwingend **„Independently published"** | frei wählbarer eigener Verlagsname |
| Nutzung außerhalb KDP | an KDP gebunden | frei — dieselbe Ausgabe kann über andere Dienstleister erscheinen |
| Expanded Distribution | zulässig | zulässig |
| Aufwand | keiner | Registrierung, Titelmeldung, Pflege |

**Einordnung:** Für einen Debüttitel, der zunächst ausschließlich über Amazon erscheinen soll, ist die Gratis-ISBN die pragmatische Wahl — der einzige spürbare Preis ist das Imprint „Independently published" auf der Produktseite. Eine eigene ISBN lohnt, sobald ein eigener Verlagsname aufgebaut, das Buch parallel über andere Dienstleister vertrieben oder eine Meldung an das Verzeichnis lieferbarer Bücher angestrebt werden soll. **Wichtig:** Jede Ausgabe (Taschenbuch, Hardcover, E-Book) braucht eine eigene ISBN; eine bereits einem Buch zugewiesene ISBN lässt sich nicht rückwirkend tauschen. Die Entscheidung ist also vor dem ersten Upload zu treffen.

> **Zu prüfen im KDP-Konto:** aktuelle Formulierung des ISBN-Dialogs, ob das Feld „Publication Date" bei Erstveröffentlichungen wirklich leer bleiben soll, und ob eine Vorbestellphase für Taschenbücher angeboten wird.

---

## 2. Buchbeschreibung (Produktseite)

Das Zeichenlimit liegt bei ca. 4.000 Zeichen inkl. Leerzeichen und HTML-Tags (⚠️ nur über Sekundärquellen belegt, im Editor gegenprüfen). Die Hauptfassung schöpft es bewusst nicht aus: Auf der Amazon-Produktseite sind nur die ersten Zeilen ohne Klick sichtbar, und ein überladener Klappentext liest sich wie Verkaufsdruck — das würde dem Versprechen des Buches („Kompass statt Beruhigungspille") direkt widersprechen.

**Tonregel für alle Fassungen:** neugierig machen, nicht überreden. Keine Superlative, keine Ausrufezeichen, keine erfundenen Auszeichnungen, Rezensionen oder Verkaufszahlen. Jede Behauptung im Text ist durch das Manuskript gedeckt (Trithemius/Buchdruck → Kap. 1; erfundene Eisenbahn-Warnung → Einleitung + Kap. 2; Edisons Angstkampagne → Kap. 2; Kodak/Warren & Brandeis 1890 → Einleitung + Kap. 5; Beleg-/Prognose-/Meinungs-Trennung → Einleitung; „wovor wirklich fürchten" → Kap. 12).

### 2.1 Hauptfassung (1.569 Zeichen inkl. Leerzeichen)

```text
1492 setzte sich ein Abt hin und schrieb eine flammende Warnung: Der Buchdruck werde das Gedächtnis ruinieren und die Menschen faul machen. Seine Streitschrift ließ er drucken.

Seitdem wiederholt sich dasselbe Muster. Die Eisenbahn sollte den Verstand zerrütten. Das Telefon die Familie zerstören. Der Taschenrechner das Kopfrechnen. Erst kam die Angst — dann kam der Alltag.

Heute heißt die Technik künstliche Intelligenz, und die Sätze klingen erstaunlich vertraut. Emre Sakalli arbeitet seit Jahren beruflich mit Automatisierung und KI. Er nimmt diese Sätze ernst, statt sie wegzulachen. Denn die Geschichte hat einen unbequemen Haken: Nicht jede Angst war albern. Die berühmte Warnung der Ärzte vor der Eisenbahn ist erfunden. Die Angstkampagne gegen den Wechselstrom war bezahlt. Und manche Sorge hatte schlicht recht — die Panik um die Schnappschuss-Kamera brachte 1890 das moderne Recht auf Privatsphäre hervor.

Dieses Buch verspricht keine Beruhigung. Es liefert einen Kompass:

• Was fünfhundert Jahre Technikangst über unsere Reflexe verraten
• Was die Daten zu Arbeit, Bildung, Diskriminierung und Energieverbrauch wirklich hergeben — Beleg, Prognose und Meinung sauber getrennt
• Wie man Heilsversprechen und Untergangsszenarien liest, ohne beiden aufzusitzen
• Und wovor man sich tatsächlich fürchten sollte

Beruhigung heißt: Jemand sagt dir, du sollst dir keine Sorgen machen. Vertrauen heißt: Du verstehst genug, um selbst zu entscheiden, worüber. Das eine macht abhängig, das andere frei.

Ein Buch für alle, die weder Panik noch Hype kaufen wollen.
```

**Warum dieser Aufbau:**
- **Zeile 1–2** ist der Haken: eine konkrete, überprüfbare Szene mit Pointe (er ließ die Warnung drucken). Sie steht vor dem „Mehr lesen"-Klick und verkauft ohne ein einziges Werbewort.
- **Der Dreisatz Eisenbahn/Telefon/Taschenrechner** liefert Wiedererkennung und führt den Titel als Formel ein.
- **Der Twist** („Nicht jede Angst war albern") ist das Alleinstellungsmerkmal gegenüber dem Vergleichsumfeld — beruhigende Titel wie *Keine Panik, ist nur Technik* und mahnende wie Spitzers *Künstliche Intelligenz* besetzen die beiden Ränder; dieses Buch besetzt die Unterscheidung. Er verhindert außerdem, dass die Beschreibung mehr verspricht, als das Buch einlöst.
- **Die Liste** macht den Nutzen scanbar und benennt die Methode (Beleg/Prognose/Meinung), statt sie zu behaupten.
- **Der Schluss** ist die Kernaussage der Einleitung, verdichtet — und kein Kaufappell.

### 2.2 Kurzfassung (544 Zeichen inkl. Leerzeichen)

Für Author Central, Anzeigen, Vorschautexte, Pressemitteilungen, LinkedIn-Ankündigung.

```text
1492 warnte ein Abt, der Buchdruck werde das Denken ruinieren — und ließ die Warnung drucken. Die Eisenbahn sollte den Verstand zerrütten, das Telefon die Familie zerstören. Erst kam die Angst, dann kam der Alltag.

Heute heißt die Technik KI. Emre Sakalli, seit Jahren beruflich mit Automatisierung befasst, zeigt das Muster — und den unbequemen Haken: Nicht jede Angst war albern. Manche war erfunden, manche bezahlt, manche hatte recht.

Kein Schönreden, keine Panik. Ein ehrlicher Kompass für alle, die selbst entscheiden wollen, was zählt.
```

### 2.3 HTML-Varianten

**Belegstand zu den Tags:** Das Dossier belegt lediglich, dass KDP „HTML-Basisformatierung (fett/kursiv/Listen)" in der Buchbeschreibung unterstützt (KDP „Metadata Guidelines for Books"). Eine **abschließende Liste der erlaubten Tags ist im Dossier nicht belegt.** `<b>`, `<i>` und `<ul>`/`<li>` fallen unter die belegte Kategorie „fett/kursiv/Listen". Für `<p>` und `<br>` gibt es im Dossier **keinen Beleg**.

> **[im KDP-Konto verifizieren]** Vor dem Speichern die HTML-Fassung in den Beschreibungseditor einfügen, speichern und die **Vorschau** kontrollieren. Werden Tags als Klartext angezeigt oder entfernt, auf die Klartextfassung (2.1/2.2) zurückfallen. Tags zählen laut Dossier **mit** in das Zeichenlimit.

**Hauptfassung als HTML** (1.801 Zeichen inkl. Tags und Entities; mit direkten Umlauten statt Entities: 1.679):

```html
<p><b>1492 setzte sich ein Abt hin und schrieb eine flammende Warnung:</b> Der Buchdruck werde das Ged&auml;chtnis ruinieren und die Menschen faul machen. Seine Streitschrift lie&szlig; er drucken.</p>
<p>Seitdem wiederholt sich dasselbe Muster. Die Eisenbahn sollte den Verstand zerr&uuml;tten. Das Telefon die Familie zerst&ouml;ren. Der Taschenrechner das Kopfrechnen. <i>Erst kam die Angst &mdash; dann kam der Alltag.</i></p>
<p>Heute hei&szlig;t die Technik k&uuml;nstliche Intelligenz, und die S&auml;tze klingen erstaunlich vertraut. Emre Sakalli arbeitet seit Jahren beruflich mit Automatisierung und KI. Er nimmt diese S&auml;tze ernst, statt sie wegzulachen. Denn die Geschichte hat einen unbequemen Haken: <b>Nicht jede Angst war albern.</b> Die ber&uuml;hmte Warnung der &Auml;rzte vor der Eisenbahn ist erfunden. Die Angstkampagne gegen den Wechselstrom war bezahlt. Und manche Sorge hatte schlicht recht &mdash; die Panik um die Schnappschuss-Kamera brachte 1890 das moderne Recht auf Privatsph&auml;re hervor.</p>
<p><b>Dieses Buch verspricht keine Beruhigung. Es liefert einen Kompass:</b></p>
<ul>
<li>Was f&uuml;nfhundert Jahre Technikangst &uuml;ber unsere Reflexe verraten</li>
<li>Was die Daten zu Arbeit, Bildung, Diskriminierung und Energieverbrauch wirklich hergeben &mdash; Beleg, Prognose und Meinung sauber getrennt</li>
<li>Wie man Heilsversprechen und Untergangsszenarien liest, ohne beiden aufzusitzen</li>
<li>Und wovor man sich tats&auml;chlich f&uuml;rchten sollte</li>
</ul>
<p>Beruhigung hei&szlig;t: Jemand sagt dir, du sollst dir keine Sorgen machen. Vertrauen hei&szlig;t: Du verstehst genug, um selbst zu entscheiden, wor&uuml;ber. Das eine macht abh&auml;ngig, das andere frei.</p>
<p><i>Ein Buch f&uuml;r alle, die weder Panik noch Hype kaufen wollen.</i></p>
```

**Kurzfassung als HTML** (633 Zeichen inkl. Tags und Entities; mit direkten Umlauten: 584):

```html
<p><b>1492 warnte ein Abt, der Buchdruck werde das Denken ruinieren &mdash; und lie&szlig; die Warnung drucken.</b> Die Eisenbahn sollte den Verstand zerr&uuml;tten, das Telefon die Familie zerst&ouml;ren. <i>Erst kam die Angst, dann kam der Alltag.</i></p>
<p>Heute hei&szlig;t die Technik KI. Emre Sakalli, seit Jahren beruflich mit Automatisierung befasst, zeigt das Muster &mdash; und den unbequemen Haken: Nicht jede Angst war albern. Manche war erfunden, manche bezahlt, manche hatte recht.</p>
<p>Kein Sch&ouml;nreden, keine Panik. <b>Ein ehrlicher Kompass f&uuml;r alle, die selbst entscheiden wollen, was z&auml;hlt.</b></p>
```

**Hinweise zur HTML-Fassung:**
- Umlaute und ß sind als HTML-Entities kodiert. Das ist die robustere Variante, falls der Editor mit der Zeichenkodierung Probleme macht; funktionieren direkte Umlaute in der Vorschau, kann man sie verwenden und spart 122 Zeichen (Hauptfassung) bzw. 49 Zeichen (Kurzfassung).
- Der Gedankenstrich ist als `&mdash;` gesetzt. Falls die Vorschau ihn nicht korrekt darstellt, durch ein einfaches `-` mit Leerzeichen ersetzen.
- Die Aufzählungspunkte („•") der Klartextfassung sind in der HTML-Fassung durch `<ul>`/`<li>` ersetzt — in der Klartextfassung müssen sie als Zeichen stehen bleiben, weil ohne Tags keine Liste erzeugt wird.
- Es wird **kein** Fettdruck über ganze Absätze gesetzt und kein `<h4>`/Überschriften-Tag verwendet: nicht belegt und optisch schreierisch.

---

## 3. Kategorien

Belegt: Bei der Einrichtung sind **bis zu 3 Kategorien** wählbar; die Kategorien **unterscheiden sich je Marketplace** (Amazon.de ≠ Amazon.com). ⚠️ Nachträglich sind über den KDP-/Author-Central-Support bis zu 10 Kategorien anforderbar (nur über Sekundärquellen belegt).

> ⚠️ **Die exakten Pfadbezeichnungen der deutschen KDP-Kategorienliste sind im Dossier nicht belegt.** Die folgenden Pfade sind daher **im KDP-Konto gegenzuprüfen** und gegebenenfalls durch die nächstliegende tatsächlich angebotene Bezeichnung zu ersetzen. Maßgeblich ist allein die Auswahlliste, die KDP im Einrichtungsdialog für den Marketplace Amazon.de anzeigt.

| Rang | Vorgeschlagener Pfad (Amazon.de) — *im KDP-Konto gegenzuprüfen* | Begründung |
|---|---|---|
| **1. Wahl** | `Bücher > Computer & Internet > Künstliche Intelligenz & Neuronale Netze` | Kernthema des Buches; hier suchen Leser, die konkret ein KI-Sachbuch wollen — das ist das Segment der direkten Vergleichstitel (Lenzen, Ait Si Abbou, Meckel/Steinacker). |
| **2. Wahl** | `Bücher > Politik & Geschichte > Geschichte > Technik- & Wissenschaftsgeschichte` | Trägt die eigentliche Hälfte des Buches: fünfhundert Jahre Technikangst von Trithemius bis zum Taschenrechner. Erschließt ein Publikum, das über KI-Regale nicht zu erreichen ist, und ist dort weniger überlaufen. |
| **3. Wahl** | `Bücher > Politik & Geschichte > Sachbuch > Gesellschaft & Soziales` (alternativ: `… > Medien & Kommunikation`) | Deckt den gesellschaftlichen Strang ab (Arbeit, Bildung, Verteilung, Machtkonzentration — Kapitel 6–8 und 12) und passt zum Tonalitäts-Benchmark Nguyen-Kim. |

**Reservekandidaten**, falls einer der Pfade in der Liste nicht existiert oder für die Nachmeldung der bis zu 10 Kategorien:
- Wirtschaft > Zukunft der Arbeit / Arbeitswelt (Kapitel 6 und 10)
- Sachbuch > Philosophie / Ethik (Kapitel 9 und 12, Maschinenethik-Umfeld)
- Ratgeber > Medienkompetenz / Digitale Bildung (Kapitel 11)
- Wissenschaft > Populärwissenschaft

**Vorgehensregel bei der Auswahl:** Nicht drei Kategorien im selben, dichtest besetzten Ast wählen. Ein breiter Kernast (KI) plus zwei Nebenäste (Technikgeschichte, Gesellschaft) erhöht die Chance auf Sichtbarkeit in weniger umkämpften Ranglisten, ohne das Buch falsch einzusortieren. Kategorien, die das Buch nicht wirklich trifft, sind auszuschließen — Fehleinordnung produziert enttäuschte Rezensionen.

---

## 4. Keywords (7 Slots)

Belegte Regeln: KDP stellt **genau 7 Keyword-Felder** bereit und empfiehlt **Phrasen von 2–3 Wörtern**; keine Wiederholung von Titel-/Kategoriebegriffen, keine irreführenden oder markenrechtlich geschützten Begriffe.

**Daraus abgeleitete Sperrliste** (Wörter, die bereits in Titel/Untertitel stehen und deshalb keinen Slot verbrauchen dürfen): *Angst, Alltag, Buchdruck, Dampflok, Smartphone, Furcht, künstliche Intelligenz*. Ebenfalls gesperrt: Produkt- und Firmennamen (ChatGPT, OpenAI, Copilot …) sowie Titel und Autorennamen von Konkurrenzbüchern.

| # | Keyword-Phrase | Begründung |
|---|---|---|
| 1 | `KI Sachbuch verständlich` | „KI" ist die gebräuchlichste deutsche Suchabkürzung und steht **nicht** im Titel (dort nur ausgeschrieben) — der Slot deckt also eine echte Lücke. „verständlich" trifft die Kaufabsicht von Einsteigern. |
| 2 | `Technikangst Geschichte` | Der zweite Themenstrang, den weder Titel noch Untertitel als Suchbegriff hergeben. Bedient Leser, die über Technik-/Kulturgeschichte einsteigen, und stützt die zweite Kategoriewahl. |
| 3 | `Zukunft der Arbeit` | Etablierte, hochfrequente Suchphrase; Kapitel 6 und 10 lösen sie inhaltlich vollständig ein (ILO, IWF, OECD, IAB, Brynjolfsson). Kein Wort davon steht im Titel. |
| 4 | `Automatisierung Arbeitsmarkt` | Die berufliche Kernkompetenz des Autors und der konkreteste Nutzenanker für Leser aus Unternehmen; ergänzt Slot 3 um die Anbieter-/Betriebsperspektive statt sie zu doppeln. |
| 5 | `digitale Mündigkeit` | Deckt das Versprechen des Buches (Kompass, nicht Beruhigung) mit dem im deutschen Bildungsdiskurs eingeführten Begriff ab. Erschließt Lehrkräfte, Eltern und Weiterbildung — die Zielgruppe von Kapitel 11. |
| 6 | `kritisches Denken Quellenkritik` | Die Methode des Buches als Suchbegriff: Beleg/Prognose/Meinung trennen, Deepfakes und Zahlen prüfen (Kapitel 9 und 11). Erreicht Leser, die kein KI-Buch suchen, sondern Urteilsfähigkeit. |
| 7 | `Chancen und Risiken Digitalisierung` | Die meistgebrauchte neutrale Formel für abwägende Sachbücher; positioniert den Titel zwischen Hype und Panik, ohne ein Konkurrenzbuch oder eine Marke zu nennen. |

**Anwendungshinweise:**
- Ein Slot = eine Phrase. Keine Kommaketten in ein Feld packen, keine Wörter über zwei Slots doppeln (in der Liste oben kommt kein Wort zweimal vor).
- Keine Wertungen wie „bestes Buch", keine Angaben zu Preis oder Ranking, keine Aussagen, die das Buch nicht einlöst — das verstößt gegen die Metadaten-Richtlinien.
- Keywords lassen sich jederzeit nachträglich ändern. Nach 4–8 Wochen anhand der Verkaufs- und Anzeigenberichte prüfen, welche Slots nichts liefern, und tauschen.
- **[im KDP-Konto verifizieren]** ob KDP inzwischen zusätzliche Hinweise zur maximalen Zeichenzahl je Keyword-Feld gibt — im Dossier ist dazu nichts belegt.

---

## 5. Cover-Briefing

Arbeitsanweisung für Gestalterin oder Bild-Tool. Verbindlich sind die technischen Eckwerte in 5.6.

### 5.1 Was das Buch ist (damit das Cover nicht lügt)

Ein deutschsprachiges Sachbuch über die Geschichte der Technikangst und eine nüchterne Bilanz der heutigen KI. Kein Ratgeber, kein Tech-Thriller, keine Untergangsprosa, keine Beruhigungsschrift. Der Ton ist souverän, konkret, mit trockenem Humor. Das Cover muss Seriosität und Zugänglichkeit gleichzeitig transportieren — es steht im Regal neben Lenzen (C.H. Beck), Ait Si Abbou (GU/Droemer) und Nguyen-Kim (Droemer), nicht neben Science-Fiction.

### 5.2 Was zu vermeiden ist (harte Ausschlüsse)

Das Buch argumentiert ausdrücklich **gegen** die Bildsprache, mit der KI üblicherweise bebildert wird. Ein Cover in dieser Ästhetik würde dem Inhalt widersprechen und die falschen Leser anziehen.

- **Keine** Roboterhände, humanoiden Roboter, Androidengesichter.
- **Keine** blauen Platinen, Leiterbahnen, Matrix-Zahlenregen, Glasfaser-Lichtstreifen, glühenden Netzwerkknoten.
- **Keine** Terminator-/Cyberpunk-Ästhetik, keine roten Kameraaugen, keine Dystopie-Signale.
- **Keine** leuchtenden Gehirne, keine halb-Mensch-halb-Maschine-Gesichter, kein „Finger berührt Bildschirm".
- **Keine** generischen KI-Stockfotos und **keine** sichtbar KI-generierten Artefakte (falsche Hände, unlesbare Pseudoschrift) — bei einem Buch über den ehrlichen Umgang mit KI wäre das ein vermeidbares Eigentor.
- **Kein** Chrom, kein Neon-Cyan-auf-Schwarz, kein Verlauf von Dunkelblau nach Violett.
- **Keine** Ausrufezeichen, keine Störer („Bestseller!", „Das Buch der Stunde"), keine erfundenen Blurbs oder Auszeichnungen.

### 5.3 Bildideen (Priorität von oben)

**Idee A — Die Zeitleiste der Angst (Empfehlung).** Eine Reihe schlichter, gleichwertig gestalteter Piktogramme oder Linolschnitt-artiger Silhouetten nebeneinander oder untereinander: Handpresse → Dampflok → Wandtelefon → Fernseher → Taschenrechner → ein neutrales, modernes Rechteck (Bildschirm/Chat-Fenster, bewusst leer). Alle im gleichen Stil, gleicher Größe, gleicher Farbe. Die Aussage entsteht durch die Gleichbehandlung: Was heute Panik auslöst, steht in einer Reihe mit dem, was längst Möbel ist. Das letzte Element bleibt leer oder nur angedeutet — die Frage ist offen. Trägt den Titel wörtlich, funktioniert als Daumennagel, kommt ohne jedes KI-Klischee aus.

**Idee B — Das Muster als Kurve.** Eine einzige, dicke, ruhige Linie über die Coverfläche: mehrere Ausschläge nach oben, die jeweils flach auslaufen — die immer gleiche Panikkurve, die immer gleiche Normalisierung. Der letzte Ausschlag steigt noch und ist abgeschnitten. Minimal beschriftbar (1492 · 1835 · 1878 · 1995 · heute). Sehr reduziert, sehr sachbuchig, extrem gut skalierbar.

**Idee C — Der historische Holzschnitt, unaufgeregt.** Ein einzelnes Motiv aus dem Buch als klare, gemeinfreie oder nachgezeichnete Grafik — eine frühe Druckerpresse oder eine frühe Lokomotive — groß, ruhig, monochrom, mit viel Weißraum. Die Spannung entsteht ausschließlich aus dem Bruch zwischen historischem Motiv und dem Untertitel, der von künstlicher Intelligenz spricht. *Rechte-Hinweis: nur zweifelsfrei gemeinfreie Vorlagen oder eigene Zeichnungen verwenden; die Rechtelage ist vor Verwendung schriftlich zu dokumentieren.*

### 5.4 Typografie

- **Titel dominiert.** „Erst kam die Angst, dann kam der Alltag" ist lang — der Umbruch ist der wichtigste gestalterische Entscheid. Empfohlen: „Erst kam die Angst," / „dann kam der Alltag." in zwei Zeilen, wobei die zweite Zeile optisch ruhiger gesetzt wird als die erste (kleiner, leichter, andere Farbe). Der Titel enthält die Dramaturgie des Buches; die Typografie soll sie nachvollziehen: erst laut, dann normal.
- **Schriftwahl:** eine kräftige, gut lesbare Grotesk oder eine moderne Serifenschrift mit Charakter. Keine Tech-/Display-Schrift, keine Schreibmaschinenschrift, keine gebrochene Schrift, kein Glitch-Effekt.
- **Untertitel** deutlich kleiner, aber vollständig und ohne Kürzung lesbar — er trägt die Suchbegriffe und die inhaltliche Einordnung.
- **Autorname** klein und unaufdringlich am unteren Rand; kein Debüt-Autor gewinnt über den Namen.
- **Daumennagel-Test:** Auf 120 Pixel Breite müssen Titelzeile 1 und die Bildidee erkennbar bleiben. Wenn nicht, ist der Titel zu klein oder das Motiv zu detailreich.

### 5.5 Farbwelt

- **Grundton:** warm und papiern — gebrochenes Weiß, Creme, Sandton oder ein sehr helles Warmgrau. Passt zum cremefarbenen Innenpapier und setzt sich im Regal von der Blau-Schwarz-Monokultur der KI-Bücher ab.
- **Eine Akzentfarbe, mehr nicht.** Empfehlung: ein warmes Rostrot/Ziegelrot oder ein tiefes Petrol. Rot signalisiert die Angst, ohne Alarm zu schreien; Petrol signalisiert Ruhe, ohne technisch zu wirken.
- **Schwarz** für Typografie und Linienführung.
- **Ausdrücklich nicht:** Neon, Farbverläufe über die ganze Fläche, Metallic-Effekte.
- Cover in Graustufen gegenprüfen: Es muss auch entsättigt funktionieren (Kontrast Titel/Hintergrund).

### 5.6 Technische Eckwerte

Belegt im Dossier (KDP „Paperback Submission Guidelines", „Set Trim Size, Bleed, and Margins"):

| Parameter | Wert | Beleg / Vorbehalt |
|---|---|---|
| Trim-Size | **6 × 9″ = 15,24 × 22,86 cm** | Dossier-Empfehlung, „regular" (nicht „large"), da Breite ≤ 6,12″ und Höhe ≤ 9″ |
| Beschnitt (Bleed) | **0,125″ = 3,2 mm** je Seite, wird weggeschnitten | belegt; Objekte, die randabfallend wirken sollen, müssen 3,2 mm über die Schnittkante hinausragen |
| Auflösung | **mind. 300 DPI**, empfohlen max. ~600 DPI | belegt; höhere Werte nur Dateigröße/Timeout-Risiko |
| max. Dateigröße | **650 MB** ⚠️ | Snippet-Wert, im Konto verifizieren |
| Farbraum | CMYK für Print; Graustufen für S/W ⚠️ | Best-Practice-Hinweis des Dossiers, keine harte KDP-Vorgabe |
| Schriften | alle Schriften einbetten | belegt (gilt auch für die Cover-PDF) |

**Gesamtmaß der Cover-Datei** (Rück-, Rücken- und Vorderseite in **einer** Datei):

```
Breite  = Beschnitt + Rückseite + Rückenbreite + Vorderseite + Beschnitt
        = 3,2 mm + 152,4 mm + R + 152,4 mm + 3,2 mm
Höhe    = Beschnitt + 228,6 mm + Beschnitt
        = 3,2 mm + 228,6 mm + 3,2 mm = 235,0 mm
```

**Rückenbreite R:**

```
R = Seitenzahl × Papierstärke je Seite
```

> ⚠️ **Der Faktor „Papierstärke je Seite" je Papiersorte (creme / weiß / Groundwood) ist im Dossier NICHT belegt.**
> **[im KDP-Konto verifizieren]** Die Rückenbreite ist zwingend über den **KDP-Cover-Vorlagengenerator (Cover Template Generator)** zu ermitteln — dort Trim-Size, Papiersorte, Tinte und die **finale** Seitenzahl eingeben; das Werkzeug liefert eine maßhaltige Vorlage mit eingezeichneten Beschnitt-, Rücken- und Sicherheitszonen. Diese Vorlage ist die verbindliche Grundlage, nicht eine selbst gerechnete Zahl.
> Zusätzlich: KDP bedruckt den Rücken erst ab einer Mindestseitenzahl. **Diese Schwelle ist im Dossier nicht belegt** — im Konto prüfen. Bei der hier erwarteten Seitenzahl (Abschnitt 6) ist sie mit Sicherheit überschritten, die Prüfung dient nur der Absicherung.
> **Konsequenz für den Ablauf:** Das Cover kann erst final gesetzt werden, **nachdem** der Innenteil abgeschlossen und die Seitenzahl fixiert ist. Jede spätere Textänderung, die die Seitenzahl verschiebt, macht eine neue Cover-Datei nötig.

**Sicherheitsabstände:** Kein Text und kein wesentliches Bildelement näher als ~5 mm an Schnittkanten oder an die Rückenfalzen. Auf dem Rücken selbst gehört ein Sicherheitsabstand zu beiden Falzkanten — bei Rückenbreiten unter ca. 10 mm ist die Rückenbeschriftung heikel und sollte klein und mittig gesetzt werden.

### 5.7 Buchrücken

Von oben nach unten, in Leserichtung von oben nach unten gedreht (deutsche Konvention):

```
Erst kam die Angst, dann kam der Alltag   ·   Emre Sakalli
```

Nur Titel und Autorname; der Untertitel passt nicht und muss nicht. Falls die Rückenbreite es hergibt: kleines Verlags-/Imprint-Signet am unteren Ende. Bei Verwendung der KDP-Gratis-ISBN steht dort „Independently published" — dann besser gar kein Signet.

### 5.8 Rückseitentext (Backcover)

Der Rückseitentext ist **kürzer** als die Amazon-Beschreibung: Er wird im Regal in wenigen Sekunden überflogen und muss ohne Scrollen funktionieren.

```text
1492 warnte ein Abt, der Buchdruck werde das Denken ruinieren.
Er ließ die Warnung drucken.

Die Eisenbahn sollte den Verstand zerrütten. Das Telefon die Familie
zerstören. Der Taschenrechner das Kopfrechnen. Erst kam die Angst,
dann kam der Alltag.

Heute heißt die Technik künstliche Intelligenz — und die Sätze
klingen erstaunlich vertraut. Nur: So einfach ist es nicht. Nicht
jede Angst war albern. Manche Warnung war frei erfunden, manche war
von Konkurrenten bezahlt, und manche hatte recht.

Emre Sakalli arbeitet seit Jahren beruflich mit Automatisierung und
künstlicher Intelligenz. Er verspricht keine Beruhigung, sondern
einen Kompass: fünfhundert Jahre Technikangst, eine ehrliche Bilanz
der Daten zu Arbeit, Bildung, Diskriminierung und Energie — und eine
klare Antwort auf die Frage, wovor man sich wirklich fürchten sollte.

Beruhigung heißt, dass dir jemand sagt, du sollst dir keine Sorgen
machen. Vertrauen heißt, dass du genug verstehst, um selbst zu
entscheiden, worüber.
```

Darunter, in kleinerer Schrift: **Autorenzeile** (1–2 Sätze, aus `01_konzept/autor_bio.md` abzuleiten und **vom Autor freizugeben**, z. B.: „Emre Sakalli leitet ein Team, das Automatisierungslösungen baut — regelbasiert wie KI-gestützt. Er lebt in Oberhausen.").

**Ebenfalls auf die Rückseite:** ISBN-Barcode-Feld. KDP platziert den Barcode automatisch in der unteren rechten Ecke der Rückseite — dieser Bereich ist **freizuhalten** (weiße oder sehr helle, ruhige Fläche, kein Text, kein Motiv). **[im KDP-Konto verifizieren]** Die exakte Größe und Position des reservierten Barcode-Feldes gibt die Cover-Vorlage vor; im Dossier ist sie nicht belegt.

---

## 6. Druckoptionen & Preiskalkulation

### 6.1 Gewählte Druckoptionen

| Option | Wahl | Beleg / Begründung |
|---|---|---|
| Bindung | Taschenbuch (Paperback) | Marktstandard im Vergleichsumfeld |
| Trim-Size | **6 × 9″ (15,24 × 22,86 cm)** | Dossier-Empfehlung für Sachbücher; bleibt **„regular"** („large" beginnt erst über 6,12″ Breite bzw. 9″ Höhe) → niedrigere Druckkosten pro Seite als „large" |
| Tinte | Schwarz | keine Farbabbildungen im Innenteil |
| Papier | **creme** (Alternative: weiß) | creme wirkt „buchiger" und ist bei Fließtext angenehmer; Maximalseitenzahl sinkt dabei von 828 auf **776** ⚠️ — bei der erwarteten Seitenzahl unkritisch |
| Beschnitt | ohne Bleed (Innenteil) | keine randabfallenden Elemente; erlaubt neben PDF auch DOC/DOCX-Upload — **empfohlen wird trotzdem PDF/X-1a mit eingebetteten Schriften** |
| Expanded Distribution | optional, später zuschaltbar | kostenlos, aber ohne Aufnahmegarantie bei Händlern/Bibliotheken; senkt bei Verkäufen über diesen Kanal die Marge (Konditionen **im Konto prüfen**) |

### 6.2 Geschätzte Seitenzahl

**Datenbasis** (Stand 2026-08-02, aus dem gebauten Manuskript `04_produktion/Erst_kam_die_Angst_Manuskript.docx`):

- Wörter gesamt: **90.960** (inkl. der kapitelweisen Quellenapparate)
- Zeichen inkl. Leerzeichen: **616.975**
- Absätze: 1.708
- davon Quellenapparate: rund **17 %** der Zeichen (105.019 von 620.035 in den Kapiteldateien)
- Satzspiegel laut `04_produktion/build_docx.py`: Georgia 10,5 pt, Zeilenabstand 15 pt, Ränder oben/unten 1,9 cm, innen 1,7 cm + Bundsteg 1,59 cm, außen 1,5 cm

**Rechenweg A — Faustregel des Vergleichstitel-Dossiers (300 Wörter/Seite):**

```
90.960 W ÷ 300 W/S ≈ 303 Seiten Fließtext
```

**Rechenweg B — aus dem tatsächlichen Satzspiegel:**

```
Satzspiegelbreite  = 15,24 − 1,70 − 1,59 − 1,50 = 10,45 cm ≈ 296 pt
Satzspiegelhöhe    = 22,86 − 1,90 − 1,90       = 19,06 cm ≈ 540 pt
Zeilen je Seite    = 540 pt ÷ 15 pt            ≈ 36, abzüglich Kolumnentitel ≈ 35
Zeichen je Zeile   = 296 pt ÷ ca. 5,4 pt mittlere Zeichenbreite (Georgia 10,5 pt)
                   ≈ 55, effektiv nach Umbruchverlust ≈ 52
Zeichen je Seite   = 35 × 52                    ≈ 1.820
Fließsatz          = 616.975 ÷ 1.820            ≈ 339 Seiten
Absatzverluste     = 1.708 Absätze × ½ Zeile ÷ 35 Z./S. ≈ 24 Seiten
                                                 ────────────
                                                 ≈ 363 Seiten
```

⚠️ Die mittlere Zeichenbreite von Georgia ist eine Schätzung; sie ist im Dossier nicht belegt und wurde nicht am gesetzten PDF gemessen (die Schrift ist in der Bauumgebung nicht installiert, ein PDF-Export war nicht möglich).

**Zuschläge (beide Rechenwege):**

| Posten | Seiten |
|---|---|
| Frontmatter (Schmutztitel, Vakat, Titelseite, Impressum, ggf. Widmung, Inhaltsverzeichnis mit Seitenzahlen) | ~12 |
| 3 Teil-Zwischentitel je mit Vakatrückseite | ~6 |
| 14 Kapitelanfänge (Einleitung + 12 Kapitel + Schluss; Weißraum am Kapitelkopf, Beginn jeweils auf neuer, ggf. rechter Seite) | ~14–21 |
| Backmatter (Über den Autor, Danksagung, ggf. gesammeltes Quellenverzeichnis) | ~4–8 |
| **Summe Zuschläge** | **~36–47** (Rechnung unten mit ~40) |

**Ergebnis:**

| | Fließsatz | + Zuschläge | **Gesamt** |
|---|---|---|---|
| Rechenweg A (300 W/S) | 303 | ~40 | **~343 Seiten** |
| Rechenweg B (Satzspiegel) | 363 | ~40 | **~403 Seiten** |

> **Planungswert: 340–400 Seiten, Mittelwert ~370.** KDP rundet auf eine gerade Seitenzahl auf.
>
> **Der Wert ist eine Schätzung und vor der Kalkulation durch die tatsächliche Seitenzahl des exportierten Druck-PDFs zu ersetzen.** Erst diese Zahl geht in den KDP-Druckkostenrechner und in den Cover-Vorlagengenerator.

**Folgerungen aus der Seitenzahl:**

1. **Bundsteg:** 301–500 Seiten → **0,625″ (15,88 mm)**. Das Bauskript setzt bereits 1,59 cm — passt. **Sollte die finale Seitenzahl 500 überschreiten, muss der Bundsteg auf 0,75″ (19,05 mm) erhöht und das Manuskript neu gesetzt werden** (was die Seitenzahl erneut verschiebt). KDP weist ausdrücklich darauf hin, den Bundsteg nach Festlegung der finalen Seitenzahl erneut zu prüfen.
2. **Maximalseitenzahl:** creme 776 ⚠️ / weiß 828 ⚠️ — beide klar eingehalten.
3. **Umfang gegenüber der GATE-2-Zielmarke:** Der Zielkorridor lag bei 256–320 Seiten. Das Manuskript ist gewachsen und liegt darüber. Zwei Stellschrauben, falls die Seitenzahl (und damit Druckkosten und Verkaufspreis) gesenkt werden soll:
   - **Quellenapparate kleiner setzen** (z. B. 9 pt / 12 pt Zeilenabstand statt 10,5 pt / 15 pt). Sie machen 17 % der Zeichen aus; die Ersparnis liegt in der Größenordnung von 15–20 Seiten und ist in Sachbüchern typografisch üblich.
   - **Zeilenabstand des Fließsatzes** von 15 pt auf 14 pt reduzieren (~7 % weniger Seiten) — Lesbarkeit vorher am Probedruck prüfen.
   - Beides ist eine Satzentscheidung, keine Kürzung des Inhalts.

### 6.3 Druckkosten

Belegt im Dossier (KDP „Druckkosten für Taschenbücher", de_DE):

```
Druckkosten = Fixkosten + (Seitenzahl × Kosten pro Seite)
```

> ⚠️ **Die konkreten Beträge für „Fixkosten" und „Kosten pro Seite" für den Marketplace Amazon.de sind im Dossier NICHT belegt.** Das Dossier hält ausdrücklich fest, dass sich Druckkosten ändern und aktuelle Werte separat zu prüfen sind.
>
> **[im KDP-Konto verifizieren]** Die beiden Beträge sind vor der Preisfestsetzung im **KDP-Druckkostenrechner** bzw. auf der Hilfeseite „Druckkosten für Taschenbücher" (de_DE) für die Kombination *Taschenbuch · 6 × 9″ · schwarze Tinte · cremefarbenes Papier · Marketplace Amazon.de · Währung EUR* abzulesen. Sie hängen zusätzlich davon ab, ob das Buch über Expanded Distribution verkauft wird.

**Ausfüllbare Kalkulation** (Werte aus dem KDP-Rechner eintragen):

| Größe | Symbol | Wert | Quelle |
|---|---|---|---|
| Fixkosten je Exemplar | `F` | **_____ €** | [im KDP-Konto verifizieren] |
| Kosten je Seite | `s` | **_____ €** | [im KDP-Konto verifizieren] |
| Finale Seitenzahl | `n` | **_____** | aus dem finalen Druck-PDF |
| **Druckkosten** | `D = F + n × s` | **_____ €** | Rechnung |

### 6.4 Royalty-Rechnung

Belegt: Die Royalty-Rate beträgt je nach Listenpreis und Marketplace **50 % oder 60 %**. Welche Rate für welchen Preisbereich auf Amazon.de gilt, ist im Dossier **nicht** aufgeschlüsselt.

> **[im KDP-Konto verifizieren]** Anwendbare Royalty-Rate für Taschenbücher auf Amazon.de sowie die Behandlung der Umsatzsteuer im Preisfeld (Brutto- oder Nettoangabe; für Bücher gilt in Deutschland ein ermäßigter Steuersatz — den anzuwendenden Satz und die KDP-Logik im Preisdialog ablesen, nicht annehmen).

**Rechenweg:**

```
Nettolistenpreis  N = Listenpreis (brutto) ÷ (1 + Umsatzsteuersatz)
Tantieme          T = (N × Royalty-Rate) − D

Mindestpreis, damit T ≥ 0:
   N_min = D ÷ Royalty-Rate
   Bruttolistenpreis_min = N_min × (1 + Umsatzsteuersatz)
```

**Ausfüllbare Kalkulation:**

| Größe | Wert | Quelle |
|---|---|---|
| Bruttolistenpreis DE (EUR) | **_____ €** | Entscheidung, siehe 6.5 |
| Umsatzsteuersatz Bücher DE | **_____ %** | [im KDP-Preisdialog verifizieren] |
| Nettolistenpreis `N` | **_____ €** | Rechnung |
| Royalty-Rate | **50 % oder 60 %** | [im KDP-Konto verifizieren] |
| Druckkosten `D` (aus 6.3) | **_____ €** | Rechnung |
| **Tantieme je verkauftem Exemplar `T`** | **_____ €** | Rechnung |

**Kontrollregel:** KDP akzeptiert keinen Listenpreis, der die Druckkosten nicht deckt — der Preisdialog zeigt den Mindestpreis an und weist einen zu niedrigen Preis zurück. Dieser angezeigte Mindestpreis ist die verlässlichste verfügbare Untergrenze; er ist zu notieren, bevor der Wunschpreis eingetragen wird.

### 6.5 Preisvorschlag DE/EU

**Ehrlicher Belegstand:** Das Vergleichstitel-Dossier `p2_vergleichstitel.md` hat Seitenzahlen, Verlage und Jahre erhoben, **aber keine Preise**. Ein Marktanker aus belegten Vergleichspreisen liegt also nicht vor.

**Vorgehen statt Zahl aus der Luft:**

1. **Marktanker erheben** (vor dem Upload, 30 Minuten Arbeit): Taschenbuchpreise der direkten Vergleichstitel auf ihren Produktseiten ablesen — Ait Si Abbou *Keine Panik, ist nur Technik* (224 S.) und *Menschenversteher* (256 S.), Lenzen *Künstliche Intelligenz* (272 S.) und *Der elektronische Spiegel* (270 S.), Precht (256 S.), Spitzer (336 S.), Meckel/Steinacker (400 S.), Nguyen-Kim (368 S.). Die Seitenzahlen aus dem Dossier machen die Preise direkt vergleichbar — insbesondere die 336–400-Seiten-Titel liegen im Umfangsbereich dieses Buches.
2. **Untergrenze bestimmen:** den von KDP angezeigten Mindestpreis aus 6.4 notieren. Bei ~370 Seiten ist der Druckkostenanteil erheblich; eine dünne Marge ist realistisch, wenn der Preis zu nah an den Vergleichstiteln der Publikumsverlage liegt — diese subventionieren Preise über Auflagenhöhe, was im Print-on-Demand nicht möglich ist.
3. **Preis festlegen** als: `max(Marktanker der 300–400-Seiten-Titel, Mindestpreis + gewünschte Marge)`, aufgerundet auf eine übliche Preisstufe (…,99 oder …,95).
4. **Marge gegenrechnen:** Formel aus 6.4 einsetzen. Liegt die Tantieme unter etwa 1,50 € je Exemplar, ist zuerst an der Seitenzahl zu arbeiten (6.2, Punkt 3) — nicht am Preis nach oben, weil ein deutlich über dem Marktanker liegender Preis bei einem unbekannten Debütautor die Verkäufe stärker drückt als die Mehrmarge einbringt.
5. **EU-Preise:** Für die übrigen EU-Marketplaces bietet KDP eine automatische Umrechnung aus dem DE-Preis an. Die umgerechneten Werte trotzdem einzeln prüfen und auf glatte Preisstufen korrigieren, und für jeden Marketplace kontrollieren, dass die Tantieme positiv bleibt. **[im KDP-Konto verifizieren]**, welche Marketplaces und Währungen aktuell angeboten werden.

**Buchpreisbindung (belegt, DE-spezifisch):** In Deutschland gilt die gesetzliche Buchpreisbindung. Praktische Folge laut KDP-Hilfe (de_DE): Der **Listenpreis muss über alle Vertriebskanäle in Deutschland identisch** sein. Wird der Preis auf Amazon.de geändert, ist er überall in Deutschland gleich zu ändern. Konsequenzen:

- Preisaktionen und Rabattaktionen für das gedruckte Buch sind in Deutschland **nicht** frei möglich — kein „Einführungspreis für zwei Wochen".
- Der Preis ist deshalb **vor** der Veröffentlichung sorgfältig zu setzen; er ist kein Marketinginstrument, das man später nachjustiert.
- Wird zusätzlich Expanded Distribution genutzt, ist die Preisgleichheit über alle deutschen Kanäle sicherzustellen.

> **Zusammengefasst:** Ein konkreter Eurobetrag wird hier bewusst **nicht** genannt, weil weder Druckkosten noch Vergleichspreise belegt vorliegen. Die Preisfindung erfolgt in einem Arbeitsschritt nach Schema 6.5, unmittelbar bevor der Preis im KDP-Formular eingetragen wird — und wird anschließend in diesem Dokument nachgetragen.

---

## 7. Veröffentlichungs-Checkliste

Sinnvolle Reihenfolge; jeder Block muss abgeschlossen sein, bevor der nächste beginnt, weil spätere Schritte auf den Ergebnissen früherer aufbauen (insbesondere: Seitenzahl → Bundsteg → Cover → Preis).

### Block A — Inhaltliche Fertigstellung (blockierend)

- [ ] **111 markierte Belegstellen am Volltext prüfen.** `03_pruefung/PRUEFLISTE_VOR_DRUCK.md` listet sie kapitelweise auf: Einleitung 5, Kap. 1 22, Kap. 2 4, Kap. 3 12, Kap. 4 10, Kap. 5 10, Kap. 6 7, Kap. 7 5, Kap. 8 4, Kap. 9 13, Kap. 10 6, Kap. 11 2, Kap. 12 7, Schluss 4. Hintergrund: In der Recherche war der Volltext-Abruf durch die Egress-Policy blockiert (HTTP 403); die Belege wurden über Suchindex-Triangulation gewonnen. Betroffen sind vor allem **Wortlaut-Zitate, Einzelanekdoten und exakte Zahlen**.
- [ ] **Priorität innerhalb der Prüfliste:** zuerst die Stellen, die im Text eine Argumentation tragen und bei denen die Prüfliste ausdrücklich „belegen oder streichen" vorsieht — u. a. Kap. 2 [10] (Harriet Davis 1890), Kap. 3 [4] (Telefon als Sittenproblem), Kap. 3 [18] (Hello Girls), Kap. 3 [19]/[20] (Blitzeinschlag Juli 1890, Gerüchtekampagne der Telegrafengesellschaften), Kap. 5 [3] (Zeitungsmeldung 1976).
- [ ] **Wortlaut-Zitate final festlegen**, insbesondere die deutschen Übersetzungen: Platon *Phaidros* 274c–275b, Trithemius *De laude scriptorum*, Erasmus *Festina lente*, Stevenson *A Plea for Gas Lamps*, Warren & Brandeis, Stoll (Newsweek 1995), Murrow und Minow.
- [ ] **Konstruiertes Rechenbeispiel Kap. 8 nachrechnen lassen** (`03_pruefung/rechenbeispiel_kap8_kontrollwerte.md`) — von einer zweiten Person, wie in der Prüfliste vorgesehen.
- [ ] Quellenapparat vereinheitlichen: kapitelweise Endnoten in eine konsistente Buchnummerierung überführen, Abgleich mit `QUELLEN.md`.
- [ ] Wiederholungs-/Humanisierungspass abschließen (Trithemius, Ludditen und der Taschenrechner-Test tauchen in mehreren Kapiteln auf — Dosierung prüfen).
- [ ] `FORTSCHRITT.md` aktualisieren: Die Umfangsangaben dort (~50.700 W) sind veraltet; der Stand liegt bei ~90.960 W.
- [ ] Schlusskorrektorat durch eine zweite Person (Orthografie, Typografie, Trennungen).

### Block B — Rechtliches und Frontmatter

- [ ] **Impressum/Copyright-Seite** erstellen: Copyright-Vermerk, Jahr, Autor, verantwortliche Person mit Anschrift (für den deutschen Markt), Imprint, ISBN, Rechtehinweise, Haftungsausschluss für externe Links. ⚠️ Das Dossier stuft die Impressumsanforderung als inhaltliche, nicht als KDP-Formatvorgabe ein — Ausgestaltung ggf. rechtlich prüfen lassen.
- [ ] **Zitatrechte prüfen:** Umfang der wörtlichen Zitate; alle Bildvorlagen (falls im Innenteil oder Cover verwendet) auf zweifelsfreie Gemeinfreiheit oder Lizenz prüfen und die Rechtelage dokumentieren.
- [ ] **Nennung realer Personen und Unternehmen** im Text gegenlesen (u. a. Kap. 12: Google/Gebru/Mitchell): Darstellung als unstrittiger Ablauf beibehalten, Wertungen als Wertungen gekennzeichnet lassen.
- [ ] **Frontmatter in der KDP-konformen Reihenfolge** aufbauen: Schmutztitel → Titelseite → Impressum/Copyright → (Widmung) → Inhaltsverzeichnis **mit Seitenzahlen** (kein Hyperlink-TOC wie im E-Book) → ggf. Vorwort.
- [ ] **Backmatter:** Über den Autor, Danksagung, ggf. gesammeltes Quellenverzeichnis.
- [ ] Autorenvita und Rückseitentext vom Autor freigeben lassen.

### Block C — Satz und Innenteil

- [ ] `04_produktion/build_docx.py` mit finalem Text laufen lassen.
- [ ] Satzentscheidung treffen: Quellenapparate kleiner setzen? Zeilenabstand? (siehe 6.2, Punkt 3) — vor dem Export, weil sie die Seitenzahl verschieben.
- [ ] **Druck-PDF exportieren:** PDF, empfohlen **PDF/X-1a**, **alle Schriften eingebettet** (in Acrobat unter Datei → Eigenschaften → Schriften: jeder Eintrag muss „Embedded" oder „Embedded Subset" zeigen). Georgia ist eine lizenzpflichtige Systemschrift — vor dem Satz prüfen, ob die Lizenz die Einbettung in ein kommerzielles Druck-PDF erlaubt, sonst auf eine frei lizenzierte Serifenschrift ausweichen.
- [ ] Bilder (falls vorhanden) ≥ 300 DPI, ≤ ~600 DPI; Graustufen; Datei ≤ 650 MB ⚠️.
- [ ] **Finale Seitenzahl `n` ablesen** und notieren — sie ist Eingangsgröße für Bundsteg, Cover und Preis.
- [ ] **Bundsteg gegen die finale Seitenzahl gegenprüfen** (24–150 → 0,375″ · 151–300 → 0,5″ · **301–500 → 0,625″** · 501–700 → 0,75″ · 701–828 → 0,875″) ⚠️ Tabelle im Konto verifizieren. Bei Wechsel der Staffel: neu setzen und die Seitenzahl erneut ablesen (Iteration einplanen).
- [ ] Außenränder ≥ 0,25″ (ohne Bleed) prüfen.
- [ ] Kontrolldurchgang am PDF: Kapitelanfänge auf der richtigen Seite, keine Schusterjungen/Hurenkinder, Inhaltsverzeichnis-Seitenzahlen stimmen, Kolumnentitel korrekt.

### Block D — Cover

- [ ] **Cover-Vorlage aus dem KDP-Cover-Vorlagengenerator ziehen** — mit Trim 6 × 9″, creme, schwarze Tinte und der **finalen** Seitenzahl. Erst daraus ergibt sich die verbindliche Rückenbreite.
- [ ] Cover nach Briefing (Abschnitt 5) gestalten; Barcode-Bereich unten rechts auf der Rückseite freihalten.
- [ ] Daumennagel-Test (120 px Breite) und Graustufen-Test bestehen.
- [ ] Cover-PDF: Schriften eingebettet, ≥ 300 DPI, CMYK.

### Block E — KDP-Konto: Verifikation vor dem Upload

**Dieser Block ist nicht optional.** Sämtliche in diesem Dokument mit ⚠️ oder **[im KDP-Konto verifizieren]** markierten Werte sind im eingeloggten Konto gegenzuprüfen, weil KDP Spezifikationen und Druckkosten regelmäßig ändert und der direkte Abruf der KDP-Seiten in der Recherche blockiert war.

- [ ] Trim-Size-Liste: Ist 6 × 9″ weiterhin als Standardgröße verfügbar und als „regular" eingestuft?
- [ ] Margin-/Bundsteg-Tabelle für die finale Seitenzahl.
- [ ] Maximalseitenzahl für schwarze Tinte auf creme (Dossier: 776 ⚠️) und die Abhängigkeit von der Trim-Size.
- [ ] Zeichenlimit der Buchbeschreibung (Dossier: ca. 4.000 ⚠️) am Zähler im Editor.
- [ ] **Unterstützte HTML-Tags** in der Beschreibung: Fassung 2.3 einfügen, speichern, Vorschau prüfen; bei Klartext-Anzeige auf 2.1 zurückfallen.
- [ ] **Deutsche Kategoriepfade** in der Auswahlliste für Amazon.de gegen Abschnitt 3 abgleichen und die tatsächlichen Bezeichnungen hier nachtragen.
- [ ] Hinweise zu Keyword-Feldern (Zeichenlimit, Verbotslisten).
- [ ] **Druckkosten** (Fixkosten + Kosten pro Seite) für Amazon.de, EUR, 6 × 9″, creme, schwarz.
- [ ] **Royalty-Rate** (50 % / 60 %) und Preisschwelle für Amazon.de.
- [ ] Umsatzsteuer-Logik im Preisdialog (brutto/netto).
- [ ] Maximale Dateigröße (Dossier: 650 MB ⚠️).
- [ ] Verfügbarkeit einer Vorbestellphase für Taschenbücher.
- [ ] Mindestseitenzahl für Rückenbedruckung.
- [ ] **Ergebnisse dieses Blocks in dieses Dokument zurückschreiben** — dann ist es beim nächsten Titel belastbar.

### Block F — Metadaten eintragen und veröffentlichen

- [ ] KDP-Titelanlage: Metadaten aus Abschnitt 1 übertragen.
- [ ] ISBN-Entscheidung treffen (1.1) — **irreversibel**, bevor der Titel veröffentlicht wird.
- [ ] Beschreibung aus Abschnitt 2 einfügen, Vorschau prüfen.
- [ ] 3 Kategorien und 7 Keywords setzen.
- [ ] Erwachseneninhalte: **Nein**.
- [ ] Manuskript-PDF und Cover-PDF hochladen.
- [ ] **Online-Vorschau (Previewer) vollständig durchblättern** — jede Seite, nicht nur stichprobenartig. Besonders: Kapitelanfänge, Tabellen/Aufzählungen, Bundsteg-Wirkung in der Doppelseite, Cover-Positionierung.
- [ ] **Druckexemplar bestellen (Proof/Author Copy) und in der Hand prüfen** — Farben, Papierton, Rückenbeschriftung, Lesbarkeit des Schriftgrads, Bundsteg im gebundenen Zustand. Erst danach freigeben.
- [ ] Preis setzen nach Schema 6.5; Tantieme für DE und alle aktivierten EU-Marketplaces gegenrechnen; **Buchpreisbindung beachten** (einheitlicher Preis über alle deutschen Kanäle).
- [ ] Expanded Distribution: bewusst an- oder abwählen.
- [ ] Veröffentlichen.

### Block G — Nach der Veröffentlichung

- [ ] Produktseite auf Amazon.de kontrollieren: Formatierung der Beschreibung, „Blick ins Buch", Kategoriezuordnung, Cover-Darstellung im Daumennagel.
- [ ] Author-Central-Profil anlegen: Autorenfoto, Vita, Buch verknüpfen.
- [ ] ⚠️ Nachmeldung weiterer Kategorien über den Support prüfen (bis zu 10 — nur über Sekundärquellen belegt).
- [ ] Nach 4–8 Wochen: Keywords anhand der Berichte auswerten und schwache Slots tauschen.
- [ ] Errata sammeln; Korrekturen gebündelt als neue Manuskriptversion hochladen.

---

## Anhang — Offene Punkte auf einen Blick

| # | Offener Punkt | Zuständig für die Klärung |
|---|---|---|
| 1 | 111 Belegstellen am Volltext prüfen | Autor / Faktencheck |
| 2 | Deutsche Kategoriepfade (Erst-, Zweit-, Drittwahl) | KDP-Konto |
| 3 | Unterstützte HTML-Tags in der Beschreibung | KDP-Editor (Vorschau) |
| 4 | Zeichenlimit Beschreibung (ca. 4.000 ⚠️) | KDP-Editor |
| 5 | Druckkosten: Fixkosten + Kosten je Seite (EUR, Amazon.de) | KDP-Druckkostenrechner |
| 6 | Royalty-Rate 50 % / 60 % und Preisschwelle für Amazon.de | KDP-Konto |
| 7 | Umsatzsteuerlogik im Preisdialog | KDP-Preisdialog |
| 8 | Rückenbreiten-Faktor je Papiersorte | KDP-Cover-Vorlagengenerator |
| 9 | Mindestseitenzahl für Rückenbedruckung; Barcode-Feldmaße | KDP-Cover-Vorlage |
| 10 | Bundsteg-Staffel gegen finale Seitenzahl ⚠️ | KDP-Konto |
| 11 | Max. Seitenzahl creme 776 ⚠️ / weiß 828 ⚠️ | KDP-Konto |
| 12 | Max. Dateigröße 650 MB ⚠️ | KDP-Konto |
| 13 | Vorbestellphase für Taschenbücher verfügbar? | KDP-Konto |
| 14 | Nachträgliche Kategorien bis 10 ⚠️ | KDP-Support |
| 15 | Preise der Vergleichstitel (Marktanker) — im Dossier nicht erhoben | eigene Erhebung auf den Produktseiten |
| 16 | Schrift-Lizenz Georgia für Einbettung in kommerzielles Druck-PDF | Autor / Lizenzbedingungen |
| 17 | Finale Seitenzahl aus dem Druck-PDF | Satz |
| 18 | ISBN-Entscheidung (Gratis vs. eigene) | Autor |
