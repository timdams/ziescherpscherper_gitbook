

# Appendix 3 : OOP Quest 

Nu we gezien hebben wat we nodig hebben om een spel te maken, zullen we de voorgaande oefening deels opnieuw maken, maar deze keer met de kracht van klassen en objecten! We noemen het spel dan ook:

![](../assets/oopquesttitel.png)


## Main
We willen de ``Main()`` methode van Program.cs zo leeg mogelijk laten. Daarom zullen we de meeste functionaliteit verpakken in een klasse SpelManager. Het enige dat we dan nog hoeven te doen in onze main is een loop starten die steeds 3 zaken zal doen:

1. Huidige locatie beschrijven.
2. Aan gebruiker tonen welke acties hij kan uitvoeren.
3. Gewenste actie van gebruiker verwerken en uitvoeren.

In code behelst dit:

```csharp
static void Main(string[] args)
{
    Console.WriteLine("Welkom bij OOP Quest. Een avontuur voor moedige en minder moedige programmeurs. Ben je er klaar voor?");
 
    SpelManager oopquest= new SpelManager();
 
    //Start gameloop
    while(!oopquest.Exit)
    {
        //Beschrijf kamer
        oopquest.BeschrijfLocatie();
        //Toon acties
        oopquest.ToonActies();
        //Lees actie uit
        oopquest.VerwerkActie();
 
    }
}
```
Een ``bool`` property ``Exit``  binnen het ``SpelManager`` object zal ons toelaten om de loop te stoppen wanneer het spel wordt beëindigd.

## SpelObject

Doorheen de verschillende locaties zullen elementen te vinden zijn. We beschrijven deze als ``SpelObject``:

```csharp
class SpelObject
{
    public string Naam { get; set; }
    public string Beschrijving { get; set; }
 
    public virtual void Beschrijf()
    {
        Console.WriteLine($"{Naam}:{Beschrijving}.");
    }
}
```

## Locatie

De gebruiker kan van locatie naar locatie gaan. Een locatie bestaat uit een aantal zaken:

* Een beschrijving en titel.
* Een lijst van SpelObjecten (items) die zich op deze locatie bevinden.
* Een lijst van Uitgangen, namelijk de richtingen waar de gebruiker naar toe kan gaan die aansluiten op een andere locatie.
* Een eerste versie van onze locatie klasse is dan:

```csharp
class Locatie: SpelObject
{
    public Locatie()
    {
        Uitgangen = new List<Exit>();
        AanwezigeObjecten= new List<SpelObjects>();
    }


    public List<Exit> Uitgangen { get; set; }
    public List<SpelObjects> AanwezigeObjecten { get; set; }
 
    public override void Beschrijf()
    {
        base.Beschrijf();
        Console.WriteLine("Voorts zie je ook nog:");
        foreach (var objects in AanwezigeObjecten)
        {
            objects.Beschrijf();
        }
        Console.WriteLine("\n*********");
    }
 
    //...
}
```


## Exit
Iedere exit in een locatie definieert minstens 2 zaken:

* De richting waar deze uitgang zich bevindt (Noord, Oost,Zuid, West).
* Een referentie naar het locatie-object waar deze uitgang toegang tot verschaft.

We krijgen dus al:

```csharp
class Exit
{
    public Exit()
    {
        BenodigdObject= new List<SpelObjects>();
    }
    public richtings UitgangRichting { get; set; }
    public Locatie GaatNaarLocatie { get; set; }

    public List<SpelObjects> BenodigdObject { get; set; }
 
    //...
}
```
Waarbij ``Richtingen`` een eigen gemaakt enum-type is:

```csharp
enum Richtingen
{
    Noord, Zuid, West, Oost
}
```

## Van locatie veranderen
Binnen de locatie klasse voegen we een methode toe die de SpelManager kan gebruiken om te weten te komen naar welke locatie de gebruiker gaat. De methode aanvaardt een ``richting`` (i.e. de richting waarin de gebruiker wenst te gaan) en zal een referentie naar het Locatie-object teruggeven waarnaar de gebruiker zal bewegen. Indien de richting waarin hij wenst te bewegen niet geldig is dan tonen we dit op het scherm:

```csharp
public Locatie KrijgLocatieNaBewegen(Richtingen richting)
{
    foreach (var exit in Uitgangen)
    {
        if (exit.UitgangRichting == richting)
        {
 
            return exit.GaatNaarLocatie;
        }
    }
    Console.WriteLine("Dat is geen geldige richting");
    return this;
 
}
```
Wanneer dus een exit wordt gevonden in de Uitgangen lijst die voldoet aan de meegegeven ``richting`` dan geven we een referentie terug naar de bijhorende locatie (``GaatNaarLocatie``). Wordt er geen exit gevonden en bereiken we dus het einde van de foreach lus dan verschijnt de tekst op het scherm en geven we een referentie terug naar de huidige locatie.

