# Kapitel 9 — Die Stimmen der Propheten

Es gibt eine Sorte Woche, in der du morgens liest, dass die künstliche Intelligenz gerade dabei ist, die Medizin neu zu erfinden, und abends, dass dieselbe Technik mit einer zweistelligen Wahrscheinlichkeit die Menschheit auslöscht. Beide Texte sind ernst gemeint. Beide berufen sich auf Fachleute. Und in beiden steht der Name derselben Person, wenn du genau hinschaust.

Das ist kein Betriebsunfall des Journalismus. Das ist der Zustand der Debatte.

Ich habe in den vergangenen Jahren in ziemlich vielen Meetings gesessen, in denen jemand eine dieser Aussagen auf eine Folie geklebt hatte, um eine Entscheidung zu begründen. Mal war es die Prognose, die den Kauf einer Plattform rechtfertigen sollte. Mal war es die Warnung, die den Verzicht rechtfertigen sollte. In beiden Fällen wurde eine Zukunftsaussage behandelt wie ein Messwert. Und in beiden Fällen war sie keiner.

Dieses Kapitel gibt dir kein Urteil darüber, wer recht behält. Ich weiß es nicht, und wer dir sagt, er wisse es, verkauft dir etwas. Es gibt dir etwas Besseres: eine Methode, mit der du eine Zukunftsaussage aufmachen und nachsehen kannst, was drinsteckt. Am Ende sollst du bei jeder Schlagzeile über die KI in dreißig Sekunden einordnen können, ob du gerade einen Befund liest, eine Rechnung oder eine Haltung.

Fangen wir mit dem stärksten Fall an, den die Optimisten haben. Und der ist stärker, als du vielleicht denkst.

## Der Fall, der kein Versprechen ist

Im Oktober 2024 ging der Nobelpreis für Chemie zur Hälfte an Demis Hassabis und John Jumper von Google DeepMind, für AlphaFold. Die andere Hälfte ging an David Baker für die Entwicklung von Proteindesign.[1]

Das ist keine Prognose. Das ist eine abgeschlossene Sache mit einer Urkunde.

Weil es der einzige Fall in diesem Kapitel ist, der ohne Konjunktiv auskommt, nehme ich ihn ausführlich auseinander. Wer einmal einen echten Durchbruch von innen gesehen hat, hält nicht mehr jede Pressemitteilung für einen.

### Warum die Faltung ein Problem war

Proteine sind die Werkzeuge des Lebens: Enzyme, die Stoffe zerlegen, Antikörper, die Eindringlinge erkennen, Rezeptoren, an die Medikamente andocken. Gebaut sind sie alle nach demselben simplen Prinzip — eine Kette aus Aminosäuren, zwanzig verschiedene Sorten, aufgereiht wie Perlen an einer Schnur. Diese Kette bleibt keine Schnur. Sie faltet sich in Sekundenbruchteilen zu einem dreidimensionalen Knäuel mit Taschen und Furchen, und erst diese Form entscheidet, was das Protein kann. Falsche Form, keine Funktion. Manchmal falsche Form, Krankheit.

1972 bekam Christian Anfinsen den Nobelpreis für Chemie, unter anderem für eine Erkenntnis, die das Problem zugleich löste und schuf: Die Information darüber, wie sich eine Kette faltet, steckt in der Kette selbst. Man muss nichts hinzufügen. Ein entfaltetes Protein findet unter den richtigen Bedingungen von allein in seine Form zurück.[23]

Damit war klar: Aus der Sequenz *muss* sich die Struktur berechnen lassen. Nur konnte es niemand.

Warum, das hat Cyrus Levinthal 1969 in ein Gedankenexperiment gepackt, das seither seinen Namen trägt. Zähle durch, wie viele räumliche Anordnungen eine mittelgroße Kette theoretisch einnehmen kann; du landest bei einer Zahl mit einer absurden Menge Nullen. Würde ein Protein sie der Reihe nach durchprobieren, bräuchte es länger als das Universum alt ist. Es faltet sich aber in Millisekunden. Die Natur probiert nicht durch, sie nimmt eine Abkürzung — und die zu berechnen, war fünfzig Jahre lang das eigentliche Problem.[23]

Was blieb, war der harte Weg: messen statt rechnen. Röntgenkristallographie, Kernspinresonanz, später Kryo-Elektronenmikroskopie. Für die Kristallographie musst du dein Protein erst dazu bringen, einen Kristall zu bilden, und viele denken gar nicht daran. Eine einzige Struktur aufzuklären, konnte Jahre kosten und war in manchen Laboren die gesamte Doktorarbeit eines Menschen. Gesammelt wurde das Ergebnis seit 1971 in der Protein Data Bank; als AlphaFold2 antrat, standen dort experimentell bestimmte Strukturen in der Größenordnung von hundertsiebzigtausend.[25]

Dem gegenüber standen mehrere hundert Millionen bekannter Aminosäuresequenzen. Sequenzieren war billig geworden, Strukturaufklärung nicht. Die Lücke zwischen „wir wissen, wie die Kette aussieht" und „wir wissen, was sie tut" wurde jedes Jahr größer.

### Der Test, den man nicht bestechen kann

Es gibt für dieses Feld eine Einrichtung, die ich für vorbildlich halte und die man in der KI-Debatte viel öfter erwähnen sollte: CASP, die *Critical Assessment of Structure Prediction*, ins Leben gerufen 1994 von John Moult und Kollegen, seither alle zwei Jahre.[24]

Der Ablauf ist so schlicht wie unbestechlich. Labore weltweit haben Strukturen experimentell aufgeklärt, aber noch nicht veröffentlicht. Die Sequenzen gehen an alle teilnehmenden Teams, die rechnen und geben ihre Vorhersagen ab. Danach werden die echten Strukturen offengelegt und Vorhersage gegen Wirklichkeit gehalten, gemessen in einem Wert, der beschreibt, wie gut die vorhergesagten Atome auf den gemessenen liegen. Niemand kann sich das Ergebnis schönrechnen, weil die Antwort erst nach der Abgabe existiert.

Vergleiche das mit dem, was uns in der KI-Berichterstattung sonst als Beleg vorgesetzt wird: hauseigene Benchmarks, ausgewählte Beispiele, eine Demo auf einer Bühne. CASP ist eine Blindprüfung mit fremdem Prüfer.

2018 trat DeepMind das erste Mal an und gewann — deutlich, aber nicht in der Nähe experimenteller Genauigkeit. Zwei Jahre später, bei CASP14 im Jahr 2020, kam AlphaFold2. Der Median über die Zielproteine lag bei rund zweiundneunzig von hundert Punkten, und die Fachwelt hatte sich vorher darauf verständigt, dass Werte um neunzig ungefähr das sind, was man auch beim Nachmessen im Labor an Streuung erwarten würde. Die Organisatoren sagten sinngemäß, das Problem sei in einem wesentlichen Sinn gelöst.[24]

Fünfzig Jahre offene Frage, ein Wettbewerb, erledigt. So etwas passiert selten, und es ist nicht dasselbe wie ein Modell, das im Chat überzeugend klingt.

### Was danach kam, ist der eigentliche Punkt

DeepMind hätte das Verfahren einbehalten können. Stattdessen erschien 2021 die Methode samt Code, dazu eine Datenbank: erst das menschliche Proteom und einige Modellorganismen, ein Jahr später der Ausbau auf rund zweihundert Millionen Vorhersagen — praktisch alles, was in den Datenbanken bekannter Sequenzen stand.[25] Sie wird nach Angaben von DeepMind von über zwei Millionen Forschenden in einhundertneunzig Ländern genutzt.[1]

