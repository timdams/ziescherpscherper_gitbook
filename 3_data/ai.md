## Programmeren met A.I.

**OPGELET: dit hoofdstuk is in opbouw en nog niet klaar**

We hebben nu al enkele hoofdstukken A.I. angstvallig in de stal gelaten. Laten we dat wilde, krachtige beest eens buitenlaten en in een omheind veldje zetten. In deze gloednieuwe sectie wil ik je enkele handvaten geven hoe je A.I. kunt gebruiken de komende maanden, in je avontuur om de beste C# programmeur ooit te worden.

We zullen enkele typische prompts bespreken die je kan gebruiken, waarbij we willen benadrukken dat:

* een prompt nooit feilloos is. Of beter: het resultaat van de prompt. Je mag nog zo'n gefinetuned prompt hebben, maar de A.I. zal altijd fouten maken. Het is dus cruciaal dat je altijd kritisch bent over de output
* alhoewel je - zeker aan de start van je C# avontuur- meestal 100% perfecte oplossingen zult terugkrijgen, deze oplossingen vaak of te complex zijn, of zich niet houden aan de specifieke afspraken die wij hanteren (denk aan schrijfwijze, naamgeving, het wel of niet toelaten van bepaalde methoden, etc.). Je zou dit allemaal in je prompt kunnen zetten, maar dat maakt de prompt dan weer onnodig complex. Je zal dus vaak zelf nog wat moeten bijsturen. 

### De verboden prompt

Het zal wel duidelijk zijn dat er één type prompt is die je als beginnende programmeur nooit mag gebruiken. Het is eigenlijk dezelfde prompt als dat je naar een drievoudig Tour de France winnaar zou gaan en hem vragen om even de Mont Ventoux voor jou op te fietsen, met jou achterop zijn rug. Je zal aan de top geraken, maar je zal zelf weinig geleerd hebben, omdat je je grijze hersenmassa - of in dit voorbeeld spiermassa- niet hebt gebruikt.

En dus volgt hier **de verboden prompt**:


>Schrijf de C# oplossing voor deze opgave: [gevolgd door de opgave].


Doe het gerust eens met een oefening die je al hebt gemaakt. Zeker de oefeningen van de eerste hoofdstukken zullen vaak perfect zijn. 

### Zoek-de-fout-prompt

De leukste prompt die je kan gebruiken is de zoek-de-fout-prompt. Hierbij vraag je A.I. om een oplossing te schrijven, maar met opzet fouten in te bouwen. Vervolgens moet jij deze fouten opsporen en verbeteren. Dit is een uitstekende oefening om je kennis te testen en te verdiepen. Het is hierbij belangrijk dat je benadrukt dat de A.I. de fouten niet aanduidt, maar dat jij ze moet vinden.


>Schrijf de C# oplossing voor deze opgave: "Vraag aan de gebruiker zijn naam. Toon de naam, gevolgd door de zin 'wat een mooie naam!'."
>
>Zorg ervoor dat er minstens drie fouten in de code zitten die een beginnende programmeur zou kunnen maken. Geef geen uitleg, alleen de code. Ik zal de fouten vervolgens proberen te vinden en te corrigeren.


Zeker voor de beginnende hoofdstukken kan het geen kwaad dat je toevoegt dat alle zogenaamde *boilerplate code* (zoals de `using` statements, de `namespace`, de `class Program` en de `static void Main`) niet getoond moet worden bij het zoeken naar fouten. Zo kan je je focussen op het échte probleem. Voeg daarom dit nog toe aan je prompt:


>Je hoeft de boilerplate code (zoals de using statements, de namespace, de class Program en de static void Main) niet te tonen.


### Vergelijkings-prompt

Je krijgt bij de oefeningen ook steeds de oplossing. Zoals steeds raad ik je aan hier pas naar te gaan kijken wanneer je zelf een poging hebt gedaan. Vervolgens kan je jouw oplossing vergelijken en reflecteren over de verschillen. 
Via volgende prompt kan je A.I. vragen om jouw oplossing te vergelijken met de zijne, en de verschillen uit te leggen:


>Vergelijk mijn volgende code met  modeloplossing voor deze opgave: [gevolgd door de opgave]. Leg de verschillen uit en waarom jouw oplossing beter is.
>
>Mijn code is:
>[gevolgd door jouw code].
>
>Dit is de modeloplossing::
>[gevolgd door de modeloplossing].



