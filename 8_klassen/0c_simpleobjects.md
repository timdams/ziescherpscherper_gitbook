
### De anatomie van een klasse

Laten we stap voor stap een klasse opbouwen en kijken wat de onderdelen zijn.

#### Object methoden (Gedrag)

Stel dat we een klasse `Mens` maken. We willen dat deze mensen iets kunnen **doen**, bv. praten.
Gedrag vertalen we in C# naar **methoden**. We voegen daarom een methode `Praat()` toe aan onze klass:



```csharp
internal class Mens
{
    public void Praat()
    {
        Console.WriteLine("Ik ben een mens!");
    }
}
```

We zien twee nieuwe aspecten:

* Het keyword **``static``** mag je **niet** voor een methode signatuur zetten (later ontdekken we wanneer dat soms wel moet) .
* Voor de methode plaatsen we **``public``** : dit is een *access modifier* die aangeeft dat de buitenwereld deze methode op het object kan aanroepen.

Je kan nu elders objecten aanmaken en ieder object z'n methode ``Praat`` aanroepen:

```csharp
Mens joske = new Mens();
Mens alfons = new Mens();
joske.Praat();
alfons.Praat();
```

Er zal twee maal ``Ik ben een mens!`` op het scherm verschijnen. Waarbij ``joske`` en ``alfons`` zelf verantwoordelijk hiervoor waren dat dit gebeurde.

<!-- \newpage -->


#### Access modifiers (Wie mag waar aan?)

De keywords `public` en `private` noemen we **access modifiers**. Ze bepalen de toegang:

* **`public`**:  "Open". Iedereen (ook code buiten de klasse) mag deze methode gebruiken.
* **`private`**: "Privé". Enkel code **binnenin de klasse zelf** mag dit gebruiken.

{% hint style='tip' %}
**Geen modifier = `private`**
Als je niets voor een methode of variabele zet, maakt C# het automatisch `private`.
`void DoeIets()` schrijven is dus hetzelfde als `private void DoeIets()`.

**Goede afspraak:** Schrijf **altijd** expliciet `private` of `public`. Zo is er nooit verwarring.
{% endhint %}

Test volgende klasse eens. Kan je `VertelGeheim` aanroepen op `joske`?

```csharp
internal class Mens
{
    public void Praat()
    {
        Console.WriteLine("Ik ben een mens!");
    }

    private void VertelGeheim()
    {
        Console.WriteLine("Ik ben verliefd op Anneke");
    }
}
```

Het antwoord is nee. De regel `joske.VertelGeheim();` zal een rode kriebellijn geven. De methode is privé en mag niet van buitenaf aangeroepen worden.



#### Waarom Private? (Encapsulatie mag je vergeten)

"Waarom zou ik iets maken dat ik niet mag gebruiken?", vraag je je misschien af.

Dit heeft te maken met **veiligheid** en **complexiteit**.
Stel dat je een methode `StartAuto()` hebt. Intern moet die methode misschien 10 stappen doen: 
1. `InjecteerBrandstof()`
2. `VonkBougies()`
3. `DraaiStartMotor()`

Je wil niet dat een bestuurder (de gebruiker van jouw klasse) per ongeluk `VonkBougies()` aanroept terwijl de motor al draait. Dus maak je die innerlijke stappen `private`. De bestuurder mag enkel aan de veilige, publieke knop `StartAuto()`.

**De klasse `Mens` gebruikt z'n eigen methoden**
Binnenin de klasse zelf mag je natuurlijk wel alles gebruiken. Kijk maar:

```csharp
internal class Mens
{
    public void Praat()
    {
        Console.WriteLine("Ik ben een mens!");
        VertelGeheim(); // DIT MAG! We zitten binnenin de klasse.
    }

    private void VertelGeheim()
    {
        Console.WriteLine("Ik ben verliefd op Anneke");
    }
}
```

Als we nu `joske.Praat()` aanroepen, zal Joske zelf zijn geheim verklappen.
{% hint style='tip' %}
Met behulp van de **dot-operator** (``.``) kunnen we aan alle informatie die ons object aanbiedt aan de buitenwereld. Ook dit zag je reeds toen je een ``Random``-object hadden: we konden maar een handvol zaken aanroepen op zo'n object, waaronder de ``Next`` methode.
{% endhint %}



Het is natuurlijk een beetje vreemd dat nu al onze objecten zeggen dat ze verliefd zijn op Anneke. Dit is niet het smurfendorp met maar 1 meisje! Dit gaan we verderop oplossen. *Stay tuned!*


#### Instantievariabelen (fields)

Methoden zijn het **gedrag**. Maar objecten hebben ook een **geheugen**. Ze moeten dingen kunnen onthouden.
Hiervoor gebruiken we **Fields** (ook wel datavelden of instantievariabelen genoemd).

Een field is een variabele die **in de klasse** staat, maar **buiten de methoden**.

```csharp
internal class Mens
{
    private int geboorteJaar = 1970; //instantievariabele

    public void Praat()
    {
        Console.WriteLine("Ik ben een mens! ");
        Console.WriteLine($"Ik ben geboren in {geboorteJaar}.");
    }
}
```

<!-- \newpage -->


Enkele belangrijke concepten:

