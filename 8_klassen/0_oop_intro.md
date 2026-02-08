
# Object georiënteerd programmeren <!--\label{ch:9}-->

Tot nu toe heb je vooral geleerd om *gestructureerd* te programmeren - soms ook wel *procedureel* programmeren genoemd - een programmeerconcept uit de jaren zestig. Hierbij schrijf je code gebruik makend van methoden, loops en beslissingsstructuren. 

Hoewel gestructureerd programmeren erg nuttig blijft, wordt het bij complexere applicaties vaak minder intuïtief en soms nodeloos complex. Een middelgroot project verzandt al gauw in moeilijk te onderhouden spaghetti code.
 
Er is echter een alternatief: **object georiënteerd Programmeren** (**OOP**, *Object Oriented Programming*). OOP bouwt voort op gestructureerd programmeren, maar maakt het mogelijk om veel krachtigere applicaties te ontwikkelen.

Bij OOP draait alles rond **klassen en objecten** die intern nog steeds gestructureerde code  bevatten. Alle bekende concepten zoals loops, methoden en beslissingsstructuren blijven bestaan. We gaan ze echter verpakken in handige, kleinere aparte klassen. Met OOP wordt onze code **modulair, leesbaarder en onderhoudsvriendelijker**. Bovendien wordt de code krachtiger en kunnen we complexere problemen eenvoudiger oplossen.


>![](../assets/attention.png)Ik zet "oplossen" tussen aanhalingstekens. Net zoals alles binnen dit domein ben jij als programmeur uiteindelijk degene die het boeltje moet oplossen. Code, programmeerparadigma's en bibliotheken zijn niet meer dan nuttig gereedschap in jouw arsenaal van programmeertools. Als jij beslist om een hamer als zaag te gebruiken... Tja, dan houd ik m'n hart vast voor het resultaat. 

Dit geldt ook voor de technieken die je nog in dit boek gaat leren: ze zijn "een tool", niets meer. Jij zal ze nog steeds zo optimaal mogelijk moeten leren gebruiken. Uiteraard is het doel van dit boek je zo duidelijk mogelijk het verschil én de bruikbaarheid van de verschillende nieuwe technieken aan te leren.

## C# is OO in hart en nieren


Toen C# werd ontwikkeld in 2001 was één van de hoofddoelen van de programmeertaal om *"een eenvoudige, moderne, objectgeoriënteerde programmeertaal voor algemene doeleinden"* te worden. **C# is van de grond af opgebouwd met het OOP paradigma  als primaire drijfveer.** Een paradigma is een algemeen geaccepteerde manier van denken en doen binnen een bepaald vakgebied, in dit geval binnen de programmeerwereld.

Wanneer we nieuwe programma's in C# ontwikkelden dan zagen we hier reeds bewijzen van. Zo zagen we steeds het keyword ``class`` bovenaan staan, telkens we een nieuw project aanmaakten:

```csharp
namespace WorldDominationTool
{
    internal class Program
    {
```

De klasse ``Program`` zorgt ervoor dat ons programma voldoet aan de C# afspraken die zeggen dat alle C# code in klassen moet staan. 



>![](../assets/care.png)Duizend mammoeten en sabeltandtijgers! Ik dacht dat ik nu wel mee zou zijn met alles wat C# me zou voorschotelen. Helaas, wolharige neushoorn-kaas, niet dus. Ik ga een voorspelling doen: van alle hoofdstukken in dit boek, wordt dit hoofdstuk hetgene waar je het meest je tanden op gaat stuk bijten. Hou dus vol, geef niet te snel op en kom geregeld hier terug. Succes gewenst!

<!-- \newpage -->



### Een wereld zonder OOP: Pong

Om de kracht van OOP te demonstreren gaan we een applicatie van lang geleden (deels) herschrijven gebruik makende van de kennis van de vorige 8 hoofdstukken. We gaan de arcadehal klassieker "Pong" deels namaken, waarbij we als doel hebben om een balletje alvast op het scherm te laten botsen. Een rudimentaire oplossing zou de volgende kunnen zijn:

```csharp
Console.CursorVisible = false;
int balX = 20;
int balY = 20;
int vX = 2;
int vY = 1;
while (true)
{
    //vX van richting veranderen aan de randen
    if (balX + vX >= Console.WindowWidth || balX+vX < 0)
    {
        vX = -vX;
    }
    balX = balX + vX; //X positie updaten
    //vY van richting veranderen aan de randen
    if (balY + vY >= Console.WindowHeight || balY+vY < 0)
    {
        vY = -vY;
    }
    balY = balY + vY; //Y positie updaten
    //Output naar scherm sturen
    Console.SetCursorPosition(balX, balY);
    Console.Write("O");
    System.Threading.Thread.Sleep(50); //50 ms wachten
    Console.Clear();
}
```

