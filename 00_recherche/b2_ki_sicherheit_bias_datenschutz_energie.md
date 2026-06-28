# KI-Risiken und Schutzmechanismen: Sicherheit/Missbrauch, Bias/Fairness, Datenschutz, Energie/Umwelt

**Recherchedossier für ein deutschsprachiges Sachbuch über KI**
Stand / Abrufdatum aller Quellen: 2026-06-28

---

## Methodische Vorbemerkung zur Quellenprüfung

Alle unten verwendeten Quellen wurden über Websuche identifiziert; Titel,
Autor/Institution, Jahr, Kernaussagen und URL wurden über die
Suchmaschinen-Indexierung gegengeprüft (häufig mit wörtlicher Textextraktion aus
der Zielseite). **Wichtige technische Einschränkung:** In der Rechercheumgebung
war der direkte Einzelseiten-Abruf (WebFetch sowie curl) durch die Egress-Policy
für sämtliche Zielhosts gesperrt (HTTP 403 / CONNECT-Denial). Die Existenz und
der Inhalt jeder URL konnten daher nur über die Suchmaschinen-Extraktion
bestätigt werden, nicht durch vollständigen Einzelabruf der Seite. Vor
Drucklegung sollten alle als Wortlaut wiedergegebenen Zitate sowie die zentralen
Zahlen noch einmal an der Primärquelle gegengelesen werden (insbesondere die mit
**[PRÜFEN]** markierten Stellen). Stark schwankende Schätzungen sind als
Spannbreite mit Quelle gekennzeichnet; unsichere Einzelwerte wurden weggelassen
oder ausdrücklich als Schätzung markiert.

Grundhaltung dieses Dossiers gemäß Auftrag: **ehrlich über Risiken, ohne
Panikmache.** Wo eine populäre Behauptung sich als überzogen, widerlegt oder
mathematisch zwangsläufig erweist (z. B. Apple-Card, COMPAS-"Unmöglichkeits"-
Debatte, 519-ml-Wasserzahl), ist das ausdrücklich vermerkt.

---

## 1. Sicherheit / Missbrauch

### 1.1 Risiko

**Maßgebliche Gesamtschau – International AI Safety Report.** Der erste
*International AI Safety Report* wurde im Januar 2025 vor dem AI Action Summit in
Paris veröffentlicht. Er wurde von 96 Fachleuten unter Vorsitz von Yoshua Bengio
erstellt und von 30 Ländern sowie EU, OECD und UN unterstützt; er ist die bislang
größte internationale wissenschaftliche Zusammenschau zu Fähigkeiten und Risiken
universeller ("general-purpose") KI. Der Bericht gibt **keine** politischen
Empfehlungen, sondern bündelt den Evidenzstand. [1]

Belegte / mit Evidenz unterlegte Missbrauchsrisiken laut Bericht:

- **Cyber:** Universelle KI kann es Angreifern unterschiedlichen Könnens
  erleichtern oder beschleunigen, Cyberangriffe durchzuführen; aktuelle Systeme
  zeigen demonstrierte Fähigkeiten bei Cybersicherheitsaufgaben **geringer und
  mittlerer Komplexität.** [1]
- **Bio/Chemie:** Neuere Systeme zeigten "einige Fähigkeit", Anleitungen und
  Fehlerbehebung zur Reproduktion bekannter biologischer/chemischer Waffen zu
  liefern und das Design neuer toxischer Verbindungen zu unterstützen. 2025
  veröffentlichten mehrere KI-Firmen Modelle bewusst mit zusätzlichen
  Sicherheitsvorkehrungen, weil Pre-Deployment-Tests die Möglichkeit nicht
  ausschließen konnten, dass die Modelle Laien bei der Entwicklung solcher Waffen
  "meaningfully" helfen könnten. [1][2]
- **Desinformation / Deepfakes:** Technische Maßnahmen von Wasserzeichen bis zur
  Detektion KI-generierter Inhalte werden im Bericht behandelt; gleichzeitig wird
  betont, dass versierte Angreifer aktuelle Schutzmaßnahmen oft umgehen können und
  die reale Wirksamkeit vieler Safeguards unsicher ist. [3]

