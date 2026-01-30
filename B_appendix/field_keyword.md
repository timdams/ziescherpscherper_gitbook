## Het `field` keyword

Sinds C# 14 is er een nieuw keyword: `field`.
Dit keyword geeft je toegang tot de **onderliggende instantievariabele (backing field)** van een property, zelfs als je deze niet expliciet hebt aangemaakt bovenaan je klasse.

Dit is vooral handig wanneer je validatie wilt toevoegen aan een property, maar niet de volledige syntax van een full property wilt schrijven waar je manueel de private instantievariabele én de property moet typen.

### Voorbeeld

Stel dat je een property hebt waarbij je wilt controleren dat de waarde niet negatief is.

**Vroeger (Full property):**

Je moest zowel de private instantievariabele (``leeftijd``) aanmaken als de publieke property.

```csharp
private int leeftijd;
public int Leeftijd
{
    get { return leeftijd; }
    set
    {
        if (value < 0) throw new ArgumentException("Leeftijd mag niet negatief zijn");
        leeftijd = value;
    }
}
```

**Met `field`:**

Je hebt geen private instantievariabele meer nodig in je code. Via `field` spreekt de property rechtstreeks de, door de compiler gegenereerde, achterliggende variabele aan.

```csharp
public int Leeftijd
{
    get;
    set
    {
        if (value < 0) throw new ArgumentException("Leeftijd mag niet negatief zijn");
        field = value;
    }
}
```

Merk op hoe je `field` gebruikt om de waarde toe te wijzen aan de interne staat van het object. De `get` kan gewoon `get;` blijven.

### Relatie met auto-properties

Auto-properties (bv. `public int Leeftijd { get; set; }`) zijn eigenlijk een afkorting waarbij de compiler voor jou een onzichtbare instantievariabele aanmaakt en de `get` en `set` implementeert.

Met het `field` keyword kan je nu **het beste van twee werelden** combineren:
1.  **Zoals auto-properties**: Je hoeft geen aparte private variabele aan te maken.
2.  **Zoals full properties**: Je kan eigen logica (validatie, logging, etc.) toevoegen aan de `get` of `set`.

In het voorbeeld hierboven zie je dat we de `get` nog steeds schrijven als een auto-property (`get;`), terwijl we de `set` zelf implementeren en gebruik maken van `field`.

