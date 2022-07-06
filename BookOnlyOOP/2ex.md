## Oefeningen

{% hint style='tip' %}
Er zijn geen aparte Exception handling oefeningen. Het is een goede gewoonte dat je vanaf nu steeds goed nadenkt waar in je programma's je Exception handling kan toepassen.
{% endhint %}


### Bankmanager 2

Breidt de bankmanager oefening uit het vorige hoofdstuk uit met volgende functionaliteiten:
* Voorzie in je programma een methode ``SimuleerOverdracht``. Je kan aan deze methode 2 ``Rekening`` objecten meegeven. Vervolgens zal de methode 5x een willekeurig bedrag van de ene naar de andere rekening sturen, hierbij wisselen de rekeningen om de beurt wie verzender en wie ontvanger is. Wanneer de methode klaar is wordt er niets teruggestuurd.
* Maak een methode ``CreeerTienerRekening`` in je programma. Deze methode geeft een nieuwe rekening terug waar de balans reeds op 50 staat. De methode aanvaardt 1 parameter: de naam van de klant, dat vervolgens in het nieuwe object wordt ingesteld. 


### Voortplanten*

Laten we het voorbeeld van de klasse ``Mens`` en de methode ``PlantVoort`` uitbreiden. Een Mens wordt gedefinieerd door een geslacht (man of vrouw), kleur_ogen (als ``enum``) en een maxlengte. Maak 2 Mens objecten aan en geef hen allemaal verschillende eigenschappen, maar zorg ervoor dat één een vrouw is en de ander een man. We passen nu de ``PlantVoort`` methode aan: de baby heeft als lengte de gemiddelde lengte van de man en vrouw. De oogkleur is 50% van de tijd die van de man en 50% van de tijd die van de vrouw. Het geslacht is willekeurig.

Introduceer echter ook een mutatie mogelijkheid: 10% van de tijd zal een baby een totaal willekeurige  oogkleur krijgen, die niet noodzakelijk die van één van de ouders is.

Voorzie een methode ``ToonMens``. Deze vat de informatie van een Mens-object in één zin samen, hierbij zal de achtergrond van de tekst de kleur van de ogen zijn. De tekst die verschijnt is: maxlengte [in meter], geslacht

Bijvoorbeeld:
1.78 m, man  

Visualiseer op het scherm wat er gebeurt indien je beide mensen 100 keer laat voortplanten (arme vrouw). 

{% hint style='warning' %}

![](../assets/neotim.png)
Zoals reeds vermeld kan je via **ziescherp.be** doorklikken naar "extra oefeningen". Er zijn enkele erg leuke Pokémon oefeningen die bij dit hoofdstuk en de volgende horen (die ik echter vanwege copyright-redenen beter niet in dit boek opneem). 
{% endhint %}