**Was ist eher spekulativ?** Der Bericht ist hier bewusst zurückhaltend. Zum
"Kontrollverlust" (loss of control) hält er fest: **breiter Konsens, dass
heutige universelle KI nicht über die Fähigkeiten verfügt, ein
Kontrollverlust-Risiko darzustellen.** Die Experteneinschätzung zur
Wahrscheinlichkeit in den nächsten Jahren gehe jedoch "stark auseinander" – von
"implausibel" bis "wahrscheinlich". Der Bericht betont ausdrücklich, dass zu
vielen Fragen "noch kein wissenschaftlicher Konsens geschmiedet" sei und er
deshalb in vielen Fällen keine "confident views" vorlege. [4]

**Wahlmanipulation / Deepfakes – belegt vs. überzeichnet.** Die Erwartung, 2024
werde das "Jahr der KI-Wahlmanipulation", hat sich in dieser Schärfe **nicht
bestätigt.** Recherchen zeigen: "Cheap fakes" (einfache, nicht-KI-Manipulation)
wurden deutlich häufiger eingesetzt als KI-Generate. Dokumentierte Einzelfälle
existieren aber sehr wohl, u. a.: KI-generierte Biden-Robocalls erreichten bis zu
ca. 25.000 Wähler in New Hampshire (Vorwahl 2024); in der Slowakei kursierte zwei
Tage vor der Wahl gefälschtes Audio eines Kandidaten; Rumänien annullierte 2024
eine Präsidentschaftswahl nach Hinweisen auf (auch KI-gestützte) ausländische
Einflussnahme. Die *kausale* Wirkung auf Wahlergebnisse ist in den meisten Fällen
**nicht quantifiziert** und methodisch schwer messbar. [5]

### 1.2 Schutz / Einordnung

- **AI-Safety-Institute / staatliche Stellen.** Großbritannien und die USA
  gründeten 2023/24 AI Safety Institutes für Modellevaluierungen. 2025 erfolgten
  Umbenennungen mit Akzentverschiebung Richtung "Security": Das UK-Institut wurde
  im Februar 2025 zum **AI Security Institute**; das US-Institut wurde im Juni
  2025 zum **Center for AI Standards and Innovation (CAISI)** umbenannt, mit Fokus
  auf "demonstrierbare Risiken" wie Cybersicherheit, Biosicherheit und chemische
  Waffen (nach Aufhebung der Executive Order 14110 im Januar 2025). [6]
- **Frontier-AI-Safety-Frameworks.** Laut Folge-Updates des Safety Reports hat
  sich die Zahl der Unternehmen mit veröffentlichten Frontier-AI-Safety-Frameworks
  seit Anfang 2025 **mehr als verdoppelt;** Techniken zum Training sicherer
  Modelle und zur Detektion KI-generierter Inhalte wurden verfeinert. Realistische
  Einschränkung: "significant gaps remain" – versierte Angreifer umgehen aktuelle
  Schutzmaßnahmen oft. [3]
- **Gegenmaßnahmen Desinformation:** Herkunftsnachweise/Wasserzeichen (z. B.
  C2PA-Standard – im Buch als technischer Ansatz erwähnenswert), Detektionstools
  und Plattform-Kennzeichnungspflichten; ergänzt durch Transparenzpflichten des
  EU AI Act (Art. 50, Kennzeichnung KI-generierter Inhalte, siehe Feld 3).

**Autonome Waffen** wurden in den geprüften Quellen dieses Dossiers nicht mit
belastbaren neuen Zahlen behandelt; für das Buch sollte die Debatte
(UN-Diskussionen über "lethal autonomous weapons systems"/LAWS) bei Bedarf
gesondert mit Primärquellen recherchiert werden, statt hier ungesicherte Angaben
aufzunehmen.

---

## 2. Bias / Fairness

### 2.1 Risiko – dokumentierte Fälle

- **COMPAS / ProPublica (2016).** Die Untersuchung "Machine Bias" von J. Angwin,
  J. Larson, S. Mattu und L. Kirchner analysierte das kommerzielle
  Rückfallprognose-Tool COMPAS (Northpointe) anhand von Daten aus Broward County,
  Florida. Kernbefund: Unter den **nicht** erneut Straffälligen wurden **45 % der
  schwarzen** Angeklagten fälschlich als künftige Rückfalltäter ("high risk")
  eingestuft, aber nur **24 % der weißen** – also etwa doppelt so hohe
  Falsch-Positiv-Rate für Schwarze. [7]
