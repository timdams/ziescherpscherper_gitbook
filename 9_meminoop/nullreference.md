## Object referenties en null

Zoals nu duidelijk is bevatten referentievariabelen steeds een referentie naar een object. Maar wat als we dit schrijven:

```csharp
Student stud1;
stud1.Naam = "Marc Jansens";
```

Dit zal een fout geven. Het object ``stud1`` bevat namelijk nog geen referentie. Maar wat dan wel?

Deze variabele bevat de waarde **``null``** . Net zoals bij value types die een default waarde hebben  als je er geen geeft (bv. 0 bij een ``int`` ), **zo bevatten reference type variabelen altijd ``null`` als standaardwaarde**. 

``null`` is een waarde die je  kan toekenen aan eender welk reference type. Je doet dit om aan te geven dat er nog geen referentie naar een effectief object in de variabele staat. Je kan dus ook op deze waarde testen. 

Van zodra je een referentie naar een object (een bestaand of eentje dat je net met ``new`` hebt aangemaakt) aan een reference type variabele toewijst (met de ``=`` operator) zal de ``null`` waarde uiteraard overschreven worden.

{% hint style='tip' %}
Merk op dat de GC enkel op de heap werkt. Indien er in de stack dus een variabele de waarde ``null`` heeft zal de GC deze nooit verwijderen!
{% endhint %}


### NullReferenceException

Een veel voorkomende foutboodschap tijdens de uitvoer van je applicatie is een ``NullReferenceException``. Deze zal optreden wanneer je code een object probeert te benaderen wiens waarde ``null`` is (een onbestaand object met andere woorden).

Laten we dit eens simuleren:

```csharp
Student stud1 = null;
Console.WriteLine(stud1.Name);
```

Dit zal resulteren in een foutboodschap in VS bij de lijn die de uitzondering detecteert: "System.NullReferenceException: 'Object reference not set to an instance of an object'. stud1 was null".


{% hint style='tip' %}
We moeten in dit voorbeeld expliciet ``= null`` plaatsen daar Visual Studio slim genoeg is om je te waarschuwen voor eenvoudige potentiële NullReference fouten en je code anders niet zal compileren.
{% endhint %}

<!-- \newpage -->



### NullReferenceException voorkomen

Objecten die niet bestaan zullen altijd ``null`` hebben. Uiteraard kan je niet altijd al je code uitvlooien waar je misschien vergeten bent een object met ``new`` aan te te maken.

Voorts kan het ook soms *by design* zijn dat een object voorlopig ``null`` is.

Gelukkig kan je controleren of een object ``null`` is als volgt:

```csharp
if(stud1 == null)
    Console.WriteLine("Oei. Object bestaat niet.")
```

#### Verkorte null controle notatie

Vaak moet je dit soort code schrijven:

```csharp
if(stud1 != null)
{
    Console.WriteLine(stud1.Name)
}
```

Op die manier voorkom je een ``NullReferenceException``. Het is uiteraard omslachtig om steeds die check te doen. Je mag daarom ook schrijven:


```csharp
Console.WriteLine(stud1?.Name)
```

Het vraagteken direct na het object geeft aan: *"Gelieve de code na dit vraagteken enkel uit te voeren indien het object voor het vraagteken niét null is".*

Bovenstaande code zal dus gewoon een lege lijn op scherm plaatsen indien ``stud1`` effectief ``null`` is, anders komt de naam op het scherm.

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

### Bevallen in code met ouders

Tijd om het voorbeeld van de *voortplanting der mensch* er nog eens bij te nemen. Beeld je nu in dat we dichter naar de realiteit willen gaan (meestal toch het doel van OOP) en de baby eigenschappen van beide willen ouders geven. Stel dat mensen een maximum lengte hebben die ze genetisch kunnen halen, aangeduid via een auto-property ``MaxLengte``. De maximale lengte van een baby is steeds de lengte van de grootste ouder (in de echte genetica is dat natuurlijk niet). 

De klasse ``Mens`` breiden we uit naar:

```csharp
internal class Mens
{
    public int MaxLengte {get; set;}
    
    public Mens PlantVoort(Mens dePapa)
    {
        Mens baby = new Mens();
        baby.MaxLengte = MaxLengte;
        if(dePapa.MaxLengte >= MaxLengte)
            baby.MaxLengte = papa.MaxLengte;
        return baby;
    }
}
```

Mooi toch?!  

<!-- \newpage -->


Om het nu volledig te maken zullen we er voor zorgen dat enkel een vrouw kan voortplanten. Voorts kan ze zich enkel voortplanten met behulp van een van een man (merk op dat OOP als doel heeft de realiteit te benaderen, maar ook te vereenvoudigen naargelang het probleem).  

Veronderstel dat het geslacht via een enumtype (``enum Geslachten {Man, Vrouw}``) in een auto-property ``Geslacht`` wordt bewaard.  We voegen daarom bovenaan in de ``PlantVoort``-methode nog een kleine check in én return'n een leeg (``null``) object als de voortplanting faalt (we zouden ook een ``Exception`` kunnen opwerpen):

```csharp
    public Mens PlantVoort(Mens dePapa)
    {
        if(Geslacht == Geslachten.Vrouw 
                && dePapa.Geslacht == Geslachten.Man)
        {
            Mens baby = new Mens();
            baby.MaxLengte = MaxLengte;
            if(dePapa.MaxLengte >= MaxLengte)
                baby.MaxLengte = papa.MaxLengte;
            return baby;
        }
        return null;
    }
```

Volgende code produceert nu een kersverse baby:

```csharp
Mens mama = new Mens();
mama.Geslacht = Geslachten.Vrouw;
mama.MaxLengte = 180;
Mens papa = new Mens();
papa.Geslacht = Geslachten.Man;
papa.MaxLengte = 169;

Mens baby = mama.PlantVoort(papa);
```


{% hint style='tip' %}
Hopelijk voel je bij dit voorbeeld hetzelfde enthousiasme als toen we Pong naar OOP omzetten. Probeer voorgaande voorbeeld eens te schrijven met je kennis VOOR je klassen en objecten kende? Doenbaar? Zeker. Veel werk? Dat nog meer. En daar is het ons om te doen: krachtige, makkelijker te onderhouden code leren schrijven!
{% endhint %}
