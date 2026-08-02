# Kapitel 6 — Nimmt die KI mir die Arbeit weg?

„Und was mache ich jetzt?"

Der Satz meiner Kollegin, in der Einleitung, zehn Sekunden nach „Gott sei Dank". Ich schulde dir die Fortsetzung.

Sie hat ihren Job behalten. Die nächtliche Übertragung der Stundenbuchungen macht der Bot, seit Jahren, klaglos. Was sie heute macht, ist das, wofür vorher nie Zeit war: die Fälle prüfen, an denen der Bot scheitert, weil ein Mensch ein Feld freihändig befüllt hat. Mit den Leuten reden, die es freihändig befüllen. Dafür sorgen, dass die Daten überhaupt stimmen, bevor sie irgendwo landen. Sie hat nicht weniger zu tun als vorher. Sie hat etwas anderes zu tun.

Und jetzt kommt der Teil, den ich mir nicht schenken darf: Das beweist genau gar nichts.

Ein Schreibtisch ist keine Volkswirtschaft. Ich könnte dir drei weitere solcher Geschichten erzählen, sie sind alle wahr, und ein Kollege aus einer anderen Firma könnte dir drei Geschichten erzählen, in denen es anders ausging. Anekdoten sind gut, um zu zeigen, wie sich etwas anfühlt. Sie taugen nichts, um zu klären, was passiert. Wenn du wissen willst, ob die KI dir die Arbeit wegnimmt, musst du dich mit Daten herumschlagen, und ein Teil dieser Daten wird dir nicht gefallen. Mir gefällt er auch nicht.

Also: Beweisaufnahme. Erst das, was belegt ist. Dann das, was geschätzt wird. Dann das, was jemand einfach behauptet. In dieser Reihenfolge, und ich sage dir jedes Mal, in welcher Kategorie wir gerade sind.

## Was tatsächlich gemessen wurde

Fangen wir mit dem an, wofür es echte Messungen gibt, keine Umfragen über Erwartungen, sondern beobachtete Arbeit von echten Leuten.

Die bekannteste Untersuchung stammt von Erik Brynjolfsson, Danielle Li und Lindsey Raymond und ist 2025 im *Quarterly Journal of Economics* erschienen. Ein Software-Unternehmen führte einen generativen KI-Assistenten im Kundenservice gestaffelt ein, was den Forschern erlaubte, Gruppen mit und ohne Assistent zu vergleichen. Datengrundlage: 5.172 Kundendienst-Mitarbeitende. Ergebnis: eine durchschnittliche Steigerung der gelösten Vorgänge pro Stunde von rund 15 Prozent — in der früheren Arbeitspapier-Fassung waren es 14.[1]

Der interessantere Befund steckt aber nicht im Durchschnitt, sondern in der Verteilung. Am stärksten profitierten die wenig erfahrenen und gering qualifizierten Beschäftigten; sie wurden nicht nur schneller, sondern auch besser. Die erfahrensten Kräfte zeigten nur kleine Zuwächse. Nebenbei stiegen Kundenzufriedenheit und Mitarbeiterbindung.[1]

Halte das fest, denn es ist der Kern des ganzen Kapitels: Das Werkzeug hebt die Basis, nicht die Spitze. Es macht aus einem Anfänger schneller einen Soliden. Aus einem Könner macht es kaum mehr, als er ohnehin ist.

Die zweite oft zitierte Zahl kommt aus der Softwareentwicklung. In einem randomisierten Experiment sollten Entwicklerinnen und Entwickler einen HTTP-Server in JavaScript implementieren. Die Gruppe mit GitHub Copilot war rund 56 Prozent schneller: 71 Minuten gegen 160.[2] Beeindruckend — und genau hier muss ich anfangen zu bremsen, obwohl mir die Zahl als Automatisierer natürlich gefällt. Es ist ein Arbeitspapier, nicht peer-reviewt. Es ist ein Laborversuch mit einer klar umrissenen Aufgabe. Und eine klar umrissene Aufgabe in einem leeren Verzeichnis hat mit dem, was Entwickler den ganzen Tag tun, ungefähr so viel zu tun wie ein Fahrschulparcours mit dem Berufsverkehr in Essen.

Wie wenig, zeigt der nächste Befund.

## Der Befund, der mir nicht in den Kram passt

