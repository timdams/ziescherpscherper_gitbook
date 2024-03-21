## Strings samenvoegen
Je kan strings en variabelen samenvoegen tot een nieuwe string op verschillende manieren:
* +-operator 
* $ string interpolation 
* Of de oude manier: ``String.Format()`` 

{% hint style='tip' %}
In dit boek verkiezen we **manier 2**, de string interpolatie. Dit is de meest moderne aanpak.
{% endhint %}


In de volgende sectie gaan we van volgende informatie uit:

* Stel dat je 2 variabelen hebt ``int leeftijd = 13`` en ``string naam = "Finkelstein"``.
* We willen de inhoud van deze variabelen samenvoegen in een nieuwe ``string result`` die zal bestaan uit de tekst: ``Ik ben Finkelstein en ik ben 13 jaar oud.``

Volgende 3 manieren tonen hoe je steeds tot voorgaande string zal komen.

### Manier 1: String samenvoegen met de +-operator
Je kan strings en variabelen eenvoudig bij elkaar 'optellen' zoals we in het begin van dit boek hebben gezien. Ze worden dan achter elkaar geplakt (**geconcateneerd**). 


```csharp
string result = "Ik ben " + naam + " en ik ben " + leeftijd+ " jaar oud.";
```

Let er op dat je tussen de aanhalingsteken (binnen de strings) spaties zet indien je het volgende deel niet tegen het vorige stringstuk wilt 'plakken'.

{% hint style='danger' %}
Toch even goed opletten hier. De volgorde van strings met andere types samenvoegen (**concateneren**) bepaalt wat de uitvoer zal zijn! Kijk zelf:

```csharp
Console.WriteLine("1"+1+1);
Console.WriteLine(1+1+"1");
Console.WriteLine("1" + (1 + 1));
```

Geeft als uitvoer:


```text
111
21
12
```

Was dit de uitvoer die je voorspeld had?

Ook in dit soort code wordt de volgorde van bewerkingen gerespecteerd. De **concatenatie gebeurt van links naar rechts en de linkse operand zal steeds bepalen wat het resultaat van de bewerking zal zijn indien er twijfel is**. Dit nieuw samengevoegde deel wordt dan de linkse operand voor het volgende deel.

