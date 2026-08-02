# Kapitel 11 — Vertrauen ist eine Fähigkeit

Nach einem Workshop, im Flur, halb schon im Mantel, fragte mich eine Kollegin: „Mal ehrlich, Emre. Vertraust du dem Zeug?"

Ich habe damals irgendetwas Halbes geantwortet. Die ehrliche Antwort wäre eine Gegenfrage gewesen, und die klingt erst einmal pedantisch: Wofür?

Denn so, wie sie gefragt hat, lässt sich die Frage nicht beantworten. Vertraust du deinem Auto? Vermutlich ja — für den Weg zur Arbeit, bei Tempo fünfzig, mit gültiger Plakette und der Inspektion vom Frühjahr. Mit denselben Reifen bei Glätte über die Landstraße zu jagen, würdest du trotzdem sein lassen. Das ist kein Widerspruch und keine Unentschlossenheit. Das ist ein differenziertes Urteil, und du fällst es jeden Tag, ohne darüber nachzudenken, weil du gelernt hast, es zu fällen. Autofahren ist eine Fähigkeit. Einschätzen, was das Auto kann, ist ein Teil davon.

Genau so meine ich das mit dem Vertrauen in KI. Es ist keine Stimmung, die man hat oder nicht hat. Es ist auch nicht die Bereitschaft, sich irgendwem hinzugeben. Es ist eine Kompetenz, die aus lauter unspektakulären Teilurteilen besteht: dieses Werkzeug, diese Aufgabe, dieser Rahmen, dieses Risiko. Man kann sie lernen. Man kann sie üben. Und wie bei der Quellenkritik, die dir irgendwann jemand beigebracht hat — dass eine Pressemitteilung nicht die Studie ist, dass ein Wikipedia-Artikel ein Einstieg ist und kein Beleg —, wird sie mit der Zeit zur zweiten Natur.

Im ersten Kapitel habe ich geschrieben: Angst ist ein Gefühl über etwas, das man nicht kennt. Skepsis ist ein Urteil über etwas, das man kennt. Der Satz hat einen dritten Teil, den ich damals unterschlagen habe. Vertrauen ist ein Urteil, das man begründen kann — und das man widerrufen kann, wenn sich die Begründung ändert. Dieses Kapitel ist der Versuch, dir das beizubringen, was ich mir in ein paar Jahren Automatisierungsprojekten zusammengesammelt habe. Es ist kein Programm mit Punkten zum Abhaken. Es sind Fragen, die ich mir mittlerweile reflexhaft stelle.

## Die einzige Frage, die wirklich zählt

Wenn mich jemand aus einem Fachbereich fragt, ob KI für seinen Prozess taugt, versuche ich, die Frage sofort umzubauen. Nicht „ist KI gut?", sondern: Was kostet hier ein Fehler, und wann merken wir ihn?

Das klingt nüchtern bis langweilig. Es ist aber der eine Gedanke, der in meinem Beruf am meisten Ärger verhindert hat, und er ist erstaunlich gut auf den Privatgebrauch übertragbar.

Nimm die eine Seite: Du lässt dir eine E-Mail entwerfen, die du nachher sowieso liest. Du sammelst Ideen für eine Präsentation und wirfst neun von zehn weg. Du lässt einen Absatz umformulieren, weil er dir zu steif ist. Du lässt dir ein kleines Werkzeug programmieren und startest es. In all diesen Fällen ist der Fehler billig — er kostet dich Sekunden — und er ist sofort sichtbar, weil du das Ergebnis unmittelbar beurteilen kannst. Bei Code sogar besonders brutal: Er läuft, oder er läuft nicht. Ich baue mir mittlerweile mit Claude Code eigene kleine Helfer für Dinge, die mich im Alltag nerven, statt für jede Kleinigkeit ein Abo abzuschließen. Das funktioniert nicht deshalb gut, weil das Modell keine Fehler macht. Es macht laufend welche. Es funktioniert, weil jeder Fehler binnen Sekunden auffliegt und mich nichts kostet außer einem weiteren Versuch.

