## Oefeningen

### Boek

Maak een klasse ``Boek`` en gebruik auto-properties voor de velden:

* Isbn (``int``)
* Title (``string``)
* Auteur (``string``)
 
Maak voorts een full property voor ``Prijs`` (``double``).

Maak een child-klasse die van ``Boek`` overerft genaamd ``TextBoek``. Een ``TextBoek`` heeft één extra property:

* ``GradeLevel`` (``int``)

Maak een child-klasse die van ``Boek`` overerft genaamd ``KoffietafelBoek``. Deze klasse heeft geen extra velden.

Voorts kunnen boeken "opgeteld" worden om als omnibus uitgebracht te worden. De titel wordt dan "Omnibus van X". waarbij X de Auteurs bevat, gescheiden met een komma. De prijs van een Omnibus is steeds de som van beide boeken gedeeld door 2. **Schrijf een ``static`` methode ``TelOp`` die twee ``Boek`` objecten als parameter aanvaardt en als returntype een nieuw ``Boek`` teruggeeft.** 

In beide child-klassen, override de ``Prijs``-setter zodat:

* Bij ``TextBoek`` de prijs enkel tussen 20 en 80 kan liggen.
* Bij ``KoffietafelBoek`` de prijs enkel tussen 35 en 100 kan liggen.

Zorg ervoor dat boeken de ``ToString`` overriden zodat je boekobjecten eenvoudig via ``Console.WriteLine(myBoek)`` hun info op het scherm tonen. Ze tonen deze info als volgt: "Title - Auteur (Isbn) _ Prijs" (bv. ``The Shining - Stephen King (05848152) _ 50``)


Maak boeken aan van de 3 klassen, toon dat de prijs niet altijd zomaar ingesteld kan worden.

{% hint style='tip' %}
Bekijk zeker de appendix indien je wilt weten hoe je de ``+`` operator kunt overriden om boeken op te tellen, zodat je geen methode nodig hebt maar gewoon kunt schrijven: ``Boek opgeteld = boek1 + boek2;``.
{% endhint %}


### Money, money, money
Maak enkele klassen die een bank kan gebruiken (of hergebruik je ``BankManager`` code uit hoofdstuk 9)

1. Abstracte klasse ``Rekening``: deze bevat een methode ``VoegGeldToe`` en ``HaalGeldAf``. Het saldo van de rekening wordt in een private variabele bijgehouden (en via de voorgaande methoden aangepast) die enkel via een read-only property kan uitgelezen worden. Voorts is er een abstracte methode ``BerekenRente`` de rente als double teruggeeft.
2. Een klasse ``BankRekening`` die een Rekening is. De rente van een BankRekening is 5% wanneer het saldo hoger is dan 100 euro, zoniet is deze 0%. 
3. Een klasse ``SpaarRekening`` die een Rekening is. De rente van een SpaarRekening bedraagt steeds 2%.
4. Een klasse ``ProRekening`` die een SpaarRekening is. De ProRekening hanteert de Rente-berekening van een SpaarRekening (``base.BerekenRente``) maar zal per 1000 euro saldo nog eens 10 euro verhogen. 

Schrijf deze klassen en toon de werking ervan in je main.

### Bookmark extra

Implementeer de ``ToString()`` methode in zowel de ``Bookmark`` als de ``HiddenBookmark`` klasse. Bij bookmark moet de output bestaan uit de titel van de site, gevolgd door de url tussen haakjes, bv:


```text
Google (www.google.com)
```

Bij ``HiddenBookmark`` wordt er achteraan nog "---HIDDEN---" gezet:


```text
Google (www.google.com) ---HIDDEN---
```

Zorg ervoor dat er géén dubbele code in HiddenBookmark staat (tip: ``base()``).


### Geometric figures

Maak een abstracte klasse ``GeometricFigure``. Iedere figuur heeft een hoogte, breedte en oppervlakte. Maak autoproperties voor van ``Hoogte`` en ``Breedte``. De ``Oppervlakte`` is een read-only property want deze wordt berekend gebaseerd op de hoogte en breedte. Deze berekening gebeurt in de methode ``BerekenOppervlakte``: deze roep je met andere woorden aan in de getter van ``Oppervlakte`` en dat resultaat geeft de getter terug 

{% hint style='warning' %}
Let er dus op dat ``Oppervlakte`` enkel een getter heeft. Een setter schrijven zou vreemde bugs geven: wat als de gebruiker de oppervlakte van de figuur zo aanpast, maar wel een andere hoogte en breedte heeft ingesteld? Je zou dan een foute oppervlakte krijgen daar die niet berekend wordt.
{% endhint %}


Voorzie een abstracte methode ``BerekenOppervlakte`` die een ``int`` teruggeeft.

Maak 3 klassen:

* **``Rechthoek``**: erft over van ``GeometricFigure``. Oppervlakte is gedefinieerd als ``breedte * hoogte``.
* **``Vierkant``**: erft over van ``Rechthoek``. Voorzie een constructor die lengte en breedte als parameter aanvaard: deze moeten gelijk zijn, indien niet zet je deze tijdens de constructie gelijk. Voorzie een 2e constructor die één parameter aanvaardt dat dan geldt als zowel de lengte als breedte. Deze klasse gebruikt de methode ``BerekenOppervlakte`` van de ``Rechthoek``-klasse.
* **``Driehoek``**: erft over van ``GeometricFigure``. Oppervlakte is gedefinieerd als ``breedte*hoogte/2``.

Maak een applicatie waarin je de werking van deze klassen aantoont.


### Dierentuin

Maak een console-applicatie waarin je een zelfverzonnen abstract klasse ``Dier`` in een ``List<Dier>`` kunt plaatsen. Ieder dier heeft een gewicht en een methode ``Zegt`` (die abstract is) die het geluid van het dier in kwestie op het scherm zal tonen. Maak enkele childklassen die overerven van ``Dier`` en uiteraard de ``Zegt`` methode overriden.

Plaats enkele dieren in de nieuw aangemaakt lijst.
Vervolgens verschijnt er een menu Wanneer de gebruiker 'q' kiest stopt het programma. Het keuze menu heeft volgende opties:

1. **Dier verwijderen** , gevolgd door de gebruiker die invoert het hoeveelste dier weg moet uit de List.
2. **Diergewicht gemiddelde**: het gemiddelde van alle dieren hun gewicht wordt getoond
3. **Dier praten**: alle dieren hun ``Zegt()`` methode wordt aangeroepen en via ``WriteLine`` getoond
4. **Opnieuw beginnen**: de List wordt leeggemaakt en het programma zal terug van voor af aan beginnen. Waarbij de lijst terug gevuld wordt met enkele start dieren.

Probeer zo modulair mogelijk te werken.