Ich habe in diesem Buch versprochen, dir auch die Zahlen zu zeigen, die gegen meine eigene Begeisterung sprechen. Hier ist die wichtigste.

Die Forschungsorganisation METR führte 2025 einen randomisierten kontrollierten Versuch durch. Teilnehmer waren 16 erfahrene Open-Source-Entwicklerinnen und -Entwickler, die an ihren eigenen, großen, ihnen bestens vertrauten Repositories arbeiteten. Also keine Laboraufgabe, sondern echte Arbeit an echtem Code, den sie seit Jahren kennen. Mit KI-Werkzeugen brauchten sie im Schnitt 19 Prozent **länger**.[3]

Das allein wäre schon unangenehm. Der eigentliche Hammer kommt danach: Dieselben Leute glaubten hinterher, sie seien rund 20 Prozent schneller gewesen. Sie waren langsamer und fühlten sich schneller. Die Differenz zwischen Wahrnehmung und Messung beträgt ungefähr vierzig Prozentpunkte.[3]

Setz dich damit einen Moment auseinander, bevor du weiterliest. Wenn erfahrene Profis in ihrem eigenen Fachgebiet um vierzig Punkte danebenliegen, was die Wirkung eines Werkzeugs auf ihre eigene Arbeit angeht — was ist dann dein Bauchgefühl wert? Und was meins? Ich habe abends Werkzeuge mit Claude Code gebaut und war überzeugt, in zwei Stunden geschafft zu haben, wofür ich sonst einen Samstag gebraucht hätte. Vielleicht stimmt das. Vielleicht habe ich auch nur die vierzig Minuten vergessen, in denen ich einen Fehler gesucht habe, den ich selbst nie gemacht hätte. Ich habe es nie gestoppt. Fast niemand stoppt es.

Der Ehrlichkeit halber gehört die andere Hälfte dazu: METR hat im Februar 2026 nachgelegt und eingeschätzt, dass spätere Werkzeuggenerationen aus dem Jahr 2025 vermutlich stärker beschleunigen.[3] Die Studie ist eine Momentaufnahme, kein Naturgesetz. Und sechzehn Teilnehmer sind sechzehn Teilnehmer.

Trotzdem bleibt eine Lehre, die ich für belastbarer halte als jede einzelne Prozentzahl: Der Produktivitätsgewinn hängt davon ab, wer du bist und was du tust. Bist du neu in einer Sache, hilft dir das Modell viel. Bist du seit fünfzehn Jahren in einem komplizierten System zu Hause, kann es dich bremsen, weil du seine Vorschläge dauernd prüfen und korrigieren musst — und das Prüfen dauert manchmal länger als das Selbermachen. Wer dir eine einzige Prozentzahl für „die Produktivität durch KI" nennt, hat entweder nur eine Studie gelesen oder verkauft dir etwas.

## Die großen Schätzungen — und warum sie Schätzungen bleiben

Jetzt wechseln wir die Kategorie. Alles, was jetzt kommt, sind **Prognosen und Modellrechnungen**, keine Messungen. Ich sage das nicht aus Bescheidenheit, sondern weil der Unterschied entscheidend ist: Man kann zählen, wie viele Vorgänge 5.172 Menschen in einer Stunde gelöst haben. Man kann nicht zählen, wie viele Jobs es 2030 gibt.

Das Weltwirtschaftsforum befragte für seinen *Future of Jobs Report 2025* rund 1.000 Unternehmen mit zusammen über 14 Millionen Beschäftigten aus 22 Branchen und 55 Volkswirtschaften. Die Erwartung dieser Arbeitgeber: bis 2030 rund 170 Millionen neu entstehende und 92 Millionen wegfallende Stellen, also ein Netto-Zuwachs von 78 Millionen Arbeitsplätzen durch KI und Informationstechnologien. 85 Prozent der Arbeitgeber planen, in Weiterbildung zu investieren.[4] Das ist eine Prognose, und zwar eine, die auf Selbstauskünften von Personalabteilungen beruht. Sie sagt aus, was Unternehmen glauben, dass sie tun werden. Ob sie es tun, steht auf einem anderen Blatt — besonders die 85 Prozent bei der Weiterbildung würde ich mir gern in fünf Jahren noch einmal ansehen.