Halte kurz inne bei dieser Zahl. Zwei Millionen Menschen, die keine KI-Firma bezahlt und die nichts zu verkaufen haben, benutzen das Ding, weil es ihre Arbeit besser macht. Das ist die härteste Währung, die es gibt. Kein Benchmark, kein Demo-Video, keine Keynote, sondern Leute, die ein Werkzeug freiwillig in ihren Alltag lassen. In den Beispielen, die DeepMind selbst anführt, geht es um Enzyme zum Abbau von Kunststoffen, um Arbeiten an vernachlässigten Tropenkrankheiten, um Malariaforschung.[1]

Und jetzt der Teil, der in den Jubelmeldungen fehlt, obwohl er die Sache erst seriös macht.

AlphaFold sagt eine Struktur voraus, es erklärt sie nicht. Es liefert kein physikalisches Verständnis des Faltungsvorgangs; wie die Kette den Weg in ihre Form findet, weiß man dadurch nicht besser als vorher. Es gibt zu jedem Abschnitt einen Konfidenzwert mit aus, und bei Proteinabschnitten, die im Zellinneren gar keine feste Form annehmen, ist dieser Wert niedrig — was für sich genommen nützlich ist, aber eben keine Antwort. Wie sich eine einzelne Mutation auf Stabilität und Funktion auswirkt, bildet das Verfahren nicht verlässlich ab. Das Zusammenspiel mehrerer Moleküle war für AlphaFold2 außer Reichweite und wurde erst mit den Nachfolgemodellen angegangen.[26]

Der schönste Einwand ist aber ein anderer, und er gehört in dieses Buch, weil er das Verhältnis von Mensch und Maschine genau trifft: AlphaFold ist auf den fünfzig Jahren experimenteller Arbeit trainiert, die es jetzt überholt. Ohne die Doktorandinnen, die Kristalle gezüchtet haben, gäbe es das Modell nicht. Das Werkzeug steht auf den Schultern derer, deren Handarbeit es überflüssig gemacht hat. Merke dir die Figur; sie kommt in diesem Buch noch einmal vor, und dann geht es um deinen Beruf.

### Der Sprung, den fast alle überlesen

Hassabis sagt nämlich noch etwas anderes. Er hält es für möglich, in den nächsten zehn bis zwanzig Jahren einen skalierbaren Prozess zu erreichen, mit dem sich praktisch alle Krankheiten angehen lassen. Sein Spin-off Isomorphic Labs, 2021 aus DeepMind ausgegründet und inzwischen mit Milliardenbeträgen finanziert, verfolgt das Ziel, die Entdeckungsphase eines Wirkstoffs auf ein bis zwei Jahre zu verkürzen.[2] In der Berichterstattung wird daraus regelmäßig „DeepMind-Chef will alle Krankheiten heilen".

Was er meint, ist nüchterner und interessanter: ein systematischer, wiederholbarer Verfahrensweg der Wirkstoffentdeckung, nicht der Endsieg über jede Krankheit.[2] Das ist ein wichtiger Unterschied, und Hassabis selbst macht ihn. Trotzdem bleibt es eine Prognose.

Und sie überspringt eine Menge. Zwischen „wir kennen die Form des Zielmoleküls" und „das Medikament ist zugelassen" liegen die Phasen, an denen Wirkstoffe seit jeher scheitern: Wirkt es im lebenden Organismus, kommt es dort an, wo es hin soll, was macht es sonst noch, verträgt der Mensch es über Jahre? Keine dieser Fragen beantwortet eine Strukturvorhersage. Sie macht den ersten Schritt schneller, und der erste Schritt war nie der teuerste.

Belegt ist die Faltung. Prognostiziert ist die Heilung.

Diesen Schnitt musst du dir merken, denn er ist der Kern des ganzen Kapitels: Zwischen einer gelieferten Leistung und der Hochrechnung, was diese Leistung als Nächstes bedeutet, liegt keine Fortsetzung, sondern ein Sprung. Der Nobelpreis beweist AlphaFold. Er beweist nicht die nächsten zwanzig Jahre.

## Die lauten Optimisten

Neben Hassabis stehen die lauteren Optimisten, und die Ehrlichkeit gebietet zu sagen, dass sie ein deutlich dünneres Fundament haben. Das heißt nicht, dass sie irren. Es heißt, dass man ihre Sätze anders lesen muss.

Reid Hoffman, Mitgründer von LinkedIn und Investor, hat 2025 mit Greg Beato ein Buch über „Superagency" geschrieben. Der Gedanke dahinter ist nicht albern: Technik verleiht vielen Menschen gleichzeitig neue Fähigkeiten und weitet dadurch ihre Handlungsmacht aus — nicht die eines Einzelnen, sondern die vieler, was wiederum auf jeden Einzelnen zurückwirkt. Hoffman nennt seine Haltung ausdrücklich „smart risk taking" statt blinden Optimismus und plädiert für eine neugierige statt einer angstgetriebenen Grundeinstellung.[3] Die Kritik hielt dem Buch entgegen, es argumentiere dünn und analysiere zu wenig.[3]

Meine eigene Einordnung, als solche gekennzeichnet: Die These ist im Prinzip prüfbar — Ausweitung von Handlungsmacht müsste sich zeigen lassen, in Gründungszahlen, in Zugangsdaten, in dem, was Leute ohne Startvorteil plötzlich selbst können. Nur wird sie meistens nicht so vorgetragen, sondern als Stimmungsangebot. Eine prüfbare These, die man nicht prüft, ist verschenkt.

Andrew Ng vergleicht KI seit Jahren mit der Elektrizität, einer Basistechnologie, die überall einsickert, und hält die Auslöschungsfurcht für stark übertrieben; die echten Existenzrisiken seien Pandemien, Klimawandel, Asteroiden, und KI sei bei deren Bewältigung eher Teil der Lösung.[4] Das Bild ist griffig, und man sollte trotzdem sehen, was es ist: eine Analogie. Analogien beweisen nichts, sie ordnen eine Erwartung. Wenn KI wie Strom ist, kommt ihre Wirkung breit, langsam und über Jahrzehnte — was ausgerechnet gegen die schnellen Umbruchsszenarien spricht, die manche Optimisten im selben Atemzug verkaufen. Zu Ngs Interessenlage gehört, dass er selbst vom Lehren und Anwenden dieser Technik lebt, unter anderem als Mitgründer von Coursera und DeepLearning.AI.[27] Das entwertet sein Argument nicht. Es gehört daneben.

Marc Andreessen schrieb 2023 einen langen Essay mit dem Titel „Why AI Will Save the World", in dem er die Existenzangst als moralische Panik einordnet, wie sie historisch auch Strom, Radio und Internet begleitet habe, und für offene Märkte statt Regulierung plädiert.[5] Eine seiner Behauptungen ist konkret genug, um sie zu prüfen: dass jedes Kind einen KI-Mentor haben könne.

Genau die haben wir in Kapitel 7 geprüft. In Edo State in Nigeria arbeiteten rund achthundert Schülerinnen und Schüler sechs Wochen lang mit GPT-4 als Tutor, begleitet von einer Lehrkraft; die Weltbank wertete den Versuch randomisiert aus und verglich den Zuwachs mit etwa zwei Jahren regulärer Schulbildung, bei rund achtundvierzig Dollar pro Kind.[30] Andreessens Satz ist also nicht aus der Luft gegriffen. Er trifft nur unter einer Bedingung zu, die im Essay nicht steht: mit Lehrkraft, als Übung, nicht als Abkürzung. Zwischen „möglich" und „möglich unter diesen Bedingungen" liegt der Unterschied zwischen Bildungspolitik und Prospekt.

