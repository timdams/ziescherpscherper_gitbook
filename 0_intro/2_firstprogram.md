
## Console-applicaties

Een console-applicatie is een programma dat zijn in- en uitvoer via een klassiek commando/shell-scherm toont. Zoals al verteld: in dat boek ga ik je enkel console-applicaties leren maken. Grafische Windows applicaties komen niet aan bod.

### In en uit - ReadLine en WriteLine

Een programma zonder invoer van de gebruiker is niet erg boeiend. De meeste programma's die we leren schrijven vereisen dan ook "input" (**IN**). We moeten echter ook zaken aan de gebruiker kunnen tonen. Denk bijvoorbeeld aan een foutboodschap of de uitkomst van een berekening tonen. Dit vereist dat er ook "output" (**UIT**) naar het scherm kan gestuurd worden.


![In het begin zullen al je applicaties deze opbouw hebben.](../assets/1_csharpbasics/inuit.png)

Console-applicaties maken in C# vereist dat je minstens twee belangrijke C# methoden leert gebruiken:

* Met behulp van **``Console.ReadLine()``** kunnen we input van de gebruiker inlezen en in ons programma verwerken.
* Via **``Console.WriteLine()``** kunnen we tekst op het scherm tonen.

<!-- \newpage -->


### Je eerste console programma

Sluit het eerder gemaakte "MyFirstProject" project af en herstart Visual Studio. Maak nu een nieuw console-project aan. Noem dit project *Demo1*. Open het Program.cs bestand via de solution Explorer (indien het nog niet open is). **Veeg de code die hier reeds staat niet weg!**

Voeg onder de lijn ``Console.WriteLine("Hello World!");`` volgende code toe (vergeet de puntkomma niet):


```csharp
Console.WriteLine("Hoi, ik ben het!");
```


Zodat je dus volgende code krijgt:

```csharp
namespace Demo1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Console.WriteLine("Hoi, ik ben het");
        }
    }
}
```

Compileer deze code en voer ze uit: **druk hiervoor weer op het groene driehoekje bovenaan**. Of via het menu Debug en dan Start Debugging.

{% hint style='danger' %}
**Moet ik niets bewaren?**

Neen. Telkens je op de groene "build en run" knop duwt worden al je aanpassingen automatisch bewaard. Trouwens: **Kies nooit voor "save as..."!** want dan bestaat de kans dat je project niet meer compileert. Dit zal aardig wat problemen in je project voorkomen, geloof me maar.
{% endhint %}

{% hint style='danger' %}
Laat je niet afschrikken door wat er nu volgt. Ik gooi je even in het diepe gedeelte van het zwembad maar zal je er op tijd uithalen . Vervolgens kunnen we terug in het babybadje rustig op de glijbaan kunnen gaan spelen en C# op een trager tempo verder ontdekken.
{% endhint %}

<!-- \newpage -->



#### Analyse van de code

Ik zal nu iedere lijn code kort bespreken. Sommige lijnen code zullen lange tijd niet belangrijk zijn. Onthoud nu alvast dat: **alle belangrijke code staat tussen de accolades onder de lijn ``static void Main(string[] args)``**!



* **Lijn 1**: Dit is de unieke naam waarbinnen we ons programma zullen plaatsen, en het is niet toevallig de naam van je project. Verander dit nooit tenzij je weet wat je aan het doen bent.Ik bespreek *namespaces* in hoofdstuk 10.
* **Lijn 3**: Hier start je echte programma. Alle code binnen deze Program accolades zullen gecompileerd worden naar een uitvoerbaar bestand. Vanaf hoofdstuk 9 zal deze lijn geen geheimen meer hebben voor je.
* **Lijn 5**: Het startpunt van iedere console-applicatie. Wat hier gemaakt wordt is een **methode** genaamd ``Main``. Je programma kan meerdere methoden (of functies) bevatten, maar enkel degene genaamd ``Main`` zal door de compiler als het startpunt van het programma gemaakt worden. Deze lijn zal ik in hoofdstuk 7 en hoofdstuk 8 uit de doeken doen.
* **Lijn 7**: Dit is een **statement** dat de ``WriteLine``-methode aanroept van de ``Console``-bibliotheek. Het zal alle tekst die tussen de aanhalingstekens staat op het scherm tonen. 
* **Lijn 8**: en ook deze lijn zorgt ervoor dat er tekst op het scherm komt wanneer het programma zal uitgevoerd worden.
* **Accolades** op lijnen 2, 4, 6, 9 tot en met 10: vervolgens moet voor iedere openende accolade eerder in de code nu ook een bijhorende sluitende volgen. We gebruiken accolades om de *scope* aan te duiden, iets dat we in hoofdstuk 5 geregeld zullen nodig hebben.