Hopelijk begrijp je deze code. Test ze maar eens in een programma. Zoals je zal zien krijgen we een balletje (``"O"``) dat over het scherm vliegt en telkens van richting verandert wanneer het aan de randen van het applicatievenster komt. De belangrijkste informatie zit in de variabelen ``balX``, ``balY`` die de huidige positie van het balletje bevatten. Voorts zijn ook ``vX`` en ``vY`` belangrijk: hierin houden we bij in welke richting (en met welke snelheid) het balletje beweegt (een zogenaamde bewegingsvector).

<!-- \newpage -->


#### Extra balletjes?

Dit soort applicatie in C# schrijven met behulp van gestructureerde programmeer-concepten is redelijk eenvoudig. Maar wat als we nu 2 balletjes nodig hebben? Laten we arrays even links laten liggen en het gewoon eens naïef oplossen. Al na enkele lijnen kopiëren merken we dat onze code ongelooflijk rommelachtig gaat worden en we bijna iedere lijn moeten dupliceren:

```csharp
Console.CursorVisible = false;
int balX = 20;
int balY = 20;
int vX = 2;
int vY = 1;

int bal2X = 10;
int bal2Y = 8;
int v2X = 2;
int v2Y = -1;

while (true)
{
    if (balX + vX >= Console.WindowWidth || balX+ vX < 0)
    {
        vX = -vX;
    }
    if (bal2X + v2X >= Console.WindowWidth || bal2X + v2X < 0)
    {
        v2X = -v2X;
    }

    balX = balX + vX;
    bal2X = bal2X + v2X;
    //enzovoort
```

**Bijna iedere lijn code moeten we verdubbelen.** Arrays zouden dit probleem deels kunnen oplossen, maar we krijgen dan in de plaats de complexiteit van werken met arrays op ons bord. Dat is voor 2 balletjes misschien wat overdreven. Het zal op de koop toe onze terug minder leesbaar maakt.

<!-- \newpage -->


### Een wereld met OOP: Pong

Uiteraard zijn we nu eventjes gestructureerd programmeren aan het demoniseren, dit is echter een bekend 21e eeuws trucje om je punt te maken. 

Wanneer we Pong met het OOP paradigma willen aanpakken dan is het de bedoeling dat we werken met klassen en objecten. 

Net zoals aan de start van dit boek ga ik je ook nu even in het diepe gedeelte van het bad gooien. Wees niet bang, ik zal je er tijdig uithalen!  Je zal versteld staan hoeveel code je eigenlijk zult herkennen.

Om Pong in OOP te maken hebben we eerst een klasse nodig waarin we ons balletje gaan beschrijven, zonder dat we al een balletje hebben. En dat ziet er zo uit:

```csharp
internal class Balletje
{
    //Eigenschappen
    public int X { get; set; }
    public int Y { get; set; }
    public int VX { get; set; }
    public int VY { get; set; }

    //Methoden
    public void Update()
    {
        if (X + VX >= Console.WindowWidth || X + VX < 0)
        {
            VX = -VX;
        }
        X = X + VX;


        if (Y + VY >= Console.WindowHeight || Y + VY < 0)
        {
            VY = -VY;
        }
        Y = Y + VY;
    }

    public void TekenOpScherm()
    {
        Console.SetCursorPosition(X, Y);
        Console.Write("O");      
    }
}
```

{% hint style='tip' %}
De code voor een nieuwe klasse schrijf je best in een apart bestand in je project. Klik bovenaan in de menu balk op "Project" en kies dan "Add class...". Geef het bestand de naam "Balletje.cs". 
{% endhint %}


Bijna alle code van zonet hebben we hier geïntegreerd in een ``class Balletje``, maar er zit duidelijk een nieuw sausje over. Vooral aan het begin zien we onze 4 variabelen terugkomen in een nieuw kleedje: namelijk als eigenschappen oftewel *properties* (herkenbaar aan de ``get`` en ``set`` keywords). 

Maar al bij al lijkt de code grotendeels op wat we al kenden. En dat is goed nieuws. OOP gooit de vorige hoofdstukken niet in de vuilbak, het gaat als het ware een extra laag over het geheel leggen. Let ook op het essentiële woordje ``class`` bovenaan, daar draait alles natuurlijk om: **klassen en objecten**. 

