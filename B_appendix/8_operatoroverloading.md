## Operator overloading

Stel, je hebt volgende klasse:

```csharp
internal class Kassa
{
    public int Totaal {get;set;}
    public int Bouwjaar {get;set;}
}
```

Je maakt even later twee kassa's aan met de nodige informatie:

```csharp
Kassa benedenKassa = new Kassa(){Totaal = 50, Bouwjaar = 1981};
Kassa bovenKassa = new Kassa(){Totaal = 40, Bouwjaar = 2000};
```

Even later wordt besloten dat beide kassa's moeten samengevoegd worden tot een gloednieuwe kassa voor beide verdiepingen samen. Bedoeling is dat het totale geld in beide kassa's opgeteld in de nieuwe kassa moet gezet worden. Het bouwjaar van de nieuwe kassa moet het bouwjaar van de oudste van de 2 originele kassa's zijn.
Je zou willen schrijven:


```csharp
Kassa nieuw = benedenKassa + bovenKassa;
```

Uiteraard heeft C# geen flauw benul hoe de **+ operator** moet toegepast worden op objecten van klassen die je zelf geschreven hebt.

### Operator overloading to the rescue

Je kan in een klasse bestaande operators (``+``,``-``,``*``, enz.) **overloaden**.  Dit betekent dat je aan C# vertelt hoe een operator moet werken voor objecten van die klasse.

Stel dat je de + wilt overloaden in je klasse dan voeg je volgende methode toe:

```csharp
internal class Kassa
{
    public int Totaal {get;set;}
    public int Bouwjaar {get;set;}

    public static Kassa operator+ (Kassa a, Kassa b)
    {
        //Zie verder
    }
}
```




Laten we deze syntax even bekijken:

* Operator overloading methoden zijn altijd ``static``.
* Het returntype is idealiter het type van de klasse zelf (logisch: twee kassa's optellen geeft een nieuwe kassa).
* ``operator+`` geeft aan welke operator je wenst te overloaden. Zie verderop met een link naar alle operators die je kan overloaden.
* Als je een operator hebt die twee operanden gebruikt (zoals de +), dan heeft de methode ook twee parameters nodig van hetzelfde type als de klasse. Dit zijn de twee elementen (operanden) die je wilt optellen met de operator.

Bekijk zeker eens de officiële documentatie[^opdoc] om te zien welke operators je allemaal kan overloaden. Tip: het zijn er veel!

[^opdoc]: Zie [docs.microsoft.com/dotnet/csharp/programming-guide/statements-expressions-operators/overloadable-operators](https://docs.microsoft.com/dotnet/csharp/programming-guide/statements-expressions-operators/overloadable-operators)

### De operator beschrijven

Vervolgens moeten we nu beschrijven hoe de operator moet werken. Finaal zal de methode een nieuw object moeten teruggeven waarin het resultaat van de operatie zit.

In het voorbeeld dat we maken, willen we dus het volgende:

```csharp
public static Kassa operator+ (Kassa a, Kassa b)
{
    Kassa resultaat = new Kassa()
        {
            Totaal = a.Totaal+b.Totaal,
            Bouwjaar = a.Bouwjaar
        };

    if(a.Bouwjaar <  b.Bouwjaar)
    {
        resultaat.Bouwjaar = b.Bouwjaar;
    }
    return resultaat;
}
```

Zoals je ziet maken we een nieuw object ``resultaat`` waarin we de som van de twee meegegeven kassa's hun totalen plaatsen, alsook het bouwjaar van de oudste van de 2 kassa's.
