## Vreemde tekens in console tonen

Niets is zo leuk als de vreemdste UNICODE tekens op het scherm tonen. In oude console-games werden deze tekens vaak gebruikt om complexe tekeningen op het scherm te tonen. Om je ietwat saaie applicaties dus wat toffer te maken leggen we daarom uit hoe je dit kan doen.


![Dwarf fortress: een van de bekendste (én meest complexe) console-games ooit waar nog steeds aan ontwikkeld, wordt gebruikt ongelooflijk veel bizarre karakters om zo een erg 'cool' ogende user interface te maken.](../assets/0_intro/kerosenethunder_mockup.png)

### UNICODE karakters tonen

Je toetsenbord heeft maar een beperkt aantal toetsen. Er zijn echter tal van andere tekens gedefinieerd die console-applicaties ook kunnen gebruiken. We zagen reeds dat al deze tekens, UNICODE-karakters, een eigen unieke code hebben die je kan opzoeken om vervolgens dat teken in je code te gebruiken, daar het ``char`` type hiermee werkt.

Dit gaat als volgt in z'n werk:

1. Zoek het teken(s) dat je nodig hebt in een UNICODE-tabel , bijvoorbeeld op **UNICODE-table.com**.
2. Plaats bovenaan je Main: `Console.OutputEncoding = System.Text.Encoding.UTF8;`
3. Je kan nu op 2 manieren dit teken in console plaatsen.

Stel je voor dat we het copyright karakter "©" wensen te gebruiken in onze applicatie. Deze heeft hexadecimale UNICODE waarde 0x00A9.

#### Manier 1: copy/paste

Kopieer het karakter zelf en plaats het in je code waar je het nodig hebt, bijvoorbeeld:


```java
Console.WriteLine("©"); 
```

Merk op dat niet alle lettertypes dit karakter kennen en dus mogelijk als een vierkantje dit op je scherm zullen tonen. Dit hangt af van het lettertype dat jouw shell-venster gebruikt (meestal is de standaard *Courier*).

#### Manier 2: hexadecimale code casten naar char

Casting leggen we pas in het volgende hoofdstuk uit, maar het kan geen kwaad om al eens een voorproefje hiervan te krijgen. 
Noteer de hexadecimale code van het karakter dat in de tabel staat. In dit geval is de code 0x00A9. Om dit teken te tonen schrijf je dan:

```java
char copyright = (char)0x00A9;
Console.WriteLine(copyright);
```

In C# schrijf je hexadecimale getallen als volgt als je ze rechtstreeks in een string wilt plaatsen: \u00A9

Wil je dus bovenstaande teken schrijven dan kan dat ook als volgt:


```java
Console.WriteLine("\u00A9");
```



### UNICODE-kunst tonen

Soms zou je multiline UNICODE-kunst (ook wel ASCII-art genoemd) willen tonen in je C# applicatie. Dit kan je eenvoudig oplossen door gebruik te maken van het ``@`` teken voor een string.

Stel dat je een toffe titel of tekening bijvoorbeeld via **ASCIIflow.com** maakt.

Je kan het resultaat eenvoudig naar je klembord kopiëren en vervolgens in je C#-code integraal copy pasten als literal voor een ``string`` op voorwaarde dat je het laat voorafgaan door ``@"`` en uiteraard eindigt met ``";``.

Bijvoorbeeld:

```java
string myname = @"
___________________   
\__    ___/\______ \  
  |    |    |    |  \ 
  |    |    |    `   \
  |____|   /_______  /
                   \/ ";
Console.WriteLine(myname);
```

{% hint style='tip' %}
Zowel de $-notatie (voor string interpolatie) als het @-teken kan je gecombineerd gebruiken bij een string:


```java
Console.WriteLine($@"1/1={1+1}. \tGeen tab");
```

Dit geeft als output (\t wordt door het apenstaartje genegeerd):


```text
1/1=2. \tGeen tab
```
{% endhint %}


{% hint style='tip' %}
In de vorige sectie legden we uit dat we tekst kunnen formateren als een geld bedrag m.b.v. ``Console.WriteLine($"{12.3456:C}");``. Het probleem was dat het euro-teken als een ``?`` op het scherm verscheen. Dit is omdat het euro-teken een nieuwe karakter is en dus binnen de UNICODE tabellen bestaat, maar niet binnen de klassieke ASCII-tabel. Willen we dit teken dus gebruiken dan moeten we de regel `Console.OutputEncoding = System.Text.Encoding.UTF8;` gebruiken:

```java
Console.OutputEncoding = System.Text.Encoding.UTF8;
Console.WriteLine($"{12.3456:C}")
```

Zal als uitvoer geven:


```text
12,35 €
```
{% endhint %}