{% hint style='tip' %}
Een klasse is een blauwdruk van een bepaalde soort 'dingen' of objecten. Objecten zijn de "echte" dingen die werken volgens de beschrijving van de klasse. Ja ik heb zonet 2x hetzelfde verteld, maar het is essentiëel dat je het verschil tussen de termen **klasse** en **object** goed begrijpt. 
{% endhint %}


Laten we eens een **balletje-object** in het leven roepen. In de main schrijven we daarom dit:

```csharp
Console.CursorVisible = false;
Balletje bal1 = new Balletje();
bal1.X = 20;
bal1.Y = 20;
bal1.VX = 2;
bal1.VY = 1;
```

Ok, interessant. Die ``new`` heb je al gezien wanneer je met ``Random`` ging werken en de code erna is ook nog begrijpbaar: we stellen eigenschappen van het nieuwe ``bal1`` object in. En nu komt het! Kijk hoe eenvoudig onze volledig ``main`` nu is geworden:

```csharp
static void Main(string[] args)
{
    Console.CursorVisible = false;
    Balletje bal1 = new Balletje();
    bal1.X = 20;
    bal1.Y = 20;
    bal1.VX = 2;
    bal1.VY = 1;

    while (true)
    {
        bal1.Update();
        bal1.TekenOpScherm();

        System.Threading.Thread.Sleep(50);
        Console.Clear();
    }
}
```

De loopcode is herleid tot 2 aanroepen van **methoden op het ``bal1`` object**: ``.Update()`` en ``.TekenOpScherm``. 

Run deze code maar eens. Inderdaad, deze code doet exact hetzelfde als hiervoor. Ook nu krijgen we 1 balletje dat op het scherm over en weer botst. 



En nu - abracadabra - kijk goed hoe eenvoudig onze code blijft als we 2 balletjes nodig hebben:

```csharp
Console.CursorVisible = false;
Balletje bal1 = new Balletje();
bal1.X = 20;
bal1.Y = 20;
bal1.VX = 2;
bal1.VY = 1;

Balletje bal2 = new Balletje();
bal2.X = 10;
bal2.Y = 8;
bal2.VX = 2;
bal2.VY = -1;

while (true)
{
    bal1.Update();
    bal2.Update(); //zo simpel!
    bal1.TekenOpScherm();
    bal2.TekenOpScherm(); //wow, zooo simpel :)
    System.Threading.Thread.Sleep(50);
    Console.Clear();
}
```

Dit is de volledige code om 2 balletjes te hebben. Hoe mooi is dat?!

**De kracht van OOP zit hem in het feit dat we de logica IN DE OBJECTEN ZELF plaatsen. De objecten zijn met andere woorden verantwoordelijk om hun eigen gedrag uit te voeren gebaseerd op externe impulsen en hun eigen interne toestand.** In onze main zeggen we aan beide balletjes "update je zelf eens", gevolgd door "teken je zelf eens". 






Wanneer we 3 of meer balletjes zouden nodig hebben dan zullen we best arrays in de mix moeten gooien. Onze code blijft echter véél eenvoudiger én krachtiger dan wanneer we in het voorgaande enkel de kennis gebruikten die we totnogtoe hadden. Omdat we toch al in het diepe eind zitten, zal ik hier toch al eens tonen hoe we 100 balletjes op het scherm kunnen laten botsen (we gaan ``Random`` gebruiken zodat er wat willekeurigheid in de balletjes zit):

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


De reden dat we nu twee loops gebruiken, is omdat we in de updatefase eerst alle objecten willen bijwerken (soms in relatie tot andere objecten) voordat we alles opnieuw op het scherm tekenen. Anders kan het zijn dat je vreemde effecten te zien krijgt als je bijvoorbeeld balletjes tegen elkaar wil laten wegbotsen.

Ok, zwem maar snel naar de kant. We gaan al het voorgaande van begin tot einde uit de doeken doen! Leg die handdoek niet te ver weg, we gaan hem nog nodig hebben.

<!-- \newpage -->


## Klassen en objecten

Een elementair aspect binnen OOP is het verschil begrijpen tussen een klasse en een object.

Wanneer we meerdere objecten gebruiken van dezelfde soort dan kunnen we zeggen dat deze objecten allemaal deel uitmaken van een zelfde klasse. **Het OOP paradigma houdt ook in dat we de echte wereld gaan proberen te modeleren in code**. OOP laat namelijk toe om onze code zo te structureren zoals we dat ook in het echte leven doen. Alles om ons heen behoort tot een bepaalde klasse die alle objecten van dat type beschrijven. 

Neem eens een kijkje aan een druk kruispunt waar fietsers, voetgangers, auto's en verkeerslichten samenkomen[^jan]. Het is een erg hectisch geheel, toch kan je alles dat je daar ziet *classificeren*. We zien bijvoorbeeld allemaal mens-objecten die tot de klasse van de Mens behoren, maar ook:

* Alle mensen hebben gemeenschappelijke eigenschappen (binnen deze beperkte context van een kruispunt): ze bewegen of staan stil (gedrag), ze hebben een bepaalde kleur van jas (eigenschap). 
* Alle auto's behoren tot een klasse Auto. Ze hebben gemeenschappelijke zaken zoals:  een bouwjaar (eigenschap), ze werken op een bepaalde vorm van energie (eigenschap) en ze staan stil of bewegen (gedrag).
* Ieder verkeerslicht behoort tot de klasse VerkeersLicht.
* Fietsers behoren tot de klasse Fietser.

[^jan]:Dit voorbeeld is gebaseerd op de inleiding van het inzichtvolle boek "Handboek objectgeoriënteerd programmeren" door Jan Beurghs (EAN: 9789059406476).



### Definitie klasse en object

Volgende 2 definities druk je best af op een grote poster die je boven je bed hangt:

* **Een klasse** is als een **blauwdruk** (of prototype) dat het gedrag en toestand beschrijft van alle objecten van deze klasse.
* Een individueel **object** is een **instantie** van een klasse en heeft een eigen *toestand*, *gedrag* en *identiteit*.

Objecten zijn instanties met een eigen levenscyclus die wordt gekenmerkt door:

* **Gedrag**: deze wordt beschreven door de **methoden** in de klasse.
* **Toestand**: deze kan wijzigen door zijn eigen gedrag, of door externe impulsen en wordt bepaald door **datavelden** die beschreven staan in de klasse (properties en instantievariabelen). 
* **Identiteit** : een unieke naam van object zodat andere objecten ermee kunnen interageren.

{% hint style='tip' %}
Je zou dit kunnen vergelijken met het grondplan voor een huis dat tien keer in een straat zal gebouwd worden. Het plan is de *klasse*. De effectieve huizen die we bouwen aan de hand van dit plan zijn de instanties of objecten van deze klasse. Ieder huis heeft een eigen toestand (ander type bakstenen, wel of geen zonnepannelen) en gedrag (rolluiken gaan open als de zon opkomt).
{% endhint %}


De klasse beschrijft het algemene **gedrag** van de individuele objecten. Dit gedrag wordt meestal bepaald door de interne staat van ieder object op zichzelf, de zogenaamde **eigenschappen**. Nemen we het voorbeeld van de klasse Auto: de huidige snelheid van een individueel auto-object is mogelijks gebaseerd op het merk (eigenschap) van die auto, alsook welke energiebron (eigenschap) die auto heeft. 

Voorts kunnen objecten ook beïnvloed worden door 'de buitenwereld': naast de interne staat van ieder object, leven de objecten natuurlijk in een bepaalde context, zoals een druk kruispunt. Andere objecten op dat kruispunt kunnen invloed hebben op wat een auto-object doet. 

Met andere woorden: we kunnen 'van buiten uit' vaak ook het gedrag en de interne staat van een object aanpassen. We hebben dit reeds zien gebeuren in het Pong-voorbeeld: de interne staat van ieder individueel balletjes-object is z'n positie alsook z'n richtingsvector. De buitenwereld, in dit geval onze ``Main`` methode kon echter de objecten manipuleren:

* Het gedrag van een balletje konden we aanpassen met behulp van de ``Update`` en ``TekenOpScherm`` methode.
* De interne staat via de eigenschappen die zichtbaar zijn aan de buitenwereld (dankzij het ``public`` keyword) .

{% hint style='tip' %}
Wanneer je later de specificaties voor een opdracht krijgt en snel wilt ontdekken wat potentiële klassen zijn, dan is het een goede tip om op zoek te gaan naar de zelfstandige naamwoorden (*substantieven*) in de tekst. Dit zijn meestal de objecten en/of klassen die jouw applicatie zal nodig hebben.
{% endhint %}


{% hint style='tip' %}
95% van de tijd zullen we in dit boek de voorgaande definitie van een klasse beschrijven, namelijk de blauwdruk voor de objecten die er op gebaseerd zijn. Je zou kunnen zeggen dat de klasse een fabriekje is dat objecten kan maken.
Echter, wanneer we het ``static`` keyword zullen bespreken gaan we ontdekken dat heel af en toe een klasse ook als een soort object door het leven kan gaan. Heel vreemd allemaal!
{% endhint %}





### Abstractie en encapsulatie

Een belangrijk concept bij OOP is het **Black-box** principe waarbij we de afzonderlijke objecten en hun werking als zwarte dozen gaan beschouwen. 