Die OECD schaut in ihrem *Employment Outlook 2025* nicht nach vorn, sondern zurück, und findet bislang wenig Belege dafür, dass KI zu Jobverlusten geführt hat. Zwei Drittel der Beschäftigten, die bereits mit KI arbeiten, geben an, ihre Arbeit sei weniger monoton oder weniger gefährlich geworden.[5] Dieselbe OECD beziffert aber auch den Anteil der Berufe mit dem höchsten Automatisierungsrisiko auf 27 Prozent der Beschäftigung im OECD-Raum.[5] Beides in einem Bericht, und beides stimmt: bisher wenig passiert, potenziell viel möglich.

Die Internationale Arbeitsorganisation hat gemeinsam mit dem polnischen Forschungsinstitut NASK im Mai 2025 einen Expositionsindex vorgelegt. Ergebnis: Weltweit arbeitet etwa jeder vierte Beschäftigte in einem Beruf mit einer gewissen Exposition gegenüber generativer KI. Die meisten dieser Jobs werden nach Einschätzung der Autoren **transformiert, nicht ersetzt**.[6]

Und hier wird es politisch. Die Exposition ist extrem ungleich verteilt: 34 Prozent der Beschäftigung in Hocheinkommensländern gegenüber 11 Prozent in Niedrigeinkommensländern. In der höchsten Expositionskategorie liegen 3,3 Prozent der weltweiten Beschäftigung — bei Frauen sind es 4,7 Prozent, bei Männern 2,4 Prozent.[6] Fast doppelt so hoch bei Frauen. Der Grund ist unspektakulär und deswegen so hartnäckig: In den Berufen, die generative KI am ehesten berührt, also Büro-, Sachbearbeitungs- und Sekretariatstätigkeiten, arbeiten überproportional viele Frauen.

Der Internationale Währungsfonds kam im Januar 2024 auf eine breitere Definition: rund 40 Prozent der Jobs weltweit seien KI-exponiert, in fortgeschrittenen Volkswirtschaften etwa 60 Prozent, wovon ungefähr die Hälfte ein Risiko sinkender Arbeitsnachfrage oder sinkender Löhne trage. In Schwellenländern liegt der Wert bei rund 40 Prozent, in Niedrigeinkommensländern bei rund 26 Prozent. Der IWF verbindet das mit einer ausdrücklichen Warnung vor wachsender Ungleichheit.[7]

Beachte die Richtung dieser Zahlen, sie ist nämlich nicht die, die man erwartet. Die reichen Länder sind *stärker* exponiert, nicht schwächer. Wer viel Bürojob hat, hat viel Angriffsfläche. Die Ungleichheitsgefahr besteht nicht darin, dass arme Länder mehr Jobs verlieren, sondern darin, dass sie von den Produktivitätsgewinnen weniger abbekommen und der Abstand größer wird. Das ist eine andere Sorge, und sie wird in der deutschen Debatte praktisch nie gestellt.

Für Deutschland gibt es einen Befund vom Institut für Arbeitsmarkt- und Berufsforschung. Nach IAB-Forschung wuchs die Beschäftigung zuletzt in Berufen mit hoher KI-Exposition mit 5,9 Prozent stärker als in Berufen mit geringer Exposition (2,5 Prozent), während sie in Berufen ohne Exposition um 1,7 Prozent zurückging.[8] Die Berufe, die am stärksten mit KI zu tun haben, wachsen also am schnellsten. Historisch, so das IAB, führte ein hohes Substituierbarkeitspotenzial ohnehin selten zu echten Jobverlusten, eher zu langsamerem Wachstum.[8]

Wenn man das zusammennimmt — und das ist jetzt meine Lesart, nicht die der Institute —, ergibt sich ein ziemlich einheitliches Bild: Verschiebung ja, Umbau ja, Ungleichheitsrisiko ernst. Massenarbeitslosigkeit findet in keiner dieser Rechnungen statt. Kein einziges der genannten Häuser prognostiziert sie.

## Wenn seriöse Ökonomen um Faktor zehn auseinanderliegen

Und jetzt der Teil, der dich davor bewahren soll, jemals wieder eine Zukunftszahl für bare Münze zu nehmen.

