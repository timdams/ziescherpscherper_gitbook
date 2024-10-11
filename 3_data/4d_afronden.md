## Over afronden

Ondertussen hebben we 3 verschillende manier gezien om getallen af te ronden, namelijk:


* Met behulp van **casting**.
* Met behulp van **``Math.Round``** .
* Met behulp van **``Convert.ToX``**.

Ieder manier gaat de data  op een andere manier behandelen in het afronden, iets wat we tot nu toe bewust even hebben genegeerd. Bij casting is het duidelijk, deze rondt dus eigenlijk naar beneden af (het zelfde als wanneer je de ``Math.Floor``-methode zou gebruiken). De twee andere manieren hebben enkele venijnige kantjes die we hier even willen bespreken.

### Addertjes bij afronden

Op het eerste zicht lijkt afronden met ``Math.Round`` en ``Convert.ToX`` gewoon te werken:

```csharp
double d1 = 4.2;
double d2 = 4.8;
Console.WriteLine($"afgerond: {Math.Round(d1)} en {Math.Round(d2)} ");
```

Dit zal de getallen **4 en 5** op het scherm tonen, zoals verwacht.

Je kan via een extra parameters de afronden nog wat bijsturen en vertellen tot hoeveel cijfer na de komma dit moet gebeuren:
    
```csharp
double d1 = 4.12343;
Console.WriteLine($"afgerond: {Math.Round(d1,1)} en {Math.Round(d1,4)} ");
```
Dit zal de getallen **4.1 en 4.1234** op het scherm tonen. Alles lijkt dus in orde.

Maar kijk wat er gebeurt wanneer we een getal afronden dat op de helft van een getal ligt:

```csharp
double d1 = 4.5;
double d2 = 5.5;
Console.WriteLine($"afgerond: {Math.Round(d1)} en {Math.Round(d2)} ");
```

Je zou 5 en 6 (of 4 en 5) verwachten. Niets is minder waar! De output hiervan wordt **4 en 6**?! 

### Bankers rounding

Zonder extra informatie zal ``Math.Round`` (en ook ``Convert.ToInt32``) altijd afronden naar het **dichtstbijzijnde even geta**l. Dit wordt ook wel **bankers rounding** genoemd. Dit is een techniek die gebruikt wordt om afrondingsfouten te minimaliseren. Dat is heel leuk en handig voor bankiers, maar voor ons als programmeurs is dit niet altijd even handig.

Gelukkig kunnen we dit gedrag aanpassen door een extra parameter mee te geven aan de ``Math.Round``-methode. Deze parameter is een **``MidpointRounding``**-enum. Deze enum heeft meerdere mogelijkheden, maar de meest gebruikte zijn:

* **``ToEven``**: Dit is de standaardwaarde en zal afronden naar het dichtstbijzijnde even getal. De zogenaamde Bankers rounding dus.
* **``AwayFromZero``**: Dit zal afronden naar het dichtstbijzijnde getal, ongeacht of het even of oneven is.

De tweede methode is de versie die wij prefereren, omdat deze het meest voorspelbare resultaat geeft. Nemen we terug ons voorbeeld, maar nu met de extra parameter:

```csharp
double d1 = 4.5;
double d2 = 5.5;
Console.WriteLine($"afgerond: {Math.Round(d1,MidpointRounding.AwayFromZero)} en {Math.Round(d2, MidpointRounding.AwayFromZero)} ");
```

Dan krijgen we **5 en 6** zoals we verwachten.

Als je op de koop toe nog eens wil afronden naar een bepaald aantal cijfers na de komma, dan kan je dit ook nog steeds doen:

```csharp
double d1 = 4.12343;
Console.WriteLine($"afgerond: {Math.Round(d1,1,MidpointRounding.AwayFromZero )} en {Math.Round(d1,4,MidpointRounding.AwayFromZero)} ");
```

