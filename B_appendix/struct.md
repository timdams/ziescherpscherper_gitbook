# Structs & Records

### De basis: Variabelen groeperen met struct

Soms wil je enkele variabelen die bij elkaar horen, samenvoegen in één geheel. Stel dat je de positie van een speler in een spel wilt bijhouden. Zonder struct zou je twee losse variabelen moeten maken:

```csharp
int spelerX = 10;
int spelerY = 20;
```

Handiger is om deze te groeperen. Een `struct` is ideaal voor dit soort kleine verzamelingen van data. Je maakt hiervoor een eigen type aan met de variabelen die je wilt groeperen (we noemen dit *fields*):

```csharp
struct Positie
{
    public int X;
    public int Y;
}
```

Je hebt nu je eigen type gemaakt en kunt dit als één variabele gebruiken:

```csharp
Positie spelerPositie;
spelerPositie.X = 10;
spelerPositie.Y = 20;
```

Hiermee heb je de basis van een struct te pakken: data groeperen.

In professionele C# code gebruiken we echter meestal **klassen** en **properties**. Toch zijn er specifieke scenario's waar `struct` en ook `record` beter passen.

## Struct 

Een `struct` (structure) lijkt qua syntax erg op een klasse, maar werkt intern anders. Het belangrijkste verschil is dat een `struct` een **Value Type** is, terwijl een klasse een **Reference Type** is.

### Eigenschappen van een Struct

*   **Value Type**: Wanneer je een struct toewijst aan een nieuwe variabele, wordt de volledige data gekopieerd. Bij een klasse wordt enkel de referentie (het adres) gekopieerd.
*   **Stack Allocation**: Structs leven meestal op de **Stack** (tenzij ze onderdeel zijn van een klasse), wat sneller geheugenbeheer toelaat dan de **Heap** (waar klassen leven).
*   **Geen overerving**: Een struct kan niet erven van een andere struct of klasse (wel interfaces implementeren).

### Wanneer gebruiken?

Gebruik structs voor kleine, eenvoudige datastructuren die zich gedragen als een "waarde", zoals coördinaten, complexe getallen of kleurcodes.

### Voorbeeld

```csharp
public struct Punt
{
    public int X { get; }
    public int Y { get; }

    public Punt(int x, int y)
    {
        X = x;
        Y = y;
    }
}
```

Doordat dit een Value Type is, gebeurt het volgende:

```csharp
Punt p1 = new Punt(10, 20);
Punt p2 = p1; // KOPIE VAN DE DATA!
// Als p1 verandert, verandert p2 NIET (indien mutable)
```

## Records

Sinds C# 9.0 is het mogelijk om `record`-types te maken. Een `record` is (standaard) een **Reference Type**, net als een klasse, maar is ontworpen met onveranderlijkheid (immutability) en data-equality in het achterhoofd.

### Waarom Records?

Vaak schrijf je klassen die enkel dienen om data bij te houden (DTO's - Data Transfer Objects). Je wilt dan vaak:

1.  Dat de data niet per ongeluk wijzigt (**Immutability**).
2.  Dat twee objecten gelijk zijn als hun data gelijk is (**Value Equality**).

Bij gewone klassen moet je hiervoor veel "boilerplate" code schrijven (`Equals`, `GetHashCode`, readonly properties). Records lossen dit op.

### Syntax

De "positional record" syntax is extreem kort:

```csharp
public record Student(string Naam, int Geboortejaar);
```

De compiler genereert achter de schermen automatisch:
*   Een constructor.
*   Read-only properties (`init`-only).
*   Correcte implementatie van `Equals()` en `GetHashCode()` (gebaseerd op de waarden).
*   Een `ToString()` die de waarden mooi weergeeft.

### Non-destructive Mutation (`with`)

Omdat records onveranderlijk zijn, kun je geen property wijzigen. Je kunt wel een *kopie* maken met één gewijzigde waarde met het `with` keyword:

```csharp
Student s1 = new Student("Tim", 1981);
Student s2 = s1 with { Naam = "Tom" }; 
// s2 is een nieuw object, s1 is ongewijzigd.
```

## Verschil Struct vs Record vs Class

Hieronder een overzicht van de belangrijkste verschillen:

| Eigenschap | Class | Struct | Record |
| :--- | :--- | :--- | :--- |
| **Type** | Reference Type (Heap) | Value Type (Stack*) | Reference Type (Heap)** |
| **Equality** | Reference Equality (vergelijkt geheugenadres) | Value Equality (vergelijkt waarden) | Value Equality (vergelijkt waarden) |
| **Bedoeld voor** | Gedrag & Data | Kleine data-objecten | Immutable Data Models |
| **Overerving** | Ja | Nee | Ja (van andere records) |

*\* Tenzij boxed of onderdeel van een klasse.*
*\*\* Sinds C# 10 bestaat er ook `record struct`, wat een Value Type record is.*

### Samenvattend advies

*   **Class**: Standaard keuze voor de meeste objecten met gedrag en data.
*   **Record**: Gebruik voor data-containers waarbij onveranderlijkheid gewenst is (API responses, config, domein objecten).
*   **Struct**: Gebruik enkel voor zeer kleine datastructuren (< 16 bytes) die extreem veel worden aangemaakt en waar performantie kritiek is (bv. game development, high-performance computing).