Daron Acemoglu, MIT-Ökonom und einer der meistzitierten Forscher zum Thema Technologie und Arbeit, hat im April 2024 ein Papier beim National Bureau of Economic Research vorgelegt: *The Simple Macroeconomics of AI*, NBER Working Paper 32487. Seine Rechnung: Der Zuwachs an totaler Faktorproduktivität durch KI werde über zehn Jahre höchstens etwa 0,66 Prozent betragen.[9] Nicht pro Jahr. Insgesamt. Sein Argument, stark verkürzt: Nur ein kleiner Teil aller Arbeitsaufgaben ist überhaupt sinnvoll von KI zu übernehmen, und bei diesem Teil sind die Kosteneinsparungen begrenzt. Der Rest ist Erzählung.

Im selben Zeitraum rechnete Goldman Sachs Research vor, generative KI könne das globale Bruttoinlandsprodukt um rund 7 Prozent heben.[10] McKinsey bezifferte das jährliche Potenzial auf 2,6 bis 4,4 Billionen US-Dollar.[11]

Das sind keine Nuancen. Das sind Welten. Zwischen „0,66 Prozent in zehn Jahren" und „7 Prozent globales BIP" liegt der Unterschied zwischen einer netten Verbesserung und einer industriellen Revolution. Beide Seiten sind seriös, beide rechnen mit Modellen, beide veröffentlichen ihre Annahmen.

Und genau das ist der Punkt: **Der Unterschied steckt nicht in den Daten, er steckt in den Annahmen.** Wie viel Prozent der Aufgaben sind automatisierbar? Wie stark sinken die Kosten? Wie schnell übernehmen Unternehmen die Werkzeuge tatsächlich? Wie viele neue Aufgaben entstehen, die es heute nicht gibt? Drehst du an diesen Stellschrauben, kommt jede beliebige Zahl heraus. Das ist kein Vorwurf an die Ökonomen — anders geht es nicht. Es ist ein Vorwurf an jeden, der eine dieser Zahlen ohne die Annahmen weitererzählt.

Merk dir diesen Satz, wir brauchen ihn im neunten Kapitel wieder: **Wer dir eine Zahl für 2035 nennt, verkauft dir eine Annahme.** Frag nach der Annahme. Wenn er sie nicht nennen kann, hat er die Zahl irgendwo abgeschrieben.

Ein Detail noch, das für die Bodenhaftung sorgt. Der AI Index der Stanford-Universität berichtet für 2024 eine organisationale KI-Adoption von rund 78 Prozent, nach 55 Prozent im Jahr zuvor.[12] Fast vier von fünf Organisationen setzen also irgendetwas mit KI ein. Wenn davon eine Produktivitätsexplosion ausginge, müsste man sie inzwischen in den Statistiken sehen. Man sieht sie nicht. Das spricht eher für Acemoglu — vorerst. Es kann auch schlicht heißen, dass es dauert. Bei der Elektrifizierung der Fabriken hat es Jahrzehnte gedauert, bis die Produktivität nachzog, weil man die Fabriken erst umbauen musste. Das ist meine Vermutung, kein Beleg.

## Was die Geschichte dazu sagt — und was meine Facharbeit dazu sagt

Wir waren im vierten Kapitel bei den Ludditen. Kurze Erinnerung, weil sie hier gebraucht wird: Die Weber, die zwischen 1811 und 1812 in Nottinghamshire und Yorkshire Strumpfwirkerstühle zerschlugen, waren keine Technikhasser. Sie waren Facharbeiter, deren Existenzgrundlage von ungelernten Arbeitskräften an neuen Maschinen unterboten wurde, in einer Zeit ohne Sozialversicherung und mit hohen Lebensmittelpreisen. Das britische Parlament stellte das Zerstören von Maschinen 1812 unter Todesstrafe; Lord Byron hielt am 27. Februar 1812 im Oberhaus eine Rede dagegen.[13]

Das ist die entscheidende Korrektur. Die Ludditen hatten nicht unrecht über ihr eigenes Leben. Sie hatten unrecht über die Textilindustrie insgesamt, die in den folgenden Jahrzehnten wuchs und mehr Menschen beschäftigte als je zuvor. Beide Sätze sind wahr, und die Spannung zwischen ihnen ist genau die Spannung, um die es in diesem Kapitel geht.

