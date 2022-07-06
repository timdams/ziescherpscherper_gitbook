## Oefeningen

### ComputerOnderdelen sorteren

Haal de Computerwinkel oefening uit hoofdstuk 12 boven. Zorg ervoor dat je elementen van het type ``ComputerOnderdeel`` kunnen gesorteerd worden op hun Prijs. Voorzie een nieuw menuitem "Sorteer onderdelen" die het gesorteerde resultaat toont.

### Carbon Footprint

Maak 4 klassen:
* ``Huis``
* ``Fabriek``
* ``Auto``
* ``Plant``

We maken een programma om de fictieve ecologische voetafdruk van bepaalde objecten te berekenen

Maak een interface ``ICarbonFootPrint`` die volgende zaken heeft:
* 1 methode ``BerekenFootprint`` die een ``int`` teruggeeft en geen parameters nodig heeft.
* 1 methode ``VerlaagFootprint`` die niets teruggeeft en geen parameters nodig heeft.

Breid de volgende klassen met de interface uit:
* De carbon footprint van een ``Huis`` is gebaseerd op het volume van het huis in kubieke meter maal 10.
* De carbon footprint van een ``Fabriek`` is gebaseerd op het aantal werknemers maal 100. 
* De carbon footprint van een ``Auto`` is gebaseerd op het merk.
* De carbon footprint van een ``Plant`` is altijd 0.

Het verlagen van de footprint in iedere klasse verzin je zelf (door bijvoorbeeld bij het huis de factor 10 met 1 te verlagen), maar merk op dat deze nooit negatief mag zijn.

Zorg ervoor dat van iedere klasse de footprint kan bevraagd worden (maak/verzin dus de nodige properties per klasse om dit te berekenen).

Plaats van iedere klasse 2 objecten in een gemeenschappelijke lijst en zorg ervoor dat:
* De footprint van alle objecten getoond wordt (planten worden overgeslagen).
* De gemiddelde footprint van alle objecten berekend wordt.
* Toont welk object de hoogste footprint heeft.
* Van alle objecten de footprint kan verlaagd worden.

