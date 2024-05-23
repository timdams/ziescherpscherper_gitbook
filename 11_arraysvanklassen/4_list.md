## List collectie

Een ``List<>``-collectie is de meest standaard collectie die je kan beschouwen als een veiligere variant op een doodnormale array. Een ``List`` heeft alle eigenschappen die we al kennen van arrays, maar ze zijn wel krachtiger. Het giet een klasse "rond" het concept van de array, waardoor je toegang krijgt tot een hoop nuttige methoden die het werken met arrays vereenvoudigen.

### List aanmaken

De klasse ``List<>`` is een zogenaamde generieke klasse (meer hierover in de appendix). Tussen de ``< >``tekens plaatsen we het datatype dat de lijst zal moeten gaan bevatten. Bijvoorbeeld:

```csharp
List<int> alleGetallen = new List<int>();
List<bool> binaryList = new List<bool>();
List<Pokemon> pokeDex = new List<Pokemon>();
List<string[]> listOfStringarrays = new List<string[]>();
```

**Zoals je ziet hoeven we bij het aanmaken van een ``List`` geen begingrootte mee te geven, wat we wel bij arrays moeten doen. Dit is één van de voordelen van ``List``: ze groeien mee.**

{% hint style='tip' %}
In dit boek behandelen we het concept generieke klassen niet. Generieke klassen oftewel **generic classes** zijn een handig concept om je klassen nog multifunctioneler te maken doordat we zullen toelaten dat bepaalde datatypes niet hardcoded in onze klasse moet gezet worden. ``List<>`` is zo'n eerste voorbeeld, maar er zijn er tal van anderen én je kan ook zelf dergelijke klassen schrijven. Bekijk zeker de appendix indien je dit interesseert.
{% endhint %}

{% hint style='tip' %}
De generieke ``List<>`` klasse bevindt zich in de ``System.Collections.Generic`` namespace. Je dient deze namespace dus als ``using`` bovenaan toe te voegen wil je deze klasse kunnen gebruiken in C# 9.0 en ouder.
{% endhint %}


### Elementen toevoegen

Via de ``Add()``-methode kan je elementen toevoegen aan de lijst. Je dient als parameter aan de methode mee te geven wat je aan de lijst wenst toe te voegen. **Deze parameter moet uiteraard van het type zijn dat de ``List`` verwacht.** 



In volgende voorbeeld maken we een List aan die objecten van het type string mag bevatten en vervolgens plaatsen we er twee elementen in.

```csharp
List<string> mijnPersonages = new List<string>();
mijnPersonages.Add("Reinhardt");
mijnPersonages.Add("Mercy");
``` 



Ook meer complexe datatypes kan je dus toevoegen:

```csharp
List<Pokemon> pokedex = new List<Pokemon>();
pokedex.Add(new Pokemon());
```

Via object syntax initializer kan dit zelfs nog sneller:
```csharp
List<Pokemon> pokedex = new List<Pokemon>()
    {
        new Pokemon(),
        new Pokemon()
    };
```

{% hint style='tip' %}

Je kan ook een stap verder gaan en ook binnenin deze initializer syntax dezelfde soort initialize syntax gebruiken om de objecten individueel aan te maken:

```csharp
List<Pokemon> pokedex = new List<Pokemon>()
    {
        new Pokemon() {Naam = "Pikachu", HP_Base = 5},
        new Pokemon() {Naam = "Bulbasaur", HP_Base = 15}
    };
```

{% endhint %}


### Elementen indexeren

**Het leuke van een ``List`` is dat je deze ook kan gebruiken als een gewone array**, waarbij je met behulp van de indexer elementen individueel kan aanroepen. Stel bijvoorbeeld dat we een lijst hebben met minstens 4 strings in. Volgende code toont hoe we de string op positie 3 kunnen uitlezen en hoe we die op positie 2 overschrijven, net zoals we reeds kenden van arrays:

```csharp
Console.WriteLine(mijnPersonages[3]);
mijnPersonages[2] = "Torbjorn";
```



Ook de klassieke werking met loops blijft gelden. **De enige aanpassing is dat ``List<>`` niet met ``Length`` werkt maar met ``Count``**:

```csharp
for(int i = 0 ; i < mijnPersonages.Count; i++)
{
    Console.WriteLine(mijnPersonages[i])
}
```


### Wat kan een List nog?

Interessante methoden en properties voorts zijn:

* ``Clear()``: methode die de volledige lijst leegmaakt en de lengte (``Count``) terug op 0 zet.
* ``Insert()``: methode om een element op een specifieke plaats in de lijst in te voegen.
* ``IndexOf()``: geeft de index terug van het element item in de rij. Indien deze niet in de lijst aanwezig is dan wordt -1 teruggegeven.
* ``RemoveAt()``: verwijdert een element op de index die je als parameter meegeeft.
* ``Sort()``: alle elementen in de lijst worden gesorteerd. Merk op dat dit niet altijd werkt zoals je verwacht. Lees zeker in hoofdstuk 17 de sectie omtrent "Interfaces in de praktijk" eerst voor je probeert een lijst van eigen objecten te sorteren.

{% hint style='danger' %}
Let op met het gebruik van ``IndexOf`` en objecten. Deze methode zal controleren of de referentie dezelfde is van een bepaald object en daar de index van teruggeven. Je kan deze methode dus wel degelijk met arrays van objecten gebruiken, maar je zal enkel je gewenste object terugvinden indien je reeds een referentie naar het object hebt en dit meegeeft als parameter.
{% endhint %}



### Een wereld met OOP: Pong list

Ikzelf ben fan van List. Het maakt je code vaak leesbaarder dan arrays en geeft je de optie om dynamisch groeiende (en krimpende) arrays te hebben, zonder dat je daar veel *boilerplate* code voor moet schrijven. Herinner je onze Pong-code waarin we 100 balletjes op het scherm lieten vliegen?

```csharp
const int AANTAL_BALLETJES = 100;
Random r = new Random();
Balletje[] veelBalletjes = new Balletje[AANTAL_BALLETJES];
for (int i = 0; i < veelBalletjes.Length; i++) //balletjes aanmaken
{
    veelBalletjes[i] = new Balletje();
    veelBalletjes[i].X = r.Next(10, 20);
    veelBalletjes[i].Y = r.Next(10, 20);
    veelBalletjes[i].VX = r.Next(-2, 3);
    veelBalletjes[i].VY = r.Next(-2, 3);
}

while (true)
{
    for (int i = 0; i < veelBalletjes.Length; i++)
    {
        veelBalletjes[i].Update(); //update alle balletjes
    }
    for (int i = 0; i < veelBalletjes.Length; i++)
    {
        veelBalletjes[i].TekenOpScherm(); //teken alle balletjes
    }
    System.Threading.Thread.Sleep(50);
    Console.Clear();
}
```

Vooral de code in de ``while`` wordt nu leesbaarder dankzij ``List<Balletje>`` (we gaan ook ineens gebruik maken van onze nieuwe default constructor die de random startwaarde instelde):

```csharp
const int AANTAL_BALLETJES = 100;
List<Balletje> veelBalletjes = List<Balletje>();
for (int i = 0; i < AANTAL_BALLETJES; i++) //balletjes aanmaken
{
    veelBalletjes.Add(new Balletje());
}

while (true)
{
    foreach(var bal in veelBalletjes)
    {
        bal.Update(); //update alle balletjes
    }
    foreach(var bal in veelBalletjes)
    {
        bal.TekenOpScherm(); //teken alle balletjes
    }
    System.Threading.Thread.Sleep(50);
    Console.Clear();
}
```