Bei Andreessen kommt hinzu, dass er als Wagniskapitalgeber ein handfestes Interesse daran hat, dass diese Technik ohne enge Regeln wächst. Das macht seine Argumente nicht automatisch falsch — Interessen und Wahrheit sind zwei verschiedene Dinge. Aber es gehört ins Bild, so wie es ins Bild gehörte, dass Edison im Stromkrieg nicht aus Sorge um die Bevölkerung vor Wechselstrom warnte.

## Die Leute, die es gebaut haben

Im Mai 2023 verließ Geoffrey Hinton Google. Er war damals fünfundsiebzig, hatte über ein Jahrzehnt für das Unternehmen gearbeitet und gilt vielen als einer der Väter des Deep Learning. Seine Begründung war knapp: Er sei gegangen, um über die Gefahren der KI sprechen zu können, ohne berücksichtigen zu müssen, wie sich das auf Google auswirkt.[6]

Anderthalb Jahre später bezifferte er in einem Interview die Wahrscheinlichkeit, dass KI die Menschheit binnen etwa dreißig Jahren auslöscht, auf zehn bis zwanzig Prozent.[6] Im selben Jahr, 2024, erhielt er zusammen mit John Hopfield den Nobelpreis für Physik, für die Grundlagenarbeit an künstlichen neuronalen Netzen.[7]

Ich möchte, dass du diese zwei Absätze nebeneinander stehen lässt und der Versuchung widerstehst, sie schnell aufzulösen. Hier warnt kein Kulturpessimist, der die Technik von außen betrachtet. Hier warnt einer der Menschen, ohne dessen Arbeit es die heutigen Systeme nicht gäbe. Das ist ungefähr so, als würde ein Chefkonstrukteur nach vierzig Jahren vom Band treten und sagen, er sei sich nicht mehr sicher, ob die Bremsen halten.

Trotzdem, und das ist der zweite Teil der Ehrlichkeit: Die Zahl „zehn bis zwanzig Prozent" ist keine Messung. Es gibt keinen Datensatz zu Zivilisationsuntergängen, aus dem man eine Häufigkeit ableiten könnte. Es ist eine subjektive Einschätzung eines außergewöhnlich kompetenten Menschen — kompetent für die Frage, wie diese Systeme funktionieren, nicht notwendigerweise kompetent für die Frage, wie sich Gesellschaften über dreißig Jahre gegen eine Technik wehren. Eine gut begründete Meinung bleibt eine Meinung. Sie in Prozent zu gießen, macht sie präziser aussehend, nicht präziser.

Am 30. Mai 2023 veröffentlichte das Center for AI Safety ein Statement, das aus genau einem Satz besteht: Die Minderung des Auslöschungsrisikos durch KI solle globale Priorität haben, neben anderen Risiken gesellschaftlichen Ausmaßes wie Pandemien und Atomkrieg.[8] Unterschrieben haben unter anderem Hinton, der Turing-Preisträger Yoshua Bengio, Sam Altman von OpenAI, Dario Amodei von Anthropic, Bill Gates — und Demis Hassabis.[8]

Der letzte Name ist der wichtigste an dieser Stelle. Der Mann mit dem Nobelpreis für den größten belegten KI-Erfolg steht auf derselben Liste wie die Warner. Wenn dein Weltbild ein sauberes Duell zwischen Begeisterten und Ängstlichen vorsieht, kannst du es hier verabschieden.

Das Ein-Satz-Format hat dabei einen Zweck: Je länger ein Aufruf, desto mehr Gründe, nicht zu unterschreiben. Das erklärt die prominente Liste — und zugleich, warum aus dem Statement so wenig folgt. Es sagt, dass etwas Priorität haben soll, nicht was zu tun ist. Wer es als Beweis für einen Expertenkonsens über die Wahrscheinlichkeit zitiert, überdehnt es.

Bengio hat noch etwas anderes getan, das mir persönlich mehr sagt als jede Prozentzahl. Er leitete den *International AI Safety Report*, veröffentlicht am 29. Januar 2025, an dem rund hundert Fachleute mitwirkten, mit einem Beirat aus dreißig Ländern sowie UN, EU und OECD. Der Bericht gibt ausdrücklich keine politischen Empfehlungen, sondern bündelt, was die Forschung tatsächlich weiß.[9] Genau das ist die seltene Gattung: eine Bestandsaufnahme, die den Unterschied zwischen Evidenz und Vermutung selbst markiert, statt ihn zu kassieren.

Und schließlich der Philosoph unter den Warnern. Der Informatiker Stuart Russell argumentiert in *Human Compatible* von 2019, das Standardmodell der KI sei falsch gebaut: Wir konstruieren Systeme, die vorgegebene Ziele immer besser erreichen, obwohl wir Ziele nie vollständig richtig formulieren können. Sein Gegenvorschlag sind Systeme, die über die menschlichen Präferenzen bewusst unsicher bleiben und sie laufend nachlernen.[10] Das ist keine Prognose, sondern ein Forschungsprogramm — und damit die Sorte Aussage, die man an ihren Ergebnissen prüfen kann.

Russells Diagnose ist mir näher als alle Prozentzahlen, weil ich sie im Kleinen ständig erlebe. Wer ein System auf eine Kennzahl optimiert, bekommt genau diese Kennzahl, samt allem, was sie nicht misst. Eine Automatisierung, die auf Durchlaufzeit getrimmt ist, erledigt die einfachen Fälle blitzschnell und schiebt die schweren in ein Postfach, das niemand leert. Das ist kein Superintelligenz-Szenario. Das ist Dienstag.

Diese Leute lächerlich zu machen, ist billig und dumm. Sie kennen die Technik von innen. Man darf ihre Schlüsse für falsch halten. Aber man muss sie widerlegen, nicht wegwitzeln.

## „Ihr habt euch in der Straße geirrt"

Die dritte Gruppe wird in Zeitungen am seltensten sauber dargestellt, weil sie in kein Lager passt. Sie sagt nicht „wird toll" und nicht „wird schlimm". Sie sagt: Ihr redet über das falsche Ding.

Yann LeCun, Turing-Preisträger von 2018 und lange Chief AI Scientist bei Meta, vertritt seit Jahren die These, dass reines Hochskalieren von Sprachmodellen nicht zu menschenähnlicher Intelligenz führt. Den heutigen Systemen fehle persistentes Gedächtnis, echte Planung und eine Verankerung in der physischen Welt; der Weg nach vorn führe über „World Models", also über Systeme, die abstrakte Repräsentationen der Welt aus sensorischen Daten lernen. Diesen Ansatz verfolgt er inzwischen in einer eigenen Gründung.[11]

LeCun ist der beste Beweis dafür, dass die Lager-Sortierung nicht funktioniert. Er hält die Weltuntergangswarnungen für überzogen und den AGI-Hype für überzogen. Gleichzeitig. Wer ihn nur als „Optimisten" zitiert, hat ihn nicht gelesen.

Gary Marcus argumentiert von der anderen Seite in dieselbe Richtung. Sein Essay „Deep Learning Is Hitting a Wall" von 2022 und seine Fortschreibung im Substack bis heute laufen darauf hinaus, dass reines Skalieren die harten Probleme nicht löst — Halluzinationen, Abstraktion, verlässliches Schlussfolgern — und dass es abnehmende Erträge gibt.[12] Ein Teil dieser Position ist Wertung, ein Teil stützt sich auf beobachtete Plateaus. Und wenn ich ehrlich bin: In meinem Arbeitsalltag komme ich Marcus näher, als mir manchmal lieb ist. Ein Modell schreibt mir in zwei Minuten ein sauberes Skript, und dreißig Minuten später scheitert dasselbe Modell daran, die Eigenheiten einer schlecht dokumentierten internen Schnittstelle zu begreifen, die jeder Kollege nach einer Woche im Haus kennt.

