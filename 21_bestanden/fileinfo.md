## De ``FileInfo`` klasse

De ``FileInfo``klasse heeft 2 specifieke doelen:

1. Ze laat toe om **meer informatie over bestanden** te verkrijgen, zoals bijvoorbeeld het moment waarop het bestand werd aangemaakt.
2. Anderzijds kan je er eenvoudig **bestanden met kopiëren, verplaatsen en verwijderen**.

We kunnen deze klasse gebruiken door eerst een object te instantiëren, waarbij we aan de constructor het path meegeven naar het te gebruiken bestand:

```csharp
FileInfo fileInfo = new FileInfo(pathNaarBestand);
```

{% hint style='tip' %}
Er is uiteraard ook een ``DirectoryInfo`` klasse met een soortgelijke werking, die we verderop bespreken.
{% endhint %}

### Meer informatie over een bestand

Nadat het ``fileInfo`` object werd aangemaakt krijg je via een hele resem properties toegang tot detail-informatie over het bestand in kwestie, zoals:

| Methode | Info | Voorbeeldoutput |
|--------|-------------|----------|
| **``Name``** |Bestandsnaam| "temp.txt"|
| **``FullName``**| Volledige pad van het bestand| ``c:\temp\temp.txt``|
| **``Extension``**|Bestandsextensie| ".txt"|
| **``Length``**| Bestandsgrootte in bytes| 21|
| **``CreationTime``**| ``DateTime`` object met datum en tijd waarop het bestand is aangemaakt| 11/06/2024 10:17:21   |
| **``LastAccessTime``**|  Laatste keer dat het bestand is geopend|  idem |
| **``LastWriteTime``**|Laatste keer dat het bestand is gewijzigd| idem  |
| **``Exists``**| ``boolean`` die aangeeft of het bestand bestaat| ``true`` |

<!-- \newpage -->

Het gebruik van deze properties wijst zichzelf uit (uiteraard zijn dit allemaal read-only properties):

```csharp
FileInfo info = new FileInfo("bondData.dat");
if (info.Exists)
{
    Console.WriteLine($"Bestandsnaam: {info.Name}");
    Console.WriteLine($"Bestandsgrootte: {info.Length}/1024 kB");
}
```

### Kopiëren, verplaatsen en verwijderen

Van zodra je een ``FileInfo``-object hebt, krijg je beschikking over tal van handige methoden. We gaan de 3 nuttigste (``CopyTo``, ``MoveTo`` en ``Delete``) eens tonen in een domme demo:

```csharp
FileInfo info = new FileInfo("bondData.dat");
if(info.Exists)
{
    fileInfo.CopyTo("supermanData.dat");
    fileInfo.MoveTo("bond2Data.dat");
    fileInfo.Delete();
}
```

Als we deze code uitvoeren zullen er 3 zaken gebeuren, op voorwaarde dat het bestand ``bondData.dat`` beschikbaar:

* Lijn 4: Een tweede bestand ``supermanData.dat`` wordt aangemaakt en zal dezelfde informatie als het originele bestand bevatten.
* Lijn 5: Het bestand ``bondData.dat`` wordt hernoemd naar ``bond2Data.dat``.
* Lijn 6: Het originele bestand wordt verwijderd. Ook al werd het hernoemd.
* Lijn 7: Als we nu de folder zouden bekijken waar de applicatie werd uitgevoerd, dan zouden we enkel nog een bestand met de naam "supermanData.dat" zien staan.


###  ``File`` of ``FileInfo``


De ``System.IO`` namespace is een nogal verwarrende klasse. Je kan dezelfde zaken op verschillende manieren doen. Er zijn verschillende Readers en Writers. Soms gebruik je static-methoden, soms object-methoden. Wat is het nu? Lig er niet te hard van wakker! Je bent nog maar aan het prille begin van je C# carrière en zal de komende jaren zeker beter aanvoelen wanneer je welke oplossingsstrategie moet toepassen.

Toch willen we kort toelichten wat het verschil is tussen ``File`` en ``FileInfo``. Je hebt gezien dat ik ze beide doorheen dit hoofdstuk door elkaar gebruikte. Beide klassen hebben veel gelijkaardige functionaliteiten, maar de ``File``-klasse is een **``static klasse``**. Terwijl ``FileInfo`` dat niet is. 

De ``File`` vereist dus niet dat je telkens een object aanmaakt wanneer je snel iets met een bestand wenst te doen. Bij ``FileInfo`` doen we dit uiteraard wel, waarbij we het path naar het te gebruiken bestand meegeven. 

En hier ligt dan ook direct een groot verschil: de ``FileInfo`` heeft bewust een **``Refresh``-methode**, omdat het niet kan garanderen dat alle ingelezen informatie later in de code nog relevant is. ``File`` zal steeds *instantaan* met het betrokken bestand werken. ``FileInfo`` doet dit enkel tijdens de constructie en bij een ``Refresh``. 