- **Amazon-Recruiting-Tool (2018).** Reuters (J. Dastin) berichtete im Oktober
  2018, dass Amazon ein experimentelles KI-Rekrutierungstool einstellte, weil es
  Frauen benachteiligte. Ursache: Training auf 10 Jahren überwiegend männlicher
  Bewerbungen; das System bewertete u. a. Lebensläufe mit dem Wort "women's" oder
  Namen reiner Frauen-Colleges schlechter. Amazon verlor das Vertrauen, das Tool
  überhaupt neutral machen zu können, und stellte es ein. [8]
- **Gender Shades (Buolamwini & Gebru, 2018).** Die Studie testete drei
  kommerzielle Gesichts-/Geschlechtsklassifikationssysteme. Höchste Fehlerrate bei
  **dunkelhäutigen Frauen: bis zu 34,7 %;** niedrigste bei hellhäutigen Männern:
  **0,8 %.** Belegte zugleich starke Verzerrung der Trainingsdatensätze (z. B.
  überwiegend hellhäutige Subjekte). Wirkung: maßgeblicher Anstoß für Debatte um
  repräsentative Trainingsdaten. [9]
- **Bias in LLMs (aktuelle Forschung).** Mehrere 2024/2025-Studien dokumentieren
  reproduzierbare Verzerrungen, u. a.: Bevorzugung weißer/männlicher Namen bei
  simulierten Auswahlentscheidungen; geschlechterstereotype Sprache in
  KI-generierten Empfehlungsschreiben (Frauen eher "communal", Männer eher
  "agentic"); stereotype Emotionszuschreibung. Es existieren strukturierte
  Benchmarks (z. B. GenderBench, 2025) zur Messung. [10]

### 2.2 Schutz / Einordnung

- **COMPAS – die faire Differenzierung.** Northpointe entgegnete, die ungleichen
  Falsch-Positiv-Raten ergäben sich aus **unterschiedlichen Basisraten** der
  Rückfälligkeit. Mathematisch wurde dies durch das **"Unmöglichkeits-Theorem"**
  (Chouldechova 2017; Kleinberg, Mullainathan, Raghavan 2016) gestützt: Bei
  ungleichen Basisraten können **Kalibrierung** (predictive parity) und
  **Fehlerratenbalance** (gleiche Falsch-Positiv-/Falsch-Negativ-Raten) **nicht
  gleichzeitig** erfüllt werden – außer im Trivialfall. Für das Buch zentral:
  "Bias" ist hier nicht nur ein Daten- oder Programmierfehler, sondern ein
  **unvermeidbarer Zielkonflikt** zwischen legitimen Fairness-Definitionen. [11]
- **Apple Card – Vorwurf untersucht, nicht bestätigt.** Nach viralen Vorwürfen
  (2019, u. a. D. H. Hansson, S. Wozniak: deutlich höhere Kreditlinien für Männer)
  untersuchte das **New York State Department of Financial Services** rund 400.000
  NY-Bewerbungen. Ergebnis (März 2021): **kein** Nachweis unrechtmäßiger
  Diskriminierung nach Fair-Lending-Recht; keine Disparität bei vergleichbaren
  Kreditmerkmalen; Geschlecht war kein Faktor. Wichtig für eine ehrliche
  Darstellung: ein **medial stark skandalisierter Fall, der einer Prüfung nicht
  standhielt** – die Behörde mahnte zugleich Modernisierung von Kredit-Scoring und
  Antidiskriminierungsregeln an. [12]
- **Gegenmaßnahmen LLM-Bias:** dokumentierte technische Ansätze umfassen
  ausgewogenere Trainingsdaten, Debias-Fine-Tuning, Instruction-/Prompt-Methoden,
  RLHF sowie standardisierte Bias-Benchmarks für Audits. [10]

---

## 3. Datenschutz

### 3.1 Risiko

