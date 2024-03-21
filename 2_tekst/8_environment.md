## Environment bibliotheek

De ``Console`` bibliotheek is maar 1 van de vele bibliotheken die je in je C# programma's kunt gebruiken. 

Een andere nuttige bibliotheek is de ``Environment``-bibliotheek. Deze geeft je applicatie allerlei informatie over de computer waarop het programma op dat moment draait. Denk maar aan het werkgeheugen, gebruikersnaam van de huidige gebruiker, het aantal processoren enz.

{% hint style='tip' %}
De laatste zin in vorige alinea is belangrijk: als je jouw programma op een andere computer laat uitvoeren zal je mogelijk andere informatie verkrijgen. 

Wil je een programma dus testen dat deze bibliotheek gebruikt, is het aangeraden om het op meerdere systemen met verschillende eigenschappen te testen.
{% endhint %}


Hier enkele voorbeelden hoe je deze bibliotheek kunt gebruiken (kijk zelf of er nog nuttige properties over je computer in staan):

```csharp
bool is64bit = Environment.Is64BitOperatingSystem;
string pcname = Environment.MachineName;
int proccount = Environment.ProcessorCount;
string username = Environment.UserName;
long memory = Environment.WorkingSet; //zal ongeveer 10 Mb teruggeven.
```

Vervolgens zou je dan de inhoud van die variabelen kunnen gebruiken om bijvoorbeeld aan de gebruiker te tonen wat z'n machine naam is:

```csharp
Console.WriteLine($"Je computernaam is {pcname}");
Console.WriteLine($"en dit programma gebruikt {memory} byte geheugen");
Console.WriteLine($"En je usernaam is {Environment.UserName}");
```

In de laatste lijn code tonen we dat je uiteraard ook rechtstreeks de variabelen uit ``Environment`` in je string interpolatie kunt gebruiken en dus niet met een tussenvariabele moet werken.

Je kan op **docs.microsoft.com/dotnet/api/system.environment** opzoeken welke nuttige zaken je nog met de bibliotheek kunt doen.

{% hint style='tip' %}
**WorkingSet** geeft terug hoeveel geheugen het programma van Windows toegewezen krijgt. Als je dus op 'run' klikt om je code te runnen dan zal dit programma geheugen krijgen en via WorkingSet kan het programma dus zelf zien hoeveel het krijgt. (Wat een vreemde lange zin.). Test maar eens wat er gebeurt als je programma maakt dat uit meer lijnen code bestaat.
{% endhint %}



### Programma afsluiten

De ``Environment`` bibliotheek heeft ook een methode om je applicatie af te sluiten. Je doet dit met behulp van ``Environment.Exit(0);`` Het getal tussen haakjes mag je zelf bepalen en is de zogenaamde foutcode die je wilt meegeven bij het afsluiten (als je dan later via logbestanden wilt onderzoeken waarom het programma stopte dan kan je opzoeken welke foutcode er werd opgeworpen via de logs van je besturingssysteem).

{% hint style='tip' %}
Wanneer we met complexere programma's gaan leren werken zal het soms nuttig zijn om ``Environment.Exit(0);`` te gebruiken. 

In deze fase ga je er nog niet veel aan hebben, daar alle code na de ``Exit`` nooit zal uitgevoerd worden.
{% endhint %}
 
 {% hint style='warning' %}

![](../assets/care.png)

Mogelijk was deze laatste sectie wat verwarrend. Dat is bewust gedaan...*sort of*. C# lineair aangeleerd krijgen kan vrij saai zijn in den beginnen. Daarom dat ik ervoor kies om hier en daar een bepaald onderwerp of bibliotheek aan te snijden, zodat je zin krijgt om dit onderwerp te gaan verkennen. Zoals al eerder verteld: C# en dan vooral alle bestaande .NET-bibliotheken is erg groot. Voor zover ik weet bestaat er niemand die iedere bibliotheek of klasse kent. Het is aan jou, als gepassioneerde programmeur, om zelf te verkennen en te onthouden welke bibliotheken je nuttig lijken en welke je links kan laten liggen (gegeven je huidige probleem of interesses). 

{% endhint %}
