### Constanten

Je zal het ``const`` keyword hier en daar in codevoorbeelden zien staan. Je gebruikt dit om aan te geven dat een variabele onveranderlijk is én niet per ongeluk kan aangepast worden. Door dit keyword voor de variabele declaratie te plaatsen zeggen we dat deze variabele na initialisatie niet meer aangepast kan worden. 

Volgende voorbeeld toont in de eerste lijn hoe je het ``const`` gebruikt. De volgende lijn zal dankzij dit keyword een error geven reeds bij het compileren en jou dus waarschuwen dat er iets niet klopt.

```csharp
const double G_AARDE = 9.81;
G_AARDE = 10.48; //ZAL ERROR GEVEN
```

Merk op hoe we de ``const`` variabelen een identifier geven: deze zetten we in ALLCAPS. Hierbij gebruiken we een liggend streepjes om het onderscheid tussen de onderlinge woorden aan te geven. Dit is geen verplichting, maar gewoon een aanbeveling.

{% hint style='tip' %}
Constanten in code worden ook soms **magic numbers** genoemd. De reden hiervoor is dat ze vaak plotsklaps ergens in de code voorkomen, maar wel op een heel andere plek werden gedeclareerd. Hierdoor is het voor de ontwikkelaar niet altijd duidelijk wat de variabele juist doet.
Het is daarom belangrijk dat je goed nadenkt over het gebruik van magic numbers én deze zeer duidelijke namen geeft. 

Er worden vele *filosofische oorlogen* gevoerd tussen ontwikkelaars over de plek van magic numbers in code. In de C/C++ tijden werden deze steeds  bovenaan aan de start van de code gegroepeerd. Op die manier zag de ontwikkelaar in één oogopslag alle belangrijke variabelen en konden deze ook snel aangepast worden. In C# prefereert men echter om variabelen zo dicht mogelijk bij de plek waar ze nodig zijn te schrijven, dit verhoogt de *modulariteit* van de code: je kan sneller een flard code kopiëren en op een andere plek herbruiken.

De applicaties die wij in dit boek ontwikkelen zijn niet groot genoeg om over te debatteren. Veel bedrijven hanteren hun eigen coding guidelines en het gebruik, naamgeving en plaatsing van magic numbers zal zeker daarin zijn opgenomen. 
{% endhint %}