- **Trainingsdaten & personenbezogene Daten.** Generative Modelle werden auf
  großen, teils aus dem Web gescrapten Korpora trainiert, die personenbezogene
  Daten enthalten können. Kernfragen: Rechtsgrundlage, Transparenz, Auskunfts- und
  Löschrechte sowie das Risiko, dass Modelle personenbezogene Daten "memorieren"
  und über Anfragen wieder ausgeben.
- **Bekannter Vorfall – OpenAI/Italien.** Die italienische Datenschutzbehörde
  **Garante** verhängte am 20. Dezember 2024 eine Geldbuße von **15 Mio. €** gegen
  OpenAI. Vorwürfe: Verarbeitung personenbezogener Daten zum Training ohne
  ausreichende Rechtsgrundlage, Verstoß gegen Transparenz-/Informationspflichten,
  fehlende Altersverifikation (<13 Jahre), Nichtmeldung einer Datenschutzverletzung
  vom März 2023. **Wichtige Einordnung:** OpenAI legte Berufung ein; ein
  italienisches Gericht **annullierte die Buße 2026 aus Zuständigkeitsgründen
  (jurisdiktional), nicht wegen Entkräftung der inhaltlichen DSGVO-Vorwürfe.**
  [13] **[PRÜFEN]** (genaues Urteilsdatum 2026 vor Drucklegung verifizieren).

### 3.2 Schutz / Einordnung

- **EU AI Act – Kernpunkte & Zeitplan.** Erste umfassende horizontale
  KI-Regulierung weltweit. Veröffentlicht im EU-Amtsblatt am 12. Juli 2024, **in
  Kraft seit 1. August 2024;** gestufte Anwendung (Art. 113):
  - **2. Februar 2025:** Verbote (verbotene Praktiken, Art. 5) anwendbar.
  - **2. August 2025:** Pflichten für GPAI-Modelle (general-purpose AI) und
    Governance; Mitgliedstaaten benennen zuständige Behörden.
  - **2. August 2026:** Großteil der Regeln, insb. Hochrisiko-Systeme nach Anhang
    III sowie Transparenzpflichten (Art. 50), anwendbar.
  - **2. August 2027:** weitere Hochrisiko-Pflichten (Sicherheitskomponenten in
    bereits regulierten Produkten) sowie volle Anwendbarkeit. [14]
- **Risikobasierter Ansatz (4 Stufen):** unannehmbares Risiko / **verboten**
  (z. B. Social Scoring durch Behörden, untargeted Scraping von Gesichtsbildern,
  Emotionserkennung am Arbeitsplatz/in Bildung, bestimmte biometrische
  Echtzeit-Fernidentifizierung); **Hochrisiko** (strenge Anforderungen);
  **begrenztes Risiko/Transparenz** (Kennzeichnungspflichten); **minimales
  Risiko** (weitgehend frei). Bußgelder gestaffelt: bis **35 Mio. € oder 7 %** des
  weltweiten Jahresumsatzes (verbotene Praktiken), bis **15 Mio. € / 3 %**
  (Hochrisiko-Verstöße), bis **7,5 Mio. € / 1 %** (Informationsverstöße); jeweils
  der höhere Betrag. [15]
- **DSGVO-Linie der Datenschutzbehörden – EDPB-Opinion 28/2024.** Der Europäische
  Datenschutzausschuss verabschiedete am **17. Dezember 2024** eine Stellungnahme
  zu KI-Modellen. Kernaussagen: (1) Ob ein KI-Modell als **anonym** gilt, ist im
  Einzelfall zu prüfen – es muss "sehr unwahrscheinlich" sein, Personen direkt
  oder indirekt zu identifizieren oder personenbezogene Daten per Anfrage zu
  extrahieren. (2) **Berechtigtes Interesse** kann taugliche Rechtsgrundlage für
  Entwicklung/Einsatz sein, aber nur bei bestandenem Drei-Stufen-Test
  (Notwendigkeit + Interessenabwägung). (3) Wurden Daten ursprünglich
  **unrechtmäßig** verarbeitet, kann das die weitere Nutzung des Modells
  beeinträchtigen. Tenor: "GDPR principles support responsible AI" – DSGVO und
  KI-Entwicklung sind vereinbar, aber an Bedingungen geknüpft. [16]

---

## 4. Energie / Umwelt

