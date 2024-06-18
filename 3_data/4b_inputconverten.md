## Invoer van de gebruiker verwerken

En applicatie die geen input van de gebruiker vergt kan even goed een screensaver zijn. We hebben reeds gezien hoe we met ``Console.ReadLine()`` de gebruiker tekst kunnen laten invoeren en die we dan vervolgens kunnen verwerken om bijvoorbeeld z'n naam op het scherm te tonen:


![Deze vereenvoudiging van de meeste van onze applicaties blijft gelden.](../assets/1_csharpbasics/inuit.png)

**De uitdaging met ``ReadLine`` is dat deze ALTIJD een string teruggeeft:**


```csharp
string userInput = Console.ReadLine();
```
Dit mag dus niet: ``int userInput = Console.ReadLine();`` en zal in een *conversion error* resulteren.

Willen we dat de gebruiker een getal invoert dan zal dit nog steeds als ``string`` moeten worden ingelezen. **Vervolgens zullen we dit vervolgens moeten converteren**.



Invoer van de gebruiker verwerken (dat een andere type dan ``string`` moet zijn) zal dus uit 3 stappen bestaan:

1. Input **uitlezen** met ``Console.ReadLine()``.
2. Input **bewaren** in een ``string`` variabele.
3. De variabele **parsen** met de ``Parse()`` bibliotheek naar het gewenste type.



Stel dat we aan de gebruiker z'n gewicht vragen, dan moeten we dus doen:

```csharp
Console.WriteLine("Geef je gewicht:");
string inputGewicht = Console.ReadLine();
double gewicht = double.Parse(inputGewicht);
```

Voorgaande code kan nog 1 lijntje sneller door ``ReadLine`` ogenblikkelijk als invoer aan de Parse-methode te geven:

```csharp
Console.WriteLine("Geef je gewicht:");
double gewicht = double.Parse(Console.ReadLine());
```




### Foutloze input

Voorgaande code veronderstelt dat de gebruiker géén fouten invoert[^geenfouten]. De conversie zal namelijk mislukken indien de gebruiker bijvoorbeeld ``Ik weeg 10kg`` invoert in plaats van ``10,3``.

**In de komende hoofdstukken mag je er altijd van uitgaan dat de gebruiker foutloze input geeft.**

### Kommagetallen in C\#

Goed opletten nu.

De invoer van kommagetallen door de gebruiker is afhankelijk van de landinstellingen van je besturingssysteem. Staat deze in Belgisch/Nederlands dan moet je kommagetallen met een **komma** invoeren (``9,81``). Staat je computer in het Engels dan moet je een **punt** gebruiken (``9.81``).


Maar: **In je C# code moet je kommagetal literals altijd met een punt schrijven**. Dit is onafhankelijk van je taalinstellingen. 


[^geenfouten]: En wat als je toch foute invoer wilt opvangen? Dan is ``TryParse`` je vriend. Meer informatie hierover in de appendix.




