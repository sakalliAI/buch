# Einleitung — Wovor hast du eigentlich Angst?

Mein erster Bot hat Stunden gezählt.

Genauer gesagt hat er Stundenbuchungen aus einem System genommen und in ein zweites übertragen. Zwei Programme, die nichts voneinander wissen wollten: In dem einen buchten die Kolleginnen und Kollegen ihre Zeiten, aus dem anderen kamen die Auswertungen. Dazwischen war eine Lücke, und in dieser Lücke saß ein Mensch.

Sie saß da schon lange. Eine Kollegin, die diese Übertragung jahrelang gepflegt hatte, jeden Monat aufs Neue, zwei Fenster nebeneinander auf dem Bildschirm, links lesen, rechts eintragen, Zeile für Zeile. Sie war gut darin. Sie hatte sich einen Rhythmus zurechtgelegt, kleine Kontrollpunkte, eine eigene Reihenfolge, mit der sie sich absicherte. Sie beschwerte sich nicht. Wenn du jemanden fragst, der so eine Aufgabe erledigt, ob sie ihn stört, sagt er meistens erst mal nein. Man arrangiert sich. Man ist stolz darauf, dass es funktioniert, gerade weil es niemand sonst so sauber hinbekommt.

Aber jeder Tippfehler wanderte weiter. Eine vertauschte Ziffer stand am Ende in einer Auswertung, auf die sich andere verließen. Und wenn zum Monatsende alles gleichzeitig fällig war, wurde es eng.

Dann kam der Bot. Kein besonders kluges Ding, ehrlich gesagt: ein Ablauf, der nachts anlief, sich in beide Systeme einloggte, die Datensätze abglich und übertrug. Regeln, keine Intelligenz. Ich erinnere mich an den Morgen nach dem ersten sauberen Durchlauf. Man geht an den Rechner, öffnet das Protokoll und rechnet fest damit, dass irgendwo etwas rot ist. Es war nichts rot. Die Zahlen stimmten. Etwas, das jahrelang Stunden gefressen hatte, war über Nacht passiert, während niemand im Haus war.

Die Erleichterung im Team war mit Händen zu greifen. Und die Kollegin, die das all die Jahre gemacht hatte, sah mich an und sagte etwas, das ich nicht vergessen habe.

Erst: „Gott sei Dank."

Und kurz danach, leiser: „Und was mache ich jetzt?"

Beide Sätze in zehn Sekunden. Ich habe damals gelacht, weil ich dachte, das sei ein Witz. War es nicht. Es war der ehrlichste Satz, den ich in diesem Projekt gehört habe, und er hat mir mehr über Automatisierung beigebracht als jede Schulung.

Denn die beiden Sätze widersprechen sich nicht. Sie stimmen beide gleichzeitig. Die Arbeit war stumpf, und sie loszuwerden war eine Befreiung. Und dieselbe Arbeit war ein Stück Sicherheit gewesen: etwas, das ihr gehörte, wofür man sie brauchte, was sie besser konnte als alle anderen. Der Bot hat ihr nicht nur eine lästige Tätigkeit abgenommen. Er hat ihr eine Antwort auf die Frage weggenommen, wozu sie da ist. Und diese Antwort hatte ihr niemand ersetzt, bevor die Maschine kam. Wir hatten wochenlang über Fehlerquoten und Laufzeiten gesprochen und keine fünf Minuten darüber, was das für die Frau bedeutet, die bis dahin die Schnittstelle war. Gefragt hatte sie auch niemand. Automatisierung wird fast immer über die Köpfe derer hinweg entschieden, deren Arbeit sie betrifft, nicht aus Bosheit, sondern weil es in den Projektunterlagen keine Zeile dafür gibt. Ich mache das heute anders herum: erst mit den Leuten reden, deren Aufgabe verschwinden soll, dann bauen. Es kostet ein paar Wochen mehr. Es erspart einem den Satz, den ich damals gehört habe.