## SpelObjects als vereisten om exit te gebruiken

Stel nu dat we soms willen dat een bepaalde locatie pas bereikt kan worden indien de gebruiker reeds een bepaald ``SpelObject`` in zijn bezit heeft. Hiervoor moeten we 2 zaken aanpassen:

* We beschrijven in de ``Exit`` klasse welk object(en) nodig zijn om deze exit te mogen gebruiken.
* We controleren of de speler het ``SpelObject`` heeft wanneer deze naar een nieuwe locatie wil gaan mbv de ``KrijgLocatieNaBewegen()`` methode.

De nieuwe, volledige ``Exit`` klasse wordt dan:

```csharp
class Exit
{
    public Exit()
    {
        BenodigdObject = new List<SpelObjects>();
    }
    public Richtingen UitgangRichting { get; set; }
    public Locatie GaatNaarLocatie { get; set; }
 
    public List<SpelObjects> BenodigdObject { get; set; }
 
    public bool ControleerMagPasseren(List<SpelObjects> spelerInventaris)
    {
        int passCount = 0;
        for (int i = 0; i < BenodigdObject.Count; i++)
        {
            if (spelerInventaris.Contains(BenodigdObject[i]))
                passCount++;
        }
 
        return passCount == BenodigdObject.Count ;
    }
}
```
In deze ietwat knullige code tellen we dus of de speler alle SpelObjecten in z’n inventory heeft (``spelerInventaris``) nodig om deze exit te gebruiken.




Deze methode ``ControleerMagPasseren`` gebruiken we nu in de ``KrijgLocatieNaBewegen()``-methode in de Locatie klasse om te bepalen of de exit mag gebruikt worden. De methode wordt dan:

```csharp
public Locatie KrijgLocatieNaBewegen(Richtingen richting, List<SpelObjects> spelerInventaris )
{
    foreach (var exit in Uitgangen)
    {
        if (exit.UitgangRichting == richting)
        {
            if(exit.ControleerMagPasseren(spelerInventaris))
                return exit.GaatNaarLocatie;
            else
            {
                Console.WriteLine("Je kan hier niet langs (je hebt niet alle vereiste items).");
                return this;
            }
        }
    }
    Console.WriteLine("Dat is geen geldige richting");
    return this;
 
}
```

## SpelManager
Rest ons nu enkel nog  de ``SpelManager`` klasse te maken. Ruw gezien is deze als volgt:


```csharp
class SpelManager
{
 
    public SpelManager()
    {
        InitialiseerSpel();
    }
    private  Locatie huidigeLocatie = null;
    public bool Exit { get; set; }
 
    public void BeschrijfLocatie()
    {
        //...
    }
 
    public  void VerwerkActie()
    {
        //...
    }
 
    public  void ToonActies()
    {
        //...
    }
 
    private  List<Locatie> SpelLocatie = new List<Locatie>();
    private List<SpelObjects> Objecten = new List<SpelObjects>();
    private List<SpelObjects>  spelerInventaris= new List<SpelObjects>();
    private  void InitialiseerSpel()
    {
        //...
    }
}
```




Wat ogenblikkelijk opvalt zijn:

* De 3 publieke methoden ``BeschrijfLocatie``,``VerwerkActie`` en ``ToonActies``
* Een instantievariabelen ``huidigeLocatie`` die een referentie bijhoudt naar de huidige locatie van de speler
* 3 lijsten met daarin de objecten die de speler heeft (``spelerInventaris``), alle objecten in het spel (``Objecten``) en alle locaties in het spel (``SpelLocatie``)
* Een ``InitialiseerSpel()`` methode waarin we alle Objecten, Uitgangen en locaties zullen aanmaken bij aanvang van het spel
* Een bool ``Exit`` zodat de externe gameloop weet wanneer het spel gedaan is

We zullen nu de afzonderlijke methoden invullen:

### BeschrijfLocatie()
```csharp
public void BeschrijfLocatie()
{
    this.huidigeLocatie.Beschrijf();
}
```

### VerwerkActie()

