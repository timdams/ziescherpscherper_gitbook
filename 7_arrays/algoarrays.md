## Algoritmes en arrays

Omdat arrays ongelooflijk groot kunnen worden, is het nuttig dat je algoritmes kunt schrijven die vlot met arrays kunnen werken. Je wilt niet dat je programma er 3 minuten over doet om gewoon te ontdekken of een bepaalde waarde in een array voorkomt of niet[^sollic]. We zullen nu 2 typische algoritmen bespreken die vaak voorkomen als je met loops en arrays aan de slag gaat gaan.

[^sollic]: Bij jobsollicaties voor programmeurs word je soms gevraagd om dergelijke algoritmes zonder hulp uit te schrijven.

{% hint style='tip' %}
Twee maar!? Er zijn tal van andere algoritmes. Denk maar aan de verschillende manieren om arrays te sorteren (bijvoorbeeld de fameuze ``bubblesort`` en ``quicksort`` algoritmes). Al deze algoritmes hier bespreken zou een boek apart vereisen. Ik toon er daarom enkele ter illustratie.
{% endhint %}



#### Manueel zoeken in arrays

Het nadeel van BinarySearch is dat deze vereist dat je array-elementen gesorteerd staan. Uiteraard is dit niet altijd gewenst. Stel je voor dat je een simulatie maakt voor een fietswedstrijd en wilt weten of een bepaalde wielrenner in de top 5 staat.

Het zoeken in arrays kan met behulp van loops tamelijk snel. Volgende applicatie gaat zoeken of het getal 12 aanwezig is in de array (de wielrenners werken met rugnummers). Indien ja dan wordt de index bewaard van de positie in de array waar het getal staat:

```csharp
int teZoekenGetal = 12;
int[] top5 = { 5, 10, 12, 25, 16 };
bool gevonden = false;
int index = 0;
do
{
    if (top5[index] == teZoekenGetal)
    {
        gevonden = true;
    }
    index++;
} while ( !gevonden && index < top5.Length);

if (gevonden)
{
    Console.WriteLine($"Nr. {teZoekenGetal} op plek {index}");
    
}
```


<!-- \newpage -->



#### Manueel zoeken met while

Ik toon nu een voorbeeld van hoe je kan zoeken in een array wanneer we bijvoorbeeld 2 arrays hebben die 'synchroon' zijn. Daarmee bedoel ik: de eerste array bevat bijvoorbeeld producten, de tweede array bevat de prijs van ieder product. De prijs van de producten staat steeds op dezelfde index in de andere array (de prijs van peren is dus 6.2, meloenen 2.9, enz.) :

```csharp
string[] producten = {"appelen", "peren", "meloenen"};
double[] prijzen = {3.3, 6.2, 2.9};
```




We vragen nu aan de gebruiker van welk product de prijs getoond moet worden:

```csharp
Console.WriteLine("Welke productprijs wenst u?");
string keuzeGebruiker = Console.ReadLine();
```

Ik toon vervolgens hoe je met ``while`` eerst het juiste product zoekt en dan vervolgens die index bewaart en gebruikt om de prijs te tonen:

```csharp
bool gevonden = false;
int productIndex = -1;
int teller = 0;
while (teller < producten.Length && keuzeGebruiker != producten[teller])
{
    teller++;
}
if (teller != producten.Length) //product gevonden!
{
    gevonden = true;
    productIndex = teller;
}
if (gevonden)
{
    Console.Write($"Prijs van {keuzeGebruiker}");
    Console.WriteLine($"is {prijzen[productIndex]}".);
}
else
{
    Console.WriteLine("Niet gevonden");
}
```