Das war vor einigen Jahren, in der Frühzeit dessen, was die Branche RPA nennt, Robotic Process Automation. Damals war die Skepsis ein Grundrauschen in jedem Meeting. Man wurde in Besprechungen gebeten, das Wort „Roboter" lieber nicht zu benutzen, weil sonst gleich die falschen Bilder im Kopf entstanden. In den Wochen nach dem ersten Bot kamen Leute aus anderen Abteilungen zu mir, und die Frage war fast nie „Kann das auch meinen Prozess?". Sie lautete „Kommt das jetzt bei uns auch?", und der Tonfall entschied darüber, was gemeint war. Manche hofften. Manche rechneten. Heute baue ich mir abends mit Werkzeugen wie Claude Code kleine Programme, die mir den Alltag erleichtern, und diese Werkzeuge sind unvergleichlich mächtiger als alles, was ich damals gebaut habe. Sie schreiben Code, lesen Dokumente, formulieren Texte. Der zweite Satz meiner Kollegin ist trotzdem geblieben. Er hat nur das Gewand gewechselt. Aus „Und was mache ich jetzt?" ist „Was, wenn die KI uns alle ersetzt?" geworden.

Diese Frage ist nicht neu. Sie ist nicht einmal hundert Jahre alt. Sie ist Jahrhunderte alt, und genau darum geht es in diesem Buch.

## Ein Mönch, der gegen den Buchdruck anschrieb

Im Jahr 1492 setzte sich der Abt Johannes Trithemius hin und verfasste eine flammende Verteidigung der Handschrift. Sein Text trägt den Titel *De laude scriptorum*, „Lob der Schreiber".[1] Seine Sorge: Der neumodische Buchdruck werde die Mönche faul machen, das Gedächtnis verkümmern lassen, das mühevoll abgeschriebene Wort entwerten. Gedrucktes Papier vergilbe ohnehin in zweihundert Jahren, während ordentliches Pergament Jahrhunderte überdauere. Der Mensch verlerne das Denken, wenn ihm die Maschine die Arbeit abnehme.

Du ahnst, was kommt. Trithemius ließ seine Streitschrift gegen den Buchdruck — drucken. Anders hätte sie kaum jemand gelesen. Der Mann, der vor der Maschine warnte, benutzte die Maschine, weil sie schlicht besser funktionierte.

Wenige Jahrzehnte später beklagte sich der Gelehrte Erasmus von Rotterdam über etwas, das uns sehr vertraut vorkommt: die schiere Flut an Büchern, diese „Schwärme neuer Bücher", in denen niemand mehr das Wichtige vom Belanglosen unterscheiden könne.[2] Informationsüberflutung, anno 1525.

Halte diesen Gedanken einen Moment fest. Das Gefühl, dass die neue Technik uns das Denken abgewöhnt, dass wir in Information ertrinken, dass etwas Wesentliches verloren geht — dieses Gefühl ist kein Produkt von ChatGPT. Es ist ein menschlicher Reflex, und er wird zuverlässig ausgelöst, seit wir Werkzeuge bauen, die uns über den Kopf zu wachsen scheinen.

## Die Sache mit der Eisenbahn

Wahrscheinlich kennst du die Geschichte: Als die ersten Eisenbahnen fuhren, hätten Ärzte gewarnt, das menschliche Gehirn halte Geschwindigkeiten über dreißig Stundenkilometer nicht aus, die Reisenden würden wahnsinnig. Oft wird ein bayerisches Medizinalkollegium als Quelle genannt.

Diese Geschichte ist großartig. Sie hat nur einen Haken: Sie stimmt vermutlich nicht.[3] Für das angeblich so berühmte Gutachten gibt es keinen belastbaren Beleg. In den bayerischen Archiven wurde trotz intensiver Suche nichts dergleichen gefunden, und die zitierte Behörde lässt sich für die Zeit um 1835 nicht einmal nachweisen. Als Ursprung gilt heute eine Polemik des Historikers Heinrich von Treitschke, Jahrzehnte nach den ersten Zügen geschrieben, danach endlos weitergereicht.[3]

Ich erzähle dir das gleich zu Beginn, weil es den Ton dieses Buches setzt. Ich bin nicht hier, um dir alte Schauergeschichten aufzutischen, über die wir gemeinsam lachen können, damit du dich der KI gegenüber überlegen fühlst. Das wäre billig. Und es wäre unehrlich. Wer die KI-Skepsis mit „damals hatte man ja auch Angst vor der Eisenbahn" abräumt, beruft sich ausgerechnet auf eine erfundene Warnung. Das ist kein guter Start für ein Gespräch über Belege.

