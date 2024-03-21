## Bestaande methoden en bibliotheken

Laten we eens kijken naar de vele methoden die reeds ingebouwd zitten in .NET en hoe we ze nu (hopelijk) beter kunnen gebruiken dankzij onze nieuwe kennis over methoden.

Sommige methoden, zoals ``WriteLine()``, vereisen dat je een aantal parameters meegeeft. De parameters dien je tussen de ronde haakjes te zetten. Hierbij weten we nu dat het uiterst belangrijk dat je de volgorde respecteert die de ontwikkelaar van de methode heeft gebruikt. Indien je echter  niet weet wat deze volgorde is kan je altijd **Intellisense** gebruiken. Typ gewoon de methode in je code en stop met typen na het eerste ronde haakje, vervolgens verschijnen alle mogelijke manieren waarop je deze methoden kan oproepen (met de pijltjes kan je alle mogelijke manieren bekijken)


![Dit soort popups bevat een schat aan informatie.](../assets/4_methoden/methoden1.png)

We zien telkens duidelijke de methode-signatuur: het return type (in dit geval ``void``) gevolgd door de naam van de methode en dan de formele parameters en hun datatype(s). Zoals al herhaardelijk aangehaald: de naam van de formele parameters doet er niet toe! 

Merk trouwens op dat je de WriteLine-methode ook mag aanroepen zonder parameters, dit zal resulteren in een lege lijn in de console.

Met behulp van de F1-toets kunnen meer info over de methode in kwestie tonen. Hiervoor dien je je cursor op de Methode in je code te plaatsen, en vervolgens op F1 te drukken. Je komt dan op de online documentatie van de methode waar erg veel informatie terug te vinden is over het gebruik ervan. Scroll naar de *overload list*, daar zien we de verschillende manieren waarop je de methode in kwestie kan aanroepen (het concept *overloaden* bespreken we in de volgende sectie). Je kan vervolgens op iedere methode klikken voor meer informatie en een codevoorbeeld.



### Intellisense
*Wat kan deze .NET bibliotheek eigenlijk?* is een veelgestelde vraag. Zeker wanneer je de basis van C# onder de knie hebt en je stilletjes aan met bestaande .NET bibliotheken wilt gaan werken. Wat volgt is een essentieel onderdeel van VS dat veel gevloek en tandengeknars zal voorkomen.

De online documentatie van VS is zeer uitgebreid en dankzij **IntelliSense** krijg je ook aardig wat informatie tijdens het typen van de code zelf. IntelliSense is de achterliggende technologie in VS die ervoor zorgt dat je minder moet typen. Als een soort assistent probeert IntelliSense een beetje te voorspellen wat je gaat typen en zal je daarmee helpen. 



Type eens het volgende in:

```csharp
System.Console.
```

Wacht nu even en er zal na het punt (``.``) een lijst komen van methoden en fields die beschikbaar zijn. Dit is IntelliSense in actie. Als er niets verschijnt of iets dat je niet had verwacht, dan is de kans groot dat er een (schrijf)fout staat in hetgene je net schreef. 

Je kan door deze lijst met de muis doorheen scrollen en zo zien welke methoden allemaal bij de ``Console`` bibliotheek horen. Indien gewenst kan je vervolgens de gewenste methode selecteren en op spatie duwen zodat deze in je code verschijnt.


![De icoontjes geven aan of het om een methode (kubus), een eigenschap (Engelse sleutel) of een "event" (bliksem) gaat. Events behandelen we niet in dit boek.](../assets/4_methoden/methoden4.png)

{% hint style='tip' %}
Vaak moet je code schrijven waarin je een getal aan de gebruiker vraagt:

```csharp
Console.WriteLine("Geef leeftijd");
int leeftijd = int.Parse(Console.ReadLine());
```

Als deze constructie op meerdere plekken in een project voorkomt dan is het nuttig om deze twee lijnen naar een methode te verhuizen die er dan zo kan uitzien:

```csharp
static int VraagInt(string zin)
{
    Console.WriteLine(zin);
    return  int.Parse(Console.ReadLine());
}
```

De code van zonet kan je dan nu herschrijven naar:


```csharp
int leeftijd = VraagInt("Geef leeftijd");
```

Het voorgaande voorbeeld toont ook ineens aan waarom methoden helpen om je code leesbaarder en onderhoudbaarder te maken. Je ``Main`` blijft gevrijwaard van veel repeterende lijnen code en heeft aanroepen naar (hopelijk) goed benoemde methoden die ieder een specifiek ding doen. Dit maakt het debuggen ook eenvoudiger: je ziet in één oogopslag meestal wat een methode doet (als je ze niet te lang hebt gemaakt natuurlijk).
{% endhint %}

### IntelliCode

Sinds Visual Studio 2022 heeft IntelliSense een ongelooflijk krachtig broertje bijgekregen, genaamd  IntelliCode. Deze tool zal ervoor zorgen dat je nog betere aanbevelingen krijgt van VS terwijl je aan het typen bent. Het gaat soms zo ver dat het lijkt alsof IntelliCode in je hoofd kan kijken en perfect kan voorspellen wat je wilt typen. **Let hier echter goed voor op**: de aanbevelingen zijn meestal erg accuraat, maar:

1. Ze zorgen ervoor dat je zelf minder moet typen en daardoor ook mogelijk jezelf niet genoeg traint. Zeker als beginnende programmeur. Ik raad je eigenlijk af om IntelliCode uit te schakelen (via het Tools&Options menu-item). Waarom? Laten we de analogie van het leren fietsen er nog eens bijhalen. Wat IntelliCode eigenlijk doet is je af en toe optillen en enkele meters hoger op de berg plaatsen. Handig, dat wel, maar je trainen in het fietsen doe je niet.
2. De aanbevelingen zijn natuurlijk soms gewoon fout of bevatten bugs die later bijvoorbeeld door hackers kunnen misbruikt worden. Of wat te denken van aanbevelingen die op zich wel zullen werken, maar wel 10x zoveel geheugen vereisen? Kortom, **wees steeds kritisch over de aanbevelingen van IntelliCode**

IntelliCode zal ook IntelliSense verbeteren door de belangrijkste, meest gebruikte methoden bovenaan te zetten. Je zal echter IntelliCode vooral herkennen wanneer er plots een hele lijn code verschijnt in het lichtgrijs, met achteraan een tandwiel. Via het tandwiel kan je deze magische, door artificiële intelligentie (A.I.) aangedreven tool ook uitschakelen.


![Wanneer we later klassen gaan schrijven, zoals in deze screenshot, zal IntelliCode soms griezelig correcte voorstellen doen.](../assets/4_methoden/codeai.png)

{% hint style='tip' %}
Google Copilot project is zelfs nog krachtiger en komt dus met een nog grotere disclaimer: **beginnende programmeurs, laat dit soort tools beter nog even links liggen!** Je leert ook niet hoofdrekenen door vanaf dag 1 met een zakrekenmachine aan de slag te gaan.
{% endhint %}

{% hint style='warning' %}
Sinds 2023 is er een gigantische opkomst van nog straffere A.I. tools, met ChatGPT voorop. Alhoewel deze tools vaak heel goede C# code kunnen genereren, raden we af deze te gebruiken, om dezelfde redenen dat je best IntelliCode niet gebruikt. Vraag daarom nooit aan ChatGPT om "oefening x" voor je op te lossen. 
Moet je dan ChatGPT volledig links laten liggen? Uiteraard niet. Gebruik hem als extra leermiddel om bijvoorbeeld stukken code toe te lichten, bepaalde concepten op een andere manier uit te leggen etc. 
{% endhint %}