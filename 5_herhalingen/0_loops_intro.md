# Loops <!--\label{ch:6}-->

In het vorige hoofdstuk hebben we geleerd hoe we onze code konden vertakken (**branching**) door beslissingen te nemen. Dit stelde ons in staat om verschillende stukken code uit te voeren, afhankelijk van de waarde van bepaalde variabelen of de invoer van de gebruiker.

Wat we nog niet konden was **terug naar een vorige plek in het algoritme gaan**. Soms willen we dat een heel stuk code 2 of meerdere keren moet uitgevoerd worden tot aan een bepaalde conditie wordt voldaan: *"Voer volgende code uit tot dat de gebruiker 666 invoert."* 

Herhalingen (**loops**) creëer je wanneer bepaalde code een aantal keer moet herhaald worden. Hoe vaak de herhaling moet duren is afhankelijk van de conditie die je hebt bepaald.  Elke keer dat de code binnen de loop wordt uitgevoerd, noemen we dit een **iteratie**. Dit betekent dat de loop bij elke iteratie zijn codeblok opnieuw doorloopt, totdat de gestelde conditie niet meer voldoet.

**Door herhalende code met loops te schrijven maken we onze code korter en bijgevolg ook minder foutgevoelig en beter onderhoudbaar.**




## Soorten loops

Er zijn verschillende categorieën loops:

* **Definite of counted loop**: een loop waarbij het aantal herhalingen vooraf bekend is. Bijvoorbeeld: alle getallen van 0 tot en met 100 tonen.
* **Indefinite of sentinel loop**: een loop waarvan op voorhand niet kan gezegd worden hoe vaak deze zal uitgevoerd worden. Invoer van de gebruiker of een interne test bepaalt wanneer de loop stopt. Bijvoorbeeld: "Voer getallen in, voer -1 in om te stoppen" of "Bereken de grootste gemene deler".
* **Oneindige loop**: een loop die nooit stopt. Soms gewenst (bv. de game loop) of, vaker, een bug.

<!-- \newpage -->


### Loops in C\#

Er zijn 3 standaard manieren om loops te maken in C#:

* **``while``**: zal 0 of meerdere keren uitgevoerd worden.
* **`` do while``**: zal minimaal 1 keer uitgevoerd worden.
* **``for``**: een alternatieve, iets compactere manier om loops te beschrijven wanneer je exact weet hoe vaak de loop zal moeten herhalen.

Daarnaast zullen we in hoofdstuk 9 een speciale loopvariant leren kennen wanneer we arrays en objecten bespreken:

* **``foreach``**: een leesbaardere manier van loopen, die vooral nuttig is wanneer je met objecten werkt.

De 3 categorieën loops die we net bespraken kunnen in principe met eender welk looptype in C# geschreven worden. Toch raad ik je aan om vanaf nu steeds wel doordacht na te denken welk looptype het best bij je probleem past. Samengevat kan je het volgende zeggen:

| Looptype          | Definite loop | Indefinite loop | Oneindige loop |
| ----------------- | :-----------------: | :-----------------: | :-----------------: |
| While en do while | x             | x               | x              |
| For               | x             |                 |                |
| Foreach           | x             |                 |                |

Deze tabel suggereert dat we met ``while`` en ``do while`` meer kunnen, wat ook zo is. Je zal echter gauw ontdekken dat je vaak terugvalt op code met een  ``for`` omdat:

1. Deze compatere code oplevert.
2. Veel problemen met een definite loop kunnen opgelost worden. 



