
## Klassen zijn eigen Datatypes

In het begin van dit boek leerde je werken met basis datatypes zoals `int`, `string`, `bool` en `double`. 
Je liep echter al snel tegen de limieten van deze eenvoudige blokjes aan. Wat als je een "Student" wil bewaren? Die bestaat uit een naam (string), een leeftijd (int) en punten (array).

**Met klassen mag je je eigen, complexe datatypes ontwerpen.**

Telkens je een klasse definiëert (bv. `class Auto`), voeg je eigenlijk een nieuw woord toe aan C#. Vanaf dan kan je variabelen maken van dat type, net zoals je vroeger `int` of `string` gebruikte.

### Hoe ziet zo'n klasse eruit?

Een klasse is de **blauwdruk**. Het beschrijft wat jouw nieuwe datatype allemaal "heeft" en "kan".

De meest eenvoudige vorm:

```csharp
class Auto
{
   // Hier komen straks properties (data) en methoden (gedrag)
}
```

{% hint style='danger' %}
De naam die je een klasse geeft moet voldoen aan de identifier regels uit hoofdstuk 2. Het is een sterke conventie om **klassenamen altijd met een Hoofdletter te laten beginnen** (PascalCase).
{% endhint %}

### Klassen in Visual Studio toevoegen

Hoewel je code voor een klasse eender waar kan schrijven, is er een gouden regel in C#: **Elke klasse krijgt zijn eigen bestand**.

1. Klik in **Solution Explorer** rechts op je projectnaam.
2. Kies **Add > Class...**
3. Geef het bestand de naam van je klasse (bv. `Auto.cs`).

![Sneltoets: Shift+Alt+C](../assets/6_klassen/addclass.png)

Je zal zien dat Visual Studio er `internal class Auto` van maakt. Trek je niets aan van die `internal`, dat betekent gewoon "enkel zichtbaar binnen dit project". Dat is voorlopig prima.

### Objecten maken: De `new` knop


Je kan nu objecten aanmaken van de klasse die je hebt gedefinieerd. Dit kan op alle plaatsen in je code waar je in het verleden ook al variabelen kon declareren, bijvoorbeeld in een methode of je ``Main``-methode.

Je doet dit door eerst een variabele te definiëren en vervolgens een object te **instantiëren** met behulp van het ``new`` keyword. De variabele heeft als datatype ``Auto``:

```csharp
Auto mijnEersteAuto = new Auto();
Auto mijnAndereAuto = new Auto();
```

We hebben nu **twee objecten aangemaakt van het type Auto** die we verderop zouden kunnen gebruiken.

Let goed op dat je dus op de juiste plekken dit alles doet:

* Klassen maak je aan als aparte bestanden in je project.
* Objecten creëer je in je code op de plekken waar je deze nodig hebt, bijvoorbeeld in je ``Main`` methode bij een Console-applicatie.

<!-- \newpage -->





Nu je klasse (de blauwdruk) klaar is, kan je objecten (de echte dingen) gaan maken. 

Herinner je de vergelijking met een **3D-printer**:
* De **klasse** (`Auto.cs`) is het digitale 3D-bestand. Dit doet op zichzelf niets.
* De **`new`** operator is de knop "Print". Hiermee maak je een tastbaar object in het computergeheugen.

```csharp
Auto mijnEersteAuto = new Auto();
```

Wat gebeurt hier?
1. `Auto mijnEersteAuto`: We maken een variabele die ruimte voorziet om (een verwijzing naar) een Auto te bewaren.
2. `new Auto()`: We bouwen effectief een nieuw Auto-object in het geheugen.
3. `=`: We koppelen de variabele aan dat nieuwe object.

### De valkuil van de lege doos (`null`)

Wat als we de `new` vergeten?

```csharp
Auto mijnDroomAuto; // Nog geen new gedaan!
// Console.WriteLine(mijnDroomAuto); // FOUT!
```

In tegenstelling tot een `int` (die stiekem 0 is), is een variabele van een klasse **leeg** als je er niets insteekt. In C# noemen we dit **`null`**.
Probeer je een lege doos te gebruiken? Dan krijg je de beruchte, veelvoorkomende rode tekst: `NullReferenceException`. 

Onthoud dus: **Geen object zonder new!**

>![](../assets/care.png)Het blijft ingewikkeld hoor.
>
>Zie het zo: Je kan geen huis bewonen als je enkel het bouwplan (de klasse) hebt. Je moet het eerst bouwen (`new`).
>
>En als je variabelen gewoon containers zijn? Dan is een `int` doos nooit leeg, er zit altijd minstens een 0 in. Maar een `Auto` doos? Die is standaard écht leeg (`null`) tot je er een auto in parkeert.













