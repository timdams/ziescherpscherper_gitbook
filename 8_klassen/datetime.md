
## OOP in de praktijk: DateTime

Gefeliciteerd! Je hebt de basis van klassen, objecten, fields en properties onder de knie.
Om te bewijzen dat je nu "C# spreekt", gaan we kijken naar een ingebouwde klasse die je constant zal gebruiken: `DateTime`.

Vroeger was dit magie. Nu kan je snappen hoe het werkt:
* Het is een **klasse** (struct eigenlijk, maar dat negeren we even).
* Het heeft **properties** (zoals `Year`, `Month`).
* Het heeft **methoden** (zoals `AddDays()`).

Laten we er eens mee spelen.

### Een DateTime maken
Er zijn twee hoofdmanieren om aan een datum te geraken:

#### 1. De "Nu" knop (Static Property)
Wil je de datum van dit eigenste moment?
```csharp
DateTime nu = DateTime.Now;
Console.WriteLine(nu);
```
`DateTime.Now` is een **static property**. Je hoeft geen `new` te doen, het is een "globale" waarde die altijd beschikbaar is.

#### 2. Een specifieke datum (De Constructor)
Wil je werken met je verjaardag? Dan moet je een **specifiek object** maken met `new`.

```csharp
// jaar, maand, dag
DateTime verjaardag = new DateTime(1990, 5, 20); 

// jaar, maand, dag, uur, minuut, seconde
DateTime apollo11 = new DateTime(1969, 7, 20, 20, 17, 0);
```

<!-- \newpage -->




<!-- \newpage -->


### Methoden en de Grote Valkuil

Je kan met datums rekenen. "Hoe laat is het binnen 5 uur?", "Welke dag was het 1000 dagen geleden?".
Hiervoor gebruiken we methoden zoals `AddDays`, `AddHours`, enz.

```csharp
DateTime vandaag = DateTime.Now;
DateTime deadline = vandaag.AddDays(7);
Console.WriteLine(deadline);
```

{% hint style='danger' %}
**OPGELET: HET IS ONVERANDERLIJK (IMMUTABLE)!**

Een veelgemaakte fout bij beginners is dit:
```csharp
DateTime mijnVerjaardag = new DateTime(1990, 1, 1);
mijnVerjaardag.AddYears(1); // FOUT! Dit doet niets met mijnVerjaardag!
Console.WriteLine(mijnVerjaardag.Year); // Nog steeds 1990
```

`DateTime` objecten zijn **immutable**. Ze kunnen nooit veranderen.
Methoden zoals `AddYears` passen het object *niet* aan, maar **geven een nieuw object terug**.

**Juiste manier:**
```csharp
mijnVerjaardag = mijnVerjaardag.AddYears(1); // VANG HET RESULTAAT OP!
```
{% endhint %}

<!-- \newpage -->


### Properties (Alleen lezen)

Herinner je de **Get-Only Properties** van het vorige hoofdstuk? `DateTime` zit er vol mee.
Je kan wel vragen welk jaar het is (`.Year`), maar je kan het jaar niet zomaar aanpassen (`.Year = 2050` werkt niet).

Enkele nuttige:
* `Year`, `Month`, `Day`
* `Hour`, `Minute`, `Second`
* `DayOfWeek` (Geeft `Monday`, `Tuesday`...)
* `DayOfYear` (1 tot 366)

```csharp
DateTime nu = DateTime.Now;
Console.WriteLine($"Het is vandaag: {nu.DayOfWeek}");
Console.WriteLine($"Dag nummer {nu.DayOfYear} van het jaar.");
```

### Static methoden

Sommige methoden zijn ``static`` dat wil zeggen dat je ze enkel rechtstreeks op de klasse kunt aanroepen. Vaak zijn deze methoden hulpmethoden waar de individuele objecten niets aan hebben. We hebben dit reeds gebruikt bij de ``Math`` en ``Console``-klassen. 

We behandelen ``static`` uitgebreid verderop in het boek.


#### De tijd uit een string inlezen

Parsen laat toe dat je strings omzet naar een ``DateTime`` object. Dit is handig als je bijvoorbeeld de gebruiker via ``Console.ReadLine()`` tijd en datum wilt laten invoeren in de *Belgische notatie*:

```csharp
string datumInvoer = Console.ReadLine(); 
DateTime datumVerwerkt = DateTime.Parse(datumInvoer, new System.Globalization.CultureInfo("nl-BE"));
Console.WriteLine(datumVerwerkt);
```

Indien je nu dit programma'tje zou uitvoeren en als gebruiker "8/11/2016" zou intypen, dan zal deze datum geparsed worden en in het object ``datumVerwerkt`` komen.

{% hint style='tip' %}
Zoals je ziet roepen we ``Parse`` aan op ``DateTime`` en dus niet op een specifiek object. Dat was ook zo reeds bijvoorbeeld bij ``int.Parse`` wat dus doet vermoeden dat zelfs het ``int`` datatype eigenlijk een klasse is!
{% endhint %}


#### IsLeapYear

Deze nuttige methode geeft een ``bool`` terug om aan te geven of de actuele parameter (type ``int``) een schrikkeljaar voorstelt of niet:

```csharp
DateTime vandaag = DateTime.Now;
if(DateTime.IsLeapYear(vandaag.Year))
    Console.WriteLine("Dit jaar is een schrikkeljaar.");
```

### TimeSpan 

Je kan DateTime objecten ook van elkaar aftrekken (optellen gaat niet!). Het resultaat van deze bewerking geeft echter niet een DateTime object terug, **maar een ``TimeSpan`` object**. Dit is nieuwe object van het type ``TimeSpan`` (wat dus een andere klasse is) dat aangeeft hoe groot het verschil is tussen de 2 DateTime objecten kunnen we als volgt gebruiken:

```csharp
DateTime vandaag = DateTime.Today;
DateTime geboorteDochter = new DateTime(2009,6,17);
TimeSpan verschil = vandaag - geboorteDochter;
Console.WriteLine($"{verschil.TotalDays} dagen sinds geboorte dochter.");
```


Je zal de ``DateTime`` klasse in véél van je projecten kunnen gebruiken waar je iets met tijd, tijdsverschillen of datums wilt doen. We hebben de klasse in deze sectie echter geen eer aangedaan. De klasse is veel krachtiger dan ik hier doe uitschijnen. Het is een goede gewoonte als beginnende programmeur om steeds de documentatie van nieuwe klassen er op na te slaan.[^datedoc]

[^datedoc]: Wanneer je in je browser zoekt op "C#" gevolgd door de naam van de klasse dan zal je zo goed als zeker als eerste *hit* de officiële .NET documentatie krijgen op [docs.microsoft.com](https://docs.microsoft.com).



<!-- \newpage -->


>![](../assets/care.png)Oef, we zijn er!
>
>We hebben de basis van Object Georiënteerd Programmeren gelegd.
>
>1.  **De Klasse**: De blauwdruk / het 3D-printer bestand.
>2.  **Het Object**: De effectieve instantie in het geheugen (gebouwd met `new`).
>3.  **Fields of instantievariabelen**: De geheime interne data (private).
>4.  **Properties**: De poortwachters (public) om die data veilig te beheren.
>5.  **Methoden**: Het gedrag van het object.
>
>Voor je verder gaat raad ik je aan om dit alles goed te laten bezinken én maximaal de komende oefeningen te maken. Het zal de beste manier zijn om de ietwat bizarre wereld van OOP snel eigen te maken.