Je kan dit nog specifieker maken door te vragen om te focussen op bepaalde aspecten, zoals efficiëntie, leesbaarheid, naamgevingen of het volgen van best practices.



>Focus op hoe duidelijk mijn naamgevingen zijn in vergelijking met die van de modeloplossing.


#### Tutor-vergelijkings-prompt

We kunnen deze prompt een stuk interactiever maken door de A.I. als een tutor te gebruiken, waarbij jij als gebruiker moet aangeven waar je vindt dat de verschillen zitten en waarom. De A.I. zal dan feedback geven op jouw analyse en eventueel bijvragen stellen om je begrip te verdiepen.

De prompt ziet er dan zo uit:

>Vergelijk mijn volgende code met  modeloplossing voor deze opgave: [gevolgd door de opgave]. 
>
>Ik zal aangeven wat ik anders vind aan mijn code in vergelijking met de modeloplossing. Geef feedback op mijn analyse en stel vragen om mijn begrip te verdiepen.
>
>Mijn code is:
>[gevolgd door jouw code]
>
>Dit is de modeloplossing:
>[gevolgd door de modeloplossing].
>
>Je mag me nu ondervragen over de verschillen die ik zal aangeven.


{% hint style='tip' %}
ChatGPT en friends worden pas krachtig wanneer je ermee in een dialoog gaan. Anders is het maar een searchengine *on steroids*.

Bovenstaande tutor-prompt, waarin je interactie eist van de A.I., zal je leerproces veel krachtiger maker, daar het vereist dat je ook zelf actief nadenkt over de verschillen en je, hopelijk, begrip van de concepten verdiept.
{% endhint %}


### Maak een variant-prompt

Ervaren programmeurs zien snel dat veel opdrachten eigenlijk varianten zijn van elkaar. Vaak is de context het enige dat verschilt. Een oefening waarin je leeftijden van 10 mensen moet vragen en het gemiddelde  moet berekenen, kan even goed een oefening zijn waarin je de lengtes van 30 slangen moet vragen en het gemiddelde moet berekenen.

Dit inzicht kan je ook gebruiken in je prompts. Je kan A.I. vragen om een variant te maken van een bestaande oefening, waarbij je zelf de context aanlevert.

>Maak een variant van deze opgave: [gevolgd door de opgave]. Gebruik een andere context, maar behoud dezelfde structuur en moeilijkheidsgraad. Geef alleen de nieuwe opgave, zonder oplossing.

Uiteraard wordt het nog langer als je zelf in de prompt aanlevert. Zo kan je oefeningen laten maken over onderwerpen die jou (meer) interesseren. Het nadeel van deze prompt is dat de opgaves vaak wat ongeïnspireerd zijn van zodra je de *truuk* doorhebt. Je kan dit oplossen door de prompt iets meer vrijheid te geven:

>Maak een variant van deze opgave: [gevolgd door de opgave]. 
>
>Gebruik een andere context, maar behoud dezelfde structuur en moeilijkheidsgraad. Geef alleen de nieuwe opgave, zonder oplossing. Probeer de context zo creatief mogelijk te maken. Het belangrijkste is de structuur en moeilijkheidsgraad behouden.

### Wees-de-compiler-prompt

Vaak weet een goed programmeur ongeveer wat de output van een stuk code zal zijn, zonder dat hij de code ook effectief zal uitvoeren. Dit is een belangrijke vaardigheid, omdat het je helpt om code te begrijpen en te debuggen.

Deze prompt zal je helpen om dit te oefenen (merk op dat je dit ook zonder A.I. kan doen, maar het is leuk om te zien of de A.I. hetzelfde antwoord geeft als jij). 

>Jij bent mijn ondervrager. Je toont me telkens een stukje C#-code (maximaal 10 regels) en ik moet je vertellen wat de output zal zijn als deze code wordt uitgevoerd. Na mijn antwoord, leg je uit waarom dat het geval is. Als mijn antwoord fout is, leg je uit wat de juiste output is en waarom.


{% hint style='warning' %}
Bij dit soort oefeningen bestaat het gevaar dat de A.I. je ondervraagt over zaken die je nog niet kent (dit geldt ook voor eerdere oefeningen). Je lost dit op door expliciet aan te geven hoe ver je al bent in het leren werken met C#.

