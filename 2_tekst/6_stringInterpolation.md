## Strings samenvoegen

Tot nogtoe gebruikten we de +-operator om strings aan elkaar te plakken. We gaan deze manier meer in detail bekijken, gevolgd door een moderner alternatief: door middel van string interpolatie met de ``$``-notatie.


In de volgende sectie gaan we van volgende informatie uit:

* Stel dat je 2 variabelen hebt ``int leeftijd = 13`` en ``string naam = "Finkelstein"``.
* We willen de inhoud van deze variabelen samenvoegen in een nieuwe ``string zin`` die zal bestaan uit de tekst: ``Ik ben Finkelstein en ik ben 13 jaar.``



### String samenvoegen met de +-operator

Je kan strings en variabelen eenvoudig bij elkaar 'optellen' zoals we in het begin van dit boek hebben gezien. Ze worden dan achter elkaar geplakt (**geconcateneerd**). 

```csharp
string zin = "Ik ben " + naam + " en ik ben " + leeftijd+ " jaar.";
```

Let er op dat je tussen de aanhalingsteken (binnen de strings) spaties zet indien je het volgende deel niet tegen het vorige deel wilt *plakken*. Is hiermee alles gezegd?! Neen, toch even goed opletten hier. **De volgorde van strings met andere types samenvoegen bepaalt wat de uitvoer zal zijn.** 

Kijk zelf:

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

Kijken we dus naar ``"1"+1+1`` dan wordt dit eerst ``"11"+1`` en vervolgens dit ``"111"``.

Bij ``1+1+"1"`` krijgen we eerst ``2+"1"``. Dit geeft vervolgens ``21``. Aangezien C# niet kan bepalen dat de string iets bevat wat een getal kan zijn, en dus besluit om beide operanden als een ``string`` te zien wat altijd de veiligste oplossing is.



### String interpolation met $-notatie

Het nadeel van de +-operator is dat je strings soms erg lang en onleesbaar worden. 

Dankzij *string interpolation* kan dit wel **waarbij we het ``$``-teken gebruiken vooraan de ``string`` om aan te geven dat specifieke delen van de zin geïnterpoleerd moeten worden**

Door het $-teken **VOOR** de string te plaatsen geef je aan dat alle delen in de string die *tussen accolades staan* als code mogen beschouwd worden. Een voorbeeld maakt dit duidelijk:


```csharp
string zin = $"Ik ben {naam} en ik ben {leeftijd} jaar.";
```

In dit geval zal de inhoud van de variabele ``naam`` tussen de string op de plek waar nu ``{naam}`` staat geplaatst worden. Idem voor ``leeftijd``.
Zoals je kan zien is dit veel meer leesbare code dan de eerste manier.

Het resultaat zal dan worden: ``Ik ben Finkelstein en ik ben 13 jaar.``


#### Berekeningen doen bij string interpolatie

Je mag eender welke *expressie* tussen de accolades zetten bij string interpolation, denk maar aan:
```csharp
string zin = $"Ik ben {leeftijd+4} jaar.";
```

Alle expressies tussen de accolades zullen eerst uitgevoerd worden voor ze tussen de string worden geplaatst. De uitvoer wordt nu dus: ```Ik ben 17 jaar.```

Eender welke expressie is toegelaten, dus je kan ook complexe berekeningen of zelfs andere methoden aanroepen:


```csharp
string zin = $"Ik ben {leeftijd*leeftijd+(3*2)} jaar.";
```

{% hint style='tip' %}
Uiteraard mag je dit dus ook gebruiken wanneer je eenvoudigere zaken naar het scherm wenst te sturen gebruik makende van ``Console.WriteLine`` en interpolatie:


```csharp
Console.WriteLine($"3 maal 9 is {3*9}");
```
{% endhint %}



### Strings mooier formatteren

Bij string interpolation kan je ook extra informatie meegeven hoe het resultaat juist weergegeven moet worden. Dit noemen we *formatteren*. Je geeft dit aan door na de expressie, binnen de accolades, een dubbelpunt te plaatsen gevolgd door de manier waarop moet geformatteerd worden.

Wil je een kommagetal tonen met maar 2 cijfers na de komma dan schrijf je:

```csharp
double number = 12.345;
Console.WriteLine($"{number:F2}");
```

Er zal ``12.35`` op het scherm verschijnen. ``F2`` na het dubbelpunt geeft aan dat je een *float* wilt met 2 beduidende cijfers na de komma. 

Merk op dat bij string formattering er **afgerond** wordt, en dus niet *afgekapt*. 


Nog enkele nuttige vormen:

* ``D5``: toon een geheel getal als een 5 cijfer getal. ``123`` wordt ``00123``. Maar ``123456`` zal volledig getoond worden. De ``Dx`` formattering werkt enkel op gehele getallen. Uiteraard zijn er dus ook andere varianten zoals ``D2``, etc.
* ``E2``: wetenschappelijke notatie met 2 cijfers precisie (``12000000`` wordt ``1,20E+007`` *"1 komma 2 maal tien tot de zevende"*). Ook hier hoeft het getal niet 2 te zijn, maar geef je dus via het getal aan tot hoeveel cijfers na de komma je wilt tonen.
* ``C``: geldbedrag. ``12,34`` wordt € 12,34. Het teken en het aantal beduidende cijfers is van de landinstellingen van de pc waarop je code wordt uitgevoerd. Het euro teken zal mogelijk als een ``?`` getoond worden. In de volgende sectie tonen we hoe je dit kan oplossen.

Alle overige format specifiers kan je in de documentatie opzoeken[^formatdoc].

[^formatdoc]: Zie [docs.microsoft.com/dotnet/standard/base-types/standard-numeric-format-strings](https://docs.microsoft.com/dotnet/standard/base-types/standard-numeric-format-strings).

<!-- \newpage -->


#### Formateren met een masker

Een andere eenvoudige manier om strings te formatteren is door middel van een masker bestaande uit 0'n. Dit ziet er als volgt uit:

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

{% hint style='tip' %}
Vanaf nu zal ik bijna altijd string interpolatie gebruiken doorheen het boek. Dit is de meest moderne aanpak en zal 99% van de tijd meer leesbare code geven.

In de appendix leg ik uit hoe je vroeger met behulp van ``String.Format()`` strings moest samenvoegen (daar je dit soms nog in *legacy* code zal tegenkomen).
{% endhint %}

<!-- \newpage -->


## Optellen van char variabelen

We hebben al gezien dat intern een ``char`` als een geheel getal wordt voorgesteld. Stel dat we volgende ``char``-variabelen aanmaken: 

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
Je zou misschien verwachten dat C# vervolgens het element op plaats 131 in de UNICODE tabel zou tonen. 

Dat is niet juist: de ``+``- operator is niet gedefinieerd voor het ``char`` datatype, maar wel voor het ``int`` datatype. Daarom beschouwt de compiler de operanden ``letter1`` en ``letter2`` als ``int``. De som van twee ``int`` waarden geeft een ``int`` resultaat. We zien daarom ``131`` op het scherm in plaats van het UNICODE karakter met waarde 131 (een Latijnse ``i`` zonder punt) . In het volgende hoofdstuk leren we hoe je dit wel kunt doen.
{% endhint %}