Net zoals een recept, zal ook in C# code van **boven naar onder worden uitgevoerd**. 

Voor ons wordt het echter pas interessant op lijn7[^hello]. Dit is het startpunt van ons programma en de uitvoer ervan. Al de zaken ervoor kan je voorlopig keihard nergeren. 

Het programma zal alles uitvoeren dat tussen de accolades van het ``Main``-blok staat. Dit blok wordt afgebakend door de accolades van lijn 6 en 9. Dit wil ook zeggen dat van zodra lijn 9 wordt bereikt, dit het signaal voor je  computer is om het programma af te sluiten. 



<!-- \newpage -->


>![](../assets/care.png)Jawadde...Wat was dit allemaal?! We hebben al aardig wat vreemde code zien passeren en het is niet meer dan normaal dat je nu denkt "dit ga ik nooit kunnen". Wees echter niet bevreesd: je zal sneller dan je denkt bovenstaande code als 'kinderspel' gaan bekijken. Een tip nodig? Test en experimenteer met wat je al kunt!
>
>Laat deze info rustig inzinken en onthoud alvast volgende belangrijke zaken:
>
>* **Al je eigen code komt momenteel enkel tussen de ``Main`` accolades.**
>* **Eindig iedere lijn code daar met een puntkomma (``;``).**
>* **Code wordt van boven naar onder uitgevoerd.**


{% hint style='tip' %}
De oerman verschijnt wanneer we een stevige stap gezet hebben en je mogelijk even onder de indruk bent van al die nieuwe informatie. Hij zal proberen informatie nog eens vanuit een ander standpunt toe te lichten en te herhalen waarom deze nieuwe kennis zo belangrijk is.
{% endhint %}



[^hello]: "Hello world" op het scherm laten verschijnen wanneer je een nieuwe programmeertaal leert is ondertussen een traditie bij programmeurs. Er is zelfs een website die dit verzamelt namelijk **helloworldcollection.de**. Deze site toont in honderden programmeertalen hoe je "Hello world" moet programmeren.



<!-- \newpage -->



### WriteLine: Tekst op het scherm

De ``WriteLine``-methode is een veelgebruikte methode in Console-applicaties. Het zorgt ervoor dat we tekst op het scherm kunnen tonen.

Voeg volgende lijn toe na de vorige ``WriteLine``-lijn in je project:

```csharp
Console.WriteLine("Wie ben jij?!");
```

De ``WriteLine`` methode zal alle tekst tonen die tussen de aanhalingstekens (``"  "``) staat. **De aanhalingstekens aan het begin en einde van de tekst zijn uiterst belangrijk! Alsook het puntkomma helemaal achteraan.**

Je code binnen de ``Main`` accolades zou nu moeten zijn:

```csharp
Console.WriteLine("Hello World!");
Console.WriteLine("Hoi, ik ben het");
Console.WriteLine("Wie ben jij?!");
```

Kan je voorspellen wat de uitvoer zal zijn? Test het eens!

{% hint style='tip' %}
Ik toon niet telkens de volledige broncode. Als ik dat zou blijven doen dan wordt dit boek dubbel zo dik. Ik toon daarom (meestal) enkel de code die binnen de ``Main`` (of later ook elders) moet komen.
{% endhint %}