Jetzt die andere Seite. Eine Zahl in einem Reporting, die ins Management geht. Eine Vertragsklausel. Eine Aussage über Medikamente. Eine Vorauswahl von Bewerbungen. Hier ist der Fehler teuer, und, das ist der eigentlich gefährliche Teil, er ist unsichtbar. Eine falsche Zahl sieht genauso aus wie eine richtige. Eine erfundene Rechtsprechung liest sich exakt wie eine echte. Ein Modell, das systematisch die falschen Leute aussortiert, produziert keine Fehlermeldung, sondern eine Kandidatenliste, die vollkommen plausibel wirkt. Amazon hat ein experimentelles Rekrutierungswerkzeug wieder eingestellt, weil es Frauen benachteiligte; die Ursache war banal, es hatte auf zehn Jahren überwiegend männlicher Bewerbungen gelernt und wertete unter anderem Lebensläufe ab, in denen „women's" vorkam oder ein reines Frauen-College stand.[1] Niemand hatte diesen Fehler programmiert. Er war auch nirgends sichtbar. Er steckte in den Daten und sah von außen aus wie ein Urteil.

Die Falle ist also nicht, dass Sprachmodelle Unsinn produzieren. Die Falle ist, dass der Unsinn genauso flüssig, selbstbewusst und ordentlich formatiert daherkommt wie das Richtige. Beim Taschenrechner konntest du dich darauf verlassen, dass die Rechnung stimmt, wenn du sie richtig eingegeben hast. Hier nicht. Was du bekommst, ist eine sehr gute Nachahmung einer richtigen Antwort, und ob sie eine ist, steht ihr nicht ins Gesicht geschrieben.

Nun kannst du einwenden, dass „teuer" doch reicht als Kriterium. Tut es nicht, und das ist der Punkt, den ich meinen Leuten am häufigsten erkläre. Eine Herzoperation ist teuer, wenn sie schiefgeht — aber sie geht nicht unbemerkt schief. Der Kombinationsfall ist der gefährliche: hohe Kosten *und* späte oder gar keine Sichtbarkeit. Dort gehört entweder eine Prüfinstanz davor, oder das Werkzeug hat dort nichts verloren.

Bemerkenswerterweise sind die europäischen Gesetzgeber bei einer sehr ähnlichen Sortierung gelandet. Der EU AI Act stuft nach Risiko: Ein Teil der Anwendungen ist schlicht verboten, darunter Social Scoring durch Behörden, das ungezielte Absammeln von Gesichtsbildern und Emotionserkennung am Arbeitsplatz und in der Bildung; ein weiterer Teil gilt als Hochrisiko und bekommt strenge Auflagen; der große Rest bleibt weitgehend frei.[2] Man kann über einzelne Einordnungen streiten, und das wird auch getan. Aber die Grundlogik ist genau die, die ich dir hier vorschlage: Nicht die Technik wird bewertet, sondern der Einsatz.

Woran erkennst du im Alltag, in welchem Feld du bist? Ich benutze zwei Fragen. Erstens: Woran würde ich merken, dass das falsch ist? Fällt dir darauf keine Antwort ein, hast du kein Werkzeugproblem, sondern ein Prüfproblem, und das musst du zuerst lösen. Zweitens: Was passiert, wenn es ausfällt oder wenn ich es abschalten muss? In Projekten frage ich das immer, bevor irgendjemand über Technologie redet. Wenn es keine Rückfallebene gibt, ist der Prozess zu wichtig für ein Experiment.

## Prüfen, ohne paranoid zu werden

Dass Sprachmodelle Dinge erfinden, ist keine Kinderkrankheit, die man wegpatcht. Es ist eine dokumentierte Grenze des Ansatzes, und zu den Kritikern, die früh darauf hingewiesen haben, dass reines Vergrößern der Modelle dieses Problem nicht löst, gehört Gary Marcus.[3] Man muss seine weiterreichenden Thesen nicht teilen, um bei der Beobachtung mitzugehen: Ein System, das gelernt hat, plausible Fortsetzungen zu erzeugen, erzeugt auch dann plausible Fortsetzungen, wenn es nichts weiß.

