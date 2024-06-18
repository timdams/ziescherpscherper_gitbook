
## Solutions en projecten 

Het wordt tijd om eens te kijken hoe Visual Studio jouw code juist organiseert wanneer je een nieuw project start. Zoals je al hebt gemerkt in de solution Explorer wordt er meer aangemaakt dan enkel een Program.cs codebestand. Visual Studio werkt volgens volgende hiërarchie:

1. Een **solution** is een folder waarbinnen **één of meerdere projecten** bestaan.
2. Een **project** is een verzameling (code)bestanden die samen een specifieke functionaliteit vormen en kunnen worden gecompileerd tot een uitvoerbaar bestand, bibliotheek, of andere vorm van output (we vereenvoudigen bewust het concept project in dit handboek).

Wanneer je dus aan de start van een nieuwe opdracht staat en in VS kiest voor "Create a new project" dan zal je eigenlijk aan een nieuwe solution beginnen met daarin één project. 

Je bent echter niet beperkt om binnen een solution maar één project te bewaren. Integendeel, vaak kan het handig zijn om meerdere projecten samen te houden. Ieder project bestaat op zichzelf, maar wordt wel logisch bij elkaar gehouden in de solution. Dat is ook de reden waarom we vanaf de start hebben aangeraden om nooit het vinkje *"Place solution and project in the same directory"* aan te duiden.




### Folderstructuur van een solution

Wanneer je in VS een nieuw project start ben je niet verplicht om de "Project name" en "Solution name" dezelfde waarde te geven. Je zal wel merken dat bij het invoeren van de "Project name" de "Solution name" dezelfde invoer krijgt. Je mag echter vervolgens perfect de "Solution name" aanpassen. 

Stel dat we een nieuw VS project aanmaken met volgende informatie:

1. Naam van het project = **Opdracht1**
2. Naam van de solution  = **Huiswerk**

En plaatsen deze in de folder ``C:\Temp``.

<!-- \newpage -->


Wanneer we het project hebben aangemaakt en de Solution Explorer bekijken zien we volgende beeld :

![Je ziet duidelijk een hiërarchie: bovenaan de solution *Huiswerk*, met daarin een project *Opdracht1*, gevuld met informatie zoals het *Program.cs* bestand.  Deze hiërarchie zal je ook terugzien als je via de verkenner vervolgens naar de aangemaakte folder zou gaan.](../assets/1_csharpbasics/solexplorer.png)<!--{width=60%}-->



![De hiërarchie anders voorgesteld. ](../assets/1_csharpbasics/huiswerk.png)<!--{width=30%}-->

**Rechterklik nu op de solution en kies "Open folder in file explorer"**. Je kan deze optie kiezen bij eender welk item in de solution explorer. Het zal er voor zorgen dat de verkenner wordt geopend op de plek waar het item staat waar je op rechterklikte. Op die manier kan je altijd ontdekken waar een bestand of of folder zich fysiek bevindt op je harde schijf.

![Tip: rechterklikken in veel programma's geeft je vaak toegang tot meer geavanceerde commando's, zo ook in VS.](../assets/1_csharpbasics/reveal.png)<!--{width=65%}-->

We zien nu een tweede belangrijke aspect dat we in deze sectie willen uitleggen: **Een solution wordt in een folder geplaatst met dezelfde naam én bevat één .sln bestand. Binnenin deze folder wordt een folder aangemaakt met de naam van het project.** Je folderstructuur volgt dus flink de structuur van je solution in VS.

![Merk op dat je mogelijk ook nog verborgen bestanden zal zien, afhankelijk van de instellingen van je verkenner.](../assets/1_csharpbasics/explore.png)<!--{width=80%}-->

<!-- \newpage -->


Je kan dus je volledige solution, inclusief het project, openen door in deze folder het .sln bestand te selecteren. **Dit .sln bestand zelf bevat echter geen code.**

{% hint style='warning' %} 

Die laatste zin heeft als gevolg dat je de **hele folderstructuur** moet verplaatsen indien je aan je solution op een andere plek wilt werken. Open gerust eens een .sln-bestand in notepad en je zal zien dat het bestand onder andere oplijst waar het onderliggende project zich bevindt. Wil je dus je solution doorgeven of mailen naar iemand, zorg er dan voor je de hele foldestructuur doorgeeft, inclusief het .sln bestand en alles folders die er bij horen.

{% endhint %}




### Folderstructuur van een project

Laten we nu eens kijken hoe de folderstructuur van het project zelf is. Rechterklik deze keer op het project in de solution explorer (**Opdracht1**) en kies weer *"Open folder in file explorer"*. 

Hier staat een herkenbaar bestand! Inderdaad, het *Program.cs* codebestand. In dit bestand staat de actuele code van Opdracht1.


Voorts zien we ook een *.csproj* bestand genaamd *Opdracht1*. Net zoals het .sln bestand zal dit bestand beschrijven welke bestanden én folder(s) deel uitmaken van het huidige project. Je kan dit bestand dus ook openen vanuit de verkenner en je zal dan je volledige project zien worden ingeladen in Visual Studio. 



{% hint style='warning' %}

