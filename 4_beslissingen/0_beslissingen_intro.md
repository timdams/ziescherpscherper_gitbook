# Beslissingen <!--\label{ch:5}-->

Nu we de elementaire zaken van C# en VS kennen is het tijd om onze programma's wat interessanter te maken. De programma's die we tot nu toe hebben ontwikkeld waren steevast lineair van opbouw.  Ze werden lijn per lijn uitgevoerd, van start tot einde, zonder de mogelijkheid om de **program flow** aan te passen. Het programma doorliep de lijnen code braaf na elkaar en wanneer deze aan het einde kwam sloot het zich af.

Onze programma's waren met andere woorden niet meer dan een eenvoudige lijst van opdrachten. Je kan het vergelijken met een lijst die je over hoe je een brood moet kopen:


```text
Neem geld uit spaarpot
Wandel naar de bakker om de hoek
Vraag om een brood
Krijg het brood
Betaal het geld aan de bakker
Keer huiswaarts
Smullen maar
```


Alhoewel dit algoritme redelijk duidelijk is en goed zal werken, zal de realiteit echter zelden zo rechtlijnig zijn. Van zodra 1 van de stappen faalt (bijvoorbeeld omdat de bakker toe is) zal ook de rest van het algoritme niet meer werken. 

Een beter algoritme zal afhankelijk van de omstandigheden (bakker gesloten, geen geld meer, enz.) andere stappen ondernemen. **Het programma zal beslissingen maken gebaseerd op keuzes** doorheen het programma:


```text
Neem geld uit spaarpot
Geld op? Stop dan hier, anders: ga verder
Wandel naar de bakker om de hoek
Bakker toe? Stop dan hier, anders: ga verder
Vraag om een brood
Krijg het brood
Betaal het geld aan de bakker
Als je honger hebt, sla dan volgende lijn over, anders: ga verder
Keer huiswaarts
Smullen maar
```