Daraus folgt eine Regel, die ich ohne Ausnahme anwende und dir ohne Ausnahme empfehle: Bei Fakten, Zahlen, Namen, Jahreszahlen und Zitaten gehst du zur Quelle. Nicht „klingt richtig". Nicht „hat drei Quellen genannt". Du öffnest sie. Es ist keine Seltenheit, dass eine genannte Quelle existiert, aber etwas anderes sagt, oder dass sie gar nicht existiert und trotzdem eine tadellose Fundstelle mit Band und Seitenzahl vorweist. Ich habe für dieses Buch jede Zahl, die du in den Kapiteln findest, gegen die Originalquelle gehalten, und ich sage dir das nicht, um mir auf die Schulter zu klopfen, sondern weil es die Arbeit ist, die der Text im Fließtext unsichtbar macht.

Und jetzt der Teil, den die Produktivitätsversprechen gern unterschlagen: Prüfen kostet. Manchmal kostet es fast nichts — Tests laufen lassen, eine Übersetzung in einer Sprache lesen, die du kannst, eine Zusammenfassung gegen ein Dokument halten, das vor dir liegt. Manchmal kostet es fast so viel wie die Arbeit selbst, und dann ist der Gewinn weg. Ein randomisiertes Experiment von METR ist dafür der beste Beleg, den ich kenne: Sechzehn erfahrene Open-Source-Entwickler arbeiteten mit KI-Werkzeugen an ihren eigenen, großen Repositories — und brauchten neunzehn Prozent *länger*, obwohl sie selbst glaubten, rund zwanzig Prozent schneller gewesen zu sein.[4] Kleine Stichprobe, ein Setting mit sehr vertrauten Codebasen, und METR hat später ergänzt, dass spätere Werkzeuggenerationen vermutlich stärker beschleunigen. Trotzdem: Die Selbsteinschätzung lag um fast vierzig Prozentpunkte daneben. Das ist die eigentliche Nachricht. Du bist kein verlässlicher Zeuge deiner eigenen Produktivität.

Meine persönliche Praxis, und das ist ausdrücklich Erfahrung und keine Studienlage: Ich lasse mir bevorzugt Dinge erklären, deren Ergebnis ich selbst beurteilen kann. Das klingt nach einer Einschränkung, ist aber der Trick, mit dem man Kompetenz aufbaut statt sie abzugeben. Wer sich nur das erklären lässt, was er nicht beurteilen kann, sammelt Behauptungen. Wer sich das erklären lässt, was knapp über seinem Niveau liegt, sammelt Verständnis — weil er die Erklärung anzweifeln, nachfragen und gegen das prüfen kann, was er schon weiß. So bin ich in Themen hineingekommen, in denen ich vorher nichts zu suchen hatte. Nicht, indem ich dem Modell geglaubt habe, sondern indem ich es so lange gelöchert habe, bis ich die Antwort selbst hätte geben können.

Zwei Handgriffe, die dabei mehr bringen als alles andere: Lass dir die Gegenposition geben, ausdrücklich und in derselben Ausführlichkeit. Und frag nach, woher etwas kommt, statt es zu übernehmen. Ein Modell, das eine Behauptung nicht auf eine überprüfbare Fundstelle zurückführen kann, hat dir gerade gesagt, dass du selbst nachschauen musst.

## Erst denken, dann fragen

Im siebten Kapitel habe ich dir Zahlen gezeigt, die mir selbst nicht gefallen. Der Befund, an dem ich am meisten kaue, stammt aus einer Befragung von 319 Berufstätigen zu 936 realen Anwendungsfällen: Wer der KI mehr vertraut, denkt weniger kritisch mit; wer sich selbst mehr zutraut, denkt mehr mit.[5] Dazu die EEG-Studie aus dem MIT Media Lab, die beim Aufsatzschreiben die schwächste neuronale Vernetzung bei den Modellnutzern maß und dafür den Begriff „cognitive debt" prägte — kleine Stichprobe, Preprint, methodisch angegriffen, also nichts, worauf ich ein Weltbild baue.[6] Aber in dieselbe Richtung zeigen beide.