### 4.1 Risiko

**Maßgebliche Quelle – IEA, *Energy and AI* (April 2025),** erste umfassende
globale Analyse der IEA zu Energie und KI. Belastbare Kernzahlen:

- **Status 2024:** Rechenzentren verbrauchten weltweit rund **415 TWh** Strom,
  etwa **1,5 %** des globalen Stromverbrauchs. Wachstum seit 2017 ca. **12 % pro
  Jahr** (mehr als viermal schneller als der Gesamtstromverbrauch). [17]
- **Projektion (Base Case):** Verdopplung auf rund **945 TWh bis 2030** (knapp
  3 % des globalen Stromverbrauchs; etwas mehr als der heutige Stromverbrauch
  Japans); rund **1.200 TWh bis 2035.** KI ist der stärkste Treiber: Strombedarf
  KI-optimierter Rechenzentren soll sich **bis 2030 mehr als vervierfachen.** [18]
- **2025-Update:** Der Stromverbrauch KI-fokussierter Rechenzentren stieg 2025 um
  rund **50 %.** [17]
- **Energiequellen:** In den nächsten ~5 Jahren decken Erneuerbare knapp die
  Hälfte der Zusatznachfrage, gefolgt von Erdgas und Kohle; Kernkraft gewinnt
  gegen Ende des Jahrzehnts an Bedeutung. [18]
- **Wasser (mit Vorsicht zu lesen):** Die IEA schätzte den Wasserverbrauch von
  Rechenzentren 2023 auf ca. **560 Mrd. Liter,** mit möglichem Anstieg auf ca.
  **1.200 Mrd. Liter bis 2030** – ohne klare Aufschlüsselung des KI-Anteils. Die
  Schätzungen zum reinen KI-Wasserfußabdruck schwanken **stark** (eine Studie
  nennt 312,5–764,6 Mrd. Liter für 2025); solche Werte sind methodisch unsicher
  und als Spannbreite zu verstehen. [19]

**Einzelmodell / Einzelanfrage – realistische Einordnung statt Extremzahlen:**

- **Training GPT-3:** ca. **1.287 MWh,** ca. **552 Tonnen CO2** (Patterson et al.,
  2021). Bezugsgröße der Autoren: vergleichbar mit mehreren Hin- und
  Rückflügen San Francisco–New York eines Verkehrsflugzeugs. [20]
- **Pro Anfrage (ChatGPT):** OpenAI-CEO Sam Altman nannte (Juni 2025) ca. **0,34
  Wh** Strom und ca. **0,3 ml** Wasser pro Anfrage; eine unabhängige Schätzung von
  **Epoch AI (2025)** für eine typische GPT-4o-Anfrage liegt bei ca. **0,3 Wh** –
  also rund **zehnmal niedriger** als ältere, oft zitierte Werte. **Wichtige
  Gegenüberstellung:** Die populäre Zahl "**ca. 500 ml Wasser pro 100-Wort-
  Antwort**" stammt aus einem Preprint der UC Riverside (Li et al., 2023) und
  schließt indirekten Wasserverbrauch der Stromerzeugung ein; sie ist methodisch
  umstritten und sollte **nicht** als gesicherter Standardwert dargestellt werden.
  [21][22]

### 4.2 Schutz / Einordnung

- **Effizienzgewinne.** Laut IEA verbessert sich die Energieeffizienz **pro
  KI-Aufgabe** "in einem in der Energiegeschichte beispiellosen Tempo" – der
  Energieverbrauch pro Aufgabe sei zuletzt jährlich um mindestens eine
  Größenordnung gesunken (Hardware + Software). [18]
- **Realistische Gesamteinordnung.** Selbst in der Verdopplungs-Projektion bleiben
  Rechenzentren bei knapp **3 % des globalen Stromverbrauchs bis 2030** – relevant
  und schnell wachsend, aber **kein dominanter Anteil** am Weltstrom. Lokale
  Belastungen (regionale Netz- und Wasserstress-Effekte an Standorten mit
  Cluster-Ansiedlung) sind das ernstere, aber differenziert zu betrachtende
  Problem. [17][18]
