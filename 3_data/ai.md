## Programmeren met A.I.

We hebben nu al enkele hoofdstukken A.I. angstvallig in de stal gelaten. Laten we dat wilde, krachtige beest eens buitenlaten en in een omheind veldje zetten. In deze gloednieuwe sectie wil ik je enkele handvaten geven hoe je A.I. kunt gebruiken de komende maanden, in je avontuur om de beste C# programmeur ooit te worden.

We zullen enkele typische prompts bespreken die je kan gebruiken, waarbij we willen benadrukken dat:

* een prompt nooit feilloos is. Of beter: het resultaat van de prompt. Je mag nog zo'n gefinetuned prompt hebben, maar de A.I. zal altijd fouten maken. Het is dus cruciaal dat je altijd kritisch bent over de output
* alhoewel je - zeker aan de start van je C# avontuur- meestal 100% perfecte oplossingen zult terugkrijgen, deze oplossingen vaak of te complex zijn, of zich niet houden aan de specifieke afspraken die wij hanteren (denk aan schrijfwijze, naamgeving, het wel of niet toelaten van bepaalde methoden, etc.). Je zou dit allemaal in je prompt kunnen zetten, maar dat maakt de prompt dan weer onnodig complex. Je zal dus vaak zelf nog wat moeten bijsturen. 

### De verboden prompt

Het zal wel duidelijk zijn dat er één type prompt is die je als beginnende programmeur nooit mag gebruiken. Het is eigenlijk dezelfde prompt als dat je naar een drievoudig Tour de France winnaar zou gaan en hem vragen om even de Mont Ventoux voor jou op te fietsen, met jou achterop zijn rug. Je zal aan de top geraken, maar je zal zelf weinig geleerd hebben, omdat je je grijze hersenmassa - of in dit voorbeeld spiermassa- niet hebt gebruikt.

En dus volgt hier **de verboden prompt**:

```text
Schrijf de C# oplossing voor deze opgave: [gevolgd door de opgave].
```

Doe het gerust eens met een oefening die ja al hebt gemaakt. Zeker de oefeningen van de eerste hoofdstukken zullen vaak perfect zijn. 

### Zoek-de-fout-prompt

De leukste prompt die je kan gebruiken is de zoek-de-fout-prompt. Hierbij vraag je A.I. om een oplossing te schrijven, maar met opzet fouten in te bouwen. Vervolgens moet jij deze fouten opsporen en verbeteren. Dit is een uitstekende oefening om je kennis te testen en te verdiepen. Het is hierbij belangrijk dat je benadrukt dat de A.I. de fouten niet aanduidt, maar dat jij ze moet vinden.

```text
Schrijf de C# oplossing voor deze opgave: "Vraag aan de gebruiker zijn naam. Toon de naam, gevolgd door de zin 'wat een mooie naam!'."

Zorg ervoor dat er minstens drie fouten in de code zitten die een beginnende programmeur zou kunnen maken. Geef geen uitleg, alleen de code. Ik zal de fouten vervolgens proberen te vinden en te corrigeren.
```

Zeker voor de beginnende hoofdstukken kan het geen kwaad dat je toevoegt dat alle zogenaamde *boilerplate code* (zoals de `using` statements, de `namespace`, de `class Program` en de `static void Main`) niet getoond moet worden bij het zoeken naar fouten. Zo kan je je focussen op het échte probleem. Voeg daarom dit nog toe aan je prompt:

```text
Je hoeft de boilerplate code (zoals de using statements, de namespace, de class Program en de static void Main) niet te tonen.
```

### Vergelijkings-prompt

Je krijgt bij de oefeningen ook steeds de oplossing. Zoals steeds raad ik je aan hier pas naar te gaan kijken wanneer je zelf een poging hebt gedaan. Vervolgens kan je jouw oplossing vergelijken en reflecteren over de verschillen. 
Via volgende prompt kan je A.I. vragen om jouw oplossing te vergelijken met de zijne, en de verschillen uit te leggen:

```text
Vergelijk mijn volgende code met  modeloplossing voor deze opgave: [gevolgd door de opgave]. Leg de verschillen uit en waarom jouw oplossing beter is.

Mijn code is:
[gevolgd door jouw code].

Dit is de modeloplossing::
[gevolgd door de modeloplossing].
```


Je kan dit nog specifieker maken door te vragen om te focussen op bepaalde aspecten, zoals efficiëntie, leesbaarheid, naamgevingen of het volgen van best practices.


```text
Focus op hoe duidelijk mijn naamgevingen zijn in vergelijking met die van de modeloplossing.
```

#### Tutor-vergelijkings-prompt

We kunnen deze prompt een stuk interactiever maken door de A.I. als een tutor te gebruiken, waarbij jij als gebruiker moet aangeven waar je vindt dat de verschillen zitten en waarom. De A.I. zal dan feedback geven op jouw analyse en eventueel bijvragen stellen om je begrip te verdiepen.

De prompt ziet er dan zo uit:
```text
Vergelijk mijn volgende code met  modeloplossing voor deze opgave: [gevolgd door de opgave]. 

Ik zal aangeven wat ik anders vind aan mijn code in vergelijking met de modeloplossing. Geef feedback op mijn analyse en stel vragen om mijn begrip te verdiepen.

Mijn code is:
[gevolgd door jouw code]

Dit is de modeloplossing:
[gevolgd door de modeloplossing].

Je mag me nu ondervragen over de verschillen die ik zal aangeven.
```

{% hint style='tip' %}
ChatGPT en friends worden pas krachtig wanneer je ermee in een dialoog gaan. Anders is het maar een searchengine *on steroids*.

Bovenstaande tutor-prompt, waarin je interactie eist van de A.I., zal je leerproces veel krachtiger maker, daar het vereist dat je ook zelf actief nadenkt over de verschillen en je begrip van de concepten verdiept.
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