Fairerweise gehört dazu, dass Marcus seine These seit Jahren fortschreibt und die Systeme seither trotzdem erheblich besser geworden sind. Eine Wand, die mehrfach angekündigt wurde und an der bisher niemand endgültig hängenblieb, verliert an Beweiskraft.

Dann gibt es noch eine Kritik, die mich an dieses Buch anders andockt, weil sie zurück in das Kapitel führt, aus dem du gerade kommst.

Im März 2021 erschien auf der Konferenz FAccT ein Aufsatz von Emily Bender, Timnit Gebru, Angelina McMillan-Major und Margaret Mitchell mit dem Titel „On the Dangers of Stochastic Parrots". Die Kernthese: Große Sprachmodelle reihen Sprachformen aneinander, ohne Bedeutung zu verstehen, und wir Menschen unterstellen ihnen den Sinn, den wir selbst hineinlesen. Die Risiken, die das Paper benennt, liegen sämtlich in der Gegenwart: Reproduktion von Verzerrungen und abwertender Sprache, ökologische und Ressourcenkosten, und die Verdrängung kritischer Forschung durch das Rennen um immer größere Modelle.[13] Gebru verlor über diesem Paper ihre Stelle bei Google; sie verließ das Unternehmen im Dezember 2020 im Streit darum, Mitchell wurde zwei Monate später entlassen.[14]

Ich bin vorsichtig damit, wem ich welchen Satz in den Mund lege, deshalb sage ich es sauber: Belegt ist die Prioritätensetzung dieses Papers, nicht ein wörtliches Verdikt über die Weltuntergangsdebatte. Aber das strukturelle Argument steht, und es ist stark. Wenn die knappe Ressource Aufmerksamkeit — in Redaktionen, in Ministerien, in Forschungsbudgets — auf ein hypothetisches Ereignis in dreißig Jahren gelenkt wird, dann steht sie nicht für die Fehlerquote eines Systems zur Verfügung, das heute über Bewerbungen, Kredite oder Gesichtserkennung mitentscheidet. Genau diese heutigen Schäden hast du im vorigen Kapitel in Zahlen gesehen, bis hin zu Fehlerraten in der Gesichtsanalyse, die sich zwischen Bevölkerungsgruppen um mehr als das Vierzigfache unterschieden.[15]

Meine Einschätzung dazu, klar als meine: Das ist kein Entweder-oder, aber es ist auch keine gleichmäßige Verteilung. Ein reales Problem mit gemessener Fehlerquote hat Vorrang vor einem hypothetischen mit geschätzter Wahrscheinlichkeit. Nicht, weil das zweite unmöglich wäre, sondern weil man am ersten heute etwas tun kann.

## Ein Szenario, das keine Vorhersage sein will

Im April 2025 erschien „AI 2027", geschrieben von Daniel Kokotajlo, der zuvor bei OpenAI gearbeitet hatte, gemeinsam mit Eli Lifland, Thomas Larsen und Romeo Dean, redaktionell begleitet von Scott Alexander. Der Text schildert detailliert, wie ein schneller Take-off aussehen könnte: KI-Firmen automatisieren ab etwa 2026 ihre eigene Forschung, 2027 entstehen Systeme, die menschliche Spitzenkräfte in allen Feldern übertreffen.[16]

Der Text wurde weltweit zitiert, meistens als Vorhersage. Er ist keine.

Der stärkste Beleg dafür steht in seiner eigenen Bauart: Das Szenario verzweigt sich am Ende in zwei verschiedene Ausgänge, je nachdem, wie die handelnden Menschen entscheiden.[16] Ein Text mit zwei Enden sagt nicht, was passieren wird. Er sagt, woran es hängt. Genau so sind Szenarien gemeint, seit Militärs und Konzerne sie benutzen: als Übungsmaterial, damit einem der Ernstfall nicht neu vorkommt.

Die Autoren bezeichnen den Text ausdrücklich als Planungswerkzeug, nicht als wörtliche Prognose — und, was noch aufschlussreicher ist, sie haben ihre eigenen Erwartungen danach verschoben: Kokotajlos persönlicher Median für AGI rückte auf etwa 2030, sein Koautor Lifland verschob den seinen um rund drei Jahre nach hinten.[16]

Das ist bemerkenswertes Verhalten, und ich meine das nicht ironisch. Jemand veröffentlicht ein Szenario, bekommt Aufmerksamkeit dafür, und korrigiert es dann öffentlich in die unspektakulärere Richtung. Wer seine eigene Prognose gegen sein eigenes Interesse revidiert, gibt dir einen Grund, ihn beim nächsten Mal ernster zu nehmen, nicht weniger ernst.

Der Schaden entstand ohnehin nicht im Text, sondern beim Weiterreichen. Aus einem verzweigten Szenario mit ausgeschriebenen Annahmen wurde in der dritten Meldung ein Datum: 2027. Derselbe Mechanismus wie beim halben Liter Wasser im vorigen Kapitel. Jede Weitergabe streicht die Bedingungen, weil Bedingungen sich schlecht in eine Überschrift setzen lassen, und am Ende steht eine Zahl, für die niemand haftet.

Bleibt die Frage darunter, und die ist es wert, klar beantwortet zu werden: Wann kommt AGI?

Niemand weiß es, und das ist keine Bequemlichkeit, sondern eine Aussage über die Beschaffenheit der Frage. Empirisch prüfbar sind die Fähigkeiten heutiger Systeme und ihre Grenzen; dafür gibt es Tests, die man gewinnen oder verlieren kann. Der Zeitpunkt, zu dem eine allgemeine, menschenähnliche Intelligenz existiert, ist aus drei Gründen nicht messbar. Es ist nicht einmal definiert, woran man sie erkennen würde — jede Definition wird von der Gegenseite als zu schwach oder zu streng abgelehnt, und erreichte Kriterien wandern weiter. Es gibt keine Vorgeschichte: null vorherige Fälle, aus denen sich eine Häufigkeit schätzen ließe. Und das Ergebnis hängt an Entscheidungen, die noch niemand getroffen hat — wie viel Kapital in welche Ansätze fließt, was reguliert wird, welche technische Hürde noch auftaucht.

Ob 2027, 2040 oder nie, ist deshalb bei den Enthusiasten genauso Spekulation wie bei den Skeptikern. Niemand hat Daten. Alle haben Intuitionen, unterschiedlich gut informiert. Wer dir hier Sicherheit anbietet, in welche Richtung auch immer, hat entweder nicht nachgedacht oder etwas zu verkaufen.

## Zwei Rechnungen, ein Faktor zehn

Wenn du dachtest, die Uneinigkeit betreffe nur ferne Zukunftsfragen, hier der Rückgriff auf Kapitel 6.

Goldman Sachs veröffentlichte 2023 eine Schätzung, nach der generative KI das globale Bruttoinlandsprodukt über zehn Jahre um rund sieben Prozent heben könnte, was etwa sieben Billionen Dollar entspräche, bei einem Produktivitätsschub von anderthalb Prozentpunkten; ungefähr zwei Drittel der US-Berufe seien exponiert, und bei diesen ließe sich ein Viertel bis die Hälfte der Tätigkeiten automatisieren.[17] McKinsey rechnete im selben Jahr über dreiundsechzig Anwendungsfälle einen jährlichen Zusatzwert von 2,6 bis 4,4 Billionen Dollar aus, drei Viertel davon in nur vier Funktionen: Marketing und Vertrieb, Kundenservice, Softwareentwicklung, Forschung und Entwicklung.[18]