- **Gegenmaßnahmen.** Ausbau Erneuerbarer/Kernkraft für RZ-Versorgung,
  effizientere Kühlung (geringerer Wasserverbrauch), Standortwahl nach
  Netz-/Wasserlage, Transparenz-/Reporting-Pflichten. Die IEA betont zugleich das
  **Potenzial von KI**, den Energiesektor effizienter zu machen (Netzsteuerung,
  Optimierung) – die Bilanz ist also nicht einseitig negativ. [18]

---

## Quellenliste

[1] Bengio, Y. et al. (International AI Safety Report Expert Panel):
International AI Safety Report 2025. 2025. Vorgelegt vor dem AI Action Summit
Paris; arXiv-Fassung 2501.17805 / internationalaisafetyreport.org.
https://internationalaisafetyreport.org/publication/international-ai-safety-report-2025
(Abruf: 2026-06-28). — *Belegnotiz:* 96 Experten, Vorsitz Bengio; größte
internationale Zusammenschau; Cyberfähigkeiten geringer/mittlerer Komplexität,
Bio/Chemie "einige Fähigkeit". (Verifiziert über Suchextraktion; PDF-Direktabruf
durch Egress-Policy gesperrt.)

[2] Transformer News / globalpolicywatch / insideglobaltech (Berichterstattung
zu International AI Safety Report, Updates 2025/2026): Bio- und Cyberrisiken,
Modellveröffentlichungen 2025 mit Zusatz-Safeguards. 2025/2026.
https://internationalaisafetyreport.org/publications (Abruf: 2026-06-28). —
*Belegnotiz:* mehrere KI-Firmen veröffentlichten 2025 Modelle mit zusätzlichen
Safeguards, weil Bio-Uplift für Laien nicht ausgeschlossen werden konnte.
**[PRÜFEN]** an Originalbericht 2026.

[3] International AI Safety Report 2025 – Second Key Update: Technical Safeguards
and Risk Management. 2025. arXiv:2511.19863.
https://arxiv.org/abs/2511.19863 (Abruf: 2026-06-28). — *Belegnotiz:* Zahl der
Frontier-AI-Safety-Frameworks seit Anfang 2025 mehr als verdoppelt; zugleich
"significant gaps remain", versierte Angreifer umgehen Schutzmaßnahmen oft.

[4] International AI Safety Report 2025 (Abschnitt loss of control / Konsensgrad).
2025. internationalaisafetyreport.org (Volltext-PDF, engl.).
https://internationalaisafetyreport.org/publication/international-ai-safety-report-2025
(Abruf: 2026-06-28). — *Belegnotiz:* breiter Konsens, dass heutige KI keinen
Kontrollverlust ermöglicht; Experteneinschätzungen zur Zukunft divergieren stark;
Bericht legt bewusst keine "confident views" vor.

[5] State of Surveillance / Recorded Future u. a. (zusammenfassende Recherche zu
KI-Desinformation Wahlen 2024–2025). 2025. — *Belegnotiz:* "Cheap fakes" 7×
häufiger als KI-Generate; Einzelfälle (NH-Biden-Robocalls ~25.000; Slowakei-Audio;
Rumänien-Annullierung); kausale Wirkung meist nicht quantifiziert.
https://stateofsurveillance.org/articles/surveillance/ai-election-disinformation-2024-2025/
(Abruf: 2026-06-28). **[PRÜFEN]** Einzelzahlen an Primärberichten.

[6] FedScoop / Harvard Kennedy School / Wikipedia (AI safety institute): Umbenennung
US-Institut zu CAISI (Juni 2025) und UK-Institut zu AI Security Institute (Feb.
2025). 2025. https://fedscoop.com/trump-administration-rebrands-ai-safety-institute-aisi-caisi/
(Abruf: 2026-06-28). — *Belegnotiz:* Fokus CAISI auf demonstrierbare Risiken
(Cyber, Bio, Chemie); Kontext Aufhebung EO 14110.

[7] Angwin, J.; Larson, J.; Mattu, S.; Kirchner, L. (ProPublica): Machine Bias /
How We Analyzed the COMPAS Recidivism Algorithm. 2016. ProPublica.
https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm
(Abruf: 2026-06-28). — *Belegnotiz:* Falsch-Positiv 45 % (schwarz) vs. 24 %
(weiß) unter den nicht erneut Straffälligen; Tool COMPAS/Northpointe; Broward
County. (Direktabruf 403; Inhalt über Suchextraktion bestätigt.)