Die praktische Konsequenz daraus ist unspektakulär und trotzdem schwer: erst selbst denken, dann die Maschine fragen. Nicht umgekehrt.

Der Grund ist nicht Disziplin um der Disziplin willen. Wenn du zuerst fragst, wird die erste Antwort zu deinem Anker, und alles, was du danach denkst, ist eine Bearbeitung dieser Antwort. Wenn du dir vorher sechzig Sekunden nimmst und eine eigene, auch schlechte Position formulierst, hast du etwas, wogegen du das Ergebnis halten kannst. Der Unterschied zwischen diesen beiden Reihenfolgen ist größer als der Unterschied zwischen zwei Modellen.

Und dann gibt es die Dinge, die du wirklich lernen willst. Dafür der Rückgriff auf Kapitel fünf: Die Meta-Analysen zum Taschenrechner fanden über die Klassenstufen hinweg überwiegend neutrale bis positive Effekte auf die Rechenleistung — mit einer Ausnahme in der vierten Klasse, also genau dort, wo die Grundfertigkeit selbst noch aufgebaut wurde.[7] Übersetzt: Das Werkzeug schadet nicht, wenn die Fähigkeit steht. Es kann schaden, wenn es sie ersetzt, bevor sie steht. Wer eine Sprache lernt, sollte den Übersetzer nicht am Anfang benutzen, sondern am Ende. Wer programmieren lernen will, sollte die ersten hundert Fehler selber suchen.

Ich mache mir da nichts vor. Es gibt Handgriffe in meinem Beruf, die ich nicht mehr von Hand mache und auch nicht mehr von Hand machen will. Das ist ein bewusster Tausch, und ich habe im ersten Kapitel geschrieben, dass wir bei jeder dieser Wellen etwas verlieren. Der Unterschied, auf den es ankommt, ist der zwischen einer Fähigkeit, die du bewusst abgibst, und einer, die dir wegrutscht, ohne dass du es merkst. Meinen Test dafür verrate ich dir: Kannst du das Ergebnis verteidigen, wenn dich jemand im Meeting danach fragt? Wenn nein, hast du kein Ergebnis. Du hast einen Text.

## Wer verbreitet das eigentlich?

Im achten Kapitel steht der Befund, der die ganze Deepfake-Debatte vom Kopf auf die Füße stellt: In den Wahlkämpfen der Jahre 2024 und 2025 wurden „cheap fakes" — also einfache Manipulationen ohne KI, aus dem Zusammenhang gerissene alte Aufnahmen, irreführende Schnitte, falsche Bildunterschriften — deutlich häufiger eingesetzt als aufwendige KI-Generate.[8] Dokumentierte KI-Fälle gibt es sehr wohl: die gefälschten Biden-Robocalls, die in der Vorwahl in New Hampshire bis zu rund 25.000 Wähler erreichten; ein gefälschtes Audio eines Kandidaten zwei Tage vor der Wahl in der Slowakei; die 2024 annullierte Präsidentschaftswahl in Rumänien. Die kausale Wirkung auf Ergebnisse ist in den meisten Fällen nicht quantifiziert.

Für dich heißt das: Auf Bildartefakte zu starren ist die schlechtere Investition. Sechs Finger und komische Ohren waren gestern, und die aufwendige Fälschung ist ohnehin die Ausnahme. Was sich lohnt, ist die Kontextprüfung, und die kostet dich zwei Minuten. Wer verbreitet das? Wo taucht es zum ersten Mal auf, und wie alt ist die früheste Fundstelle? Gibt es das Original, und zeigt es dasselbe? Berichtet außer diesem einen Kanal noch irgendjemand darüber, der etwas zu verlieren hat?