Als je meerdere bewerkingen op een bestand wilt doen na elkaar is ``FileInfo`` aangeraden, daar je anders meerdere keren de file expliciet zou openen en sluiten met de ``File`` klasse. Wil je echter maar *kort en krachtig* iets met het bestand doen (bv. controleren of het bestaat met ``File.Exist``) dan gebruik je beter de ``File`` klasse. Maar toegegeven, dit is geen harde wet. Ik zou daarom momenteel aanbevelen: gebruik wat je zelf het prettigst vindt. Van zodra je professionele code moet beginnen schrijven waarbij performantie en veiligheid belangrijk is, dan wordt het tijd om *in-depth* na te denken over het gebruik van specifieke klassen.

## ``DirectoryInfo`` klasse

Uiteraard is er ook een ``DirectoryInfo`` klasse. En net zoals ``FileInfo`` een tegenhanger in de vorm van de  ``File`` klasse heeft, zo is er ook de ``Directory`` klasse. Ook hier is ``Directory`` een **static klasse**, en ``DirectoryInfo`` niet. De uitleg van zonet over het verschil blijft dus ook hier gelden.

Deze klasse geeft dus meer informatie over een folder en het gebruik is identiek aan de ``FileInfo``-klasse. Eerst moet er weer een object van aan gemaakt worden:

```csharp
DirectoryInfo dirInfo = new DirectoryInfo(@"c:\temp");
```

Wederom kunnen we de typische properties (``LastAccesTime``, ``CreationTime``, enz. ) en methoden (``Create``, ``Delete``, ``MoveTo`` enz.) aanroepen. 

<!-- \newpage -->

### ``GetFiles`` en ``GetDirectories``

De ``DirectoryInfo``-klasse heeft nog 2 erg nuttige methoden om te bekijken welke elementen in de folder staan.  ``GetFiles`` en ``GetDirectories`` geven een array van respectievelijk ``FileInfo`` en ``DirectoryInfo`` objecten terug. Vervolgens kunnen we deze arrays van paths gebruiken om bijvoorbeeld deze bestanden te verwijderen.

Volgende code toont hoe je kunt visualiseren welke elementen zich in de ``c:\temp``-folder bevinden:

```csharp
DirectoryInfo tempInfo = new DirectoryInfo(@"C:\temp");

if(tempInfo.Exists)
{
    var bestanden = tempInfo.GetFiles();
    var folders = tempInfo.GetDirectories();

    foreach (var folder in folders)
    {
        Console.WriteLine($"Folder:{folder.Name}");
    }
    foreach (var bestand in bestanden)
    {
        Console.WriteLine(bestand.Name);
    }
}
```

#### Filteren op bestanden

De ``GetFiles``-methode aanvaardt enkele handige parameters die je toelaten om naar specifieke bestanden te zoeken. 

Ten eerste kan je een **searchPattern** als ``string`` meegeven. Hierbij kan je met behulp van de asterisk (``*``) en het vraagteken aangeven bepaalde zaken maar te zoeken. 

Volgende voorbeeld zal alle bestanden die extensie ".txt" hebben teruggeven:

```csharp
var tekstBestanden= tempInfo.GetFiles("*.txt");
``` 

En deze zal alle bestanden teruggeven wiens bestandsnaam start met "Tim" en dan nog 1 teken bevat. De extensie maakt niet uit: 

```csharp
var timBestanden= tempInfo.GetFiles("Tim?.*");
``` 

<!-- \newpage -->

#### Zoeken in subfolders

Via een tweede argument bij ``GetFiles`` kan je ook aangeven om niet enkel in de huidige folder te zoeken, maar ook in de subfolders.  Volgende voorbeeld zal alle bestanden zoeken die eindigen op ".txt" , inclusief in de subfolders:

```csharp
var gevonden = tempInfo.GetFiles("*.txt", SearchOption.AllDirectories );
```

#### Recursief een folderstructuur verwerken

Stel dat je alle subfolders en bestanden in die subfolders wilt oplijsten, inclusief folders in subfolders, en zo voort. Hiervoor bestaat geen ingebouwde .NET methode. Je zal dit dus zelf moeten oplossen, waarbij we een **recursie**-structuur zullen moeten aanmaken. Een recursieve methode roept zichzelf terug aan tot aan een bepaalde voorwaarde wordt voldaan. In dit geval wanneer er geen nieuwe subfolders meer worden gedetecteerd in de huidige folder.

Volgende methode zal telkens in de huidige folder, die je meegeeft als argument, alle bestanden en folders van oplijsten. Het zal vervolgens zichzelf aanroepen met als argument telkens één van de subfolders in de huidige folder: 

```csharp
static void ToonFoldersEnBestanden(string path)
{
    foreach (string bestand in Directory.GetFiles(path))
    {
        Console.WriteLine(bestand);
    }

    foreach (string folder in Directory.GetDirectories(path))
    {
        Console.WriteLine(folder);
        ToonFoldersEnBestanden(folder); 
    }
}
```

De eerste ``foreach`` lijst de bestanden op. De tweede loop zal de folders tonen en ook zichzelf *recursief aanroepen*.

{% hint style='tip' %}
Een klassieke fout bij recursie is een methode schrijven zonder **stopvoorwaarde**. Gelukkig hebben we dat probleem hier niet: de methode stopt met zichzelf aanroepen als er geen subfolders meer zijn in de huidige folder.  

Pas wel op: als je deze methode uitvoert op bijvoorbeeld "c:", zal er waarschijnlijk heel veel tekst op je scherm verschijnen. Dat kan lang duren.

{% endhint %}

