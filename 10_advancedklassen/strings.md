## Spelen met strings

In deze sectie duik ik dieper in de ``String`` klasse om aan te tonen dat er tal van nuttige zaken bestaan om met strings te werken.

### Splitsen en samenvoegen

#### Split

Aan het einde van dit hoofdstuk willen we een csv-bestand (comma separated value) splitsen. De ``Split`` methode laat toe een string te splitsen op een bepaald teken. Het resultaat is steeds een **array van strings**.

```csharp
string data = "12,13,20";
string[] gesplitst = data.Split(',');

for(int i = 0; i<gesplitst.Length;i++)
{
    Console.WriteLine(gesplitst[i]);
}
```

Uiteraard kan je dit dus gebruiken om op eender welk teken te splitsen. Je kan dus even goed splitsen op een tab (``\t``) of bijvoorbeeld een kommapunt (``;``).

#### Join

Via ``Join`` kunnen we een array van strings terug samenvoegen. Het resultaat is een nieuwe string.

Volgende voorbeeld zal de eerder array van het vorige voorbeeld opnieuw samenvoegen maar nu met telkens een ``;`` tussen iedere string:


```csharp
string joined = String.Join(";", gesplitst);
```

Voorgaande methoden zijn ``static`` en moet je dus via de klasse ``String`` doen en niet via de objecten zelf.



### Tekst files uitlezen

De ``System.IO`` namespace bevat tal van nuttige methoden en klassen om met bestanden te werken. Bij C# 10 heb je deze namespace automatisch, bij C# 9 en ouder moet je deze manueel toevoegen bovenaan je file: ``using System.IO;``. We gaan deze namespace nog meer uit de doeken doen in hoofdstuk 19, maar hier alvast een voorproefje.

Via ``System.File.ReadAllLines()`` kunnen we een tekstbestand uitlezen. De methode geeft een array van string terug. Per lijn die eindigt met een newline (``\r\n``) zal een nieuwe string aan de array toegevoegd worden.

```csharp
string[] lines = File.ReadAllLines(@"c:\mypoem.txt");
for (int i = 0; i < lines.Length; i++)
{
    Console.WriteLine(lines[i]);
}
```

#### CSV uitlezen

Dankzij ``ReadAllLines`` en ``Split`` hebben we nu alle bouwstenen om eenvoudig een csv-bestand te verwerken.

Stel je voor dat een bestand ``soccer.csv`` volgende tekst bevat:


```text
Dams;Tim;1981
Hamdaoui;Mounir;1984
Stoffels;José;1950
```

Volgende code zal dit bestand uitlezen en de individuele data op het scherm tonen:

```csharp
string[] lines = File.ReadAllLines(@"c:\soccerstars.csv");
for (int i = 0; i < lines.Length; i++)
{
    string[] splitted = lines[i].Split(';');

    Console.WriteLine($"Voornaam speler {i}= {splitted[1]}" );
    Console.WriteLine($"Achternaam speler {i}= {splitted[0]}");
    Console.WriteLine($"Geboortejaar speler {i}= {splitted[2]}");
}
```


#### CSV downloaden

Vaak zal je een online bestand willen verwerken. De ``WebClient`` klasse heeft tal van manieren om met online bronnen te werken. Deze klasse bevindt zich in de ``System.Net`` namespace en vereist dus dat je bovenaan je code volgende lijn toevoegt:


```csharp
using System.Net
```

Volgende code toont hoe we een bestand van een specifieke locatie kunnen downloaden:

```csharp
WebClient wc = new WebClient();
string csv = wc.DownloadString("www.fakeaddress.com/mydata.csv");
```

Dit bestand is 1 platte tekst. Willen we deze vervolgens verwerken dan moeten we deze splitsen in lijnen:


```csharp
string[] split = csv.Split('\n');
```

We hebben nu een ``for`` nodig die lijn per lijn zal splitsen:

```csharp
for (int i = 1; i < splitted.Length; i++)
{
    string[] lijnsplit = splitted[i].Split(',');
    Console.WriteLine("Data 1="+lijnsplit[0]);
    Console.WriteLine("Data 2=" + lijnsplit[1]);
}
```

In dit voorbeeld ga ik er vanuit dat de eerste lijn in het bestand een *header* bevat, die we dus moeten overslaan. Daarom start ik de loop vanaf lijn 1.