Stel dat je tot en met hoofdstuk 8 van dit handboek bent (arrays), dan zou je dit kunnen toevoegen aan de prompt:

>Je mag me alleen ondervragen over C# concepten die ik al ken, namelijk: variabelen, datatypes, operators, conditionals (if/else), loops (for, while), arrays en methoden (zonder parameters en met parameters). Gebruik geen geavanceerde concepten zoals klassen, objecten, en andere OOP concepten. Ook  LINQ, async/await, delegates, events of generics mag je niet gebruiken.
{% endhint %}

### Vereenvoudigings-prompt

Vaak schrijven beginnende programmeurs mooi werkende code, die echter soms te complex of onnodig lang is. Dit kan het moeilijk maken om de code te begrijpen en te onderhouden. Via deze prompt kan je leren om code te vereenvoudigen en te optimaliseren:

> Je gaat me trainen in het oefenen van het vereenvoudigen van C# code. Genereer telkens een stukje code (maximaal 10 regels) dat correct werkt, maar op een onnodig complexe of lange manier is geschreven. Ik zal proberen de code te vereenvoudigen en optimaliseren. Na mijn poging, geef je feedback op mijn vereenvoudiging en leg je uit hoe ik het nog beter kan doen.

### Stopt dit ooit?

Er zijn natuurlijk honderden manieren tegenwoordig om A.I. te gebruiken in je leerproces. Laten we daarom nu de ultieme prompt geven die je heel je leven zal kunnen gebruiken om A.I. te helpen om je te helpen:

> Je bent de beste leerkracht en coach ooit. Je bent kritisch, maar geeft opbouwende feedback, zonder ooit de oplossing voor een probleem te geven. Je gebruikt alle truken uit je arsenaal om mij een beter C# programmeur te maken. Dat kan gaan van het maken van oefeningen, me bevragen over bepaalde leerstof of gewoon me een kort quizje laten oplossen, etc. Alle pedagogische en didactische trucs mogen gebruikt worden.
>
>Je daagt me uit, maar helpt me ook als ik vastzit. Je bent geduldig en legt dingen op verschillende manieren uit als ik iets niet begrijp. Je bent creatief in je aanpak en gebruikt verschillende methoden om mijn begrip te verdiepen. Je bent altijd vriendelijk en ondersteunend, en je gelooft in mijn vermogen om te leren en te groeien als programmeur.

{% hint style='warning' %}
Of als je echt geen inspiratie hebt. Vraag gewoon aan A.I. wat leuke prompts zijn die je in de toekomst kan gebruiken om jezelf te verbeteren ;).
{% endhint %}
 
 <!-- DUMPMCHATGPT 
 Een paar mogelijke formats die je telkens kan herhalen:

1. Reflectieve vraag

Laat studenten nadenken over waarom ze AI nu zouden mogen gebruiken.

"Hoe zou jij dit hoofdstuk uitleggen aan een AI? Welke termen moet je definiëren?"

"Welke fouten zou een AI waarschijnlijk maken als hij dit programmeerconcept uitlegt?"

2. Prompt-experiment

Geef een concrete promptopdracht.

"Vraag aan ChatGPT: 'Schrijf een programma in C# dat…' en vergelijk met je eigen code."

"Vraag: 'Leg in eenvoudige taal uit wat een loop doet' en controleer of de uitleg klopt met je kennis."



"Welke stijlregels of conventies zijn niet gevolgd?"

4. Vergelijkingsoefening

Studenten schrijven zelf een oplossing.

Daarna vragen ze AI om een oplossing.

Vergelijk: wat is beter, wat is slechter, wat is gewoon anders?

5. Creatief misbruik

Laat ze AI iets totaal fout vragen, en dan analyseren waarom dat gevaarlijk is.

"Vraag: 'Geef me één regel code die een hele applicatie kan maken.' Waarom is dat onmogelijk of misleidend?"

6. AI als tutor

"Stel een vraag die je niet goed begrijpt (over dit hoofdstuk) en kijk hoe AI antwoordt. Verbeter zelf het antwoord waar nodig."

"Gebruik AI als rubber duck: laat het stap voor stap meedenken, maar controleer elk detail."

7. Ethische insteek

Een korte reflectievraag: Wanneer is het nuttig/gevaarlijk om AI te gebruiken in plaats van zelf programmeren?
  -->