Daron Acemoglu vom MIT, der später den Wirtschaftsnobelpreis erhielt, legte im April 2024 eine Modellrechnung vor, die auf höchstens etwa 0,66 Prozent Zuwachs der totalen Faktorproduktivität über zehn Jahre kommt. Seine Begründung ist unspektakulär und deshalb schwer wegzuwischen: KI ist nur einem Teil der Tätigkeiten ausgesetzt, ungefähr einem Fünftel, und davon lässt sich wiederum nur ein knappes Viertel profitabel automatisieren.[19]

Dieselbe Technik. Ungefähr dieselbe Datenlage. Ergebnisse, die um eine Größenordnung auseinanderliegen.

Wo der Unterschied entsteht, kannst du an den Zahlen oben ablesen, und das ist lehrreicher als jedes Urteil darüber, wer recht hat. Beide Seiten schätzen, welcher Anteil der Arbeit betroffen ist, welcher Anteil davon sich lohnt und wie schnell Einsparung in gemessene Produktivität übergeht. Drei Schätzungen, multipliziert. Setzt du jede einzelne um den Faktor zwei anders an — und das kann man mit guten Gründen —, steht am Ende das Achtfache.

Das ist kein Skandal, sondern der Normalfall bei Modellrechnungen: Das Ergebnis hängt an Annahmen, und die Annahmen sind Urteile. Wer entscheidet, welcher Anteil der Aufgaben betroffen ist und wie schnell sich Investitionen in Produktivität übersetzen, hat die Antwort im Wesentlichen schon gewählt, bevor er rechnet. Beide Seiten sind seriös. Beide sind Prognose. Und wenn dir das nächste Mal jemand eine dieser Zahlen als Tatsache verkauft, weißt du jetzt, dass er entweder das Kleingedruckte nicht gelesen hat oder darauf setzt, dass du es nicht liest.

## Vier Fragen, die du an jede Prognose stellen kannst

Hier ist das eigentliche Werkzeug dieses Kapitels. Vier Fragen, die dich weniger als eine Minute kosten.

**Was hat die Person davon?** Das ist keine Unterstellung, sondern eine Buchhaltung. Ein Wagniskapitalgeber verdient an Wachstum. Ein Konzernchef verkauft Lizenzen. Ein Institut, das vor Risiken warnt, sammelt Spenden für Risikoforschung. Ein Professor gewinnt Renommee mit der Gegenposition zum Mainstream. Interessen widerlegen niemanden, aber sie sagen dir, in welche Richtung sich ein Irrtum wahrscheinlich neigt. Und sie erklären, warum Hintons Google-Abgang so viel Gewicht bekam: Er hat seine Warnung teuer gemacht, statt Nutzen aus ihr zu ziehen.

**Steht ein überprüfbares Datum darin?** „Irgendwann wird KI alles verändern" kostet nichts und lässt sich nie widerlegen. „2027 übertreffen Systeme menschliche Spitzenkräfte in allen Feldern" ist eine echte Behauptung, an der man scheitern kann. Prognosen mit Datum sind mutiger und wertvoller, auch wenn sie öfter danebenliegen. Wer nur in Nebel spricht, hat sich der Prüfung entzogen.

**Wird ein Mechanismus genannt oder nur eine Kurve verlängert?** Das ist die schärfste der vier Fragen. Eine Extrapolation sagt: Es ging drei Jahre steil bergauf, also geht es weiter bergauf. Ein Mechanismus sagt: Es geht weiter, weil A auf B wirkt und B auf C. Acemoglu nennt einen Mechanismus, den du prüfen und angreifen kannst. LeCun nennt einen: fehlendes Gedächtnis, fehlende Planung, fehlende Verankerung. Das meiste, was du in Wirtschaftsteilen liest, ist verlängerte Kurve. Kurven kennen keine Sättigung, Mechanismen schon.

**Wie ist diese Person das letzte Mal ausgegangen?** Prognostiker haben eine Bilanz, man muss sie nur nachschlagen. Wer in den letzten fünf Jahren dreimal das Ende der Skalierung ausgerufen hat und dreimal überholt wurde, darf weiter reden — aber sein vierter Anlauf zählt weniger als der erste. Und wer eine Vorhersage öffentlich revidiert hat, zählt mehr.

Zusammen ergeben die vier Fragen keine Wahrheit, sondern eine Gewichtung. Am Ende steht bei mir meistens nicht „stimmt" oder „stimmt nicht", sondern ein Satz wie: gut begründete Meinung, erkennbares Eigeninteresse, kein prüfbares Datum. Das ist wenig — und sehr viel mehr als das, womit die meisten Diskussionen an dieser Stelle arbeiten.

## Das Werkzeug an drei alten Fällen

Damit du siehst, dass die vier Fragen nicht nur auf dem Papier funktionieren, führe ich sie an drei Fällen vor, deren Ausgang wir kennen.

**Erster Fall: Clifford Stoll, 1995.** Du bist ihm in Kapitel 5 begegnet. Der Astronom und frühe Internet-Kenner schrieb in *Newsweek*, keine Online-Datenbank werde die Tageszeitung ersetzen, keine CD-ROM einen guten Lehrer und kein Computernetz die Arbeitsweise von Regierungen verändern.[20] Er lag falsch, in jedem einzelnen Punkt.

Jetzt die vier Fragen. Interesse: praktisch keins — Stoll verkaufte kein Konkurrenzprodukt. Datum: vorhanden und klar, deshalb ließ sich der Text überhaupt widerlegen. Mechanismus: ja, und ein plausibler dazu — er beschrieb, was das Netz 1995 tatsächlich nicht konnte. Bilanz: unbekannt, es war seine erste große Vorhersage dieser Art.

Nach diesen vier Fragen hätte Stoll gut abgeschnitten. Er lag trotzdem daneben, aus einem Grund, den sie nicht abdecken: Er hatte die Gegenwart korrekt beschrieben und stillschweigend fortgeschrieben. Der Fehler saß nicht im Argument, sondern in der Zeitachse. Ihm zugute zu halten ist, dass er es später offen einräumte, mit trockenem Spott über sich selbst.[20] Fachkenntnis schützt nicht vor Fehlprognosen. Sie sorgt nur dafür, dass man die falsche Vorhersage souveräner formuliert.

**Zweiter Fall: die Mikroelektronik-Debatte, 1980.** In der Bundesrepublik lief unter dem Stichwort „Mikroelektronik — die dritte industrielle Revolution" eine ernsthafte Auseinandersetzung über technologisch verursachte Massenarbeitslosigkeit, in seriösen Publikationen, mit Gutachten und Anhörungen.[28]

Vier Fragen. Interesse: ehrlich verteilt — Gewerkschaften hatten eines, Arbeitgeberverbände auch, Wissenschaftler eher wenig. Datum: meist keins, und das ist der Schwachpunkt; „in den kommenden Jahrzehnten" ist nicht widerlegbar. Mechanismus: einer der besten, die je vorgetragen wurden — Rationalisierung ersetzt Arbeitskraft, das ist keine verlängerte Kurve, sondern eine Wirkkette. Bilanz: keine.

Und trotzdem trat die befürchtete Massenarbeitslosigkeit in dieser Form nicht ein. Für Deutschland zeigt die Forschung, dass Regionen mit hoher Automatisierungsexposition keine überdurchschnittlichen Jobverluste erlitten.[29] Der Mechanismus war richtig beschrieben und trotzdem unvollständig: Er erfasste die verschwindenden Tätigkeiten, nicht die entstehenden. Ein genannter Mechanismus ist also besser als eine verlängerte Kurve, aber keine Garantie. Er ist ein Ausschnitt, und wer den Ausschnitt wählt, wählt das Ergebnis mit.

