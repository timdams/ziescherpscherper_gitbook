## Escape characters




>![](../assets/attention.png)De voorman hier! Escape characters zijn niet de boeiendste materie om te bespreken. Je zou nog kunnen hopen dat het een opvolger is van Prison Break of zo. Helaas is dat niet zo. Echter: als je escape characters beheerst zal je veel eenvoudiger én mooier tekst op je scherm kunnen toveren. Let dus even goed op a.u.b.


Naast letters en tekens mogen in string en chars ook escape characters staan. In C# hebben bepaalde tekens namelijk een speciale functie. Denk maar aan de dubbele aanhalingstekens (`"`) om het begin en einde van een string-literal mee aan te geven.
 
We hebben dus een manier nodig om aan te duiden wanneer de compiler het eerstvolgende teken, zoals een ``"`` als een ``char`` moet beschouwen. We lossen dit op met behulp van escape characters.  **Deze worden met een backslash (`\`) aangeduid, gevolgd door het karakter dat we wensen te gebruiken.**

### Voorbeeld van escape characters

Laten we eens kijken naar de werking van het weglatingsteken als voorbeeld (de zogenaamde apostrof of afkappingsteken, om bijvoorbeeld ``'s avonds`` te schrijven)
De volgende code zal de compiler verkeerd interpreteren, omdat hij denkt dat we een leeg karakter willen opslaan:


```csharp
char weglatingsteken = ''';
```

Het gevolg is een berg aan foutboodschappen omdat er na het sluitende weglatingsteken (het tweede) plots nog één (het derde) verschijnt. VS is volledig in de war en weet niet wat doen. 


![Hulp! VS snapt er niets van!](../assets/1_csharpbasics/escape.png)

**Escape characters to the rescue!** We gaan met de backslash aanduiden dat het volgende teken (het tweede weglatingsteken) een ``char`` voorstelt en niet het sluitende teken in de code.


```csharp
char weglatingsteken = '\'';
```

Een backslash in een char of string-literal geeft aan dat het volgende teken als een literal moet worden gezien en niet als een speciaal teken in C#.

### Veel gebruikte escape chars

Er zijn verschillende escape characters in C# toegelaten. We lijsten hier de belangrijkste[^escapover] op:

```text
\'      //de apostrof zoals zonet besproken.
\"      //een aanhalingsteken.
\\      //een backslash in je tekst tonen. 
\\\\    //twee backslashes.
\n      //een nieuwe lijn (zogenaamde *enter* of *newline*).
\t      //Horizontale tab.
\uxxxx  //een teken met als hexadecimale UNICODE waarde xxxx.
```

[^escapover]: Voor een totaal overzicht kijk eens op [docs.microsoft.com/dotnet/csharp/programming-guide/strings](https://docs.microsoft.com/dotnet/csharp/programming-guide/strings/).

<!-- \newpage -->


### Escape characters in strings

Aangezien strings eigenlijk bestaan uit 1 of meerdere char-elementen, is het logisch dat je ook in een string met escape characters kunt werken. Het woord "'s avonds" schrijf je bijvoorbeeld als volgt:


```csharp
string woord = "\'s avonds";
```

Idem met aanhalingstekens. Stel je voor dat je een programma wilt schrijven dat C# code op het scherm toont. Dat doe je dan met volgende, nogal Inception-achtige, manier:

```csharp
string inceptionCode = "Console.WriteLine(\"Cool he\");";
Console.WriteLine(inceptionCode);
```

Merk op dat we voorgaande code nog meer Inception-like kunnen maken door de string ineens in de WriteLine methode te plaatsen:


```csharp
Console.WriteLine("Console.WriteLine(\"Cool he\");");
```

Beide voorbeelden zullen dus volgende tekst op het scherm geven: ``Console.WriteLine("Cool he");``

### Biep biep

``\a`` mag je enkel gebruiken als je een koptelefoon op hebt daar dit het escape character is om de computer een biepje te laten doen. 

Volgende codevoorbeeld zal, als alles goed gaat, een zin op het scherm tonen en dan ogenblikkelijk erna een biepje:


```csharp
Console.WriteLine("Een zin en dan nu ... de biep\a");
```



### Witregels en tabs

We gebruiken vooral escape characters in strings om bijvoorbeeld witregels en tabs aan te geven. Test bijvoorbeeld volgende lijn code eens:

```csharp
string eenString = "Een zin.\t na een tab \nDan eentje op een nieuwe regel";
Console.WriteLine(eenString);
```

Dit zal als output geven:


```csharp
Een zin.         na een tab
Dan eentje op een nieuwe regel
```

### Over tabstops

Als je het niet gewoon bent de tab-toets op je toetsenbord te gebruiken dan is de eerste werking van \t mogelijk verwarrend. Nochtans is \t in een string gebruiken exact hetzelfde als op de tab-toets duwen. 

In je console-scherm zijn de tab stops vooraf bepaald. Wanneer je dus een tab invoegt zal de cursor zich verplaatsen naar de eerstvolgende tab stop. In volgende tekstuitvoer zie je de tabstops op de tweede lijn "gevisualiseerd":


```text
01234567890123456789012345678901234567890123456789
        1       2       3       4       5
```

Bovenstaande uitvoer werd als volgt gemaakt:

```csharp
Console.WriteLine("01234567890123456789012345678901234567890");
Console.WriteLine("\t1\t2\t3\t4\t5");
```


Tabstops zijn nuttig om je data mooi uitgelijnd in een tabel te plaatsen. Als je dat dan nog eens combineert met de UNICODE karakters om tabellen te tekenen kan je toffe dingen maken. Deze karakters, de zogenaamde "Box Drawing" subset, staan in UNICODE gedefinieerd als de tekens met hexadecimale code 0x2500 en verder. Bekijk zeker eens een datasheet met alle tekens.[^ascitekenen].


[^ascitekenen]:www.unicode.org/charts/PDF/U2500.pdf


### Het verbatim karakter ``@``

Het apenstaartje (``@``) voor een ``string`` literal plaatsen is zeggen "beschouw alles binnen de aanhalingstekens als effectieve karakters die deel uitmaken van de inhoud van de tekst". Dit teken heet daarom binnen C# niet voor niets het **verbatim** karakter. Het is belangrijk te beseffen dat **escape characters genegeerd worden** wanneer we het verbatim karakter gebruiken. Dit is vooral handig als je bijvoorbeeld een netwerkadres wilt schrijven en niet iedere ``\`` wilt escapen:

```csharp
string zonderAt = "C:\\Temp\\Myfile.txt";
string metAt = @"C:\Temp\Myfile.txt";
```

Merk op dat aanhalingstekens nog steeds *ge-escape'd* moeten worden. Heb je dus een stuk tekst met een aanhalingsteken in dan zal je zonder het apenstaartje moeten werken.

<!-- \newpage -->


Uiteraard kan je ook het apenstaartje gebruiken in ``Console.WriteLine``. Volgende zal dus de escape karakters tonen in plaats van "uitvoeren":


```csharp
Console.WriteLine(@"Om een tab te tonen gebruik je \t in C#.");
```

Wat zal resulteren in volgende uitvoer:


```text
Om een tab te tonen gebruik je \t in C#.
```



