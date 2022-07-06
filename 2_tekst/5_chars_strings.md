# Tekst gebruiken in code

Ieder teken dat je op je toetsenbord kunt intypen is een ``char``. Je toetsenbord bevat echter maar een kleine selectie van alle mogelijkheden (vergelijk jouw toetsenbord bijvoorbeeld maar eens met dat van iemand in pakweg Spanje, Tunesië of China). Voor we gaan kijken hoe in C# input van het toetsenbord wordt uitgelezen moeten we even kijken hoe al die duizenden tekens in een computer eigenlijk worden voorgesteld. Het antwoord: de **UNICODE standaard**.  Heel lang geleden was er al een standaard die uniformiseerde hoe een tekens moest worden voorgesteld: de ASCII-standaard. Deze standaard zei letterlijk "dat teken wordt voorgesteld door die hexadecimale waarde". Iedereen die de ASCII-standaard volgde kon dan zo alle, in ASCII gedefinieerde,  tekens naar elkaar communiceren. 

UNICODE is de standaard die de  ASCII-standaard opvolgt omdat die te klein (qua aantal bits) bleek te zijn om naar de toekomst toe de ontelbare nieuwe tekens in voor te stellen. De ASCII standaard kan 128 karakters voorstellen (m.b.v. 7 bit), wat uiteraard in het niets valt in vergelijking met de meer dan 1 miljoen tekens in UNICODE (dankzij de 16 bit voorstelling). Uiteraard heeft de UNICODE-standaard die eerste 128 van ASCII als eerste gezet en zijn beide tabellen dus compatibel (*UNICODE is een superset van ASCII*). Dankzij UNICODE kunnen we nu elke smiley, letter uit elke alfabet en zelfs gewoon icoontjes, wereldwijd delen met elkaar op dezelfde manier.

Voor de statistieknerds onder ons: er zijn 1,111,998 UNICODE karakters mogelijk. Momenteel zijn er daarvan 137,929 gedefinieerd. We hebben dus nog wel wat plek.


![De eerste 128 karakters met hun waarden (bron Wikipedia)](../assets/1_csharpbasics/ascii.png)

De eerste 32 karakters zijn "onzichtbare" karakters die een historische reden (in ASCII) hebben om in de lijst te staan, maar sommige ervan zijn ondertussen niet meer erg nuttig. Origineel werd ASCII ontwikkeld als standaard om via de telegraaf te combineren. Vandaar dat vele van deze karakters commando's lijken om oude typemachines aan te sturen (line feed, bell, form feed, etc) want dat zijn ze dus ook effectief!

## Tekst datatypes

In het vorige hoofdstuk werkten we vooral met getallen en haalden we maar kort het ``string`` en ``char`` datatype aan. In dit hoofdstuk gaan we dieper in op deze 2 veelgebruikte datatypes.

### Char

Een **enkel karakter** (cijfer, letter, leesteken, enz.) als 'tekst' opslaan kan je doen door het `char`-type te gebruiken. Zo kan je bijvoorbeeld één enkel karakter als volgt tonen:

```java
char eenLetter = 'X';
Console.WriteLine("eenLetter=" + eenLetter);
```

Het is belangrijk dat je de apostrof (``'``) niet vergeet voor en na het karakter dat je wenst op te slaan daar dit de literal voorstelling van `char`-literals is. Zonder die apostrof denkt de compiler dat je een variabele wenst aan te roepen van die naam.

Je kan eender welk UNICODE-teken in een `char` bewaren, namelijk een letter, een cijfer of een special teken zoals `%`, `$`, `*`, `#`, enz. **Intern wordt de UNICODE van het character bewaard in de variabele, zijnde een 16 bit getal**.

Merk dus op dat volgende lijn: ``char eenGetal = '7';`` weliswaar een getal als teken opslaat, maar dat intern de compiler deze variabele steeds als een character zal gebruiken. **Als je dit cijfer zou willen gebruiken als effectief cijfer om wiskundige bewerkingen op uit te voeren, dan zal je dit eerst moeten converteren naar een getal** (we zullen dit in hoofdstuk 4 uitleggen).



### String

**Een ``string`` is een reeks van 0, 1 of meerdere `char`-elementen.**

We gebruiken het ``string`` datatype om tekst voor te stellen. Je begrijpt waarschijnlijk zelf wel waarom het ``string`` datatype een belangrijk en veelgebruikt type is in eender welke programmeertaal: er zijn maar weinig applicaties die niet minstens enkele lijnen tekst vertonen (ja, zelfs Flappy Bird had tekst, of hoe denk je dat je score werd voorgesteld op het scherm?).

{% hint style='tip' %}
In hoofdstuk 8 zullen we ontdekken dat strings eigenlijk zogenaamde arrays zijn. 
{% endhint %}


#### Strings declareren
Merk op dat we bij een ``string`` literal gebruik maken van aanhalingstekens (`"`) terwijl bij een ``char`` literal we een apostrof gebruiken (`'`). Dit is de manier om een string van een char te onderscheiden (naast het feit dat een string uit meer dan 1 element kan bestaan)

Volgende, uiterst boeiende, code geeft drie keer het cijfer 1 onder elkaar op het scherm, maar de eerste keer gaat het om het een ``char`` (enkelvoudig teken), dan en een ``string`` (reeks van tekens) en dan een ``int`` (effectief getal):

```java
char eenKarakter = '1'; 
string eenString = "1"; 
int eenGetal = 1;
 
Console.WriteLine(eenKarakter);
Console.WriteLine(eenString);
Console.WriteLine(eenGetal);
```

Het programma zal driemaal een ``1`` onder elkaar tonen. Boeiend programma hoor.