Denn die Wahrheit ist komplizierter, und sie ist interessanter. Manche Technikängste waren erfunden. Manche wurden bewusst geschürt, von Leuten, die etwas davon hatten. Und manche waren vollkommen berechtigt. Diese drei auseinanderzuhalten — darum geht es. Wer alles in einen Topf wirft und „war doch alles halb so wild" darüberstreut, betreibt dasselbe Geschäft wie die Panikmacher, nur mit umgekehrtem Vorzeichen.

## Ein Muster, das sich wiederholt

Wenn du die letzten fünfhundert Jahre durchgehst, taucht dasselbe Muster auf, immer wieder, fast schon langweilig in seiner Regelmäßigkeit. Eine neue Technik erscheint. Sie macht Angst. Es wird gewarnt, gespottet, verboten, gepredigt. Dann, nach einer Weile, wird sie Alltag, so selbstverständlich, dass die nächste Generation sich kaum vorstellen kann, dass jemand je Angst davor hatte.

Der Buchdruck. Die Eisenbahn. Die Elektrizität, vor der man sich fürchtete wie heute mancher vor dem Mobilfunkmast. Das Telefon, das angeblich die Familie zerrütten würde. Das Auto. Das Radio, das Fernsehen, der Taschenrechner, der Computer, das Internet, das Smartphone. Jedes Mal dieselbe Kurve: erst der Schrecken, dann der Alltag.

Die Wissenschaft hat dafür inzwischen einen Namen. Die Psychologin Amy Orben nennt es den „Sisyphos-Zyklus der Technikpaniken": Jede Generation rollt denselben Stein den Berg hinauf, fürchtet sich vor dem Neuen mit fast denselben Argumenten wie die Generation davor, vergisst es anschließend und ist dann ehrlich überrascht, wenn die eigenen Kinder dasselbe mit der nächsten Technik durchmachen.[4] Wir lernen das Muster nicht, weil wir es nach jedem Durchlauf wieder vergessen.

Genau dieses Vergessen will dieses Buch beheben. Wenn du das Muster einmal klar vor dir siehst, verändert sich, wie du auf die künstliche Intelligenz schaust. Nicht weil das Muster beweist, dass alles gut wird. Sondern weil es dir die Panik aus den Knochen nimmt und den Kopf frei macht für die Fragen, die wirklich zählen.

## Drei Sorten von Angst

Ich muss an dieser Stelle ehrlich sein, sonst können wir uns die nächsten zweihundert Seiten sparen.

Nicht jede Angst vor neuer Technik war Unsinn. Als die Kodak-Kamera Ende des 19. Jahrhunderts plötzlich jeden zum Schnappschuss-Fotografen machte, brach eine echte Sorge um die Privatsphäre aus. Wildfremde Leute konnten dich auf der Straße ablichten, ohne zu fragen, und das Bild landete irgendwo, wo du es nie zu sehen bekamst. Diese Sorge war so berechtigt, dass zwei amerikanische Juristen 1890 einen Aufsatz schrieben, der das moderne Recht auf Privatsphäre begründete.[5] Die Angst hatte recht, und sie hinterließ etwas Bleibendes. Oder das Smartphone: Dass die ständige Erreichbarkeit unseren Schlaf stört, ist keine Kulturpessimisten-Behauptung, sondern inzwischen gut belegt.[6] Manchmal liegt die Angst eben richtig.

Die zweite Sorte ist unangenehmer, weil sie berechnend ist. Ende der 1880er Jahre führte Thomas Edison eine regelrechte Angstkampagne gegen den Wechselstrom seiner Konkurrenten Westinghouse und Tesla. Wechselstrom war technisch überlegen, und genau das war das Problem: Edison hatte auf Gleichstrom gesetzt. Also ließ sein Umfeld öffentlich Tiere mit Wechselstrom töten, um ihn als Killerstrom vorzuführen, und prägte für den Tod durch Stromschlag den Ausdruck „to be Westinghoused".[7] Auf Empfehlung aus demselben Lager wählte der Staat New York für die Todesstrafe Wechselstrom; am 6. August 1890 wurde William Kemmler als erster Mensch auf dem elektrischen Stuhl hingerichtet, ein qualvoller Vorgang.[8] Hier warnte niemand aus Sorge. Hier verteidigte ein etablierter Anbieter sein Geschäftsmodell mit Leichenbildern. Wenn dir heute jemand mit sehr drastischen Bildern erklärt, warum eine bestimmte Technik gefährlich ist, lohnt die Frage, wem die Antwort nützt.