**Dritter Fall: Amaras Gesetz, angewandt auf uns selbst.** Roy Amara, Präsident des Institute for the Future, brachte die Regel aus Kapitel 4 auf die Formel, dass wir die Wirkung einer Technik kurzfristig überschätzen und langfristig unterschätzen.[21]

Dieser Satz besteht die eigenen vier Fragen nicht besonders gut. Ein Datum steht nicht darin, ein Mechanismus auch nicht — er beschreibt ein Muster, nicht dessen Ursache. Streng genommen ist Amaras Gesetz genau die Sorte unwiderlegbarer Aussage, vor der ich dich gerade gewarnt habe: Egal was passiert, es lässt sich hinterher passend machen.

Ich halte es trotzdem für nützlich, weil es nicht als Prognose taugt, wohl aber als Korrektur der eigenen Erwartung. Angewandt auf unsere drei Lager heißt es: Die Optimisten haben für das nächste Jahr wahrscheinlich unrecht und für das nächste Jahrzehnt möglicherweise recht. Die Skeptiker haben für das nächste Jahr wahrscheinlich recht und laufen Gefahr, das Jahrzehnt zu verpassen. Beide sagen die Wahrheit über verschiedene Zeitfenster und streiten dann darüber, wer lügt. Nimm den Satz als Werkzeug für dich selbst, nicht als Argument gegen andere.

Ein letzter Hinweis, der zu Kapitel 2 zurückführt. Die berühmteste Technikangst der Geschichte, die angebliche bayerische Ärztewarnung vor dem Wahnsinn bei dreißig Stundenkilometern, ist mit hoher Wahrscheinlichkeit nie ausgesprochen worden.[22] Sie wird trotzdem in jedem zweiten Vortrag über Innovation erzählt, weil sie eine gute Geschichte ist. Das gilt in beide Richtungen: Der schaurige KI-Fall, der zu gut passt, um wahr zu sein, sollte dich genauso misstrauisch machen wie der Wunderfall.

## Was ich selbst glaube, und warum das wenig wiegt

Jetzt bin ich dir meine eigene Position schuldig, und ich markiere sie als das, was sie ist: Meinung, kein Beleg.

Ich bin Praktiker. Ich baue mit meinem Team Automatisierungen, ich schreibe mir abends mit Claude Code kleine Werkzeuge für meinen eigenen Alltag, und ich sehe jeden Tag beides — was diese Systeme können und woran sie hängenbleiben. Ich habe kein Modell, mit dem ich das Jahr 2035 ausrechnen könnte. Ich habe stattdessen etwas, das die Propheten beider Lager oft nicht haben: eine tägliche Rückkopplung mit der Wirklichkeit.

Diese Rückkopplung wirkt in beide Richtungen dämpfend. Wenn ich am Montag ein Modell erlebe, das eine Aufgabe erledigt, für die mein Team vor drei Jahren eine Woche gebraucht hätte, kann ich die Weltuntergangsfraktion nicht mehr für hysterisch halten; hier bewegt sich wirklich etwas, und zwar schnell. Wenn ich am Dienstag zusehe, wie dasselbe Modell an einem Formularfeld scheitert, weil ein Fachbereich seit 2011 eine Sonderregel pflegt, die nirgends aufgeschrieben ist, kann ich die Rede von der nahen Superintelligenz nicht mehr ernst nehmen. Die Welt ist voll von diesen Sonderregeln. Sie sind die eigentliche Reibung, und sie stehen in keinem Benchmark.

Drei Stellen, an denen Ankündigung und Wirklichkeit in meinem Berufsalltag auseinanderfielen. Ich nenne keine Hersteller, weil ich das Muster bei allen gesehen habe.

Die erste: die Demo mit fünf Dokumenten. Ein System liest Rechnungen aus, erkennt Positionen, ordnet Kostenstellen zu, auf der Bühne in achtzig Sekunden. Im Pilotbetrieb kommen dann viertausend Dokumente aus elf Jahren, darunter schief eingescannte Faxe, ein Lieferantenname, der 2017 geändert wurde, und handschriftliche Vermerke am Rand, die im Zweifel wichtiger sind als der gedruckte Text. Die Trefferquote fällt nicht dramatisch. Sie fällt genau so weit, dass jemand jeden Vorgang nachsehen muss — und damit ist der Nutzen weg, denn Prüfen kostet fast so viel wie Machen.

Die zweite: der Zeitgewinn, der woanders wieder verschwindet. Wir haben Aufgaben, bei denen ein Modell heute in einer Stunde erledigt, wofür früher zwei Tage angesetzt waren. Das ist real, ich habe es mehrfach gemessen. Nur war die Erstellung selten der Engpass. Der Engpass war die Abstimmung — wer schaut drüber, wer gibt frei, wessen Fachbereich muss zustimmen. Diese Woche Wartezeit hat kein Modell verkürzt. Wer Automatisierung an der falschen Stelle einbaut, bekommt ein sehr schnelles Teilstück in einem gleich langsamen Prozess. Das ist der häufigste Grund, warum Produktivitätsversprechen sich nicht in Zahlen niederschlagen, und er ist so unglamourös, dass ihn kein Vortrag erwähnt.

Die dritte geht gegen meine eigene Skepsis. Ich habe abends Werkzeuge gebaut, für die ich vor fünf Jahren einen Entwickler und ein Budget gebraucht hätte, und zwar in einer Sitzung. Nicht als Prototyp, sondern als Ding, das seither läuft. Wer diese Erfahrung nicht gemacht hat und über KI redet, redet über Berichte. Der Haken: Das Ding läuft für einen Nutzer, mit einem Eingabeformat, ohne Rechteverwaltung, ohne Protokollierung, ohne Vertretungsregelung. Dasselbe für zweihundert Kollegen belastbar zu machen, ist weiterhin Monatsarbeit. Der Sprung liegt am Anfang und nicht am Ende, und beide Lager reden, als läge er in der Mitte.

Deshalb misstraue ich beiden Extremen, und zwar aus demselben Grund: Beide sprechen aus großer Höhe über eine Technik, die aus der Nähe betrachtet erheblich unordentlicher ist. Wer täglich damit arbeitet, wird selten Prophet. Man wird bescheidener, und man wird schneller darin, Behauptungen an der eigenen Erfahrung zu messen. Das ist keine tiefe Weisheit, das ist Bodenhaftung. Ich halte sie für das wirksamste Gegenmittel gegen Hype und Panik gleichermaßen, und du bekommst sie nicht durch Lektüre, sondern durch Benutzen. Zwei Wochen ernsthafte Arbeit mit einem dieser Werkzeuge bringen dich in der Einschätzung weiter als zwanzig Artikel.

Und noch etwas glaube ich, ebenfalls ohne Beleg: Die wichtigste Frage der nächsten Jahre wird nicht durch Prognosen entschieden. Sie wird durch Entscheidungen entschieden — von Gesetzgebern, von Unternehmen, von Leuten wie dir und mir, die morgens festlegen, welche Aufgabe sie abgeben und welche nicht. Eine Prognose beschreibt eine Zukunft, in der niemand handelt. So eine Zukunft hat es noch nie gegeben.

Damit kommen wir an die Grenze dessen, was dieses Kapitel leisten kann. Was du nicht bekommen hast, ist die Antwort auf die Frage, was kommt. Die hat niemand, und wer sie anbietet, hat dieses Kapitel nicht nötig gehabt.

