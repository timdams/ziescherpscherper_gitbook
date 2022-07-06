## Berekeningen met System.Math

Een groot deel van je leven als ontwikkelaar zal bestaan uit het bewerken van variabelen in code. Meestal zullen die bewerkingen voorafgaan van berekeningen. De ``System.Math`` bibliotheek zal ons hier bij kunnen helpen. Zoals de naam al doet vermoeden staat deze bibliotheek voor *Mathematics*: wiskunde!


### De Math-bibliotheek
De Math-bibliotheek bevat methoden voor een groot aantal typische wiskundige bewerkingen (sinus, cosinus, vierkantswortel, macht, afronden, enz.) en kan je dus helpen om leesbaardere en kortere expressies te schrijven.

Stel dat je de derde macht van een variabele ``getal`` wenst te berekenen. *Zonder* de Math-bibliotheek zou dat er zo uitzien:


```java
double result = getal * getal * getal; //SLECHTE MANIER
```

Dit valt nog mee, maar wat als je 3 tot de zevende macht moest berekenen? Kortom, laten we eens kijken hoe ``Math`` ons kan helpen. *Met* de Math-bibliotheek kunnen we gebruik maken van de ``Pow`` (**Power**) methode:


```java
double result = Math.Pow(getal, 3);
```

Deze methode vereist twee parameters:
* De eerste is het grondtal 
* De tweede is de exponent ("tot de hoeveelste macht")

#### De Math bibliotheek ontdekken

Als je in Visual Studio ``Math`` schrijft in je code, gevolgd door een punt (``.``) krijg je alles te zien wat de Math-bibliotheek kan doen:


![De sterretjes geven de meestgebruikte methoden in deze bibliotheek aan. Vervolgens verschijnen alle overige methoden, properties, enz. alfabetisch.](../assets/4_methoden/methoden3.png)


Een kubusje voor een naam wil zeggen dat het om een **Methode** gaat (zoals ``Console.ReadLine()``). Een vierkantje met twee streepjes in zijn constanten (zoals ``Pi``(``π``) en het getal van Euler (``e``)).

#### Methoden gebruiken

De meeste methoden zijn zeer makkelijk in gebruik en werken bijna allemaal op een soortgelijk manier. Meestal moet je 1 of meerdere parameters tussen de haken meegeven en het resultaat moet je altijd in een nieuwe variabele opvangen. 

Enkele voorbeelden:

```java
double sineHoekA = Math.Sin(345); //IN RADIALEN!
double derdeMachtVan20 = Math.Pow(20, 3);
double complexer = 3 + derdeMachtVan20 * Math.Round(sineHoekA);
```

Twijfel je over de werking van een methode, gebruik dan de help als volgt:

1. Schrijf de Methode zonder parameters. Bijvoorbeeld ``Math.Pow()`` (je mag de error negeren). 
2. Plaats je cursor op ``Pow``.
3. Druk op ``F1`` op je toetsenbord.
4. Je krijgt nu de help-files te zien van deze methode.
5. In hoofdstuk 7 leggen we uit hoe je die help-files moet lezen.

#### PI (π)

Ook het getal Pi (``3.141...``) is beschikbaar in de Math-bibliotheek. Het witte icoontje voor PI bij Intellisense toont aan dat het hier om een *field* gaat: een eenvoudige variabele met een specifieke waarde. In dit geval gaat het zelfs om een ``const`` field, met de waarde van Pi van het type double.


```java
public const double PI;
```

Je kan deze als volgt gebruiken in berekeningen zoals

```java
double straal = 5.5;
double omtrek = Math.PI * 2 * straal;
```



### Constanten

Je zal het ``const`` keyword hier en daar in codevoorbeelden zien staan. Je gebruikt dit om aan te geven dat een variabele onveranderlijk is én niet per ongeluk kan aangepast worden. Door dit keyword voor de variabele declaratie te plaatsen zeggen we dat deze variabele na initialisatie niet meer aangepast kan worden. Dit heeft 2 voordelen:

1. Jij (of mede-ontwikkelaars) zullen niet per ongeluk deze variabele aanpassen waardoor andere stukken code plots vreemde bugs lijken te krijgen.
2. Het is ook een vorm van documentatie. Meestal staan constanten bovenaan je code gegroepeerd en zo weten lezers van jouw code ogenblikkelijk welke constanten er zullen gebruikt (want meestal komen deze op meerdere plaatsen voor én zijn ze dus belangrijk voor de goede werking van je code).

Volgende voorbeeld toont in de eerste lijn hoe je het ``const`` gebruikt. De volgende lijn zal dankzij dit keyword een error geven reeds bij het compileren en jou dus waarschuwen dat er iets niet klopt.

```java
const double G_AARDE = 9.81;
G_AARDE = 10.48; //ZAL ERROR GEVEN
```

Merk op de schrijfwijze van ``const`` identifiers: deze zetten we in ALLCAPS, waarbij we liggende streepjes gebruiken om het onderscheid tussen de onderlinge woorden aan te geven ("gaarde" is anders een vreemd woord).

{% hint style='tip' %}
Constanten in code worden ook soms **magic numbers** genoemd. De reden hiervoor is dat ze vaak plotsklaps ergens in de code voorkomen, maar wel op een heel andere plek werden gedeclareerd. Hierdoor is het voor de ontwikkelaar niet altijd duidelijk wat de variabele juist doet.
Het is daarom belangrijk dat je goed nadenkt over het gebruik van magic numbers én deze zeer duidelijke namen geeft. 

Er worden vele filosofische, bijna theologische, strijden gevoerd tussen ontwikkelaars over de plek van magic numbers in code. In de C/C++ tijden werden deze steeds aan de start van de code gegroepeerd. Op die manier zag de ontwikkelaar in één oogopslag alle belangrijke variabelen en konden deze ook snel aangepast worden. In C# prefereert men echter om variabelen zo dicht mogelijk bij de plek waar ze nodig zijn te schrijven, dit verhoogt de *modulariteit* van de code: je kan sneller een flard code kopiëren en op een andere plek herbruiken.

De applicaties die wij in dit boek ontwikkelen zijn niet groot genoeg om over te debatteren. Veel bedrijven hanteren hun eigen coding guidelines en het gebruik, naamgeving en plaatsing van magic numbers zal zeker daarin zijn opgenomen. 
{% endhint %}




### Bereik in code weten 
Het bereik van datatypes ligt weliswaar vast (zie hoofdstuk 2). Maar het is nuttig om weten dat deze ook in de compiler gekend is.  Ieder datatype heeft een aantal ingebouwde zaken die je kan gebruiken om onder andere de maximum en minimum-waarde van een datatype te gebruiken.  Volgende voorbeeld toont hoe dit kan:

```java
string startZin = "Het bereik van het type double is:";
Console.WriteLine($"{startZin} {double.MinValue} tot {double.MaxValue}.");
```

Dit geeft op het scherm: 

``Het bereik van het type double is: -1.7976931348623157E+308 tot 1.7976931348623157E+308.``

Je kan met andere woorden met `int.MaxValue` en `int.MinValue` het minimum- en maximumbereik van het type ``int`` verkrijgen. Wil je dit van een ``double``, dan gebruik je `double.MaxValue` enz. Zelfs oneindig is beschikbaar bij kommagetallen als ``.PositiveInfinity`` en  ``.NegativeInfinity``. 