Und dann gibt es die dritte Sorte, die schlicht verpufft ist. Der Schriftsteller Robert Louis Stevenson schrieb 1878 einen Aufsatz gegen das elektrische Licht: Es sei grauenhaft, überirdisch, eine Zumutung für das menschliche Auge, ein Licht, das nur auf Morde und Verbrechen scheinen sollte oder in die Gänge von Irrenanstalten.[9] In England musste vor motorisierten Fahrzeugen jahrelang ein Mann mit roter Fahne herlaufen; die Fahne verschwand 1878 aus dem Gesetz, die Tempolimits von Schrittgeschwindigkeit blieben noch Jahrzehnte.[10] Beides klingt heute komisch. Beides war damals ernst gemeint, von ernst zu nehmenden Leuten.

Drei Sorten, ein Gefühl. Von außen sehen sie identisch aus, und das ist der eigentliche Ärger: Im Moment der Angst kannst du nicht erkennen, in welcher der drei Kategorien du gerade steckst. Die Aufregung fühlt sich bei einer erfundenen Warnung genauso echt an wie bei einer berechtigten. Nachträglich sortieren kann jeder; im Rückblick sind wir alle klug. Die Kunst ist, die Sortierung zu versuchen, während man mittendrin steht, mit unvollständigen Informationen und einem Bauchgefühl, das laut dazwischenredet. Dafür braucht man kein Orakel, sondern ein paar unbequeme Fragen: Wer behauptet das? Woher weiß er es? Was hat er davon? Und was müsste passieren, damit ich meine Meinung ändere?

## Kompass statt Beruhigungspille

Deshalb verspreche ich dir nicht, dass die KI harmlos ist. Ich verspreche dir etwas Nützlicheres: einen ehrlichen Kompass. Und weil das eine große Behauptung ist, sage ich dir konkret, wie dieses Buch arbeitet.

Erstens trenne ich drei Dinge, die in Debatten dauernd ineinanderlaufen. Ein **Beleg** ist etwas, das passiert ist oder gemessen wurde: eine Studie, ein Gesetz, ein Datum, ein Urteil. Eine **Prognose** ist eine Schätzung über die Zukunft, egal wie seriös die Institution ist, die sie ausspricht. Eine **Meinung** ist eine Position, meine oder die von jemand anderem. Wenn ich meine Meinung sage, schreibe ich dazu, dass es meine Meinung ist. Wenn ich eine Zahl bringe, findest du in den Endnoten, woher sie kommt, damit du es selbst nachprüfen kannst. Erfundene Studien und herbeizitierte Experten gibt es hier nicht.

Zweitens zeige ich dir bei strittigen Fragen beide Seiten mit Namen und Zahlen. Ein Beispiel, das dich in Teil drei wieder einholen wird: Goldman Sachs schätzte 2023, generative KI könne die weltweite Wirtschaftsleistung um rund sieben Prozent steigern.[11] Der MIT-Ökonom Daron Acemoglu rechnete 2024 vor, der Produktivitätseffekt liege über zehn Jahre bei höchstens 0,66 Prozent.[12] Das ist keine kleine Meinungsverschiedenheit, das ist ein Faktor von rund zehn, zwischen zwei Adressen, die beide ernst zu nehmen sind. Beide Zahlen sind Prognosen, keine Messwerte. Wer dir nur eine davon zeigt, verkauft dir etwas.

Drittens: Wo ich es nicht weiß, sage ich, dass ich es nicht weiß. Das kommt öfter vor, als mir lieb ist. Die Forschung zu vielen KI-Wirkungen ist zwei, drei Jahre alt, teilweise als Vorabdruck veröffentlicht und noch nicht unabhängig wiederholt. Ich werde dir das jedes Mal dazusagen, statt eine wacklige Zahl fett zu setzen, weil sie gut in meine Argumentation passt.

Und viertens sage ich dir, wo ich befangen bin. Ich verdiene mein Geld damit, dass Automatisierung funktioniert. Ich baue diese Dinge, ich mag sie, und ich freue mich, wenn sie laufen. Jemand mit dieser Biografie hat einen eingebauten Drall zur guten Nachricht. Ich kann diesen Drall nicht abstellen, aber ich kann ihn dir offenlegen und mich zwingen, die Zahlen, die mir nicht passen, genauso ausführlich zu behandeln wie die anderen. An mindestens einer Stelle in Teil zwei wirst du merken, dass mir eine Studie sichtlich gegen den Strich geht. Sie steht trotzdem drin, mit allem, was für sie spricht.