* De instantievariabele ``geboorteJaar`` zetten we private: we willen niet dat de buitenwereld het geboortejaar van een object kan aanpassen. Beeld je in dat dat in de echte wereld ook kon. Dan zou je naar je kameraad kunnen roepen "Hey Adil, jouw geboortejaar is nu 1899! Ha!" Waarop Adil vloekend verandert in een steenoud mannetje.
* We geven de variabele een beginwaarde ``1970``. Alle objecten zullen dus standaard in het jaar 1970 geboren zijn wanneer we deze met ``new`` aanmaken.
* We kunnen de inhoud van de instantievariabelen lezen en veranderen vanuit andere delen in de code. Zo gebruiken we ``geboorteJaar`` in de tweede lijn van de ``Praat`` methode. Als je die methode nu zou aanroepen dan zou het geboortejaar van het object dat je aanroept mee op het scherm verschijnen.

{% hint style='danger' %}

Ik moet ook dringend enkele extra *niet-officiële* identifier regels in het leven roepen:

* Klassenamen en methoden in klassen beginnen altijd met een hoofdletter.
* Alles dat ``public`` is in een klasse begint ook met een hoofdletter.
* Alles dat ``private`` is begint met een kleine letter (of liggend streepje), tenzij het om een methode gaat, die begint altijd met een hoofdletter.

Dit zijn geen officiële regels, maar afspraken die veel programmeurs onderling hebben gemaakt. Het maakt de code leesbaarder.
{% endhint %}



>![](../assets/gotopolice.png)Hola! Stop! Ik zag u denken: "Als ik dat field gewoon `public` maak, ben ik van al dat gezeur af."
>
> **Fields/instantievariabelen zet je ALTIJD private.**
>
> "Waarom?", hoor ik u vragen. Wel, stel dat je `public int geboorteJaar` maakt. Dan kan iemand anders in zijn code schrijven: `joske.geboorteJaar = -500;`.
> Een mens geboren in het jaar -500? Dat klopt niet.
> Door het field `private` te houden, en een methode `VeranderGeboortejaar` te maken, kunnen we controleren of de waarde wel klopt!

Kijk maar:

```csharp
internal class Mens
{
    private int geboorteJaar = 1970;

    public void VeranderGeboortejaar(int nieuwJaar)
    {
        // We beschermen ons field!
        if(nieuwJaar > 1900 && nieuwJaar < 2030)
        {
            geboorteJaar = nieuwJaar;
        }
    }
```

Zo bepalen wij (de klasse) de regels. De buitenwereld moet zich eraan houden.
Verderop in dit boek leren we **Properties**, wat dé C#-manier is om dit nog makkelijker te doen. Maar het principe blijft hetzelfde: Bescherm je data!


<!-- \newpage -->



#### Andere lieven

We kunnen nu het probleem oplossen dat al onze mensen verliefd zijn op Anneke. Volgende code toont dit:

```csharp
internal class Mens
{
    private string lief = "niemand";

    public void VeranderLief(string nieuwLief)
    {
        lief = nieuwLief;
    }
    public void Praat()
    {
        Console.WriteLine("Ik ben een mens!");
        VertelGeheim();
    }

    private void VertelGeheim()
    {
        if( lief != "niemand")
            Console.WriteLine($"Ik ben verliefd op {lief}.");
        else
            Console.WriteLine("Ik ben op niemand verliefd.");
    }
}
```

Nu kunnen we dus *"Temptation Island - de OOP editie"* beginnen:

```csharp
Mens deelnemer1 = new Mens();
Mens deelnemer2 = new Mens();
deelnemer1.Praat();
deelnemer2.Praat();

deelnemer2.VeranderLief("Phoebe");
deelnemer1.Praat();
deelnemer2.Praat();

deelnemer1.VeranderLief("Camilla");
deelnemer1.Praat();
deelnemer2.Praat();
```

<!-- \newpage -->


De uitvoer van voorgaande code zal zijn:


```text
Ik ben een mens!
Ik ben op niemand verliefd.
Ik ben een mens!
Ik ben op niemand verliefd.
Ik ben een mens!
Ik ben op niemand verliefd.
Ik ben een mens!
Ik ben verliefd op Phoebe.
Ik ben een mens!
Ik ben verliefd op Camilla.
Ik ben een mens!
Ik ben verliefd op Phoebe.
```



>![](../assets/attention.png)Veel beginnende programmeurs maken fouten op het correct kunnen onderscheiden wat de klassen en wat de objecten in hun opgave juist zijn. Het is altijd belangrijk te begrijpen dat een klasse weliswaar beschrijft hoe alle objecten van dat type werken, maar op zich gaat die beschrijving steeds over 1 object uit de verzameling. *Say what now?!*


### Veelgemaakte naamgevingsfouten

Beginners maken vaak fouten tegen de namen van hun klassen. Hier zijn twee regels:

**1. Het Meervoud-Probleem (`Student` vs `Studenten`)**
Een klasse is een blauwdruk voor **één** ding.
* FOUT: `class Studenten { ... }` 
* JUIST: `class Student { ... }`

Later in je code zal je dan een *lijst* maken van het type `Student`. Maar de klasse zelf beschrijft er maar eentje.

**2. Het Nummer-Probleem (`Level1`, `Level2`)**
Stel, je maakt een game met levels.
* FOUT: `class Level1`, `class Level2`, `class Level3`...
* JUIST: `class Level` 

Je maakt één klasse `Level` (met een field `int LevelNummer` of `string Naam`). En daarna maak je zoveel objecten als je wil:
```csharp
Level grot = new Level();
Level strand = new Level();
Level vulkaan = new Level();
```

Als je merkt dat je `Klasse1`, `Klasse2` aan het typen bent... Stop! Je hebt waarschijnlijk **één klasse** nodig, en **meerdere objecten**.





