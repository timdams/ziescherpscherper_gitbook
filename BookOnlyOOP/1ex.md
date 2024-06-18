## Oefeningen


### RapportModule

Ontwerp een klasse ``Rapport`` die je zal tonen wat je graad is gegeven een bepaald behaald percentage. Het enige dat je aan een ``Rapport``-object moet kunnen geven is het behaalde percentage (int) dat wordt bijgehouden via een auto-property genaamd ``Percentage``. Via een methode ``PrintGraad`` kan de behaalde graad weergegeven worden, gebaseerd op dit percentage. Dit zijn de mogelijkheden:

* Minder dan 50%: ``"Niet geslaagd"``.
* Tussen 50% en 68% (68 incl.): ``"Voldoende"``.
* Tussen 68% en 75% (75 incl.): ``"Onderscheiding"``.
* Tussen 75% en 85% (85 incl.): ``"Grote onderscheiding"``.
* Meer dan 85%: ``"Grootste onderscheiding"``.

Test je klasse door enkele objecten in je ``main`` en te onderzoeken of deze de juiste graden op het scherm printen. Bijvoorbeeld:

```csharp
Rapport mijnpunten = new Rapport();
mijnpunten.Percentage = 65;
mijnpunten.PrintGraad();
```

### Bibliotheek*

Boeken in een bibliotheek mogen maximum 14 dagen uitgeleend worden. Schrijf een console-applicatie om de volgende gegevens te tonen door middel van een klasse ``BibBoek``:
* de naam van de ontlener, die werd ingelezen (auto-property).
* de datum van vandaag (auto-property met private set). Gebruik uiteraard  de ``DateTime`` klasse.
* de datum dat het boek ten laatste terug moet ingeleverd worden (readonly property).

### Nummers

Maak een klasse ``Nummers``. Deze klasse bevat 2 getallen (type ``int``) die via een auto-property kunnen aangepast worden. Er zijn 4 methoden:

* ``Som``: geeft de som van beide getallen terug.
* ``Verschil``: geeft het verschil van beide getallen terug.
* ``Product``: geeft het product van beide getallen terug.
* ``Quotient``: geeft de deling van het eerste door het tweede getal terug; toon een foutboodschap op het scherm indien er een deling door nul zal gebeuren.

Toon in je ``main`` aan dat je code werkt (op de volgende pagina tonen we een voorbeeld).



Volgende code zou bijvoorbeeld onderstaande output moeten geven:

```csharp
Nummers paar1 = new Nummers();
paar1.Getal1 = 12;
paar1.Getal2 = 34;
Console.WriteLine($"Paar: {paar1.Getal1}, {paar1.Getal2}");
Console.WriteLine($"Som = {paar1.Som()}");
Console.WriteLine($"Verschil = {paar1.Verschil()}");
Console.WriteLine($"Product = {paar1.Product()}");
Console.WriteLine($"Quotient = {paar1.Quotient()}");
```

Output:


```text
Paar: 12, 34
Som = 46
Verschil = -22
Product = 408
Quotient = 0,352941176470588
```

### BankManager*


#### Deel 1

We maken een ``Rekening`` klasse die kan gebruikt worden om de bankrekening van een klant voor te stellen. Deze heeft volgende zaken:

* Een instantievariabele van het type ``int`` genaamd ``balans``. Deze variabele houdt het totale bedrag bij dat op de rekening staat.
* 2 auto-properties van type ``string`` namelijk ``NaamKlant`` en ``RekeningNummer``.
* 1 readonly property  ``Balans`` die de balans teruggeeft.

Voorzie 3 methoden:

1. ``HaalGeldAf``: bepaald bedrag (als parameter type ``int``) wordt van de ``balans`` verwijderd.
2. ``StortGeld``: bepaald bedrag (als parameter type ``int``) wordt op de rekening gezet en aan ``balans`` toegevoegd.
3. ``ToonInfo``: het totale bedrag op de rekening wordt getoond op het scherm, alsook de naam van de klant en het rekeningnummer (*ook de staat wanneer je deel 2 hebt gemaakt wordt getoond*).