```csharp
string actie = Console.ReadLine();
bool error = false;
if (actie == "n")
    huidigeLocatie = huidigeLocatie.KrijgLocatieNaBewegen(Richtingen.Noord, spelerInventaris);
else if (actie == "o")
    huidigeLocatie = huidigeLocatie.KrijgLocatieNaBewegen(Richtingen.Oost, spelerInventaris);
else if (actie == "w")
    huidigeLocatie = huidigeLocatie.KrijgLocatieNaBewegen(Richtingen.West, spelerInventaris);
else if (actie == "z")
    huidigeLocatie = huidigeLocatie.KrijgLocatieNaBewegen(Richtingen.Zuid, spelerInventaris);
else if (actie == "e")
    Exit = true;
else
{
    error = true;
}
Console.Clear();
if(error)
    Console.WriteLine("Onbekende actie");

```
We laten de speler dus toe door ``n,o,w,z`` in te typen dat gecontroleerd wordt naar welke nieuwe locatie zal gegaan worden. We passen hierbij de ``huidigeLocatie`` property van de SpelManager aan naar de, al dan niet nieuwe, locatie.

### ToonActies()
```csharp
public  void ToonActies()
{
    Console.WriteLine("Mogelijke acties: (typ bijvoorbeeld n indien u naar het noorden wil)");
    Console.WriteLine("n= noord");
    Console.WriteLine("o= oost");
    Console.WriteLine("z= zuid");
    Console.WriteLine("w= west");
 
    Console.WriteLine("e=exit");
 
}
```

### InitialiseerSpel()
In deze methode definiëren nu de volledige spelinhoud. Wil je dus bijvoorbeeld dit spel uitbreiden met extra kamers en objecten, dan doe je dat in deze methode. Ter illustratie tonen we eerst hoe we 2 locaties aanmaken en deze aan elkaar hangen mbv de Uitgangen (waarbij kamer één zich ten zuiden van kamer 2 bevindt)

```csharp
private  void InitialiseerSpel()
{
    //Maak Locaties
    Locatie l1 = new Locatie()
    {
       Title = "De poort",
       Beschrijving = "Je staat voor een grote grijze poort die op een kier staat. Rondom je is prikkeldraad, je kan enkel naar het noorden, door de poort gaan. "
    };
 
    Locatie l2 = new Locatie()
    {
       Title = "Receptie",
       Beschrijving = "De receptie....veel blijft er niet meer over van wat eens een bruisende omgeving was. Hier en daar zie je skeletten van , waarschijnlijk, enkele studenten. Een grote poort staat op een kier naar het zuiden. Je ziet twee deuren aan de westelijke en noordelijke zijde."
    };
 
    //Place Uitgangen
    l1.Uitgangen.Add(new Exit() { UitgangRichting = richtings.Noord, GaatNaarLocatie = l2 });
 
    l2.Uitgangen.Add(new Exit() { UitgangRichting = richtings.Zuid, GaatNaarLocatie = l1 });
 
    //Voeg locatie toe
    SpelLocatie.Add(l1);
    SpelLocatie.Add(l2);
 
    huidigeLocatie = l1;
}
```

Vergeet niet op het einde de 2 kamers toe te voegen aan de ``SpelLocatie`` lijst van de SpelManager, alsook in te stellen wat de beginkamer is.

## GameInit met SpelObject als conditie om kamer in te kunnen
Stel dat we even later in een kamer een sleutel plaatsen die als conditie dient om een andere kamer te kunnen openen. We schrijven dan in de ``GameInit()`` methode:


```csharp
    Locatie l6 = new Locatie()
    {
        Title = "Gang",
        Beschrijving = "Een brede gang waar makkelijk 5 mensen schouder aan schouder door kunnen. Zowel in het oosten als het westen zie je een deur."
    };
 
    Locatie l7 = new Locatie()
    {
        Title = "Computerruimte",
        Beschrijving = "Eindelijk; je hebt het gehaald. De plek waar iedereen naar toe wil: het computerlabo!"
    };
 
    //Place objects in rooms
    SpelObjects keytol7 = new SpelObjects() { Beschrijving = "Verroest en groot", Naam = "Sleutel" };
    l5.AanwezigeObjecten.Add(keytol7);
    //...
 
    l6.Uitgangen.Add(new Exit() { UitgangRichting = richtings.West, GaatNaarLocatie = l4 , BenodigdObject= new List<SpelObjects>(){keytol7}});
    l6.Uitgangen.Add(new Exit() { UitgangRichting = richtings.Oost, GaatNaarLocatie = l7 });
 
    //Voeg locatie toe
    //..
    SpelLocatie.Add(l6);
    SpelLocatie.Add(l7);
```

## Een volledige GameInit ter illustratie
We hebben nu de belangrijkste onderdelen geschreven. We tonen daarom een iets uitgebreider spel (demo zeg maar) waarin we alles gecombineerd in actie zien:


```csharp
private  void InitialiseerSpel()
{
    //Maak Locaties
    Locatie l1 = new Locatie()
    {
        Title = "De poort",
        Beschrijving = "Je staat voor een grote grijze poort die op een kier staat. Rondom je is prikkeldraad, je kan enkel naar het noorden, door de poort gaan. "
    };
 
    Locatie l2 = new Locatie()
    {
        Title = "Receptie",
        Beschrijving = "De receptie....veel blijft er niet meer over van wat eens een bruisende omgeving was. Hier en daar zie je skeletten van , waarschijnlijk, enkele studenten. Een grote poort staat op een kier naar het zuiden. Je ziet twee deuren aan de westelijke en noordelijke zijde."
    };
 
    Locatie l3 = new Locatie()
    {
        Title = "Koffieruime",
        Beschrijving = "Je staat in de koffieruimte achter de receptie. Menig pralinetje is hier vroeger met veel gusto opgesmikkeld. Een lege pralinedoos is het enige bewijs dat het hier ooit gezellig was. Een deur is de enige uitgang uit deze kamer naar het oosten."
    };
 
    Locatie l4 = new Locatie()
    {
        Title = "Tuin",
        Beschrijving = "Het is duidelijk herfst. Een kale boom en vele bruine bladeren op de grond...mistroosteriger kan eigenlijk niet. Je ziet een deur in het zuiden en in het westen en een grote klapdeur naar het noorden."
    };
 
    Locatie l5 = new Locatie()
    {
        Title = "Cafetaria",
        Beschrijving = "Ooit was dit een bruisende locati: veel eten, geroezemoes en licht door de grote ruiten. Nu enkel stof en lege tafel. Enkel een klapdeur is zichtbaar naar het zuiden."
    };
 
    Locatie l6 = new Locatie()
    {
        Title = "Gang",
        Beschrijving = "Een brede gang waar makkelijk 5 mensen schouder aan schouder door kunnen. Zowel in het oosten als het westen zie je een deur."
    };
 
    Locatie l7 = new Locatie()
    {
        Title = "Computerruimte",
        Beschrijving = "Eindelijk; je hebt het gehaald. De plek waar iedereen naar toe wil: het computerlabo!"
    };
 
    //Place objects in rooms
    SpelObjects keytol7 = new SpelObjects() { Beschrijving = "Verroest en groot", Naam = "Sleutel" };
    l5.AanwezigeObjecten.Add(keytol7);
 
    //Place Uitgangen
    l1.Uitgangen.Add(new Exit() { UitgangRichting = richtings.Noord, GaatNaarLocatie = l2 });
 
    l2.Uitgangen.Add(new Exit() { UitgangRichting = richtings.Zuid, GaatNaarLocatie = l1 });
    l2.Uitgangen.Add(new Exit() { UitgangRichting = richtings.West, GaatNaarLocatie =  l3});
    l2.Uitgangen.Add(new Exit() { UitgangRichting = richtings.Noord, GaatNaarLocatie = l4 });
 
    l3.Uitgangen.Add(new Exit() { UitgangRichting = richtings.Oost, GaatNaarLocatie = l2 });
 
    l4.Uitgangen.Add(new Exit() { UitgangRichting = richtings.Zuid, GaatNaarLocatie = l2 });
    l4.Uitgangen.Add(new Exit() { UitgangRichting = richtings.West, GaatNaarLocatie = l6 });
    l4.Uitgangen.Add(new Exit() { UitgangRichting = richtings.Noord, GaatNaarLocatie = l7 });
 
    l5.Uitgangen.Add(new Exit() { UitgangRichting = richtings.Zuid, GaatNaarLocatie = l4 });
 
    l6.Uitgangen.Add(new Exit() { UitgangRichting = richtings.West, GaatNaarLocatie = l4 , BenodigdObject= new List<SpelObjects>(){keytol7}});
    l6.Uitgangen.Add(new Exit() { UitgangRichting = richtings.Oost, GaatNaarLocatie = l7 }); 
 
    l7.Uitgangen.Add(new Exit() { UitgangRichting = richtings.Oost, GaatNaarLocatie = l6 }); 
 
    //Voeg locatie toe
    SpelLocatie.Add(l1);
    SpelLocatie.Add(l2);
    SpelLocatie.Add(l3);
    SpelLocatie.Add(l4);
    SpelLocatie.Add(l5);
    SpelLocatie.Add(l6);
    SpelLocatie.Add(l7);
 
    huidigeLocatie = l1;
}
```

### What’s missing? Veel! 
Maar een eerste uitdaging zou kunnen zijn: hoe kunnen we de speler objecten van de grond laten oprapen en in de  inventaris plaatsen? Dat raadsel  laten we aan jou over over om op te lossen!
