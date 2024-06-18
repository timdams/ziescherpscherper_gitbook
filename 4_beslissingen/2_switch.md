## Switch

Een ``switch`` statement is een element om een veelvoorkomende constructie van ``if``/``if else``...``else``  eenvoudiger te schrijven. Vaak komt het voor dat we bijvoorbeeld aan de gebruiker vragen om een keuze te maken (bijvoorbeeld een getal van 1 tot 10, waarbij ieder getal een ander menu-item uitvoert van het programma), zoals:

```csharp
Console.WriteLine("Kies: 1)afbreken\n2)opslaan\n3)laden:");
int option = int.Parse(Console.ReadLine());
 
if (option == 1)
    Console.WriteLine("Afbreken gekozen");
else if (option == 2)
    Console.WriteLine("Opslaan gekozen");
else if (option == 3)
    Console.WriteLine("Laden gekozen");
else
    Console.WriteLine("Onbekende keuze");
```

Met een ``switch`` kan dit eenvoudiger wat ik zo meteen demonstreer. Eerst bekijken we hoe ``switch`` juist werkt. De syntax van een ``switch`` is  specialer dan de andere programma flow-elementen (``if``, ``while``, enz.), namelijk als volgt:

```csharp
switch (value)
{
    case constant:
        statements
        break;
    case constant:
        statements
        break;
    default:
        statements
        break;
}
```

Laten we eens kijken welke nieuwe zaken we hier terugvinden[^switchnieuw]:

* **``value``** is de testvariabele die wordt gebruikt als test in de switch (``option`` in het voorbeeld).
* Iedere mogelijke waarde van value begint met het **``case``** keyword. Gevolgd door de waarde (de **case constant**) die ``value`` moet hebben om in deze case te *springen*.
* Na het **dubbelpunt** volgt vervolgens de **code** die moet uitgevoerd worden in deze ``case``. Deze code mag bestaan uit meerdere lijnen code. Accolades zijn hier trouwens niet verplicht.
* Iedere case moet  afgesloten worden met het **``break``** keyword.
* Tijdens de uitvoer zal de switch de inhoud van de testvariabele (``value``) vergelijken met iedere case constant. Dit gebeurt van boven naar beneden. Wanneer een gelijkheid wordt gevonden dan wordt die case uitgevoerd. 
* Indien geen case wordt gevonden die gelijk is aan ``value`` dan zal de code binnen de **``default``**-case uitgevoerd worden (de ``else`` achteraan indien alle vorige ``if else``-tests negatief waren). 

{% hint style='tip' %}
We zijn dus 4 gereserveerde keywords rijker:

* ``switch``
* ``case``
* ``break``
* ``default``
{% endhint %}

Het menu van zonet kunnen we nu herschrijven naar een ``switch``:

```csharp
Console.WriteLine("Kies: 1)afbreken\n2)opslaan\n3)laden:");
int option = int.Parse(Console.ReadLine());

switch (option)
{
    case 1:
        Console.WriteLine("Afbreken gekozen");
        break;
    case 2:
        Console.WriteLine("Opslaan gekozen");
        break;
    case 3:
        Console.WriteLine("Laden gekozen");
        break;
    default:
        Console.WriteLine("Onbekende keuze");
        break;
}
```

{% hint style='tip' %}
De case waarden moeten constanten zijn en mogen dus geen variabelen zijn. Constanten zijn de welgekende *literals* (``1``, ``"1"``, ``1.0``, ``1.d``, ``'1'``, enz.). Uiteraard moeten de case waarden van hetzelfde datatype zijn als die van de testwaarde.
{% endhint %}


[^switchnieuw]: Sinds C# 7 is de ``switch`` met enkele krachtige uitbreidingen vergroot. Ik heb bewust gekozen om deze niét in dit boek op te nemen omdat ze anders je eerste contact met ``switch`` nodeloos moeilijker maakt dan zou moeten. 
Toch nieuwsgierig wat *de nieuwe switch* kan? Lees dan zeker eens [thomasclaudiushuber.com/2021/02/25/c-9-0-pattern-matching-in-switch-expressions](https://thomasclaudiushuber.com/2021/02/25/c-9-0-pattern-matching-in-switch-expressions) voor een mooi overzicht van alle nieuwigheden.





### Fallthrough

Soms wil je dat dezelfde code uitgevoerd wordt bij 2 of meer cases. Je kan ook zogenaamde fallthrough cases beschrijven wat er als volgt uit ziet:

```csharp
switch (option)
{
    case 1:
        Console.WriteLine("Afbreken gekozen");
        break;
    case 2:
    case 3:
        Console.WriteLine("Laden of opslaan gekozen");
        break;
    default:
        Console.WriteLine("Onbekende keuze");
        break;
}
```

In dit geval zullen zowel de waarden ``2`` en ``3`` resulteren in de zin "Laden of opslaan gekozen" op het scherm.