Das ist der Unterschied zwischen Beruhigung und Vertrauen. Beruhigung ist, wenn dir jemand sagt, du sollst dir keine Sorgen machen. Vertrauen ist, wenn du genug verstehst, um selbst zu entscheiden, worüber du dir Sorgen machen musst und worüber nicht. Das eine macht dich abhängig. Das andere macht dich frei.

## Wer hier mit dir redet

Ein Wort zu mir, damit du weißt, aus welcher Ecke ich komme. Aus dem Ruhrgebiet, um genau zu sein, aus Oberhausen.

Mein Großvater kam als Gastarbeiter nach Deutschland. Mein Vater wurde mit vierzehn nachgeholt, ohne ein Wort Deutsch, und machte eine Ausbildung zum Schlosser. Meine Mutter lernte er in einem Dorf in der Türkei kennen; als ich zur Welt kam, war sie siebzehn. Ein Kind, das ein Kind bekam, tausend Kilometer von der eigenen Familie entfernt, in einer Sprache, die ihr auch nach fünfunddreißig Jahren noch schwerfällt. Ich habe als Jugendlicher gern Ausreden gesucht und dabei auch mal auf die Herkunft geschoben, wenn etwas nicht lief. Heute weiß ich es besser: Jeder ist seines Glückes Schmied. Und Technik ist eines der mächtigsten Werkzeuge, die einem das Schmieden erleichtern, wenn man keine Angst davor hat, sie in die Hand zu nehmen.

Angefangen habe ich mit sieben. Erste Webseiten, HTML, zusammengeklaubt aus dem, was ich finden konnte, mit dieser vollkommen unverhältnismäßigen Begeisterung darüber, dass da etwas auf dem Bildschirm erscheint, weil ich es hingeschrieben habe. Später in der Schulzeit kamen erste kleine Programme dazu. Dann eine Ausbildung zum Informatikkaufmann, wo ich anfing, mit VBA und Access meine eigenen Aufgaben zu automatisieren, ganz eigennützig, weil ich keine Lust auf Fleißarbeit hatte. Irgendwann bekam ich die Chance, ein RPA-Team mitaufzubauen, und automatisierte als Entwickler die Prozesse der Kolleginnen und Kollegen. Da entstand auch der Bot vom Anfang dieses Buches.

Heute leite ich ein Team, in dem Delivery Manager die Verantwortung für Crews tragen, die Automatisierungslösungen bauen: mal mit klassischen, regelbasierten Werkzeugen, mal mit künstlicher Intelligenz, je nachdem, was die Aufgabe braucht. Nicht KI um der KI willen. Ein sauber gebauter, stumpfsinniger Ablauf ist oft die bessere Lösung als ein Sprachmodell, das kreativ wird, wo niemand Kreativität bestellt hat. Privat baue ich mir abends mit Claude Code kleine Helfer für Dinge, die mich stören: flexibel, auf mich zugeschnitten, statt für jede Kleinigkeit ein weiteres Abo abzuschließen. Das ist übrigens der Teil, der mich an dieser Technik am meisten begeistert. Nicht dass sie Konzernen Kosten spart, sondern dass eine einzelne Person sich abends etwas bauen kann, wofür man vor zehn Jahren ein Projektbudget gebraucht hätte. Ich bin kein Philosoph und kein Zukunftsforscher, sondern Praktiker. Ich habe die Skepsis nicht aus Studien gelernt, sondern an echten Schreibtischen gesehen, auf den Gesichtern von Menschen, die nicht wussten, ob die Maschine ihr Freund oder ihr Nachfolger sein würde.

Schon als Student habe ich in einer Facharbeit eine These vertreten, an die ich bis heute glaube: Automatisierung nimmt uns nicht einfach die Arbeit weg, sie verschiebt die Tätigkeit. Sie räumt das Stumpfe ab und schiebt uns das Anspruchsvollere zu. Das ist keine bequeme These, denn die Verschiebung tut weh, solange sie passiert, und sie trifft nicht alle gleich. Ob sie auch für die KI trägt, ist eine offene Frage, und ich werde sie in Teil zwei gegen die Daten laufen lassen, auch gegen die, die ihr widersprechen.