[8] Dastin, J. (Reuters): Amazon scraps secret AI recruiting tool that showed
bias against women. 2018. Reuters.
https://www.technologyreview.com/2018/10/10/139858/amazon-ditched-ai-recruitment-software-because-it-was-biased-against-women/
(Sekundärbeleg MIT Tech Review zum Reuters-Bericht) (Abruf: 2026-06-28). —
*Belegnotiz:* Training auf 10 J. überwiegend männlicher Lebensläufe; Abwertung
von "women's"/Frauen-Colleges; Projekt eingestellt.

[9] Buolamwini, J.; Gebru, T.: Gender Shades: Intersectional Accuracy Disparities
in Commercial Gender Classification. 2018. Proceedings of Machine Learning
Research (Conf. on Fairness, Accountability and Transparency); MIT Media Lab.
https://www.media.mit.edu/publications/gender-shades-intersectional-accuracy-disparities-in-commercial-gender-classification/
(Abruf: 2026-06-28). — *Belegnotiz:* Fehlerrate dunkelhäutige Frauen bis 34,7 %,
hellhäutige Männer 0,8 %; drei kommerzielle Systeme.

[10] Sammelbeleg LLM-Bias-Forschung 2024/2025: u. a. GenderBench (arXiv:2505.12054,
2025); "More Women, Same Stereotypes" (arXiv:2503.15904, 2025); Studien zu
Namen-/Hiring-Bias und Empfehlungsschreiben. https://arxiv.org/pdf/2505.12054
(Abruf: 2026-06-28). — *Belegnotiz:* dokumentierte Bevorzugung weißer/männlicher
Namen; "communal" vs. "agentic"-Sprache; Mitigations-Techniken.

[11] Chouldechova, A. (2017): Fair prediction with disparate impact (Big Data);
Kleinberg, J.; Mullainathan, S.; Raghavan, M. (2016): Inherent Trade-Offs in the
Fair Determination of Risk Scores. arXiv:1703.00056 u. a.
https://arxiv.org/pdf/1703.00056 (Abruf: 2026-06-28). — *Belegnotiz:*
Unmöglichkeits-Theorem: Kalibrierung und Fehlerratenbalance bei ungleichen
Basisraten nicht gleichzeitig erfüllbar; erklärt COMPAS-Debatte.

[12] New York State Department of Financial Services: Report on the Apple Card
Investigation. März 2021. NY DFS.
https://www.dfs.ny.gov/reports_and_publications/202103_report_apple_card_investigation
(Abruf: 2026-06-28). — *Belegnotiz:* ~400.000 NY-Bewerbungen geprüft; kein
Nachweis unrechtmäßiger Diskriminierung; Geschlecht kein Faktor; Vorwurf medial
überzeichnet.

[13] Garante per la protezione dei dati personali / Euronews / Reuters-Bericht:
Italien verhängt 15 Mio. € Bußgeld gegen OpenAI (20.12.2024); Annullierung durch
ital. Gericht 2026 (jurisdiktional).
https://www.euronews.com/next/2024/12/20/italys-privacy-watchdog-fines-openai-15-million-after-probe-into-chatgpt-data-collection
(Abruf: 2026-06-28). — *Belegnotiz:* Rechtsgrundlage/Transparenz, Altersverif.,
Breach-März-2023; Annullierung 2026 nicht wegen Entkräftung der DSGVO-Vorwürfe.
**[PRÜFEN]** genaues Urteilsdatum/Instanz 2026.

[14] AI Act Service Desk (Europäische Kommission) / artificialintelligenceact.eu:
Implementation Timeline EU AI Act. 2024/2025. In Kraft 1.8.2024; Verbote
2.2.2025; GPAI 2.8.2025; Hochrisiko/Transparenz 2.8.2026; volle Anwendbarkeit
2.8.2027. https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act
(Abruf: 2026-06-28). — *Belegnotiz:* gestufte Anwendung nach Art. 113.