Näher an uns dran, und in Deutschland: 1980 diskutierte die Bundesrepublik unter dem Stichwort „Mikroelektronik — die dritte industrielle Revolution" ernsthaft die Gefahr einer technologisch verursachten Massenarbeitslosigkeit.[14] Das war keine Stammtischsorge, das war eine Debatte in seriösen Publikationen, mit Gutachten und Anhörungen. Man kann heute darüber schmunzeln, sollte es aber nicht. Die Sorge war rational begründet, sie hat sich nur in dieser Form nicht bewahrheitet — sonst würden wir heute nicht über Fachkräftemangel reden. Das ist meine Einordnung, keine Statistik.

Damit sind wir bei der These, die ich als Student in einer Facharbeit vertreten habe und die ich hier ausdrücklich als **meine These** kennzeichne, nicht als Befund: **Automatisierung nimmt nicht die Jobs, sie verschiebt die Tätigkeit.**

Was spricht dafür? Der ILO-Befund, dass die meisten exponierten Jobs transformiert statt ersetzt werden.[6] Der OECD-Befund, dass bisher wenig Jobverluste zu sehen sind.[5] Der IAB-Befund, dass exponierte Berufe in Deutschland schneller wachsen.[8] Die WEF-Erwartung eines Netto-Zuwachses.[4] Und ein historisches Muster, das seit den Ludditen ziemlich stabil ist.

Was spricht dagegen? Dass „bisher" kein Argument über morgen ist. Dass alle historischen Vergleiche voraussetzen, dass diese Technik im Kern wie frühere Techniken funktioniert, und das ist eine Annahme, keine Erkenntnis. Und dass die These, so wie ich sie mit Anfang zwanzig aufgeschrieben habe, einen blinden Fleck hat, den ich damals nicht sah und der mir heute am meisten zu schaffen macht.

## Der Durchschnitt tröstet niemanden

Der blinde Fleck ist der Durchschnitt.

„Die Beschäftigung bleibt insgesamt erhalten" ist ein wahrer Satz, der einem einzelnen Menschen nichts nützt. Wenn dein Job verschwindet und woanders zwei neue entstehen, für die du weder qualifiziert bist noch umziehen kannst, dann ist die volkswirtschaftliche Bilanz positiv und dein Leben trotzdem kaputt. Die Weber von Nottingham sind nicht dadurch satt geworden, dass die Textilindustrie vierzig Jahre später boomte. Die Tätigkeitsverschiebung, die ich in meiner Facharbeit gefeiert habe, ist für die betroffene Person keine Verschiebung. Sie ist ein Bruch.

Und es gibt einen Befund, der mich mehr beunruhigt als alle anderen in diesem Kapitel. Er stammt ausgerechnet wieder von Brynjolfsson, zusammen mit Bharat Chandar und Ruyu Chen, aus dem Stanford Digital Economy Lab, ausgewertet auf Basis von ADP-Lohndaten von über 25 Millionen Beschäftigten. Titel: *Canaries in the Coal Mine?* — Kanarienvögel im Bergwerk. Seit der Verbreitung generativer KI zeigt sich in den am stärksten KI-exponierten Berufen ein relativer Beschäftigungsrückgang von etwa 13 bis 16 Prozent bei Berufseinsteigerinnen und Berufseinsteigern zwischen 22 und 25 Jahren, während ältere Kohorten zwischen 35 und 49 Jahren zulegten. Der Rückgang konzentriert sich auf Anwendungen, die Tätigkeiten **automatisieren**, nicht auf solche, die sie unterstützen.[15]

Erinnerst du dich an den Befund aus dem Kundenservice? Dort war die KI die große Chance für die Unerfahrenen, weil sie deren Leistung anhob. Hier ist sie das Problem der Unerfahrenen, weil sie deren Einstiegsjobs überflüssig macht. Das ist kein Widerspruch, das ist dieselbe Medaille von beiden Seiten. Wenn ein Werkzeug die Leistung von Anfängern auf ein solides Niveau hebt, dann steigt der Wert des Anfängers für die Arbeit, die er tut — und gleichzeitig sinkt die Zahl der Anfänger, die man dafür braucht.

Wenn dieser Befund sich bestätigt, und ich betone: Es ist eine Studie, sie ist neu, sie misst relative Verschiebungen in einem einzelnen Land — dann trifft die KI genau die Menschen, die am wenigsten Puffer haben. Nicht mich, mit fünfzehn Jahren Berufserfahrung und einem Team. Sondern den, der gerade fertig geworden ist und den ersten Job sucht, in dem er das Handwerk lernen soll. Wer keine Einstiegsjobs mehr hat, hat in zehn Jahren keine Erfahrenen. Das ist meine Sorge, und ich habe keine gute Antwort darauf.

