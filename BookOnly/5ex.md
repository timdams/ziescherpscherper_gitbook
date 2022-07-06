## Oefeningen

### Boekhouder

Maak een 'boekhoud-programma': de gebruiker kan de hele tijd positieve en negatieve , gehele, getallen invoeren. Telkens hij op enter duwt wordt de huidige invoer aan de balans bijgevoegd. Wanneer de gebruiker ``q`` invoert stopt het programma en toont het de informatie die we als volgt hebben bijgehouden:

* De balans van alle ingevoerde getallen: dit is gewoon de som van de getallen. Als de gebruiker dus de getallen 4, -10 en 8 invoerde dan zal de balans op +2 staan (4 -10 + 8).
* De som van alle negatieve invoeren. Als de gebruiker dus 4, -10, 8 en -6 invoerde dan zal dit getal op -16 staan (= -10 -6).
* De som van alle positieve invoeren. Als de gebruiker dus 4, -10, 8 en -6 invoerde dan zal dit getal op +12 staan (= 4 + 8). 
* Het gemiddelde van alle ingevoerde getallen, tot 1 cijfer na de komma nauwkeurig.

Deze 4 getallen worden steeds geüpdatet en getoond wanneer de gebruiker een nieuw getal invoert en op enter duwt.

### Casino extra
Vul de casino oefening uit vorige hoofdstuk aan zodat de gebruiker kan blijven raden tot het juist is. Toon op het einde het aantal pogingen dat nodig was.

### Hoger Lager

Vul de vorige casino oefening aan maar genereer nu een getal tussen 1 en 100. Telkens de gebruiker een gok doet toon je of het te zoeken getal hoger of lager is.

Kan je vervolgens ervoor zorgen dat er maar een maximaal aantal pogingen (door jou in te stellen) is toegestaan?

### Tekenen

Twee getallen tussen 2 en 20 worden ingelezen (invoercontrole!). Er moet een open rechthoek afgedrukt worden bestaande uit sterretjes (``*``), waarbij de ingelezen getallen respectievelijk de breedte en de hoogte van de rechthoek voorstellen. Als bijvoorbeeld 10 en 4 werden ingelezen, wordt de volgende rechthoek getoond:


```text
* * * * * * * * * *
*                 *
*                 *
* * * * * * * * * *
```




### RNA Transscriptie

DNA heeft steeds een RNA-complement (DNA is het gevolg van RNA transscriptie). Schrijf een programma dat een ingevoerde DNA-string omzet naar een RNA-string. De gebruiker voert steeds 1 DNA-nucleotide in per keer en duwt op enter, de RNA string wordt steeds groter. De omzetting is als volgt: G wordt C. C wordt G. T wordt A. A wordt U.

Als de gebruiker dus ``ACGTGGTCTTAA`` heeft ingevoerd moet het resultaat: ``UGCACCAGAAUU`` zijn. Ga er van uit dat de gebruiker letter per letter invoert (telkens dus enter na een letter) en je de omgezette string doet groeien (m.b.v. ``+=``).


### Become Neo

![](../assets/neotim.png)

Volgende code genereert een beeld zoals dat ook in de cultfilm The Matrix (1999) plaatsvindt. 
```java
Random rangen = new Random();
Console.ForegroundColor = ConsoleColor.Green;
while (true)
{
    //Genereer nieuw random teken:
    char teken = Convert.ToChar(rangen.Next(62, 400));
    //Zet teken op scherm
    Console.Write(teken);
    
    //10 ms pauze tussen ieder frame (pas gerust aan)
    System.Threading.Thread.Sleep(10); 
    
    //Af en toe donker kleurtje
    if(rangen.Next(0, 3) == 0)
    {
        Console.ForegroundColor = ConsoleColor.DarkGreen;
    }
    else
    {
        Console.ForegroundColor = ConsoleColor.Green;
    }
}
```

Vul de code aan zodat de karakters random kleuren krijgen. Kan je het nog cooler maken?


### Wiskundequiz

Maak een applicatie die je kan gebruiken om je tafels van vermenigvuldigen te oefenen. De applicatie vraagt steeds een willekeurige vermenigvuldiging (enkel getallen tussen 1 tot en met 10) en de gebruiker moet de oplossing invoeren.
Indien correct gaat de gebruiker verder. Bij fout stopt het programma en wordt getoond hoeveel keer je juist hebt ingevoerd.

### Wiskundequiz met levels

Bouw levels in de voorgaande wiskundequiz. Per 5 juiste antwoorden, stijg je 1 level. Het level bepaalt het bereik van getallen die gegenereerd worden bij de oefening. Bijvoorbeeld level 1 enkel getallen van 1 tot en met 5, level 2 tot en met 10, level 3 tot en met 20 enz.

Wat pittiger: Kan je ervoor zorgen dat het bereik van de getalgeneratie met een formule afhankelijk is van het level? Zodat je de grenzen per level niet moet hardcoden?

### Wiskunde-quizprogramma

Integreer voorgaande quiz met een menu. Het menu wordt aan de start getoond en geeft de gebruiker de optie om te kiezen wat hij wenst te doen:
* Gewoon spelen
* Starten op een bepaald level (de gebruiker moet vervolgens het level invoeren)
* Studeren: de oplossing wordt steeds getoond. De gebruiker hoeft niets in te voeren, elke 5 seconden verschijnt de volgende opgave met oplossing.