Auf Erkennungswerkzeuge würde ich mich dabei nicht verlassen. Der internationale KI-Sicherheitsbericht hält fest, dass technische Schutzmaßnahmen von Wasserzeichen bis zur Detektion von versierten Angreifern oft umgangen werden und ihre reale Wirksamkeit unsicher ist.[9] Die Filter kommen — Herkunftsnachweise, Kennzeichnungspflichten, und der EU AI Act bringt seine Transparenzregeln für KI-generierte Inhalte mit sich.[2] Aber wir sind mitten in dem Zustand, den ich im ersten Kapitel den Erasmus-Moment genannt habe: Die Register sind noch nicht geschrieben.

Das zuverlässigste Warnsignal ist übrigens kein technisches. Es ist das Gefühl, sofort teilen zu müssen. Inhalte, die genau die Wut auslösen, die dich zum Weiterleiten bringt, sind nicht deshalb falsch — aber sie sind so gebaut, dass sie an deiner Prüfung vorbeikommen. Die Pause ist das Werkzeug.

## Was ich jungen Leuten mitgebe

Meine Frau und ich sind ehrenamtlich im Jugendbereich engagiert, und ich mag die Rolle als Mentor sehr, wahrscheinlich weil ich in meiner eigenen Jugend keinen hatte und heute weiß, wie viel mir das erspart hätte. Ich bin kein Pädagoge, und was jetzt kommt, ist ausdrücklich kein Fachurteil. Es ist das, was ich sage, wenn mich ein Sechzehnjähriger fragt.

Erstens: Das Ding ist weder dein Freund noch dein Feind. Es ist ein Produkt, hinter dem ein Geschäftsmodell steht, und es ist darauf trainiert, dir zu gefallen. Das ist keine Verschwörung, das ist Produktentwicklung. Aber es heißt, dass Zustimmung von dort keine Bestätigung ist.

Zweitens: Benutz es nicht für das, was du gerade lernen sollst. Nicht nie. Später. Der Unterschied zwischen „ich habe die Hausaufgabe abgegeben" und „ich kann das jetzt" fällt dir in dem Moment nicht auf, in dem du ihn machst, und in der Klausur ist es zu spät.

Drittens, und das ist mir am wichtigsten: Was du eintippst, ist aus deiner Hand. Der Europäische Datenschutzausschuss hat 2024 festgehalten, dass ein KI-Modell nur dann als anonym gelten kann, wenn es sehr unwahrscheinlich ist, Personen daraus zu identifizieren oder personenbezogene Daten per Anfrage wieder herauszuholen — was im Einzelfall zu prüfen ist und keineswegs pauschal gilt.[10] Also: keine Namen von Freunden, keine Fotos von anderen, keine Sachen, die du in fünf Jahren nicht mehr im Netz haben willst. Zur Frage des Alters gibt es institutionelle Positionen; die UNESCO empfiehlt für die eigenständige Nutzung solcher Plattformen ein Mindestalter von dreizehn Jahren, während die DSGVO ihre Schwelle bei sechzehn ansetzt.[11] Ich zitiere das, statt eine eigene Zahl zu erfinden.

Und dann sage ich noch etwas, das nichts mit Technik zu tun hat. Jeder ist seines Glückes Schmied. Das Werkzeug entscheidet nicht, wo du landest. Es beschleunigt nur den, der schon losgelaufen ist.

## Wann Misstrauen richtig ist

Misstrauen ist nicht das Gegenteil von Vertrauen. Beide sind Urteile, und beide sind Teil derselben Fähigkeit. Das Gegenteil von beidem ist Gleichgültigkeit — einfach zu benutzen, was da ist, und nicht wissen zu wollen, wie es funktioniert.

Es gibt vier Situationen, in denen mein Misstrauen sofort anspringt, und alle vier kommen aus dem Beruf.

Wenn nicht klar ist, was mit den Daten passiert. Das ist keine theoretische Sorge: Die italienische Datenschutzbehörde verhängte im Dezember 2024 ein Bußgeld von 15 Millionen Euro gegen OpenAI, unter anderem wegen fehlender Rechtsgrundlage für die Verarbeitung personenbezogener Daten zum Training und wegen Verstößen gegen Transparenzpflichten; ein italienisches Gericht hob die Buße 2026 auf, aber aus Zuständigkeitsgründen, nicht weil die inhaltlichen Vorwürfe entkräftet worden wären.[12] Wenn ein Anbieter dir nicht in zwei Sätzen sagen kann, ob deine Eingaben zum Training verwendet werden, hast du deine Antwort.

