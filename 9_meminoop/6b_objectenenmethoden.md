## Objecten en methoden

Wat betekent dit nu voor methoden?
Als je een object meegeeft aan een methode, geef je **een kopie van de sleutel** mee.
De methode krijgt dus toegang tot **jouw huis** (het object in de Heap).

Als de methode iets verandert in het huis (bv. de muren schilderen), **dan is dat permanent**. Als jij later met jouw sleutel binnenkomt, zijn de muren geschilderd.

#### Voorbeeld: De Schildersmethode

```csharp
void VerfHuis(Huis huisOmTeVerven)
{
    huisOmTeVerven.Kleur = "Roze"; // Permanente wijziging!
}
```

Het gebruik:

```csharp
Huis mijnHuis = new Huis { Kleur = "Wit" };
VerfHuis(mijnHuis);

Console.WriteLine(mijnHuis.Kleur); // Roze!
```

Dit is het grote verschil met value types (zoals `int`).
* Bij `int` geef je een fotokopie van het getal. De methode kan op de kopie krabbelen, dat boeit jou niet.
* Bij `object` geef je de sleutel. De methode kan je hele inboedel veranderen.

{% hint style='warning' %}
**Let op voor onbedoelde neveneffecten (side effects).**
Als je een object aan een methode geeft, weet dan dat die methode je object kan aanpassen zonder dat je het direct ziet in de aanroep.
{% endhint %}


### Objecten maken Objecten (The Factory)

Methoden kunnen ook nieuwe objecten **maken** en teruggeven.
Denk aan een autofabriek. Je geeft specificaties (parameters) en je krijgt een sleutel van een nieuwe auto terug (return value).

```csharp
public Auto MaakSportwagen(string kleur)
{
    Auto nieuweAuto = new Auto();
    nieuweAuto.Kleur = kleur;
    nieuweAuto.Pk = 500;
    return nieuweAuto; // Geef de SLEUTEL terug
}
```

Het gebruik:
```csharp
Auto mijnDroom = fabriek.MaakSportwagen("Rood");
```

###  Objecten die zichzelf maken

Een klasse kan dus zelfs methoden bevatten die nieuwe objecten van *zichzelf* teruggeven.
Denk aan celdeling of voorplanting.

```csharp
internal class Mens
{
    public string Naam { get; set; }

    public Mens KrijgKindje(string naamKind)
    {
        Mens baby = new Mens();
        baby.Naam = naamKind;
        return baby;
    }
}
```

En dan de magie van het leven in code:

```csharp
Mens mama = new Mens { Naam = "Alice" };
Mens baby = mama.KrijgKindje("Bob");

Console.WriteLine($"Mama heet {mama.Naam} en kindje heet {baby.Naam}");
```

Dit principe (methoden die objecten teruggeven) is de basis voor veel geavanceerde design patterns die je later zal leren.

