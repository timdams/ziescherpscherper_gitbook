## Oefeningen

{% hint style='tip' %}
Vanaf dit punt zullen de meeste oefeningen iets "vragen" aan de gebruiker. Hiermee wordt bedoeld dat je de gebruikersinput via ``ReadLine`` moet inlezen en indien nodig moet converteren naar het gewenste type.
{% endhint %}

### Vierkant
Schrijf een programma om de omtrek en de oppervlakte van een vierkant te bepalen. De zijde wordt ingelezen. Zorg ervoor dat de uitvoer er als volgt uitziet:


```text
zijde: … 
omtrek: … 
oppervlakte: …
```

### Euro naar dollar*

Ontwerp een toepassing waarmee je een bedrag (als kommagetal) in Euro aan de gebruiker vraagt. Je programma zal dit bedrag omzetten naar dollar. Je hoeft niet af te ronden. Het resultaat op het scherm wordt als volgt weergegeven: ``[x] EUR is gelijk aan [y] USD``. 


### BMI berekenaar*
Maak een programma dat aan de gebruiker z'n lengte en gewicht vraagt en vervolgens de berekende BMI (Body Mass Index) toont.
Gebruik ``Math.Round`` om de uitkomst tot maximum 2 cijfers na de komma te tonen.

Reken na met je rekenmachine of je uitkomst wel degelijk klopt!

### Het Orakeltje van Delphi
Gebruik een random generator om een orakel (een duur woord voor waarzegger) te maken, namelijk de kleine broer of zus van het "Orakel van Delphi". Het programma zal aan de gebruiker vertellen hoe lang deze nog zal leven. Bijvoorbeeld: "Je zal nog 15 jaar leven.".
 
Het orakel zal enkel realistische getallen geven. M.a.w., getallen tussen de 5 en 125 jaar.



### Op-de-poef
Een vaste klant in je café bestelt altijd "op-de-poef". Dat wil zeggen dat hij niet onmiddellijk betaalt en dat z'n rekeningen worden neergeschreven. Ooit zal de klant dan gevraagd worden de hele som te betalen.

Schrijf een programma dat 5 keer na elkaar aan de barman vraagt om een bedrag in te voeren. Het ingevoerde bedrag wordt opgeteld bij wat er reeds op de rekening staat. Na 5 keer wordt de totale som getoond alsook hoeveel weken het duurt indien de klant wekelijks 10 euro afbetaalt.

Voorbeeldwerking:


```text
Voer bedrag in?
12
De poef staat op 12 euro.
Voer bedrag in?
14
De poef staat op 26 euro.
Voer bedrag in?
3
De poef staat op 29 euro.
Voer bedrag in?
8
De poef staat op 37 euro.
Voer bedrag in?
2
De poef staat op 39 euro.
*************************
Totaal van de poef is 39 en zal 4 weken duren om volledig afbetaald te worden.
```

