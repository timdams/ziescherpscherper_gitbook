### NullReferenceException: De Meest Voorkomende Fout

Je hebt een variabele (een stukje papier in je rugzak), maar er staat **niets op geschreven**.
Geen adres. Het is, zoals we zeggen, `null`.

```csharp
Student s; // Waarde is 'null'
```

Als je nu probeert om naar dat adres te gaan (`s.Naam = ...`), crasht je programma.
C# zegt: *"Hey, je stuurt me naar een adres, maar je papiertje is leeg!"*

> **System.NullReferenceException: Object reference not set to an instance of an object.**

Dit is de manier van C# om te zeggen: "Je probeert iets te doen met `null`".

<!-- \newpage -->



### Controleren op Null

Je kan je code beschermen ("Defensive Programming") door te checken of iets null is.

#### De klassieke check (`!=`)
```csharp
if (s != null)
{
    Console.WriteLine(s.Naam);
}
```

#### De moderne check (`is not null`)
Sinds C# 9 is dit leesbaarder (leest als een zin):
```csharp
if (s is not null)
{
    Console.WriteLine(s.Naam);
}
```

#### De Elvis Operator (`?.`)
Dit is de kortste manier.
*"Als s niet null is, geef me de naam. Als s wel null is, doe niets en geef gewoon null terug."*

```csharp
string naam = s?.Naam;
```
Het vraagteken is de beveiliging. Als `s` null is, crasht het niet, maar wordt `naam` gewoon ook `null`.

<!-- \newpage -->



### Return ``null``

Uiteraard mag je ook expliciet ``null`` teruggeven als resultaat van een methode. Stel dat je een methode hebt die in een array een bepaald object moet zoeken. Wat moet de methode teruggeven als deze niet gevonden wordt? Inderdaad, we geven dan ``null`` terug.

Volgende methode zoekt in een array van studenten naar een student met een specifieke naam en geeft deze terug als resultaat. Enkel als de hele array werd doorlopen en er geen match is wordt er ``null`` teruggegeven (de werking van arrays van objecten wordt later besproken): 

```csharp
static Student ZoekStudent(Student[] array, string naam)
{
    Student gevonden = null;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i].Name == naam)
            gevonden = array[i];
    }

    return gevonden;
}
```

### DNA Mengen: Twee objecten maken één nieuw

Laten we alles samenbrengen in één krachtig voorbeeld. Tijd om het voorbeeld van de *voortplanting der mensch* er nog eens bij te nemen. Beeld je nu in dat we dichter naar de realiteit willen gaan (meestal toch het doel van OOP): we willen twee `Mens` objecten combineren om een nieuwe `Mens` (baby) te maken. De baby krijgt vervolgens de eigenschappen van beide ouders.

```csharp
internal class Mens
{
    public string Naam { get; set; }
    public int Intelligentie { get; set; }
    
    // Methode die een ANDER object als parameter neemt
    public Mens MaakBaby(Mens partner, string naamBaby)
    {
        // 1. Check op null!
        if (partner is null)
        {
            Console.WriteLine("Je hebt een partner nodig!");
            return null; // Of gooi een Exception
        }

        // 2. Maak nieuw object (in de Heap)
        Mens baby = new Mens();
        baby.Naam = naamBaby;

        // 3. DNA Mengen: Gemiddelde intelligentie van 'this' en 'partner'
        baby.Intelligentie = (this.Intelligentie + partner.Intelligentie) / 2;

        // 4. Geef sleutel terug
        return baby;
    }
}
```

Het gebruik:

```csharp
Mens alice = new Mens { Naam = "Alice", Intelligentie = 100 };
Mens bob = new Mens { Naam = "Bob", Intelligentie = 80 };

Mens charlie = alice.MaakBaby(bob, "Charlie");
// Charlie heeft intelligentie 90
```

>![](../assets/care.png) **Conclusie van hoofdstuk 9**
>
>Dit was een technische deep-dive. Maar essentieel.
>Je snapt nu dat variabelen slechts verwijzingen zijn. 
>Dat `null` betekent dat de verwijzing ontbreekt.
>En dat methoden objecten kunnen manipuleren, aanmaken en teruggeven.
>
>Dit is de ware kracht van OOP: Objecten die met elkaar interageren om complexe systemen te bouwen. Op naar het volgende hoofdstuk!