Also drehen wir die Frage um. Wenn die Zukunft der Maschinen offen ist, dann ist die einzige Größe in dieser Rechnung, über die wir tatsächlich etwas wissen, nicht die Maschine. Wir sind es. Was können Menschen, das keine Skalierung erreicht, und was davon lohnt es sich zu behalten, ganz gleich, welches der drei Lager am Ende recht bekommt?

---

## Quellen zu Kapitel 9

*(Endnoten-Nummerierung kapitelweise; Mapping auf das zentrale `QUELLEN.md`. Einordnung je Beleg: [belegt] / [Prognose] / [Meinung]. Die Nummern [1]–[22] sind gegenüber der Vorfassung unverändert; [23]–[30] sind Ergänzungen.)*

[1] Demis Hassabis & John Jumper: Nobelpreis für Chemie 2024 (gemeinsam mit David Baker für Proteindesign); AlphaFold2 (2020), ca. 200 Mio. vorhergesagte Proteinstrukturen; AlphaFold-Datenbank von über 2 Mio. Forschenden in 190 Ländern genutzt; von DeepMind angeführte Anwendungsbeispiele (u. a. Enzyme zum Kunststoffabbau, vernachlässigte Tropenkrankheiten, Malariaforschung). NobelPrize.org; Google DeepMind. → QUELLEN.md Nr. 92. **[belegt]** — *Die Anwendungsbeispiele sind im Text ausdrücklich als Angaben von DeepMind gekennzeichnet.*

[2] ▲ Demis Hassabis zu einem „skalierbaren Prozess" gegen praktisch alle Krankheiten in 10–20 Jahren; Isomorphic Labs (DeepMind-Spin-off 2021, Milliardenfinanzierung, Ziel 1–2 Jahre Entdeckungsphase). Interviews/Berichterstattung 2025–26 (u. a. Fortune, The AI Insider). → QUELLEN.md Nr. 91. **[Prognose]** — *Wortlaut und Finanzierungszahl vor Drucklegung an der Primärquelle prüfen; die Einschränkung „skalierbarer Prozess, nicht Endsieg über jede Krankheit" ist im Text mitgeführt. Die Aufzählung der nachgelagerten Entwicklungsphasen ist allgemeines Fachwissen der Arzneimittelentwicklung, keine Aussage von Hassabis.*

[3] Reid Hoffman & Greg Beato: *Superagency: What Could Possibly Go Right with Our AI Future*. Simon & Schuster, 2025; „smart risk taking" als Selbstbeschreibung; kritische Rezeption u. a. Kirkus Reviews („poor arguments and little critical analysis"). → QUELLEN.md Nr. 93. **[Meinung]** — *Die Bemerkung zur prinzipiellen Prüfbarkeit der These ist im Text als Einschätzung des Autors gekennzeichnet.*

[4] ▲ Andrew Ng: „AI is the new electricity" (seit ca. 2016); Position gegen die Existenzrisiko-Furcht, reale Existenzrisiken Pandemien/Klimawandel/Asteroiden (Äußerungen 2023). → QUELLEN.md Nr. 94. **[Meinung]** — *Im Text bewusst paraphrasiert; das kursierende wörtliche Zitat liegt nur über Sekundärberichterstattung vor und wurde deshalb nicht als Zitat gesetzt.*

[5] Marc Andreessen: *Why AI Will Save the World*. a16z, Juni 2023. — Einordnung der Existenzangst als „moral panic"; KI-Mentor für jedes Kind; Plädoyer für offene Märkte statt Regulierung. → QUELLEN.md Nr. 95. **[Meinung]**

[6] ▲ Geoffrey Hinton: Austritt bei Google (Mai 2023) mit der Begründung, frei über die Gefahren sprechen zu können; Dezember 2024 Einschätzung „10–20 %" Auslöschungsrisiko binnen ca. 30 Jahren. Washington Post (2.5.2023), CNN, MIT Technology Review. → QUELLEN.md Nr. 98. **[Meinung / Risikoeinschätzung]** — *Austrittsbegründung im Text paraphrasiert, nicht als Wortzitat; vor Drucklegung am Originalinterview verifizieren.*

[7] Geoffrey Hinton & John Hopfield: Nobelpreis für Physik 2024. NobelPrize.org. → QUELLEN.md Nr. 99. **[belegt]**

[8] Center for AI Safety: *Statement on AI Risk*, 30. Mai 2023 (Ein-Satz-Statement); Unterzeichner u. a. Hinton, Bengio, Altman, Hassabis, Amodei, Gates. safe.ai. → QUELLEN.md Nr. 100. **[belegt]** — *Der Statement-Satz ist im Text sinngemäß auf Deutsch wiedergegeben; englischer Originalwortlaut für die Druckfassung vorhalten. Die Deutung des Ein-Satz-Formats (niedrige Unterschriftskosten, geringe Handlungsfolge) ist im Text als Überlegung des Autors gehalten.*

[9] *International AI Safety Report*, Vorsitz Yoshua Bengio, 29. Januar 2025; ca. 100 Fachleute, Beirat aus 30 Ländern sowie UN/EU/OECD; ausdrücklich ohne Politikempfehlungen. → QUELLEN.md Nr. 101 (= Nr. 73). **[belegt]**

[10] Stuart Russell: *Human Compatible: Artificial Intelligence and the Problem of Control*. Viking/Penguin, 2019. → QUELLEN.md Nr. 102. **[Meinung / Forschungsprogramm]**

[11] ▲ Yann LeCun (Turing-Preisträger 2018, langjähriger Chief AI Scientist bei Meta): LLMs seien kein Weg zu menschenähnlicher Intelligenz; World-Model-Ansatz; eigene Gründung. Interviews/Vorträge 2023–2025. → QUELLEN.md Nr. 107. **[Meinung / Forschungsthese]** — *Position im Text paraphrasiert; konkretes Zitat vor Drucklegung an einem Originalinterview verankern.*

[12] Gary Marcus: *Deep Learning Is Hitting a Wall*. Nautilus, März 2022; Fortschreibung im Substack „Marcus on AI" (2024, „diminishing returns"). → QUELLEN.md Nr. 103. **[Meinung / teils empirisch gestützt]** — *Der im Text angeschlossene Einwand (mehrfach fortgeschriebene These bei weiterhin steigender Leistungsfähigkeit) ist Wertung des Autors.*

