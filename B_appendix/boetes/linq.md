##	LINQ methoden gebruiken bij arrays (-3 punten)

*(-3 punten)*

Zonder in detail te gaan, weet dat je bij arrays dankzij Linq een aantal handige methoden hebt die je niet mag gebruiken. Dit jaar moet je al je bewerkingen op arrays manueel m.b.v. loops doen.

Zijn dus **niet toegestaan** ([bron](https://www.completecsharptutorial.com/linqtutorial/linq-average-count-max-sum-first-contains-elementat-distinct-example-csharp.php#:~:text=Average()%20%2D%20Average%20Method%20calculates,numeric%20values%20from%20the%20list)):

* ``Average()`` - Average Method calculates the average value of numeric data.
* ``Count()`` – Count method count the present items in list.
* ``Max()`` – It picks the maximum numeric values from the list.
* ``Min()`` – It picks the minimum numeric values from the list.
* ``Sum()`` – It calculates the sum of total numeric value present in the list.
* ``First()`` – It picks the first value present in the list.
* ``Last()`` – It picks the last value present in the list.
* ``Contains()`` – It find the value in the list and returns Boolean (true/false) result.
* ``ElementAt()`` – It picks the value from the list on the given position.
* ``Distinct()`` – It removes duplicate value and picks only unique elements.

Opgelet: de [Array. methoden zoals IndexOf, Fill etc. zijn wél toegestaan](https://learn.microsoft.com/en-us/dotnet/api/system.array?view=net-8.0).


### Uitgewerkt voorbeeld

In de opgave staat "bereken het gemiddelde van de waarden in de array ``leeftijden``. Dan is volgende oplossing **niet** toegestaan:

```csharp
double gemiddelde = leeftijden.Average();
```

De juiste oplossing is dan wel:

```csharp
double som=0;
for(int i = 0; i < leeftijden.Length; i++)
{
    som+= leeftijden[i];
}
double gemiddelde = som/leeftijden.Length;