Wenn niemand haftet. Frag ruhig direkt, wer geradesteht, wenn das Ergebnis Schaden anrichtet. Wenn die Antwort ist, dass das System ja nur unterstützt und die Entscheidung beim Menschen liegt, dann prüf, ob dieser Mensch überhaupt in der Lage ist, die Entscheidung zu prüfen — oder ob er nur der ist, der klickt.

Wenn du das Ergebnis nicht prüfen kannst. Dazu habe ich oben alles gesagt.

Und wenn es keinen Ausschalter gibt. Kein Rückfall auf den alten Prozess, keine Möglichkeit, das Ding für zwei Wochen anzuhalten und trotzdem weiterzuarbeiten. Das ist das Kriterium, das in Projekten am häufigsten vergessen wird, und das teuerste.

Was Misstrauen nicht heißt: Alles Schlimme, das behauptet wird, stimmt. Bei der Apple Card kursierte 2019 der Vorwurf, Frauen bekämen systematisch niedrigere Kreditrahmen; die New Yorker Finanzaufsicht prüfte rund 400.000 Anträge und fand keinen Nachweis unrechtmäßiger Diskriminierung, das Geschlecht war kein Faktor.[13] Und beim berühmtesten Bias-Fall überhaupt, dem Rückfallprognose-Tool COMPAS, zeigte ProPublica 2016 zwar deutlich unterschiedliche Falsch-Positiv-Raten zwischen schwarzen und weißen Angeklagten[14] — aber die Mathematik dahinter ist unbarmherziger, als beide Streitparteien wahrhaben wollten: Bei ungleichen Grundraten lassen sich Kalibrierung und gleiche Fehlerraten nicht gleichzeitig erfüllen.[15] Fairness ist hier kein Programmierfehler, den man behebt, sondern ein Zielkonflikt, den jemand entscheiden muss. Wenn dir ein Anbieter sagt, sein Modell sei „fair", ist die richtige Rückfrage: nach welcher Definition, und wer hat das ausgesucht?

Aus alldem ist mir im Lauf der Jahre ein Satz geblieben, den ich im achten Kapitel schon einmal aufgeschrieben habe und der für mich das Kapitel zusammenhält. Die entscheidende Frage ist selten „Kann die Technik das?". Die entscheidende Frage ist: Wer haftet, wer prüft, wer kann es abschalten?

## Kurz für Organisationen

Ein Absatz für alle, die so etwas nicht nur benutzen, sondern einführen.

Im vierten Kapitel steht, was ich in Automatisierungsprojekten gelernt habe: Was von außen wie Technikangst aussieht, ist fast immer eine Beteiligungs- und Verteilungsfrage. Die Leute fürchten nicht den Bot. Sie fürchten, dass mit dem Bot über ihren Kopf hinweg entschieden wird. Wenn du sie erst einbeziehst, wenn die Lösung fertig ist, bekommst du Widerstand — und der ist dann berechtigt. Wenn du den Fachbereich die Ausnahmeregeln definieren lässt, bevor irgendwer eine Zeile baut, bekommst du Mitarbeit und nebenbei die besseren Anforderungen, weil dort das Wissen sitzt.

Dazu drei Dinge, die in meinen Projekten den Unterschied gemacht haben. Benenne namentlich, wer prüft, und gib dieser Person die Zeit dafür. Schreib auf, was das System nicht darf, nicht nur, was es soll. Und sag ehrlich, was mit der eingesparten Zeit passiert, bevor jemand danach fragt. Der letzte Punkt kostet am meisten Mut und spart am meisten Ärger.

Und eine Selbstverständlichkeit, die keine ist: Nicht jeder Prozess braucht KI. Vieles, was heute als KI-Projekt verkauft wird, ist ein Regelwerk mit vierzehn Fällen, und dann bau ein Regelwerk. Es ist billiger, prüfbarer und es halluziniert nicht.