Was die Beschäftigten selbst denken, hat die OECD 2022 in sieben Ländern erhoben, im Finanzsektor und in der Industrie. Rund 20 Prozent waren sehr oder äußerst besorgt, in den nächsten zehn Jahren ihren Job zu verlieren. In Firmen, die KI bereits einsetzten, kannten 20 Prozent (Finanz) beziehungsweise 15 Prozent (Industrie) jemanden persönlich, der wegen KI seinen Job verloren hatte.[16] Das ist keine eingebildete Angst. Für einen von fünf Menschen in diesen Betrieben hat sie ein Gesicht.

Gleichzeitig zeigen dieselben OECD-Erhebungen eine deutliche Lohnprämie für KI-Kompetenzen, auch gegenüber vergleichbaren Beschäftigten mit anderen fortgeschrittenen Fähigkeiten.[16] Beides zusammen ergibt die unbequemste Formel dieses Kapitels: Die Technik entwertet nicht Menschen, sie entwertet **bestimmte Tätigkeiten** und wertet andere auf. Wer die Bewegung mitmacht, gewinnt. Wer sie nicht mitmachen kann, verliert. Und ob du sie mitmachen kannst, hängt von Alter, Beruf, Bildung, Geld und Zeit ab — also von lauter Dingen, die schon vorher ungleich verteilt waren.

## Die Prüffragen, angelegt

Im fünften Kapitel habe ich dir ein Werkzeug in die Hand gegeben. Legen wir es an.

**Ist die Sorge über die Technik oder über ihre Verteilung?** Bei der Job-Angst ist die Antwort ziemlich eindeutig: über die Verteilung. Keine der oben genannten Institutionen erwartet, dass die Arbeit ausgeht. Fast alle erwarten, dass sich verschiebt, wer welche Arbeit macht und was sie einbringt. Die Ludditen hatten kein Maschinenproblem, sie hatten ein Verteilungsproblem. Wer heute „die KI nimmt uns die Jobs" sagt, meint fast immer: „Ich fürchte, ich stehe auf der falschen Seite der Verschiebung." Das ist eine völlig andere Frage — und, das ist der Punkt, eine politisch beantwortbare. Technik kann man nicht verhandeln. Verteilung schon.

**Wer profitiert davon, dass ich das glaube?** Diese Frage schneidet in beide Richtungen, und das ist ihre Stärke. Von der Panik profitieren erst einmal die Anbieter: Ein Werkzeug, das angeblich ganze Berufe ersetzt, lässt sich teurer verkaufen als eines, das die Bearbeitung von Servicetickets um 15 Prozent beschleunigt. „Wir ersetzen euer Team" ist ein besserer Pitch als „Wir helfen euch ein bisschen". Ein Teil der Untergangsrhetorik über den Arbeitsmarkt ist schlicht Marketing mit umgekehrtem Vorzeichen. Von der Entwarnung profitieren aber auch Leute: Arbeitgeber, die keine Umschulung bezahlen wollen, und Politiker, die sich um die Verteilungsfrage drücken. Und, damit du es von mir hörst: Ich profitiere selbst. Ich verdiene mein Geld mit Automatisierung. Wenn du glaubst, dass Automatisierung Tätigkeiten verschiebt statt Jobs zu vernichten, ist das für mein Geschäft angenehmer. Rechne das ein, wenn du meine These liest. Ich habe versucht, sie mit Befunden zu prüfen statt mit Wunschdenken, und ich habe dir den METR-Befund und die Kanarienvögel nicht verschwiegen. Aber ich bin nicht neutral, und niemand ist es.

## Und heute?

Die Beweisaufnahme endet nicht mit einem Freispruch und nicht mit einem Schuldspruch. Sie endet mit einem Befund, der sich in einem Satz sagen lässt: Die Arbeit geht nicht aus, aber sie zieht um — und niemand garantiert dir, dass sie dorthin zieht, wo du stehst.

