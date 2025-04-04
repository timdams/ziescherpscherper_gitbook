## Objecten en methoden

### Objecten als actuele parameters

Klassen zijn "gewoon" nieuwe datatypes. Alle regels die we dus al kenden in verband met het doorgeven van variabelen als parameters in een methoden blijven gelden voor de meeste klassen (behalve ``static`` klassen die we in volgend hoofdstuk zullen aanpakken).

**Het enige verschil is dat we objecten by reference meegeven aan methoden**. Aanpassingen aan het object in de methode zal dus betekenen dat je het originele object aanpast dat aan de methode werd meegegeven, net zoals we bij arrays zagen. Hier moet je dus zeker rekening mee houden. 

Stel dat we volgende klasse hebben waarin we temperatuurmetingen willen opslaan, alsook wie de meting heeft gedaan:

```csharp
internal class Meting
{
    public int Temperatuur { get; set; }
    public string OpgemetenDoor { get; set; }
}
```

We voegen vervolgens een methode aan de klasse toe die ons toelaat om deze meting op het scherm te tonen in een bepaalde kleur. 

```csharp
public void ToonMetingInKleur (ConsoleColor kleur)
{
    Console.ForegroundColor = kleur;
    Console.WriteLine($"{Temperatuur} graden C gemeten door: {OpgemetenDoor}");
    Console.ResetColor();
}
```

Het gebruik van deze klasse zou er als volgt kunnen uitzien:

```csharp
Meting m1 = new Meting();
m1.Temperatuur = 26; 
m1.OpgemetenDoor = "Lieven Scheire";
Meting m2 = new Meting();
m2.Temperatuur = 34; 
m2.OpgemetenDoor = "Ann Dooms";

m1.ToonMetingInKleur(ConsoleColor.Red);
m2.ToonMetingInKleur(ConsoleColor.Pink);
```

<!-- \newpage -->


### Objecten in methoden aanpassen

Je kan ook methoden schrijven die meegegeven objecten aanpassen daar we deze **by reference** doorsturen. Een voorbeeld waarin een meting als parameter meegeven en toevoegen aan een andere meting, waarna we de originele meting "resetten":

```csharp
public void VoegMetingToeEnVerwijder(Meting inMeting)
{
    Temperatuur += inMeting.Temperatuur;
    inMeting.Temperatuur = 0;
    inMeting.OpgemetenDoor =  "";
}
```

We zouden deze methode als volgt kunnen gebruiken (ervan uitgaande dat we 2 objecten ``m1`` en ``m2`` van het type ``Meting`` hebben):

```csharp
m1.Temperatuur = 26; 
m1.OpgemetenDoor = "Lieven Scheire";
m2.Temperatuur = 5; 
m2.OpgemetenDoor = "Lieven Scheire";
m1.VoegMetingToeEnVerwijder(m2);
Console.WriteLine($"{m1.Temperatuur} en {m2.Temperatuur});
```

Dit zal resulteren in volgende output:


```text
31 en 0
```


### Objecten als resultaat

Weer hetzelfde verhaal: ook klassen mogen het resultaat van een methoden zijn. Stel dat we een nieuw meting object willen maken dat de dubbele temperatuur bevat van het object waarop de methode wordt aangeroepen:

```csharp
public Meting GenereerRandomMeting()
{
    Meting result = new Meting();
    result.Temperatuur = Temperatuur * 2;
    result.OpgemetenDoor = $"{OpgemetenDoor} Junior";
    return result;
}
```



Deze methode kan je dan als volgt gebruiken:

```csharp
m1.Temperatuur = 26; 
m1.OpgemetenDoor = "Lieven Scheire";
Meting m3 = m1.GenereerRandomMeting();
```

Het object ``m3`` zal een temperatuur van ``52`` bevatten en zijn opgemeten door ``Lieven Scheire Junior``.

### Bevallen in code

In voorgaande voorbeeld zagen we reeds dat objecten dus objecten van het eigen type kunnen teruggeven. Laten we dat voorbeeld eens doortrekken naar hoe de bevalling van een kind in C# zou gebeuren.

Baby's zijn kleine mensjes. Het is dan ook logisch dat mensen een methode ``PlantVoort`` hebben (we houden geen rekening met het geslacht). Volgende klasse ``Mens`` is dus perfect mogelijk:

```csharp
class Mens
{
    public Mens PlantVoort()
    {
        return new Mens();
    }
}
```

Vervolgens kunnen we het volgende doen:

```csharp
Mens oermoeder = new Mens();
Mens dochter;
Mens kleindochter;
dochter =  oermoeder.PlantVoort();
kleindochter = dochter.PlantVoort();
```

Het is een interessante oefening om deze code eens uit te tekenen in de stack en heap inclusief de verschillende referenties. 

{% hint style='tip' %}
Ik ga voorgaande code over enkele pagina's nog uitbreiden om een meer realistisch *voortplantingsscenario* te hebben (sommige zinnen verwacht je nooit te zullen schrijven in je leven... *I was wrong*).
{% endhint %}