Neem het voorbeeld van de auto: deze is in de echte wereld ontwikkeld volgens het blackbox-principe. De werking van de auto kennen tot in het kleinste detail is niet nodig om met een auto te kunnen rijden. De auto biedt een aantal zaken aan de buitenwereld aan (het stuur, pedalen, het dashboard), wat we de **"interface"** noemen. De interface kan je gebruiken om de interne staat van de auto uit te lezen of te manipuleren. Stel je voor dat je moest weten hoe een auto volledig werkte voor je ermee op de baan kon...

Binnen OOP wordt dit blackbox-concept **abstractie** en **encapsulatie** genoemd. Het doel van OOP is programmeurs zoveel mogelijk af te schermen van de interne werking van je klasse code. Vergelijk het met de methoden uit hoofdstuk 7: "if it works, it works" en dan hoef je niet in de code van de methode te gaan zien wat er juist gebeurt telkens je de methode wil gebruiken.

Bij encapsulatie bedoelen we dat we alle zaken die samen horen bij een auto samenvoegen tot één geheel. De motor, de banden, ieder componentje in de motor, enz. Al deze zaken *encapsuleren* we in één geheel. Vervolgens gaan we met de hulp van abstractie de complexiteit naar de buitenwereld toe kunnen vereenvoudigen.

Kortom: *hoe minder de buitenwereld moet weten om met een object te werken, hoe beter.* 

Beeld je in dat je 10 lijnen code nodig had om een random getal te genereren. Niemand zou de klasse ``Random`` nog gebruiken. Dankzij de ontwikkelaar van deze klasse hoeven we maar 2 zaken te kunnen:

* Een ``Random``-object aanmaken met ``new``/
* De ``Next``-methode aanroepen om een getal uit het object te krijgen

Wat er nu juist in die methode gebeurt boeit ons niet. *It just works!* Met dank aan abstractie en de kracht van OOP.

### Tijd voor taart

Een truukje om de belangrijkste concepten van OOP te onthouden is het acroniem **A PIE**, dat staat voor:

* **A**bstractie
* **P**olymorfisme
* **I**nheritance, oftewel overerving
* **E**ncapsulatie

Abstractie (het vereenvoudigen van de complexe, interne structuur van een klasse) en encapsulatie (alle aspecten die in de klasse horen) hebben we net besproken. Polymorfisme zullen we pas in hoofdstuk 16 aanpakken. Inheritance komt al in hoofdstuk 13 in actie. Nog even geduld dus.

### Objecten in de woorden van Steve Jobs

Steve Jobs, de oprichter van Apple, was een fervent fan van OOP. In een interview in 1994 voor het Rolling Stone magazine gaf hij volgende uitleg:

*"Objects are like people. They’re living, breathing things that have knowledge inside them about how to do things and have memory inside them so they can remember things. And rather than interacting with them at a very low level, you interact with them at a very high level of abstraction, like we’re doing right here.*

*Here’s an example: If I’m your laundry object, you can give me your dirty clothes and send me a message that says, "Can you get my clothes laundered, please." I happen to know where the best laundry place in San Francisco is. And I speak English, and I have dollars in my pockets. So I go out and hail a taxicab and tell the driver to take me to this place in San Francisco. I go get your clothes laundered, I jump back in the cab, I get back here. I give you your clean clothes and say, "Here are your clean clothes."*

*You have no idea how I did that. You have no knowledge of the laundry place. Maybe you speak French, and you can’t even hail a taxi. You can’t pay for one, you don’t have dollars in your pocket. Yet, I knew how to do all of that. And you didn’t have to know any of it. All that complexity was hidden inside of me, and we were able to interact at a very high level of abstraction. That’s what objects are. They encapsulate complexity, and the interfaces to that complexity are high level."*

Vooral die laatste zin verdient het om nog eens in vet herhaald te worden: **"They encapsulate complexity, and the interfaces to that complexity are high level."**


>![](../assets/attention.png)Ik zie dat je gereedsschapkist al aardig gevuld is. Zoals je misschien al gemerkt hebt aan deze sectie, zullen we vanaf nu ook geregeld minder "praktische" en eerder "filosofische" zaken tegenkomen. Maar wees gerust, je zal toch een grotere gereedsschapkist nodig hebben. Echter, net zoals een voorman niet alleen moet kunnen metsen en timmeren, maar ook stabiliteitsplannen begrijpen, zal ook jij moeten begrijpen wat de grotere ideeën achter bepaalde concepten zijn.
>
>Zet nu je helm maar op, want in de volgende sectie gaan we wel degelijk onze handen lekker vuil maken!