Für meine Kollegin ging der Umzug gut aus. Sie hatte Zeit, sie hatte ein Team, das sie mitgenommen hat, und sie hatte eine Aufgabe, die auf sie gewartet hat. Das war Glück und Organisation, nicht Naturgesetz. Wäre der Bot in einem Betrieb aufgetaucht, in dem niemand über das Danach nachgedacht hätte, hätte derselbe technische Vorgang ein anderes Ergebnis gehabt. Die Technik entscheidet nicht, wie die Geschichte ausgeht. Sie entscheidet nur, dass es eine Geschichte gibt.

Bleibt eine Voraussetzung, über die dieses Kapitel stillschweigend hinweggegangen ist. Alles, was ich dir hier gezeigt habe — Umschulung, Tätigkeitsverschiebung, mit der Bewegung mitgehen, die Lohnprämie für neue Fähigkeiten — setzt eine Sache voraus, die niemand prüft: dass wir überhaupt noch lernfähig sind, während wir uns von Maschinen helfen lassen.

Der Kollege aus dem ersten Kapitel hat genau danach gefragt. Ob er das Denken verlernt, wenn er das Ding jeden Tag benutzt. Wenn die Arbeit bleibt, sich aber verschiebt, hängt alles an dieser Frage. Es gibt Daten dazu. Sie sind nicht so beruhigend, wie ich es gern hätte.

---

## Quellen zu Kapitel 6

