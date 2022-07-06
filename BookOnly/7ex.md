## Oefeningen


### Kill/Death-ratio deel 2

Maak een programma dat toelaat om de kills en deaths van x spelers in te voeren, waarbij x aan de start van het programma wordt gevraagd aan de gebruiker. Vervolgens zal het programma vertellen welke speler de beste k/d-ratio heeft.

### LeveringsBedrijf
Maak een programma voor een koeriersbedrijf. Maak een array die 10 postcodes bevat (zelf te kiezen) van gemeenten waar het bedrijf naar levert. Maak een tweede array die de prijs bevat per kg voor iedere respectievelijke gemeente. Het eerste element van deze array bevat dus de prijs/kg om naar de gemeente te leveren die als eerste in de array met postcodes staat.

Vraag aan de gebruiker een postcode en het gewicht van het pakket. Vervolgens wordt de prijs/kg opgezocht voor die gemeente en wordt de prijs berekend, gegeven het ingegeven gewicht.

Indien het bedrijf niet levert aan de ingetypte postcode dan wordt een foutmelding weergegeven.


```text
Geef gewicht pakket
45
Naar welke postcode wenst u dit pakket te versturen?
2020
Dit zal 9630 euro kosten.
```

{% hint style='tip' %}
Je zou deze oefening ook met meerdimensionale arrays kunnen oplossen, waarbij je de prijs in de ene kolom en de postcode in de volgende plaatst. Op die manier blijft de informatie ook 'bij elkaar'.
{% endhint %}

### Hamming distance
De *hamming distance* is het aantal tekens dat twee reeksen verschillen indien we ieder element vergelijken op dezelfde plaats in de andere reeks.

Maak een programma dat aan de gebruiker vraagt om twee DNA strings in te voeren (een reeks bestaande uit de letters G, A, C & T). Beide reeksen moeten even lang zijn. Bereken de hamming distance tussen beide reeksen.

De hamming distance van volgende twee DNA strings is 7, omdat er 7 elementen in beide strings staan die niet gelijk zijn aan mekaar op dezelfde plek (aangeduid met ``^``).

```
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
^ ^ ^  ^ ^    ^^
```

### Galgje 
Maak een spel, vergelijkbaar met het populaire woordspelletje "galgje", waarin de speler een woord moet raden.



### Password generator 
Ontwerp een consoletoepassing waarmee je een wachtwoord genereert voor een gebruiker. Het wachtwoord is opgebouwd uit:

* de 2 eerste letters van de familienaam, waarbij de eerste letter een hoofdletter is en tweede letter kleine letter. 
* het zonenummer van het telefoonnummer zonder de 0.
* het eerste cijfer van de postcode in het kwadraat.

{% hint style='danger' %}

Schrijf nooit een paswoord manager die je paswoorden gortdroog als ``string`` bewaart. **Secure code** schrijven is een hele discipline op zich en laat je best nog even links liggen tot je C# zelf goed in de vingers hebt.
{% endhint %}

