# Bestandsverwerking <!--\label{ch:18}-->

Op vraag van velen is het nu tijd om één van de meest gebruikte .NET namespaces te bekijken: **System.IO**[^sysio]. 

{% hint style='tip' %}
Vergeet zeker niet bovenaan je code **``using System.IO;``** toe te voegen indien je ook maar één voorbeeld uit dit hoofdstuk wilt kunnen maken.
{% endhint %}




De System.IO namespace is een zeer uitgebreide bibliotheek die alle methoden bevat die je nodig hebt om input en output (I/O) operaties te verrichten. Dit betekent dat je met behulp van deze namespace bestanden en folders (ook wel *mappen* of *directories* genoemd) kunt uitlezen, schrijven, maken en verwijderen, en zo voort.

Het zal je met andere woorden toelaten om toegang te krijgen tot, onder andere, het lokale bestandssysteem. 



[^sysio]: Zoals steeds, kijk zeker eens naar de officiële documentatie op [learn.microsoft.com/en-us/dotnet/api/system.io](https://learn.microsoft.com/en-us/dotnet/api/system.io).


...met alle voor-en nadelen als gevolg. Je zal namelijk rechtstreeks:

* **Wijzigingen op je harde schijf** kunnen aanbrengen. Het is belangrijk om voorzichtig te zijn wanneer je werkt met bestanden en folders. Eén kleine fout kan leiden tot het verwijderen van belangrijke bestanden of gegevensverlies. En ja, ook ik heb dit al meegemaakt.

* **Niet altijd de juiste gebruikersrechten hebben**  om bepaalde I/O bewerkingen uit te voeren. Dit hangt af van de rechten die je gecompileerde programma heeft binnen het besturingssysteem. Zorg ervoor dat je controleert of je voldoende rechten hebt voordat je probeert een bestand te lezen of te schrijven.


{% hint style='danger' %}

**Enkele tips voor je begint**

Om de voorgaande waarschuwing te benadrukken, nog 2 belangrijke tips:

1. **Back-ups**: Backups maken is altijd belangrijk. Maar de voorbije 17 hoofdstukken heb je normaal gezien nooit code geschreven die effectief zaken kon kapot maken op je computer. Daar komt dus vanaf nu verandering in. Tijd dus voor die wekelijkse backup!
2. **Try-catch gebruiken**: Eigenlijk hebben we voorlopig maar beperkt aan *exception handling* moeten doen. 99% van de tijd wisten we heel goed welke uitzonderingen konden optreden en schreven we onze code er naar. Echter, vanaf nu zal je programma ook zaken benaderen *buiten het programma*. Tot aan dit hoofdstuk was enkel de gebruikersinput iets dat van buiten kwam. We waren meestal zelf de eindgebruiker, en gingen uit van foutloze invoer (*ik weet het, naïef*). Bestanden luisteren echter niet zo goed. Het kan dus goed zijn dat een bestand toch niet op die plaats staat waar je dacht dat het stond, of dat je toch niet de juiste rechten hebt. Kortom,**exception handling zal vanaf nu essentieel worden**.

{% endhint %}

## Bestands- en folderlocaties

Ieder bestand en folder op je harde schijf wordt gedefinieerd door een unieke locatie, **path** genoemd. Als je een bestand genaamd ``mijnData.txt`` hebt in de "temp"-folder van je c-schijf, dan is het **full path** van dit bestand: 

```text
c:\temp\mijnData.txt
```

Folders hebben ook een path, in het vorige voorbeeld is het full path van de temp-folder: 

```text
c:\temp\
```

In C# zullen deze paths altijd als ``string``  worden verwerkt. 

{% hint style='danger' %}

Let er op dat een path **niet hoofdlettergevoelig** is. Je kan dus geen 2 bestanden met de naam "mijnData.txt" en "MijnData.TXT" in dezelfde folder hebben. Zowel Windows als Mac OS hebben een niet hoofdlettergevoelige bestandsstructuur.

{% endhint %}


{% hint style='danger' %}

Bij MacOS werkt men met *forward slashes* in plaats van *backward slashes*. 

{% endhint %}

### Bestandslocatie zonder path

Als je geen specifiek path aangeeft wanneer je een bestand wilt gebruiken, gaat je programma ervan uit dat het zich in de folder van het programma zelf zich bevindt. Voor de meeste projecten is dit meestal de ``\bin\Debug``-folder tijdens het ontwikkelen en testen.

<!-- \newpage -->
 
Volgende voorbeeld (we lopen even al vooruit) zal de tekst "Het einde is nabij" wegschrijven naar een bestand "doem.txt" op één van volgende locaties:    

* Lijn 1: Naar de plek waar het programma wordt uitgevoerd.
* Lijn 2: Naar de temp-folder.

```csharp
File.WriteAllText("doem.txt", "Het einde is nabij");
File.WriteAllText(@"c:\temp\doem.txt", "Het einde is nabij");
```

In het tweede geval is belangrijk te controleren of je wel schrijfrechten hebt voor die folder. Heb je die niet dan zal je een **``UnauthorizedAccessException``** krijgen. We gebruiken dus best exception handling wanneer we met bestanden werken.

```csharp
try
{
    File.WriteAllText("doem.txt", "Het einde is nabij");
}
catch(UnauthorizedAccessException)
{
    Console.WriteLine($"Geen schrijfrechten!")
}
```


### ``System.IO.Path``

Het is niet altijd duidelijk of je applicatie op een Mac of Windows zal uitgevoerd worden. Je kan er dus maar beter rekening mee houden dat je applicatie soms met andere paths zal werken dan je gewend bent (Mac OS werkt bijvoorbeeld niet met een "c:\"-schijf notatie). Het is daarom veiliger om te werken met de ``System.IO.Path``-klasse, die ons in staat stelt om op een platformonafhankelijke manier met paden en bestandsnamen te werken.

Stel dat we een bestandsnaam willen samenstellen uit verschillende delen, dan gebruiken we hier de erg nuttige **``Combine``-methode** voor:

```csharp
string folder = "data";
string bestand = "dagboek.txt";
string fullPath = Path.Combine(directory, filename);
Console.WriteLine(fullPath);
```

Afhankelijk van het besturingssystemen zal de output dus verschillend zijn. Op Windows:

```text
data\dagboek.txt
```
Op Mac OS wordt dit echter:

```text
data/dagboek.txt
```

De ``Path``-klasse heeft ook nog tal van nuttige methode zoals: ``ChangeExtension``, ``GetDirectoryName``, ``GetFileNameWithoutExtension``, ``GetFullPath``, enz. Met behulp van de ``GetRandomFileName``-methode kan je een willekeurige folder- of bestandsnaam verkrijgen. Dit is handig als je een tijdelijke bestand wil aanmaken en zeker wil zijn dat de naam niet al bestaat. Een andere handige methode is ``GetTempPath``, deze geeft je het path naar de temp-folder van de huidige gebruiker. Het is een goede gewoonte om tijdelijke werkbestanden voor je applicatie in deze folder te plaatsen. En het is nog toffer als je deze ook verwijderd wanneer ze niet meer nodig zijn.

### Speciale folders

Soms wil je bestanden opslaan in speciale folders zoals op het bureaublad. Hiervoor kun je de ``Environment.GetFolderPath``-methode gebruiken. Deze methode vereist een parameter van het type ``Environment.SpecialFolder``, wat een ingebouwde enum is. Deze enum bevat een hele hoop *gekende* locaties van Windows-folders, zoals het bureaublad, de temp-folder,  "Mijn documenten"-folder, enz. Dit zorgt ervoor dat je bestand altijd op de juiste plek komt, ongeacht de gebruikersomgeving. 

In dit voorbeeld plaatsen we ons onheilspellende bericht op het bureaublad van de huidige gebruiker:

```csharp
string desktopPath = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
string fullPath = Path.Combine(desktopPath, "doem.txt");
File.WriteAllText(fullPath, "Het einde is nabij"); 
```

### Controleren dat folder of bestand bestaat

Het is een goede gewoonte om steeds te controleren of een bestand of folder al bestaat, voor je ermee gaat werken. Soms wil je een bestaand bestand zeker niet overschrijven. Of wil je een folder aanmaken als deze nog niet bestaat. Controleer dit dus altijd in je programma én vraag aan de gebruiker wat te doen bij twijfel. Overschrijf of verwijder nooit een bestand of folder zonder de gebruiker hierover te waarschuwen. Zeker wanneer het om een bestand gaat dat niet door jouw programma beheerd wordt.

Het controleren of een bestand bestaat doe je met de ``File.Exists``-methode:

```csharp
if(File.Exists(desktopPath))
{
    //werk met bestand
}
else
{
    Console.WriteLine("Dit bestand bestaat niet.");
}
``` 
<!-- \newpage -->

Het controleren van het bestaan van een folder doe je met ``Directory.Exists()``:

```csharp
if(Directory.Exists(tempPath))
{
    //werk met folder
}
```

{% hint style='tip' %}
Om de voorbeeldcode in dit hoofdstuk behapbaar te houden, zullen we niet telkens overal deze controle doen.
{% endhint %}

### Folder of bestand aanmaken


Na de controle kan je dan beslissen om het bestand of folder aan te maken. Dat kan met de ``File.Create`` en ``Directory.CreateDirectory``-methoden:


```csharp
if (!Directory.Exists(tempPath))
{
    Directory.CreateDirectory(tempPath);
}
```

en

```csharp
if (!File.Exists(desktopPath))
{
    File.Create(desktopPath);
}
```