[13] Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, Margaret Mitchell (als „Shmargaret Shmitchell"): *On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?* FAccT '21, ACM, März 2021, DOI 10.1145/3442188.3445922. → QUELLEN.md Nr. 104. **[belegt]** — *Im Text sind nur die im Paper dokumentierten Risiken zugeschrieben; das Argument „Weltuntergangsdebatte lenkt von Gegenwartsschäden ab" ist ausdrücklich als strukturelles Argument bzw. Einschätzung des Autors gekennzeichnet und keiner Person als Zitat unterstellt.*

[14] Timnit Gebru: Abgang bei Google im Dezember 2020 im Streit um das Stochastic-Parrots-Paper; Margaret Mitchell rund zwei Monate später entlassen. MIT Technology Review (4.12.2020). → QUELLEN.md Nr. 105. **[belegt]**

[15] Joy Buolamwini & Timnit Gebru: *Gender Shades*. PMLR / MIT Media Lab, 2018 — Fehlerraten bis 34,7 % gegenüber 0,8 % je nach Gruppe. Call-back auf Kapitel 8. → QUELLEN.md Nr. 79. **[belegt]**

[16] Daniel Kokotajlo, Eli Lifland, Thomas Larsen, Romeo Dean (Red. Scott Alexander): *AI 2027*. April 2025, ai-2027.com; von den Autoren ausdrücklich als hypothetisches Planungswerkzeug deklariert; Szenario mit zwei alternativen Ausgängen; spätere Verschiebung der AGI-Mediane (Kokotajlo ca. 2030; Lifland um ca. 3 Jahre). → QUELLEN.md Nr. 106. **[Prognose / Szenario]** — *▲ Die Angabe der zwei Verzweigungen (Endungen des Szenarios) ist vor Drucklegung an ai-2027.com zu verifizieren.*

[17] Goldman Sachs Research (Joseph Briggs & Devesh Kodnani): *Generative AI Could Raise Global GDP by 7%*. 2023 — ca. 7 % globales BIP über 10 Jahre (≈ 7 Bio. USD), +1,5 Prozentpunkte Produktivitätswachstum; ca. zwei Drittel der US-Berufe exponiert, davon 25–50 % der Tätigkeiten automatisierbar. → QUELLEN.md Nr. 96. **[Prognose]**

[18] McKinsey Global Institute / McKinsey Digital: *The Economic Potential of Generative AI*. Juni 2023 — 2,6–4,4 Bio. USD jährlich über 63 Anwendungsfälle; ca. 75 % des Werts in vier Funktionen (Marketing/Vertrieb, Customer Operations, Software-Engineering, F&E). → QUELLEN.md Nr. 97. **[Prognose]**

[19] Daron Acemoglu: *The Simple Macroeconomics of AI*. NBER Working Paper Nr. 32487, April 2024 — max. ca. 0,66 % TFP-Zuwachs über 10 Jahre; Annahmen ca. 20 % exponierte Tätigkeiten, davon ca. 23 % profitabel automatisierbar. Call-back auf Kapitel 6. → QUELLEN.md Nr. 110. **[Prognose / Modellrechnung]** — *Die im Text angeschlossene Rechnung „drei multiplizierte Schätzungen" ist eine Veranschaulichung des Autors, keine Angabe der zitierten Studien.*

[20] ▲ Clifford Stoll: *Why the Web Won't Be Nirvana*. Newsweek, 26./27. Februar 1995; spätere Selbstkorrektur (2010). Call-back auf Kapitel 5. → QUELLEN.md Nr. 35. **[belegt als Fehlprognose]** — *Die drei Vorhersagen sind im Text sinngemäß wiedergegeben; englischer Originalwortlaut vor Drucklegung an der Newsweek-Fassung prüfen.*

[21] ▲ Roy Amara (Institute for the Future): Amara's Law — kurzfristige Über-, langfristige Unterschätzung technischer Wirkung; Datierung meist auf ca. 1978, Erstnennung unsicher. Call-back auf Kapitel 4. → QUELLEN.md Nr. 53. **[belegt als Zuschreibung, Datierung unsicher]**

[22] Zur „bayerischen Ärztewarnung" als wahrscheinliche Legende: *Eisenbahnkrankheit* (Forschungsstand); W. K. Mück (Archiv-Negativbefund). Call-back auf Kapitel 2. → QUELLEN.md Nr. 5, 6. **[belegt als Mythos]**

[23] ▲ Christian B. Anfinsen: Nobelpreis für Chemie 1972 (Arbeiten zur Ribonuklease); „Anfinsen-Dogma" — die Information für die native Faltung steckt in der Aminosäuresequenz. Cyrus Levinthal: *How to Fold Graciously*, 1969 — Levinthal-Paradox: astronomische Zahl möglicher Konformationen gegenüber Faltungszeiten im Millisekundenbereich. NobelPrize.org; Standardliteratur der Strukturbiologie. → QUELLEN.md Nr. 119. **[belegt]** — *Jahreszahlen, Preisbegründung und Formulierung des Levinthal-Arguments vor Drucklegung prüfen; keine Wortzitate im Text.*

[24] ▲ CASP — *Critical Assessment of Structure Prediction*, initiiert 1994 von John Moult u. a., zweijährliche Blindprüfung; CASP13 (2018) erster AlphaFold-Sieg; CASP14 (2020) AlphaFold2 mit einem Median-GDT-Wert um 92, Schwellenbereich um 90 als experimentnahe Genauigkeit; Einordnung der Organisatoren, das Problem sei in wesentlichem Sinn gelöst. predictioncenter.org; Nature 2020. → QUELLEN.md Nr. 120. **[belegt]** — *Medianwert, Metrik und die Aussage der Organisatoren am CASP14-Bericht verifizieren; im Text sinngemäß, ohne Wortzitat.*

[25] ▲ Protein Data Bank (seit 1971), Bestand zum Zeitpunkt von AlphaFold2 in der Größenordnung von 170.000 experimentell bestimmten Strukturen; AlphaFold2 in Nature, Juli 2021, samt Code; AlphaFold Protein Structure Database (DeepMind/EMBL-EBI), Start Juli 2021 mit Humanproteom und Modellorganismen, Ausbau Juli 2022 auf über 200 Mio. Vorhersagen. rcsb.org; alphafold.ebi.ac.uk. → QUELLEN.md Nr. 121. **[belegt]** — *PDB-Bestandszahl und Ausbaudaten an den Betreiberangaben prüfen.*

[26] ▲ Grenzen der Strukturvorhersage: Konfidenzmaß pLDDT je Rest; niedrige Konfidenz bei intrinsisch ungeordneten Bereichen; keine Aussage über Faltungsweg und Dynamik; unzuverlässige Erfassung der Effekte einzelner Mutationen; Molekülkomplexe erst mit Nachfolgemodellen (AlphaFold-Multimer; AlphaFold3, Nature, Mai 2024). → QUELLEN.md Nr. 122. **[belegt]** — *Einzelpunkte an der AlphaFold2/3-Primärliteratur belegen. Die Bemerkung, das Modell stehe auf den Daten der experimentellen Strukturbiologie, ist Überlegung des Autors.*

[27] ▲ Andrew Ng: Mitgründer von Coursera, Gründer von DeepLearning.AI. → QUELLEN.md Nr. 123. **[belegt]** — *Im Text nur als Interessenlage angeführt, ausdrücklich ohne Entwertung seiner Argumente.*

[28] ▲ Bundeszentrale für politische Bildung, *Aus Politik und Zeitgeschichte* 7/1980: *Mikroelektronik — die dritte industrielle Revolution*. — Zeitgenössische Debatte über technologisch verursachte Massenarbeitslosigkeit. Call-back auf Kapitel 5 und 6. → QUELLEN.md Nr. 30. **[belegt als zeitgenössische Debatte]** — *Belegstelle prüfen; die Bewertung des Ausgangs ist im Text als Einordnung des Autors markiert.*

[29] Berkeley Roundtable on the International Economy (BRIE): *Automation and the Future of Work in Germany*, 2022; ergänzend OECD: *The Risk of Automation for Jobs in OECD Countries*, 2016. — Keine überdurchschnittlichen Jobverluste in hochautomatisierten deutschen Regionen; Produktivitätszuwächse eher mit regionalem Beschäftigungswachstum verbunden. Call-back auf Kapitel 5. → QUELLEN.md Nr. 31. **[belegt]**

[30] De Simone, Martín; Tiberti, Federico u. a. (Weltbank): *From Chalkboards to Chatbots: Transforming Learning in Nigeria*, 2024/25 — Edo-State-Pilot, ca. 800 Schüler:innen, 9 Schulen, 6 Wochen, randomisiert, GPT-4 über Microsoft Copilot als begleiteter Tutor; Lernzuwachs verglichen mit ca. zwei Jahren regulärer Schulbildung, ca. 48 USD pro Kind; Caveats in Kapitel 7 ausgeführt. Call-back auf Kapitel 7. → QUELLEN.md Nr. 65. **[belegt]** — *Im Text als Prüfung der Andreessen-Behauptung verwendet, nicht als Bestätigung des Essays insgesamt.*