Pas de ``HaalGeldAf`` methode aan zodat als returntype het bedrag (``int``) wordt teruggegeven. Indien het gevraagde bedrag meer dan de ``balans`` is dan geef je al het geld terug dat nog op de rekening staat en toon je in de console dat niet al het geld kon worden gegeven (error die verschijnt: ``Rekening leeg nu``.)




Maak 2 instanties van het type ``Rekening`` aan en toon aan dat je geld van de ene Rekening aan de andere kunt geven, als volgt:

```csharp
//rekening 2 geeft 300 euro aan rekening 1
rekening1.StortGeld(rekening2.HaalGeldAf(300));
```

Test je klasse.

1. Nieuwe klant aanmaken
2. Status van bestaande klant tonen 
3. Geld op een bepaalde Rekening zetten 
4. Geld van een bepaalde Rekening afhalen
5. Geld tussen 2 Rekeningen overschrijven

Voorzie extra functionaliteit naar keuze.

#### Deel 2
Voeg aan de ``Rekening``-klasse een auto-property,genaamd ``Staat``, met private set toe van het type ``RekeningStaat`` toe, dat een enumeratie bevat. De Rekening kan in volgende staten zijn ``Geldig``, ``Geblokkeerd``. Een rekening is Geldig wanneer een nieuwe rekening wordt geopend.

Maak een bijhorende publieke methode waarmee je de Rekening van staat kunt veranderen. Deze methode (noem ze ``VeranderStaat``) vereist geen parameters. Telkens je ze aanroept wordt de staat omgewisseld. Als dus het object momenteel op ``Geldig`` stond, dan wordt ze nu ``Geblokkeerd`` en omgekeerd.

Indien een persoon geld van of naar een Geblokkeerde rekening wil sturen dan zal er een error op het scherm verschijnen, namelijk ``Gaat niet. Rekening geblokkeerd``. Idem bij de ``StortGeld`` methode.

Indien de ``HaalGeldAf`` methode wordt aangeroepen en er werd meer geld afgehaald dan de balans dan zal de rekening ook op Geblokkeerd gezet worden na het verschijnen van de foutboodschap ("Rekening leeg nu").

### Persoon

Ontwerp en implementeer een klasse Persoon met 2 auto-properties (``string``) ``Achternaam`` en ``Voornaam``. 

Voeg bovendien een full property ``GeboorteDatum`` toe (type ``DateTime``). De geboortedatum kan enkel waarden tussen 1/1/1990 en vandaag (moment dat code wordt uitgevoerd) liggen. Indien dit niet de situatie is, wordt de huidige datum van uitvoeren gebruikt. 

Definieer vervolgens een methode ``BerekenLeeftijd``, die op basis van de ingestelde geboortedatum en de huidige datum (dat programma wordt uitgevoerd) de leeftijd van de persoon teruggeeft als ``int``.  



### Verjaardag
Maak een applicatie die aan de gebruiker z'n geboortedatum vraagt (dag/maand, bv. 18/3). Vervolgens toont het programma op welke dag hij volgend jaar jarig zal zijn (Monday, Tuesday, enz.) én hoeveel dagen hij nog moet wachten. Uiteraard gebruik je ``DateTime`` voor deze applicatie.

{% hint style='tip' %}
Je hebt geen eigen klasse nodig. Doel van deze oefening is dat je leert werken met de bestaande ``DateTime`` en ``TimeSpan`` klassen. Je mag dus alles in de Main schrijven.
{% endhint %}


{% hint style='tip' %}
Volgende methode geeft de naam (als ``string ``) van de dag terug in de taal van het systeem waarop je applicatie draait:

``System.Globalization.DateTimeFormatInfo.CurrentInfo.GetDayName();``

```
{% endhint %}

Voorbeeld invoer en uitvoer:


```text
Wanneer is je verjaardag (d/m, bv. 18/3)
20/5
Je bent over 124 dagen jarig op een Dinsdag
```