[1] Brynjolfsson, Erik; Li, Danielle; Raymond, Lindsey: *Generative AI at Work*. The Quarterly Journal of Economics 140(2), 2025, S. 889–942. — 5.172 Kundendienst-Mitarbeitende; ~15 % mehr gelöste Vorgänge/Std. (Arbeitspapier-Fassung 14 %); größte Gewinne bei wenig erfahrenen Kräften; höhere Kundenzufriedenheit und Mitarbeiterbindung. → QUELLEN.md Nr. 55.
[2] Peng, Sida; Kalliamvakou, Eirini; Cihon, Peter; Demirer, Mert: *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*. 2023, arXiv:2302.06590. — ~56 % schneller (71 vs. 160 Min.); Arbeitspapier, nicht peer-reviewt, Lab-Setting. Einschränkungen im Text benannt. → QUELLEN.md Nr. 56.
[3] METR: *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*. 2025, arXiv:2507.09089. — RCT mit 16 erfahrenen Entwickler:innen an eigenen Repositories; 19 % langsamer mit KI bei gegenteiliger Selbstwahrnehmung (~20 % schneller geschätzt). Update Februar 2026: spätere 2025er-Werkzeuge vermutlich stärker beschleunigend. → QUELLEN.md Nr. 64.
[4] World Economic Forum: *The Future of Jobs Report 2025*. 2025. — ~1.000 Unternehmen, >14 Mio. Beschäftigte, 22 Branchen, 55 Volkswirtschaften; bis 2030 erwartete 170 Mio. neue / 92 Mio. wegfallende / netto +78 Mio. Stellen; 85 % der Arbeitgeber planen Weiterbildungsinvestitionen. **Als Prognose/Selbstauskunft im Text gekennzeichnet.** → QUELLEN.md Nr. 57.
[5] OECD: *OECD Employment Outlook 2025*. OECD Publishing, 2025. — Bislang wenig Belege für KI-bedingte Jobverluste; zwei Drittel der KI-Nutzenden empfinden ihre Arbeit als weniger monoton/gefährlich; 27 % der OECD-Beschäftigung in Berufen mit höchstem Automatisierungsrisiko. → QUELLEN.md Nr. 59.
[6] Gmyrek, Pawel; Berg, Janine u. a. (ILO / NASK): *Generative AI and Jobs: A Refined Global Index of Occupational Exposure*. ILO Working Paper 140, veröffentlicht 20.05.2025. — ~1 von 4 Beschäftigten weltweit GenAI-exponiert; 34 % (Hocheinkommen) vs. 11 % (Niedrigeinkommen); höchste Expositionskategorie 3,3 % der weltweiten Beschäftigung, Frauen 4,7 % vs. Männer 2,4 %; Transformation statt Ersatz. **Schätzung/Index, im Text gekennzeichnet.** → QUELLEN.md Nr. 61.
[7] Cazzaniga, Mauro u. a. (IMF): *Gen-AI: Artificial Intelligence and the Future of Work*. IMF Staff Discussion Note, Januar 2024. — ~40 % der Jobs weltweit KI-exponiert; ~60 % in fortgeschrittenen Volkswirtschaften (davon etwa die Hälfte mit Abwärtsrisiko für Löhne/Arbeitsnachfrage); Schwellenländer ~40 %, Niedrigeinkommensländer ~26 %; ausdrückliche Ungleichheitswarnung. **Schätzung.** → QUELLEN.md Nr. 62.
[8] ▲ IAB — Institut für Arbeitsmarkt- und Berufsforschung: *KI und Arbeitsmarkt*. IAB-Forschungsbericht 2025 (Juli 2025). — Beschäftigungswachstum +5,9 % in Berufen mit hoher KI-Exposition vs. +2,5 % bei geringer und −1,7 % ohne Exposition; hohes Substituierbarkeitspotenzial historisch eher langsameres Wachstum als Jobverluste. → QUELLEN.md Nr. 58. **Einzelne Zahlen vor Drucklegung direkt am IAB-Volltext (fb2325.pdf) verifizieren.**
[9] Acemoglu, Daron: *The Simple Macroeconomics of AI*. NBER Working Paper 32487, April 2024. — Höchstens ~0,66 % Zuwachs der totalen Faktorproduktivität über zehn Jahre. **[Prognose]**, im Text als solche gekennzeichnet. → QUELLEN.md Nr. 110.
[10] Goldman Sachs Research (Briggs, Joseph; Kodnani, Devesh): *Generative AI Could Raise Global GDP by 7%*. 2023. — ~7 % globales BIP. **[Prognose]**. → QUELLEN.md Nr. 96.
[11] McKinsey: *The Economic Potential of Generative AI*. Juni 2023. — 2,6–4,4 Bio. USD jährliches Potenzial. **[Prognose]**. → QUELLEN.md Nr. 97.
[12] Stanford HAI: *AI Index Report*, Kapitel „Economy". — Organisationale KI-Adoption 2024 ~78 % (nach 55 % im Vorjahr). → QUELLEN.md Nr. 72. **Adoptionszahl vor Drucklegung am AI-Index-Kapitel bestätigen; die im Text angeschlossene Deutung (Elektrifizierungs-Verzögerung) ist als Vermutung des Autors gekennzeichnet.**
[13] Ludditen: Wikipedia *Luddite* / Nottinghamshire Heritage Gateway; Conniff, Richard: *What the Luddites Really Fought Against*, Smithsonian Magazine, März 2011; *Destruction of Stocking Frames Act 1812* (52 Geo. 3 c. 16), royal assent 20.03.1812; Byron-Rede im House of Lords, 27.02.1812. → QUELLEN.md Nr. 44, 45, 46. (Ausführlich in Kapitel 4.)
[14] ▲ bpb / *Aus Politik und Zeitgeschichte* 7/1980: *Mikroelektronik — die dritte industrielle Revolution*. — Zeitgenössische Debatte über technologisch verursachte Massenarbeitslosigkeit. → QUELLEN.md Nr. 30. **Belegstelle vor Drucklegung prüfen; die Bewertung des Ausgangs ist im Text ausdrücklich als Einordnung des Autors markiert, nicht als Statistik.**
[15] Brynjolfsson, Erik; Chandar, Bharat; Chen, Ruyu (Stanford Digital Economy Lab): *Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence*. 2025. — ADP-Lohndaten von >25 Mio. Beschäftigten; relativer Beschäftigungsrückgang ~13–16 % bei 22- bis 25-Jährigen in stark KI-exponierten Berufen, Zuwächse bei 35- bis 49-Jährigen; Effekt konzentriert auf automatisierende (nicht augmentierende) Anwendungen. → QUELLEN.md Nr. 63.
[16] OECD: *OECD Employment Outlook 2023 — Artificial Intelligence and the Labour Market* (Arbeitgeber- und Beschäftigten-Surveys 2022, >2.000 Arbeitgeber / >5.300 Beschäftigte, Finanz- und Industriesektor, 7 Länder). — ~20 % sehr/äußerst besorgt über Jobverlust in den nächsten 10 Jahren; 20 % (Finanz) bzw. 15 % (Industrie) kannten in KI-einsetzenden Firmen jemanden, der wegen KI den Job verlor; Lohnprämie für KI-Kompetenzen. → QUELLEN.md Nr. 60.
