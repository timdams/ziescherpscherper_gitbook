## Records & structs

### Records

Sinds C# 9.0 is het ook mogelijk om zogenaamde ``record``-klassen te maken. Erg vaak schrijf je klassen die niet meer moeten doen dan wat data eenmalig wegschrijven en onthouden,  dat je dan vervolgens via readonly getters kunt uitlezen, zoals:

```csharp
internal class Student
{
    public Student(string naam, int geboorteJaarIn, bool isIngeschreven)
    {
        Naam = naam;
        Geboortejaar = geboorteJaarIn;
        IsIngeschreven = isIngeschreven;
    }

    public string Naam {get;}
    public int Geboortejaar {get;}
    public bool IsIngeschreven {get;}
}
```

Wanneer je een dergelijke klasse nodig hebt kan dit sinds C# 9.0 vereenvoudigd geschreven worden als een ``record``:

```csharp
public record Student
{
    public string Naam { get; init; }
    public int Geboortejaar { get; init; }
    public bool IsIngeschreven { get; init; }
}
```

Het ``init`` keyword geeft aan dat deze auto-property eenmalig kunnen ge**set** worden bij het aanmaken van het record via de object initializer syntax:

```csharp
Student eenNieuweStudent = new Student 
            {   Naam = "Tim", 
                Geboortejaar = 1981,
                IsIngeschreven = false
            };
```

Er zijn nog tal van extra's die je krijgt met ``record``s (o.a. eenvoudig objecten vergelijken) maar die ga ik niet bespreken. 
