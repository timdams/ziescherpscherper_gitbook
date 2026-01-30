### De kracht van Auto-Properties

Zoals we in het vorige hoofdstuk zagen, zijn **Auto-Properties** de kortere versie van properties, ideaal voor situaties zonder extra validatie-regels.

```csharp
public string Voornaam { get; set; }
```

Dit ene regeltje code bespaart ons het typen van een private field en een heleboel accolades.
Maar vergis je niet: **C# doet dat typwerk stiekem toch voor jou.** Bij het compileren maakt C# zelf een onzichtbaar private field aan dat de data bewaart.

### Wanneer gebruiken?
De vuistregel is simpel:
* **Start altijd met Auto-Properties.** (Sneller, leesbaarder).
* **Upgrade naar Full Properties** pas als je logica nodig hebt (zoals validatie of berekeningen).

{% hint style='tip' %}
**Visual Studio Tip**:
Je hoeft niet bang te zijn voor die upgrade. Als je later beslist dat `Voornaam` toch niet leeg mag zijn:
1. Zet je cursor op de naam van de property (`Voornaam`).
2. Druk `Ctrl + .` (of klik op de lamp/schroevendraaier).
3. Kies **"Convert to full property"**.

**Opgelet**: Merk op dat de syntax die VS gebruikt om een full property te schrijven anders is dan wat ik hier uitleg. Wanneer je VS laat doen krijg je een oplossing met allerlei ``=>`` tekens. Dit is heet **Expression Bodied Member syntax (EBM)**. Ik behandel deze nieuwere C# syntax in de appendix.
{% endhint %}



### Auto-Properties initialiseren

Wat als we willen dat een property standaard een bepaalde waarde heeft?
Bij fields deden we dit: `private int score = 100;`.
Bij auto-properties kan dit ook direct:

```csharp
public int Score { get; set; } = 100;
public string Huisdier { get; set; } = "Kat";
```

Elk nieuw object dat je maakt, zal nu starten met 100 punten en een kat. Simpel!


### Read-Only varianten (Dieper graven)

We zagen al de **private set**. Maar er is nog een variant: de **pure read-only** auto-property.

#### 1. Private Set (Aanpasbaar door de klasse)
De buitenwereld kan enkel lezen. De klasse zelf kan de waarde aanpassen (via methoden).

```csharp
// Kan aangepast worden door methoden als 'LevelUp()' of 'Reset()'
public int HuidigLevel { get; private set; } 
```

#### 2. Get Only (Immutable / Onveranderlijk)
Als je de `set` volledig weglaat bij een auto-property, ontstaat er iets speciaals.

```csharp
// Kan NOOIT meer veranderen na het aanmaken!
public string GeboortePlaats { get; } = "Hasselt";
```

Een **Get-Only** auto-property kan je **enkel** een waarde geven:
1. Met een initializer (zoals hierboven).
2. Of in de **constructor** (zie volgende hoofdstukken).

Eens het object bestaat, zit deze waarde muurvast. Zelfs de eigen klasse kan het niet meer aanpassen via methoden. Dit is geweldig voor data die echt nooit mag veranderen (zoals een ID-nummer of geboorteplaats).

{% hint style='info' %}
Dit concept noemt men **Immutability** (onveranderlijkheid). Het maakt je code robuuster omdat je zeker weet: "Eens dit object bestaat, blijft deze data voor altijd zo".
{% endhint %}

### Samenvatting

| Type | Syntax | Wie mag het aanpassen? |
| :--- | :--- | :--- |
| **Full Property** | `get { ... } set { ... }` | Iedereen (via logica) |
| **Auto Property** | `get; set;` | Iedereen (direct) |
| **Private Set** | `get; private set;` | Enkel de klasse zelf |
| **Get Only** | `get;` | **Niemand** (behalve constructor) |