Warum mich das umtreibt: Ich erlebe zu viele Menschen, die sich vor dem Neuen wegducken, nach dem Motto, früher sei alles besser gewesen. War es nicht. Wer dem Fortschritt grundsätzlich misstraut, müsste konsequenterweise mit dem Pferd zur Arbeit reiten statt mit Auto oder Bus. Macht aber keiner. Wir nehmen die Bequemlichkeiten, die uns die alten, einst gefürchteten Techniken schenken, völlig selbstverständlich. Meine Frau und ich arbeiten ehrenamtlich mit Jugendlichen, und dort sehe ich beides: die, die sich alles zutrauen, und die, die von vornherein glauben, das sei nichts für sie. Ich hatte in meiner Jugend keinen Mentor. Ich weiß ziemlich genau, was mir das gekostet hat. Dieses Buch ist der Versuch, für ein Thema die Rolle zu übernehmen, die mir damals gefehlt hat.

## Wie dieses Buch gebaut ist

Damit du weißt, was dich erwartet, hier die Landkarte.

Der **erste Teil** zeigt dir das Muster. Wir gehen zurück zu Trithemius und seinem Buchdruck, steigen in einen frühen Zug, sehen dem Stromkrieg zu, hören beim Telefon und beim Fernsehen zu, wie dieselben Sätze in neuen Kostümen wiederkehren. Und wir schauen uns an, warum unser Verstand auf Neues so verlässlich mit Furcht reagiert und warum das evolutionär eine ziemlich gute Idee war. Dazu kommen die Werkzeuge, mit denen die Forschung solche Wellen beschreibt: was eine moralische Panik ausmacht, warum wir kurzfristig immer zu viel und langfristig immer zu wenig erwarten, und warum man eine Technik am Anfang leicht steuern könnte, aber noch nicht versteht — und am Ende versteht, aber kaum noch steuern kann. Am Ende des ersten Teils wirst du den Reflex erkennen, sobald du ihn siehst, auch bei dir selbst. Das ist keine Immunisierung. Ich erkenne ihn bei mir auch und habe ihn trotzdem.

Der **zweite Teil** zieht eine ehrliche Bilanz der KI von heute. Nimmt sie dir die Arbeit weg? Macht sie uns dümmer? Was ist mit Diskriminierung, Datenschutz, Falschinformation, Energieverbrauch? Hier wird es konkret. Rechenzentren verbrauchten 2024 rund 415 Terawattstunden Strom, etwa anderthalb Prozent des weltweiten Verbrauchs[13] — und die eigentliche Arbeit beginnt genau da: Ist das viel? Verglichen womit? Solche Fragen sind der Alltag dieses Teils. Hier trenne ich Beleg, Prognose und Meinung besonders streng, und hier schenke ich dir nichts, in keine Richtung. Du wirst Studien finden, die eine deutliche Produktivitätssteigerung messen, und daneben eine, in der erfahrene Entwickler mit KI-Unterstützung langsamer wurden, obwohl sie selbst überzeugt waren, schneller zu sein.[14] Beide sind seriös. Beide stehen drin.

Der **dritte Teil** führt vom Fürchten zum Vertrauen. Wir hören uns die großen Prognosen an, die euphorischen wie die düsteren, und lernen, sie zu lesen. Das ist eine Fähigkeit für sich: 1995 erklärte der Astronom und frühe Netzpionier Clifford Stoll in *Newsweek*, warum das Internet weder den Handel noch die Zeitungen noch die Schule ernsthaft verändern werde.[15] Er war klug, er kannte das Netz besser als fast jeder andere, und er lag daneben. Danach reden wir darüber, was vom Menschen bleibt, wenn die Maschine immer mehr kann. Im zwölften Kapitel sage ich dir, wovor ich tatsächlich Angst habe, und das ist nicht das, was in den Schlagzeilen steht. Und am Ende bekommst du etwas Praktisches in die Hand: wie man Vertrauen aufbaut, ohne naiv zu werden. Vertrauen ist keine Stimmung, es ist eine Fähigkeit, und Fähigkeiten kann man lernen.

Die Kollegin von damals hat ihren Job übrigens behalten. Sie macht heute nicht mehr die nächtliche Übertragung, die der Bot erledigt. Sie macht das, wofür vorher nie Zeit war. Ihre Tätigkeit hat sich verschoben, genau wie in meiner Facharbeit. Ob das auch im großen Maßstab so kommt, mit der KI, das ist keine ausgemachte Sache, und wir werden den Daten dazu auf den Grund gehen.

