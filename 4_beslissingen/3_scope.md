## Scope van variabelen

De locatie waar je een variabele aanmaakt bepaalt de **scope** van de variabele. Binnen deze scope zal een variabele gebruikt kunnen worden door andere code. Je kan de scope vergelijken als verschillende kamers in een gebouw. Variabelen die zij aangemaakt in een kamer zijn enkel in die kamer bruikbaar.

Eenvoudig gezegd zullen steeds de **omliggende accolades de scope van de variabele bepalen**. Indien je de variabele dus buiten die accolades nodig hebt dan heb je een probleem: de variabele is enkel bereikbaar binnen de accolades vanaf het punt in de code waarin het werd gedeclareerd.

Zeker wanneer je begint met ``if``, loops, methoden, enz. zal de scope belangrijk zijn: deze code-constructies gebruiken steeds accolades om codeblocks aan te tonen. Een variabele die je dus binnen een if-blok aanmaakt zal enkel binnen dit blok bestaan, niet erbuiten.

Volgende voorbeeld toont bijvoorbeeld de scope van de variabele ``getal``:

```csharp
if( iLoveCSharp == true)
{
    Console.WriteLine("Hoeveel punten op 10 geef je C#?"):
    int getal ; //Start scope getal
    getal = int.Parse(Console.ReadLine());
} // einde scope getal

Console.WriteLine(getal); // FOUT! getal niet in deze scope
```

De variabele ``getal`` wordt aangemaakt  tussen de accolades van de ``if`` en "verdwijnt" dus van zodra we die *kamer* verlaten (laatste accolade).

Wil je dus ``getal`` ook nog buiten de ``if`` gebruiken zal je je code moeten herschrijven zodat ``getal`` VOOR de ``if`` wordt aangemaakt. Nu is de scope van variabele groter: daar we steeds naar de *omliggende* accolades moeten kijken. In dit geval bepalen dus de accolades op lijn 1 en 9 de scope:

```csharp
{
    int getal = 0 ; //Start scope getal
    if( iLoveCSharp == true)
    {
        Console.WriteLine("Hoeveel punten op 10 geef je C#?"):
         getal = int.Parse(Console.ReadLine());
    } 
    Console.WriteLine(getal); 
} // einde scope getal
```

De buitenste accolades zetten we er even om de scope te benadrukken (maar hoeven dus niet). 

{% hint style='tip' %}
Merk op dat indien je aan nesting doet, de scope doorheen de *inner* geneste codeblocken doorloopt en pas eindigt bij de accolade van het block waarbinnen de variabele werd gedeclareerd.
{% endhint %}



### Variabelen met zelfde naam
Zolang je in de scope van een variabele bent, kan je geen nieuwe variabele met dezelfde naam aanmaken:

Volgende code is dus niet toegestaan:

```csharp
int getal = 0;
{
    int getal = 5; //Deze lijn is niet toegestaan
}
```

Je krijgt de foutboodschap: "A local variable named 'getal' cannot be declared in this scope because it would give a different meaning to 'getal', which is already used in a 'parent or current' scope to denote something else." 

Enkel de tweede variabele een andere naam geven is toegestaan in het voorgaande geval.

In volgende voorbeeld is dit dus wel geldig, daar de scope van de eerste variabele afgesloten wordt door de accolades:

```csharp
{
    int getal = 0 ;
    //....
}
//Verder in code
{
    int getal = 5;
}
```
