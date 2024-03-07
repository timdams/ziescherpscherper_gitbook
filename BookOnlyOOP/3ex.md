
## Oefeningen


### Digitale kluis

#### Basiskluis

Maak een klasse ``DigitaleKluis`` die we gaan gebruiken om een kluis voor te stellen.

De klasse heeft volgende elementen:

* Een fullproperty ``Code`` met private set. De get van deze property zal altijd -666 teruggeven, tenzij ``CanShowcode`` op ``true`` staat, in dit geval zal de effectieve code worden terug gegeven die in de bijhorende instantievariabele  ``code`` staat. 
* Een overloaded constructor die als parameter een geheel getal toelaat. Dit getal zal worden toegewezen aan ``Code`` en is dus de toegangscode 
* Een auto-property ``CanShowCode`` type bool, om aan te geven of de code van buitenuit kan gezien worden.
* Een read-only property ``CodeLevel`` van type ``int``. Deze property zal het level van de code teruggeven (ongeacht CanShowCode). Het level is eenvoudigweg de effectieve code gedeeld door 1000 als geheel getal (dus indien de code 500 is zal 0 worden teruggegeven, indien de code 2000 is wordt 2 teruggegeven, enz.) 
* Een private variabele ``aantalPogingen`` om bij te houden hoe vaak de gebruiker geprobeerd heeft de code te vinden.
* Een methode ``TryCode`` die een geheel getal als parameter aanvaardt. De methode geeft een ``true`` terug indien de code correct was, anders ``false``. Deze methode kan gebruikt worden om extern een code te testen , indien deze overeenkomt met de bewaarde code dan zal gemeld worden dat de code geldig is en wordt ook getoond hoeveel keer de gebruiker geprobeerd heeft ``Deze code is geldig. Aantalpogingen = 5``. Indien de gebruiker -666 meegaf dan  verschijnt er ``CHEATER`` op het scherm. Indien de gebruiker een foute code meegaf dan meldt de methode dat dit een foute code was (``"geen geldige code"``) en wordt het aantal pogingen met 1 verhoogd.  Deze methode kan maar 10 keer aangeroepen worden (ongeacht of de juiste code werd meegegeven of niet).Indien dus ``aantalPogingen`` 10 of meer is zal er op het scherm verschijnen ``Je hebt je 10 pogingen opgebruikt.Sorry.``.


Maak enkele Digitale Kluis objecten aan in je ``Main`` en test of je bovenstaande klasse correct is geïmplementeerd.

#### Kluizen kraken 

Voeg aan de klasse een ``static`` methode ``BruteForce`` toe waar je een kluis-object aan kan geven. De methode zal een aantal random codes *bruteforcen* (met een loop die 10 verschillende getallen test) door telkens de ``TryCode`` methode van de meegegeven kluis aan te roepen. Wanneer toevallig de juiste code werd gevonden zal het aantal pogingen getoond worden.

{% hint style='tip' %}
*Beeld je in dat Bruteforce een student is. Ik maak een kluis-object aan en vertel aan die student niet welke code ik heb gekozen. Vervolgens geef ik hem mijn object en zeg hem "Je krijgt 10 pogingen om met TryCode de kluiscode te raden. Succes!"*
{% endhint %}

### Bibliotheek deel 2

Neem de Bibliotheek oefening uit hoofdstuk 9 erbij. Zorg ervoor dat de ``BibBoek`` klasse volgende zaken heeft:

* Een default constructor die de ``Uitgeleend`` datum op gisteren zet.
* Een overloaded constructor die toelaat om de ontlener (``string``) en ``Uitgeleend`` (``DateTime``) als parameters mee tegen en in te stellen in het object. Indien de meegeven datum later is dan de huidige datum dan zal er een uitzonderingen worden opgeworpen.
* Een ``static`` methode ``VeranderAlgemeneUitleenTermijn`` , die 1 ``int`` als parameter aanvaardt.De methode zorgt ervoor dat het aantal dagen dat je boek mag uitlenen verandert wordt naar de meegeven parameter. Tip: dit zal vereisen dat je een static instantievariabele hebt die je vervolgens in je ``InleverDatum`` getter gebruikt.
