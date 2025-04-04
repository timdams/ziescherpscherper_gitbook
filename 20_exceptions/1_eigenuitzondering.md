## Zelf exceptions maken

We zijn ondertussen al gewend aan het opvangen van uitzonderingen met behulp van ``try`` en ``catch``. Ook bij exception handling wordt overerving toegepast. De uitzonderingen die we opvangen zijn steeds objecten van het type ``Exception`` of van een afgeleide klasse. Denk maar aan de ``NullReferenceException`` klasse die werd overgeërfd van ``Exception``. 

{% hint style='tip' %}
Dat wil zeggen dat ``Exception``s ook maar "gewone klassen" zijn en dus ook aan alle andere regels binnen C# moeten voldoen. Zo ondersteunen ze polymorfisme (*sooooon!*), kan je ze in arrays plaatsen, enz.
{% endhint %}


Bijgevolg is het logisch dat je in je code **uitzonderingen zelf kunt maken en opwerpen**. Vervolgens kan je deze elders opvangen. 

Een voorbeeld van een bestaand ``Exception`` type gebruiken. We gaan zelf een ``Exception`` object aanmaken (met ``new``) en dit vervolgens opwerpen wanneer we een uitzondering opmerken.  In dit geval wanneer ``getal`` de waarde ``0`` heeft: 

```csharp
static int ResultaatBerekening(int getal)
{
    if (getal != 0)
        return 100 / getal;
    else
        throw new DivideByZeroException("BOEM. ZWART GAT!");
}
 
 
static void Main(string[] args)
{
    try
    {
        Console.WriteLine(ResultaatBerekening(0));
    }
    catch(DivideByZeroException e)
    {
        Console.WriteLine(e.Message);
    }
}
```

De uitvoer zal zijn:


```text
BOEM. ZWART GAT!
```


De lijn ``throw new DivideByZeroException("BOEM. ZWART GAT!");`` zorgt er dus voor dat we een eigen foutboodschap verpakken en opwerpen.

### Een eigen exception ontwerpen

Je kan ook eigen klassen overerven van ``Exception`` zodat je eigen uitzonderingen kan maken. Je maakt hiervoor gewoon een nieuwe klasse aan die je laat overerven van de Exception-klasse. Een voorbeeld:

```csharp
internal class Timception: Exception
{
    public override string ToString()
    {
        string extrainfo = "Exception Generated by Tim Dams:\n";
        return $"{extrainfo}. {base.ToString()}";
    }
}
```

{% hint style='tip' %}
Merk op dat we hier met ``base.ToString()`` ervoor zorgen dat ook de foutboodschap van het parent-gedeelte van de uitzondering wordt weergegeven. 
{% endhint %}


Om deze exception nu zelf op te werpen gebruiken we het keyword **``throw``** gevolgd door een object van het type uitzondering dat je wenst op te werpen. 

In volgende voorbeeld gooien we onze eigen exception op een bepaald punt in de code op en vangen deze dan op:

```csharp
static void Main(string[] args)
{
    try
    {
        TimsMethode();
    }
 
    catch (Timception e)
    {
       Console.WriteLine(e.ToString());
    }     
}
static public void TimsMethode()
{
    //doe dingen
    //...
    //"when suddenly: a wild exception appears"
    throw new Timception();
}
```




