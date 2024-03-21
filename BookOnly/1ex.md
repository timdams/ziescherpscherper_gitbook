## Oefeningen

{% hint style='tip' %}
Oefeningen met een sterretje achter zijn oefeningen die in de komende hoofdstukken nog zullen terugkomen. Gooi je oplossing dus niet weg.
{% endhint %}

### Kill/Death-ratio*

De Kill/Death-ratio van een speler geeft weer hoe vaak de speler in een computergame sterft tegenover het aantal keer dat hij een andere speler doodt. Kortom, hoe groter dit getal, hoe beter de speler is. Maak twee variabelen ``double kills`` en ``double deaths`` aan. Wijs er jouw typische scores aan toe die je haalt in een spel naar keuze. Bereken en toon vervolgens je kill/death-ratio.

{% hint style='warning' %}
**Begrijp je waarom we best één van beide variabelen in ``double`` zetten?** Lees de waarschuwing van de voorman bij Expressies zeker nog eens na... Of test eens wat er gebeurt indien je met ``int`` zou werken.
{% endhint %}

### Je gewicht in het heelal

Je massa is overal dezelfde. Je gewicht daarentegen is afhankelijk van de zwaartekracht van de plek waar je bent. Zo is je gewicht veel groter op Jupiter dan op Mars.

Maak een variabele ``double gewichtOpAarde`` aan. Wijs een gewicht toe (bv. het jouwe). Schrijf nu een programma dat onder elkaar jouw gewicht op verschillende planeten toont.

Hier de omzettingstabel (je gewicht op Mercurius is dus je gewicht op aarde x 0.38):

* Mercurius: 0.38
* Venus: 0.91
* Aarde: 1.00
* Mars: 0.38
* Jupiter: 2.34
* Saturnus: 1.06
* Uranus: 0.92
* Neptunus: 1.19
* Pluto: 0.06 (we laten de discussie achterwege laten of Pluto wel of geen planeet is)

De output zijn verschillende lijnen onder elkaar in de vorm van:

``Je weegt op [planeet] [gewichtopdieplaneet] kg.``

Plaats de zin met Jupiter in het rood, daar je daar het zwaarst weegt en die van Pluto in het groen.




### Tekstmaker

Met de methode ``System.IO.File.WriteAllText();`` kan je een ``string`` naar een bestand wegschrijven.

Je geeft hierbij 2 argumenten mee: de bestandsnaam, en de inhoud van het bestand.

Volgende voorbeeld schrijft bijvoorbeeld de zin "Ik ben cool" weg naar een bestand dat zal aangemaakt worden genaamd "me.txt":


```csharp
System.IO.File.WriteAllText("me.txt", "Ik ben cool");
```

Schrijf een programma dat aan de gebruiker de naam van het bestand vraagt, gevolgd door wat er in het bestand moet geschreven worden. Vervolgens maak je dit bestand aan en plaats je die inhoud er in.

{% hint style='tip' %}
Als je enkel een bestandsnaam meegeeft (en geen volledige folderpath) dan wordt het bestand geplaatst op de plek waar het programma wordt uitgevoerd.

Standaard staat je gecompileerde programma in de "bin\debug\net6.0\ folder" van je project.

Als je dus een solution hebt aangemaakt genaamd "Oefening" in de folder "C:\Temp" dan zal het bestand zich in de volgende folder bevinden "C:\Temp\Oefening\Oefening\bin\debug\net6.0".

Je kan ook snel naar deze folder gaan door in de solution explorer aan de rechterzijde in VS te rechterklikken op je project en dan te kiezen voor: *Open folder in file explorer*.
{% endhint %}
