## Environment bibliotheek

De ``Console`` bibliotheek is maar 1 van de vele bibliotheken die je in je C# programma's kunt gebruiken. 

Een andere nuttige bibliotheek is de ``Environment``-bibliotheek. Deze geeft je applicatie allerlei informatie over de computer waarop het programma op dat moment draait. Denk maar aan het werkgeheugen, gebruikersnaam van de huidige gebruiker, het aantal processoren enz.

{% hint style='danger' %}
De laatste zin in vorige alinea is belangrijk: als je jouw programma op een andere computer laat uitvoeren zal je mogelijk andere informatie verkrijgen. 

Wil je een programma dus testen dat deze bibliotheek gebruikt, is het aangeraden om het op meerdere systemen met verschillende eigenschappen te testen.
{% endhint %}


Hier enkele voorbeelden hoe je deze bibliotheek kunt gebruiken (kijk zelf of er nog nuttige properties over je computer in staan):

```csharp
bool is64bit = Environment.Is64BitOperatingSystem;
string pcname = Environment.MachineName;
int proccount = Environment.ProcessorCount;
string username = Environment.UserName;
long memory = Environment.WorkingSet; //zal ongeveer 10 Mb zijn
```

Vervolgens zou je dan de inhoud van die variabelen kunnen gebruiken om bijvoorbeeld aan de gebruiker te tonen wat z'n machine naam is:

```csharp
Console.WriteLine($"Je computernaam is {pcname}");
Console.WriteLine($"Dit programma gebruikt {memory} byte geheugen");
Console.WriteLine($"En je usernaam is {Environment.UserName}");
```

In de laatste lijn code tonen we dat je uiteraard ook rechtstreeks de variabelen uit ``Environment`` in je string interpolatie kunt gebruiken en dus niet met een *tussenvariabele* moet werken.

Je kan in de documentatie[^docenv] opzoeken welke nuttige zaken je nog met de bibliotheek kunt doen.


**WorkingSet** bijvoorbeeld geeft terug hoeveel geheugen het programma van Windows toegewezen krijgt. Als je dus op 'run' klikt om je code te runnen dan zal dit programma geheugen krijgen en via WorkingSet kan het programma dus zelf zien hoeveel het krijgt. Test maar eens wat er gebeurt als je programma maakt dat uit meer lijnen code bestaat.


[^docenv]: Zie [docs.microsoft.com/dotnet/api/system.environment](https://docs.microsoft.com/dotnet/api/system.environment).

### Programma afsluiten

De ``Environment`` bibliotheek heeft ook een methode om je applicatie af te sluiten. Je doet dit met behulp van ``Environment.Exit(0)``. Het getal tussen haakjes mag je zelf bepalen en is de zogenaamde *exitcode* die je wilt meegeven bij het afsluiten. Als je dan later via logbestanden wilt onderzoeken waarom het programma stopte dan kan je dit zien aan de hand van deze *exitcode*.


>![](../assets/care.png)Mogelijk was deze laatste sectie wat verwarrend. Dat is bewust gedaan...*sort of*. C# leren kan in het begin soms nogal saai lijken. Daarom dat ik ervoor kies om hier en daar een iets meer geavanceerd aspect te bespreken. 
>
>Zoals al eerder verteld: C# komt met een hele grote hoop bibliotheken (denk maar een ``Environment`` en ``Console``). Voor zover ik weet, bestaat er niemand die iedere bibliotheek of klasse kent. Het is aan jou, als gepassioneerde programmeur, om zelf te ontdekken welke bibliotheken je nuttig lijken gegeven een bepaald probleem.