## Was das alles nicht kann

Wenn du bis hierher gekommen bist, hast du einen brauchbaren Werkzeugkasten. Du weißt, wie du eine Aufgabe einsortierst, wie du prüfst, ohne dich zu ruinieren, in welcher Reihenfolge du denkst und wann du besser nein sagst. Das ist keine Kleinigkeit. Es ist genau das, was ich mir von jedem wünsche, der in meinen Workshops sitzt.

Es hat nur eine Grenze, und ich will nicht so tun, als hätte es sie nicht.

All das schützt dich als Einzelnen. Es schützt dich nicht davor, dass eine Handvoll Unternehmen die Infrastruktur besitzt, auf der das alles läuft. Es schützt dich nicht davor, dass die Gewinne aus dieser Umwälzung sich dort sammeln, wo ohnehin schon Kapital liegt. Es schützt dich nicht davor, dass irgendwo eine Behörde oder ein Arbeitgeber eine Entscheidung über dich trifft, bei der du gar nicht gefragt wirst, ob du das Ergebnis prüfen kannst.

Individuelle Kompetenz hat eine Decke, und wir stoßen mit dem Kopf dagegen. Deshalb kommt jetzt das letzte Kapitel, und darin sage ich dir, wovor ich tatsächlich Angst habe. Es ist nicht die Maschine. Das habe ich schon zweimal angedeutet, und ich löse es jetzt ein.

---

## Quellen zu Kapitel 11

[1] Jeffrey Dastin (Reuters): *Amazon scraps secret AI recruiting tool that showed bias against women*, Oktober 2018. — Training auf zehn Jahren überwiegend männlicher Bewerbungen; Abwertung von „women's" und reinen Frauen-Colleges; Projekt eingestellt. → QUELLEN.md Nr. 78.

[2] Verordnung (EU) 2024/1689 (EU AI Act); Implementation Timeline des AI Act Service Desk der Europäischen Kommission. — Risikobasierter Ansatz mit vier Stufen; verbotene Praktiken nach Art. 5 (u. a. Social Scoring durch Behörden, ungezieltes Scraping von Gesichtsbildern, Emotionserkennung am Arbeitsplatz und in der Bildung) anwendbar seit 2.2.2025; Hochrisiko-Systeme nach Anhang III und Transparenzpflichten nach Art. 50 anwendbar seit 2.8.2026. → QUELLEN.md Nr. 84.

[3] Gary Marcus: *Deep Learning Is Hitting a Wall*, Nautilus 2022, fortgeführt im Substack „Marcus on AI" (2024). — Position: Halluzinationen und Reasoning-Schwächen lassen sich durch reines Hochskalieren nicht lösen. Im Text als Position gekennzeichnet, nicht als Konsens; die *Existenz* der Grenze (Halluzination) ist in der Recherchelage unstrittig, quantitative Fehlerraten werden im Text bewusst nicht genannt. → QUELLEN.md Nr. 103.

[4] METR: *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*, 2025, arXiv:2507.09089; Update Februar 2026. — 16 erfahrene Entwickler:innen, RCT, 19 % langsamer bei gegenteiliger Selbsteinschätzung (~20 % schneller); Einschränkungen und das spätere METR-Update sind im Text genannt. → QUELLEN.md Nr. 64.

[5] Hao-Ping Lee et al. (Microsoft Research / Carnegie Mellon): *The Impact of Generative AI on Critical Thinking*, CHI 2025, DOI 10.1145/3706598.3713778. — 319 Berufstätige, 936 reale Anwendungsfälle; höheres Vertrauen in die KI korreliert mit weniger kritischem Denken, höheres Selbstvertrauen mit mehr. → QUELLEN.md Nr. 67.

[6] Nataliya Kosmyna et al. (MIT Media Lab): *Your Brain on ChatGPT: Accumulation of Cognitive Debt…*, 2025, arXiv:2506.08872. — EEG-Studie, n=54; schwächste neuronale Konnektivität bei LLM-Nutzung; Begriff „cognitive debt". Preprint, kleine Stichprobe, methodische Kritik in einem Folge-Kommentar — im Text ausdrücklich vermerkt. → QUELLEN.md Nr. 66.