Kijken we dus naar ``"1"+1+1`` dan wordt dit eerst ``"11"+1`` en vervolgens de ``string`` ``"111"``.
Bij ``1+1+"1"`` krijgen we eerste ``2+"1"``, dit geeft vervolgens ``21`` (aangezien C# niet kan bepalen dat de string iets bevat wat een getal kan zijn, en dus besluit om beide operanden als een ``string`` te zien wat altijd de veiligste oplossing is).
{% endhint %}



### Manier 2: String interpolation met $
In de oude dagen van C# gebruikten we ``String.Format()`` (zie hierna) om meerdere strings en variabelen samen te voegen tot één string. Het nadeel van de +-operator uit manier 1 is dat je strings erg lang en onleesbaar worden. 

Dankzij *string interpolation* kan dit wel **waarbij we het ``$``-teken gebruiken vooraan de ``string`` om aan te geven dat specifieke delen van de zin geïnterpoleerd moeten worden**

Door het $-teken **VOOR** de string te plaatsen geef je aan dat alle delen in de string die *tussen accolades staan* als code mogen beschouwd worden. Een voorbeeld maakt dit duidelijk:


```csharp
string result = $"Ik ben {naam} en ik ben {leeftijd} jaar oud.";
```

In dit geval zal de inhoud van de variabele ``naam`` tussen de string op de plek waar nu ``{naam}`` staat geplaatst worden. Idem voor ``leeftijd``.
Zoals je kan zien is dit veel meer leesbare code dan de eerste manier.

Het resultaat zal dan worden: ```Ik ben Finkelstein en ik ben 13 jaar oud.```


#### Berekeningen doen bij string interpolatie
Je mag eender welke *expressie* tussen de accolades zetten bij string interpolation, denk maar aan:


```csharp
string result = $"Ik ben {naam} en ik ben {leeftijd+4} jaar oud.";
```

Alle expressies tussen de accolades zullen eerst uitgevoerd worden voor ze tussen de string worden geplaatst. De uitvoer wordt nu dus: ```Ik ben Finkelstein en ik ben 17 jaar oud.```

Eender welke expressie is toegelaten, dus je kan ook complexe berekeningen of zelfs andere methoden aanroepen:


```csharp
string result = $"Ik ben {leeftijd*leeftijd+(3*2)} jaar oud.";
```

{% hint style='tip' %}
Uiteraard mag je dit dus ook gebruiken wanneer je eenvoudigere zaken naar het scherm wenst te sturen gebruik makende van ``Console.WriteLine`` en interpolatie:


```csharp
Console.WriteLine($"3 maal 9 is {3*9}");
```
{% endhint %}



#### Mooier formatteren
Zowel bij string interpolation (manier 2) als de manier hierna kan je ook bepalen hoe de te tonen variabelen en expressies juist weergegeven moeten worden. Je geeft dit aan door na de expressie, binnen de accolades, een dubbelpunt te plaatsen gevolgd door de manier waarop moet geformatteerd worden.

Wil je bijvoorbeeld een kommagetal tonen met maar 2 cijfers na de komma dan schrijf je:

```csharp
double number = 12.345;
Console.WriteLine($"{number:F2}");
```

Er zal ``12.35`` op het scherm verschijnen. ``F2`` geeft aan dat je een *float* wilt met 2 beduidende cijfers na de komma. 

Merk op dat bij string formatting er **afgerond** wordt. 

{% hint style='tip' %}
Nog enkele nuttige vormen:
* D5: toon een geheel getal als een 5 cijfer getal (``123`` wordt ``00123``) (werkt uiteraard enkel op gehele getallen!)
* E2: wetenschappelijke notatie met 2 cijfers precisie (``12000000`` wordt ``1,20E+007`` i.e. *"1 komma 2 maal tien tot de zevende"*)
* C: geldbedrag (``12,34`` wordt $ 12,34 : teken van valuta afhankelijk van instellingen pc). Het euro teken zal als een ``?`` getoond worden. In de volgende sectie tonen we hoe je dit kan oplossen.

Alle overige format specifiers staan hier opgelijst: **docs.microsoft.com/dotnet/standard/base-types/standard-numeric-format-strings**.
{% endhint %}

Een andere eenvoudige manier om strings te formatteren is door middel van een soort masker bestaande uit 0'n. Dit ziet er als volgt uit:

```csharp
double number = 12.345;
Console.WriteLine($"{number:0.00}");
```

We geven hierbij aan dat de variabele tot 2 cijfers na de komma moet getoond worden. Indien deze maar 1 cijfer na de komma bevat dan deze toch met twee cijfers getoond worden. Volgende voorbeeld toont dit:

```csharp
double number = 12.3;
Console.WriteLine($"{number:0.00}");
```

Er zal ``12,30`` op het scherm verschijnen.

Je kan dit masker ook gebruiken om te verplichten dat getallen bijvoorbeeld steeds met **minimum** 3 cijfers voor de komma getoond worden. Volgende voorbeeld toont dit:

```csharp
double number = 12.3;
double number2 = 99999.3;
Console.WriteLine($"{number:000.00}");
Console.WriteLine($"{number2:000.00}");
```

Geeft als uitvoer:
```text
012.30
99999.30
```

### Manier 3: String.Format()
String interpolatie met het $-teken is een nieuwe C# aanwinst. Je zal echter geregeld documentatie en online code tegenkomen die nog met ``String.Format`` werkt (ook zijn er nog zaken waar het te verkiezen is om ``String.Format`` te gebruiken i.p.v. 1 van vorige manieren). Om die reden bespreken we dit nog in dit boek.

``String.Format`` is een ingebouwde methode die string-interpolatie toelaat op een iets minder intuïtieve manier, als volgt:


```csharp
string result = String.Format("Ik ben {0} en ik ben {1} jaar.", naam, leeftijd);
```

Het getal tussen de accolades geeft telkens aan de hoeveelste parameter na de string hier in de plaats moet gezet worden (0= de eerste, 1= de tweede, enz). De eerste parameter is ``naam``, de tweede is ``leeftijd``.

Volgende code zal een ander resultaat geven:


```csharp
string result = String.Format("Ik ben {1} en ben {1} jaar.", naam, leeftijd);
```

Namelijk: ``Ik ben 13 en ik ben 13 jaar oud.``

{% hint style='tip' %}
Je kan deze vorm van formateren ook toepassen in ``Console.WriteLine`` zonder dat je expliciet ``String.Format`` hiervoor moet aanroepen:


```csharp
Console.WriteLine("Gratis formateren. {0} maal hoera voor .NET!", 3);
```
{% endhint %}


{% hint style='tip' %}
Wanneer we in hoofdstuk 8 arrays uit de doeken gaan doen zal je ontdekken dat alles in de digitale wereld begint te tellen vanaf 0, en niet 1 zoals wij gewend zijn. Het eerste element in een lijst, zoals hier boven, heeft daarom index 0, het tweede 1, enz.
{% endhint %}

## Optellen van char variabelen

We hebben al gezien dat intern een ``char`` als een geheel getal (de UNICODE) wordt voorgesteld. Stel dat we volgende ``char``-variabelen aanmaken. 

```csharp
char letter1 = 'A';
char letter2 = 'B';
```

Bij string mogen we de +-operator gebruiken om 2 strings aan elkaar te plakken. **Bij char mag dat niet!** Of beter, dit mag maar zal niet het resultaat geven dat je mogelijk verwacht wanneer je voor het eerst hiermee leert werken. Oordeel zelf:


```csharp
Console.WriteLine(letter1 + letter2);
```

**Wanneer je deze code uitvoert dan krijg je `131` te zien** (en dus niet "AB" zoals je misschien had verwacht).

Had je dit verwacht? Denk eraan dat het char-type z’n waarde als getallen bijhoudt, de zogenaamde UNICODE-voorstelling van het karakter. Als de compiler het volgende ziet staan:

``letter1 + letter2`` 

dan zal de compiler deze twee waarden letterlijk optellen en het nieuw verkregen getal als resultaat geven:

* De UNICODE-voorstelling van `A` is 0x041 oftewel **`65`**. In het geheugen staat dus het geheel getal ``65``.
* `B` wordt voorgesteld door **`66`**.
* Als we dus de variabelen ``letter1`` en ``letter2`` optellen geeft dit **131**. 


{% hint style='tip' %}
Je zou misschien verwachten dat C# vervolgens het element op plaats 131 in de UNICODE tabel zou tonen. Dat is niet zo: omdat de ``+`` operator niet is gedefinieerd voor het ``char`` datatype maar wel voor het ``int`` datatype, besluit de compiler om de twee operanden (``letter1`` en ``letter2``) als ``int`` operanden te hanteren. Aangezien ``int+int`` een ``int`` als resultaat geeft, krijgen we dus ``131`` op het scherm en niet het UNICODE element 131 (we zien in het volgende hoofdstuk hoe je dit wel kunt doen).
{% endhint %}