[15] EU AI Act, Art. 99 (Penalties) / Verordnung (EU) 2024/1689. 2024.
EUR-Lex / artificialintelligenceact.eu.
https://artificialintelligenceact.eu/article/99/ (Abruf: 2026-06-28). —
*Belegnotiz:* Bußgelder bis 35 Mio. €/7 % (verbotene Praktiken), 15 Mio. €/3 %
(Hochrisiko), 7,5 Mio. €/1 % (Informationsverstöße); risikobasierte 4-Stufen-
Systematik.

[16] European Data Protection Board (EDPB): Opinion 28/2024 on certain data
protection aspects related to the processing of personal data in the context of
AI models. 17.12.2024. EDPB.
https://www.edpb.europa.eu/system/files/2024-12/edpb_opinion_202428_ai-models_en.pdf
(Abruf: 2026-06-28). — *Belegnotiz:* Anonymität fallweise; berechtigtes Interesse
mit Drei-Stufen-Test; Folgen unrechtmäßiger Datenverarbeitung; "GDPR principles
support responsible AI".

[17] International Energy Agency (IEA): Energy and AI – Executive summary / News
(Data centre electricity use surged in 2025). April 2025 / 2025-Update. IEA.
https://www.iea.org/reports/energy-and-ai/executive-summary (Abruf: 2026-06-28).
— *Belegnotiz:* 2024: 415 TWh / 1,5 % global; +12 %/Jahr seit 2017; KI-fokussierte
RZ +50 % in 2025. (Direktabruf 403; Zahlen über Suchextraktion bestätigt.)

[18] International Energy Agency (IEA): Energy and AI – Energy demand from AI /
Pressemitteilung. April 2025. IEA.
https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai (Abruf: 2026-06-28).
— *Belegnotiz:* Base Case 945 TWh (2030, ~3 % global), 1.200 TWh (2035);
KI-RZ-Bedarf bis 2030 mehr als vervierfacht; Erneuerbare ~½ der Zusatznachfrage;
Effizienz pro Aufgabe ~Größenordnung/Jahr.

[19] IEA-Wasserzahlen (referiert über Pew Research / ELI Fact Sheet / ScienceDirect)
sowie Studie zu KI-Wasserfußabdruck-Szenarien. 2025/2026. — *Belegnotiz:* RZ-
Wasserverbrauch ~560 Mrd. l (2023), ~1.200 Mrd. l (2030); KI-Wasserfußabdruck-
Schätzung 312,5–764,6 Mrd. l (2025) – stark schwankend, methodisch unsicher.
https://www.pewresearch.org/short-reads/2025/10/24/what-we-know-about-energy-use-at-us-data-centers-amid-the-ai-boom/
(Abruf: 2026-06-28). **[PRÜFEN]** Wasserzahlen an IEA-Primärtext.

[20] Patterson, D. et al.: Carbon Emissions and Large Neural Network Training.
2021. arXiv:2104.10350. https://arxiv.org/pdf/2104.10350 (Abruf: 2026-06-28). —
*Belegnotiz:* GPT-3-Training ~1.287 MWh, ~552 t CO2.

[21] Epoch AI: How much energy does ChatGPT use? 2025. epoch.ai.
https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use (Abruf:
2026-06-28). — *Belegnotiz:* typische GPT-4o-Anfrage ~0,3 Wh, ~10× niedriger als
ältere Schätzungen; Altman-Angabe 0,34 Wh / 0,3 ml konsistent (DCD-Bericht).
https://www.datacenterdynamics.com/en/news/sam-altman-chatgpt-queries-consume-034-watt-hours-of-electricity-and-0000085-gallons-of-water/

[22] Li, P. et al. (UC Riverside): Making AI Less "Thirsty" – Water footprint of
AI. 2023 (Preprint, mehrfach aktualisiert). arXiv:2304.03271.
https://arxiv.org/pdf/2505.09598 (verwandter Benchmark "How Hungry is AI?", 2025,
zur Einordnung) (Abruf: 2026-06-28). — *Belegnotiz:* populäre Zahl ~500 ml/
100-Wort-Antwort inkl. indirektem Wasser der Stromerzeugung; methodisch
umstritten, nicht als Standardwert darstellen. **[PRÜFEN]** Originalfassung
Li et al. (arXiv:2304.03271).