Aber eines steht fest: Die Lok fährt los, ob wir nun Angst haben oder nicht. Die Frage ist bloß, ob wir am Bahnsteig stehen bleiben — oder einsteigen und schauen, wohin sie fährt. Ich finde, einsteigen ist die klügere Wahl. Lass mich dir zeigen, warum.

---

## Quellen zu dieser Einleitung
*(Endnoten-Nummerierung kapitelweise; Mapping auf das zentrale `QUELLEN.md`.)*

[1] Johannes Trithemius: *De Laude Scriptorum (Lob der Schreiber)*. 1492 (gedruckt). Vgl. krit. Ausgabe hrsg. Klaus Arnold, Übers. R. Behrendt, 1974; History of Information. → QUELLEN.md Nr. 1, 3. ▲ Wortlaut vor Druck verifizieren.
[2] Erasmus von Rotterdam: Klage über die „Bücherflut" (Adagium *Festina lente*, 1525/26). → QUELLEN.md Nr. 4. ▲ vor Druck am Original absichern.
[3] Zur „bayerischen Ärztewarnung" als wahrscheinliche Legende, zum Archiv-Negativbefund und zum Treitschke-Ursprung: *Eisenbahnkrankheit* (Überblick m. Forschungsstand); W. K. Mück (kein Obermedizinalkollegium um 1835 nachweisbar). → QUELLEN.md Nr. 5, 6.
[4] Amy Orben: *The Sisyphean Cycle of Technology Panics*. Perspectives on Psychological Science 15(5), 2020, DOI 10.1177/1745691620919372. → QUELLEN.md Nr. 54.
[5] Samuel D. Warren & Louis D. Brandeis: *The Right to Privacy*. 4 Harvard Law Review 193 (1890). → QUELLEN.md Nr. 43.
[6] Elektronische Mediennutzung & Schlafqualität (Meta-Analyse). → QUELLEN.md Nr. 41.
[7] Zum „Stromkrieg": Edisons AC-Angstkampagne, Harold P. Brown, öffentliche Tier-Elektrokutionen, Begriff „to be Westinghoused"; technische Überlegenheit und Durchsetzung des Wechselstroms. → QUELLEN.md Nr. 9, 10.
[8] Erste Hinrichtung auf dem elektrischen Stuhl: William Kemmler, 6.8.1890, Auburn (New York), Wechselstrom. → QUELLEN.md Nr. 11.
[9] Robert Louis Stevenson: *A Plea for Gas Lamps*. 1878, in *Virginibus Puerisque*, 1881 („horrible, unearthly, obnoxious to the human eye"). → QUELLEN.md Nr. 12. ▲ Deutsche Übersetzung der zitierten Wendungen vor Drucklegung festlegen; im Text bewusst Paraphrase.
[10] *Locomotive Acts* (Großbritannien): Red Flag Act 1865; Wegfall der roten Fahne 1878; Anhebung der Tempolimits 1896. → QUELLEN.md Nr. 18. ▲ Datierungen vor Drucklegung final prüfen.
[11] Goldman Sachs Research (Briggs/Kodnani): *Generative AI Could Raise Global GDP by 7%*. 2023. [Prognose] → QUELLEN.md Nr. 96.
[12] Daron Acemoglu: *The Simple Macroeconomics of AI*. NBER Working Paper 32487, April 2024 (≤ 0,66 % TFP über zehn Jahre). [Prognose] → QUELLEN.md Nr. 110.
[13] IEA: *Energy and AI*. April 2025 (Rechenzentren 2024: rund 415 TWh, ca. 1,5 % des weltweiten Stromverbrauchs). → QUELLEN.md Nr. 86.
[14] Gegenläufige Produktivitätsbefunde: Brynjolfsson/Li/Raymond, *Generative AI at Work*, QJE 140(2), 2025 (~15 %); Peng et al., *GitHub Copilot*, arXiv:2302.06590, 2023 — gegenüber METR: *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*, arXiv:2507.09089, 2025 (19 % langsamer bei gegenteiliger Selbsteinschätzung). → QUELLEN.md Nr. 55, 56, 64.
[15] Clifford Stoll: *Why the Web Won't Be Nirvana*. Newsweek, 1995. → QUELLEN.md Nr. 35. ▲ Wortlaut/Datum vor Drucklegung am Originalartikel prüfen.
