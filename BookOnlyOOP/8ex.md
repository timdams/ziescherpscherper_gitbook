## Oefeningen

### Een eigen huis

#### Basis
Gebruik compositie, polymorfisme én overerving om een klasse ``Huis`` te voorzien van enkele kamers, waarbij iedere kamer een klasse op zich is (denk aan ``BadKamer``, ``Salon``, etc). Alle kamers erven over van de klasse ``Kamer``.
Iedere kamer heeft een oppervlakte (in vierkante meter), een naam en prijs. Standaard is de prijs van een kamer 400 euro, maar mogelijke child-klassen zullen deze property soms overriden:

Maak minstens volgende klassen:

* Badkamer: kost 500 euro.
* Gang: kost 10 euro per vierkante meter dat deze kamer groot is.
* Salon: kost 300 euro indien er geen schouw aanwezig is (via ``bool`` bijhouden) anders 500 euro.


De klasse ``Huis`` heeft een array van kamers. De klasse heeft ook een methode ``BerekenPrijs`` die de totale prijs van het huis berekent gebaseerd op de prijzen van iedere kamer in de array.

Test je klasse door enkele huizen te maken en er enkele kamers in te plaatsen (bepaal zelf hoe je de kamers aan het huis toevoegt: via een methode, constructor, etc) en vervolgens de prijs ervan te tonen.

#### Mapmaker

Voorzie een ``Teken`` methode die een huis kan tekenen, gebruikmakend van de ``Teken``-methoden van de kamers. Hiervoor dien je een ``X`` en ``Y`` coördinaat per , alsook lengtes en breedter per huis én kamer te hebben zodat je deze op de juiste plekken op het scherm kan plaatsen.

Kan je ervoor zorgen dat een architect nieuwe kamers kan toevoegen en verwijderen?
