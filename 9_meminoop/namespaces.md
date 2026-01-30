## Namespaces en `using`

Je zal het keyword `namespace` al vaak bovenaan bestanden hebben zien staan.
Maar wist je dat dit eigenlijk de "achternaam" van je klasse is?

### Het probleem: Naamconflicten

Stel, je maakt een game met een `Monster` klasse.
Je downloadt een bibliotheek van iemand anders, en die heeft óók een `Monster` klasse.
Als je nu `new Monster()` typt... welke bedoel je dan?

Namespaces lossen dit op door klassen te groeperen.

* Jouw monster heet volledig: `MijnGame.Monster`
* Het andere monster heet: `AndereBibliotheek.Monster`

Het is als **Jan**. Er zijn veel Jannen. Maar er is maar één **Jan Peeters**.

### Hoe maak je een namespace?

Eenvoudig: je zet het helemaal bovenaan je bestand.

**De moderne manier (File-Scoped Namespace):**
```csharp
namespace MijnGame; // Let op de puntkomma!

class Monster 
{
    // ...
}
```

**De oude manier (Block-Scoped Namespace):**
Vroeger moest je accolades gebruiken, waardoor al je code insprong. Je ziet dit nog in oudere code.
```csharp
namespace MijnGame
{
    class Monster 
    {
        // Alles moest inspringen... irritant!
    }
}
```

### Het `using` keyword

Niemand heeft natuurlijk zin om telkens de volledige naam te typen als er geen verwarring mogelijk is:
```csharp
MijnGame.Database.Models.Speler s = new MijnGame.Database.Models.Speler(); // Pff...
```

Met `using` zeg je tegen C#: *"Als ik 'Speler' typ, bedoel ik die uit 'MijnGame.Database.Models'".*

```csharp
using MijnGame.Database.Models;

//Verderop 
Speler s = new Speler(); // Veel beter!
```

### Waar zijn mijn `using`s heen?

Misschien valt het je op dat je in moderne .NET projecten vaak geen `using System;` meer moet typen om bijvoorbeeld `Console.WriteLine` te kunnen gebruiken.
De klasse `Console` zit nochtans in de `System` namespace, waardoor je voluit eigenlijk `System.Console.WriteLine` zou moeten schrijven. Vroeger moest je daarom altijd manueel `using System;` toevoegen bovenaan je bestand.

Dat dit nu niet meer hoeft, komt door **Implicit Usings**.

In je projectbestand (`.csproj`) staat vaak dit aan:
`<ImplicitUsings>enable</ImplicitUsings>`

Dit zorgt ervoor dat de meest gebruikte namespaces (zoals `System`, `System.Linq`, `System.Collections.Generic`) automatisch voor jou worden geïmporteerd in **elk bestand**.
C# helpt je dus om minder boilerplate code te schrijven.

{% hint style='info' %}
Namespaces zijn dus nog steeds **super relevant** (elke klasse heeft er een!), maar je hoeft er gelukkig steeds minder code voor te schrijven.
{% endhint %}