[7] Ray Hembree & Donald J. Dessart: *Effects of Hand-Held Calculators in Precollege Mathematics Education: A Meta-Analysis*, Journal for Research in Mathematics Education 17(2), 1986, S. 83–99. — Überwiegend neutrale bis positive Effekte über die Klassenstufen hinweg, mit Ausnahme der vierten Klasse. → QUELLEN.md Nr. 28.

[8] Zusammenfassende Recherche zu KI-Desinformation in den Wahlen 2024–2025 (State of Surveillance / Recorded Future u. a.). — „Cheap fakes" deutlich häufiger als KI-Generate; dokumentierte Einzelfälle: KI-generierte Biden-Robocalls mit bis zu ca. 25.000 erreichten Wählern in New Hampshire, gefälschtes Kandidaten-Audio in der Slowakei, Annullierung der rumänischen Präsidentschaftswahl 2024; kausale Wirkung meist nicht quantifiziert. → QUELLEN.md Nr. 75. ▲ **Einzelzahlen vor Drucklegung an Primärberichten prüfen.**

[9] Yoshua Bengio et al.: *International AI Safety Report 2025* sowie *Second Key Update: Technical Safeguards and Risk Management*, arXiv:2511.19863. — Wasserzeichen und Detektion KI-generierter Inhalte werden behandelt; versierte Angreifer umgehen aktuelle Schutzmaßnahmen oft, reale Wirksamkeit vieler Safeguards unsicher. → QUELLEN.md Nr. 73 und Nr. 74.

[10] European Data Protection Board: *Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models*, 17.12.2024. — Anonymität eines Modells ist im Einzelfall zu prüfen; es muss „sehr unwahrscheinlich" sein, Personen zu identifizieren oder personenbezogene Daten per Anfrage zu extrahieren. → QUELLEN.md Nr. 85.

[11] UNESCO: *Guidance for Generative AI in Education and Research*, 2023. — Empfohlenes Mindestalter 13 für die eigenständige Nutzung generativer KI-Plattformen; Hinweis auf die DSGVO-Schwelle von 16 Jahren. Im Text als institutionelle Position gekennzeichnet, nicht als eigenes pädagogisches Urteil. → QUELLEN.md Nr. 68.

[12] Garante per la protezione dei dati personali; Berichterstattung Euronews/Reuters. — Bußgeld von 15 Mio. € gegen OpenAI am 20.12.2024 (u. a. fehlende Rechtsgrundlage für Trainingsdatenverarbeitung, Transparenzverstöße); Annullierung durch ein italienisches Gericht 2026 aus Zuständigkeitsgründen, nicht wegen Entkräftung der inhaltlichen DSGVO-Vorwürfe. → QUELLEN.md Nr. 83. ▲ **[PRÜFEN]** genaues Urteilsdatum/Instanz 2026.

[13] New York State Department of Financial Services: *Report on the Apple Card Investigation*, März 2021. — Rund 400.000 New Yorker Anträge geprüft; kein Nachweis unrechtmäßiger Diskriminierung, Geschlecht kein Faktor. → QUELLEN.md Nr. 81.

[14] Julia Angwin, Jeff Larson, Surya Mattu, Lauren Kirchner (ProPublica): *Machine Bias*, 2016. — COMPAS/Northpointe, Broward County; unter den nicht erneut Straffälligen 45 % Falsch-Positiv-Rate bei schwarzen gegenüber 24 % bei weißen Angeklagten. → QUELLEN.md Nr. 77.

[15] Alexandra Chouldechova: *Fair prediction with disparate impact*, 2017; Jon Kleinberg, Sendhil Mullainathan, Manish Raghavan: *Inherent Trade-Offs in the Fair Determination of Risk Scores*, 2016, arXiv:1703.00056. — „Unmöglichkeitstheorem": Bei ungleichen Basisraten sind Kalibrierung und Fehlerratenbalance nicht gleichzeitig erfüllbar. → QUELLEN.md Nr. 80.