**Een .cs-bestand rechtstreeks vanuit de verkenner openen werkt niet zoals je zou verwachten.** VS zal weliswaar de inhoud van het bestand tonen, maar je kan verder niets doen. Je kan niet compileren, debuggen, enz. De reden is eenvoudig: een *.cs* bestand op zichzelf is nutteloos. Het heeft pas een bestaansreden wanneer het wordt geopend in een project. Het project zal namelijk beschrijven hoe dit specifieke bestand juist moet gebruikt worden in het huidige project.

{% endhint %}

<!-- \newpage -->


#### De bin-folder 

De "obj" folder ga ik in dit handboek negeren. Maar kijk eens wat er in de "bin" folder staat?! Een folder genaamd **"debug"**. In deze folder zal je de gecompileerde (debug-)versie van je huidige project terecht komen. Je zal wat moeten doorklikken tot de *binnenste folder* (die de naam van de huidige .net versie bevat waarin je compileert).

![Inhoud van bin/debug/net8.0 nadat project werd gecompileerd](../assets/1_csharpbasics/debugin.png)

Je kan in principe vanuit deze folder ook je gecompileerde project uitvoeren door te dubbelklikken op *Opdracht1.exe*. Je zal echter merken dat het programma ogenblikkelijk terug afsluit omdat het programma aan het einde van de code altijd afsluit. Voeg daarom volgende lijn code toe onderaan in je Main: ``Console.ReadLine()``. Het programma zal nu pas afsluiten wanneer je op Enter hebt gedrukt en de gecompileerde versie kan dus nu vanuit de verkenner gestart worden, hoera!

Merk op dat je de volledige inhoud van deze folder moet meegeven indien je je gecompileerde resultaat aan iemand wilt geven om uit te voeren.

<!-- \newpage -->



### Meerdere projecten

![Er is geen limiet op het aantal projecten in 1 solution. De enige beperking is de kracht van je computer.](../assets/1_csharpbasics/solprojhier.png)<!--{width=80%}-->

Ik zei net dat een solution meerdere projecten kan bevatten. Maar hoe voeg je een extra project toe? Terwijl je huidige solution open is (waar je een project wenst aan toe te voegen) kies je in het menu voor *File->Add->New project...*

![Ook "Existing project..." is een handige actie om te kennen!](../assets/1_csharpbasics/addproj.png)<!--{width=80%}-->

Je moet nu weer het klassieke proces doorlopen om een console-project aan te maken. Alleen ontbreekt deze keer het "Solution name" tekstveld, daar dit reeds gekend is.

Wanneer je klaar bent zal je zien dat in de solution Explorer een tweede project is verschenen. Als we de folderstructuur van onze solution opnieuw bekijken, zien we dat er een nieuwe folder (Opdracht2) is verschenen met een eigen Program.cs en .csproj-bestand.

![Gelukkig kan je zaken dichtklappen m.b.v. driehoekjes naast iedere item.](../assets/1_csharpbasics/2project.png)<!--{width=50%}-->

Nu rest ons nog één belangrijke stap: **selecteren welk project moet gecompileerd en uitgevoerd worden**. In de solution explorer kan je zien welk het *actieve* project is, namelijk het project dat vet gedrukt staat.

Je kan nu op 2 manieren kiezen welk project moet uitgevoerd worden:

**Manier 1**: Rechterklik in de Solution Explorer op het actief te zetten project en kies voor  "Set as startup project."

**Manier 2**: Bovenaan, links van de groene "compiler/run" knop, staat een selectieveld met het actieve project. Je kan hier een andere project selecteren. 

![Tijd om naar Opdracht2 over te schakelen.](../assets/1_csharpbasics/activepr.png)<!--{width=60%}-->

{% hint style='warning' %}

Controleer altijd goed dat je in het juiste Program.cs bestand bent aan het werken. Je zou niet de eerste zijn die maar niet begrijpt waarom de code die je invoert z'n weg niet vindt naar je debugvenster. Inderdaad, vermoedelijk heb je het verkeerde Program.cs bestand open *of* heb je het verkeerde actieve project gekozen. 

{% endhint %}

{% hint style='tip' %} 

Ook nu reeds heb je mogelijk interesse in meerdere projecten in 1 solution. Je kan nu perfect je opdrachten groeperen onder 1 solution, maar toch iedere opdracht mooi gescheiden houden. In de echte wereld gebruikt men meerdere projecten in 1 solution om het overzicht te bewaren en alles zo modulair mogelijk aan te pakken. Denk maar aan een solution met een projecten dat de (unit)testen bevat, een project voor de *frontend*, en nog een project voor de *backend*.


{% endhint %}

#### Delen met de oma

Om een gecompileerde .NET applicatie te kunnen uitvoeren op een computer heb je nog een **.NET runtime** nodig. Gebruikers die geen Visual Studio hebben geïnstalleerd hebben deze runtime meestal niet op hun systeem. 

Wil je dus dat je oma kan genieten van jouw laatste creatie, zorg er dan voor dat ze de juiste .NET runtime heeft draaien. Je zal haar hier wat mee moeten helpen want je moet de runtime installeren[^dotnerruntime] voor die versie *waar tegen jouw applicatie is gecompileerd*. 

[^dotnerruntime]: Je kan alle .NET runtimes hier terugvinden:[dotnet.microsoft.com/en-us/download/dotnet](https://dotnet.microsoft.com/en-us/download/dotnet)