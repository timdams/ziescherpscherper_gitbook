## Properties

We zagen zonet dat fields of instantievariabelen (interne data) meestal `private` zijn om ze te beschermen. Maar hoe kunnen we ze dan veilig aanpassen?
Vroeger gebruikten programmeurs methoden (bv. `GetLeeftijd()` en `SetLeeftijd(5)`).
In C# doen we dit slimmer, met **Properties**.

{% hint style='tip' %}
**Properties** zijn de poortwachters van je data. Ze lijken op variabelen, maar zijn even krachtig als methoden.
{% endhint %}



### Star Wars: Waarom Properties?

In het Star Wars universum heb je goede oude "Darth Vader". Hij behoort tot de mysterieuze klasse van de Sith Lords. Een Sith Lord heeft een hoeveelheid energie (*The Force* zeg maar) waarmee hij kattekwaad kan uithalen. Deze energie kan nooit onder nul gezet worden.

Als we werken met een **public field**, hebben we een probleem:

```csharp
internal class SithLord
{
    public int Energie; // SLECHT IDEE!
}
//...
SithLord vader = new SithLord();
vader.Energie = -9999; // Oh nee, negatieve energie! Ongeldig!
```

We hebben dus een soort **douanier** of **buitenwipper** nodig die bij de ingang van onze variabele staat en controleert: "Hey, is die waarde wel groter dan 0?".

In C# noemen we die buitenwipper een **Property** (Eigenschap).

### Twee smaken properties
In C# heb je twee manieren om properties te schrijven:

1. **Full Properties**: Je schrijft alle code zelf. Handig als je **validatie** (controle) nodig hebt.
2. **Auto-Properties**: De "luie" manier. Handig als je gewoon data wil opslaan zonder speciale regels.


### 1. Full Properties (De controlefreak)

Een full property werkt samen met een **Private Field**.
* Het **private field** is de kluis waarin de data écht zit (`private int energie;`).
* De **property** is het loket met de douanier (`public int Energie`). De buitenwereld praat enkel met het loket.

Dit noemen we ook wel de **Backing Field** strategie.

```csharp
internal class SithLord
{
    // 1. Het Backing Field (De kluis - privé!)
    private int energie;

    // 2. De Property (Het loket - publiek!)
    public int Energie
    {
        get
        {
            // Code die wordt uitgevoerd als iemand de waarde VRAAGT
            return energie; 
        }
        set
        {
             // Code die wordt uitgevoerd als iemand een waarde wil INSTELLEN
             // 'value' is een speciaal woordje dat de nieuwe waarde bevat
             if(value >= 0)
             {
                 energie = value; // Stop het in de kluis
             }
        }
    }
}
```

Nu is onze Sith Lord veilig:
```csharp
SithLord vader = new SithLord();
vader.Energie = -50; // De setter weigert dit! energie blijft onveranderd.
vader.Energie = 100; // Dit mag wel.
```

{% hint style='tip' %}
Merk op dat we `energie` gebruiken (met underscore). Dit is een veelgebruikte afspraak voor **private backing fields**. Zo vergis je je minder snel met de property `Energie` (Hoofdletter).
{% endhint %}



Dankzij voorgaande code kunnen we nu buiten het object de property ``Energie`` gebruiken als volgt:

```csharp
SithLord Vader = new SithLord();
Vader.Energie = 20; //set
Console.WriteLine($"Vaders energie is {Vader.Energie}"); //get
```

Laten we eens inzoomen op de full property code.




#### Full property: identifier en datatype
De eerste lijn van een full property beschrijft de naam (identifier) en datatype van de property: ``public int Energie``

**Een property is altijd ``public``** daar dit de essentie van een property net is "de buitenwereld gecontroleerde toegang tot de interne staat van een object geven".

Vervolgens zeggen we wat voor **datatype** de property moet zijn en geven we het een naam die moet voldoen aan de identifier regels van weleer. Voor de buitenwereld zal een property zich gedragen als een gewone variabele, met de naam ``Energie`` van het type ``int``.


Indien je de property gaat gebruiken om een instantievariabele naar buiten beschikbaar te stellen, dan is het een goede gewoonte om dezelfde naam als dat veld te nemen maar nu met een hoofdletter (dus ``Energie`` i.p.v. ``energie``).

#### Full property: get gedeelte

Indien je wenst dat de property data **naar buiten** kan sturen, dan schrijven we de get-code. Binnen de accolades van de ``get`` schrijven we wat er naar buiten moet gestuurd worden.

```csharp
get
{
    return energie;
}
```

Dit werkt dus identiek aan een methode met een returntype. **Het element dat je met ``return`` teruggeeft in de get code moet uiteraard van hetzelfde type zijn als waarmee je de property hebt gedefinieerd (``int`` in dit geval).**

We kunnen nu van buitenaf toch de waarde van ``energie`` uitlezen via de property en het get-gedeelte, bijvoorbeeld ``int uitgelezen = palpatine.Energie;``.

{% hint style='tip' %}
We mogen eender wat doen in het get-gedeelte (net zoals bij methoden) zolang er finaal maar iets uitgestuurd wordt m.b.v. ``return``. Ik zal hier verderop meer over vertellen, want soms is het handig om *getters* te schrijven die de data transformeren voor ze uitgestuurd wordt.
{% endhint %}

<!-- \newpage -->


#### Full property: set gedeelte

In het set-gedeelte schrijven we de code die we moeten hanteren indien men van buiten een waarde aan de property wenst te geven om zo een instantievariabele aan te passen. 

```csharp
set
{
    energie = value;
}
```

De waarde die we van buiten krijgen (als een parameter zeg maar) zal altijd in een lokale variabele **``value``** worden bewaard binnenin de set-code. Deze zal van het type van de property zijn. 

{% hint style='tip' %}
Deze ``value`` parameter is een geserveerd keyword van de ``set`` syntax en kan je niet hernoemen of voor iets anders gebruiken. 
{% endhint %}


Vervolgens kunnen we ``value`` toewijzen aan de interne variabele indien gewenst: ``energie = value;``. Uiteraard kunnen we die toewijzing dus ook gecontroleerd laten gebeuren, wat ik zo meteen uitleg.

We kunnen vanaf nu van buitenaf waarden toewijzen aan de property en zo ``energie`` toch bereiken: ``palpatine.Energie = 50;``.

{% hint style='danger' %}
Je bent niet verplicht om een property te maken wiens naam overeen komt met een bestaande instantievariabele (**maar dit wordt wel aangeraden**). 

Dit mag dus ook:

```csharp
internal class Auto
{
    private int benzinePeil;

    public int FuelLevel
    {
        get { return benzinePeil; }
        set { benzinePeil = value; }
    }
}
```
{% endhint %}


{% hint style='tip' %}
Visual Studio heeft een ingebouwde *snippet* om snel een full property, inclusief een bijhorende private instantievariabele, te schrijven. **Typ "propfull" gevolgd door twee maal op de tab-toets te duwen.**
{% endhint %}




### Full property met toegangscontrole

De full property ``Energie`` heeft nog steeds het probleem dat we negatieve waarden kunnen toewijzen (via de ``set``) die dan vervolgens zal toegewezen worden aan ``energie``.

**Properties hebben echter de mogelijkheid om op te treden als wachters van en naar de interne staat van objecten.**

We kunnen in de ``set`` code extra controles inbouwen. Aangezien de variabele ``value`` de waarde krijgt die we extern aan de property toewijzen, kunnen we deze controleren en zo nodig de toewijzing voorkomen. Volgende voorbeeld zal enkel de waarde toewijzen indien deze groter of gelijk aan 0 is:

```csharp
public int Energie
{
    get
    {
        return energie;
    }
    set
    {
        if(value >= 0)
            energie = value;
    }
}
```

Volgende lijn zal dus geen effect hebben:


```csharp 
palpatine.Energie = -1;
```

We mogen de code binnen ``set`` en ``get`` zo complex maken als we zelf willen. 

{% hint style='tip' %}
Probeer wel steeds de OOP-principes te hanteren wanneer je met properties werkt: in de ``get`` en ``set`` van een property mogen enkel die dingen gebeuren die de verantwoordelijkheid van de property zelf zijn. Je gaat dus bijvoorbeeld niet controleren of een andere property geen illegale waarden krijgt, daar is die andere property voor verantwoordelijk.
{% endhint %}





<!-- \newpage -->


### 2. Auto Properties (De snelle oplossing)

Vaak heb je echter geen speciale regels nodig. Je wil gewoon "een variabele die public is".
Vroeger moesten programmeurs daar gigantisch veel full properties voor typen.

C# heeft hiervoor de **Auto Property** uitgevonden. Dit is syntaxversuikering (syntactic sugar).
Je schrijft dit:
```csharp
public int Leeftijd { get; set; }
```

En C# maakt **achter de schermen** automatisch een onzichtbaar backing field aan en schrijft de get/set code voor jou.

**Wanneer gebruik je wat?**
* Heb je **controle/validatie** nodig? -> **Full Property**
* Gewoon data opslaan? -> **Auto Property**

{% hint style='tip' %}
Typ `prop` en druk 2x op TAB in Visual Studio om razendsnel een auto-property te maken.
{% endhint %}

---

### Read-only Properties

Soms wil je dat data wel gelezen kan worden, maar niet aangepast.
Bijvoorbeeld: Je mag weten hoeveel `Levens` de speler heeft, maar je mag dat niet zomaar aanpassen.

**Optie 1: Alleen een getter (Full Property)**
```csharp
public int Levens
{
    get { return levens; }
    // Geen set = niet aanpasbaar van buitenaf!
}
```

**Optie 2: Private Set (Auto Property)**
Je kan de setter `private` maken. Zo kan je **in de klasse zelf** de waarde wel nog aanpassen, maar de buitenwereld niet.
```csharp
public int Score { get; private set; }
```
Dit is erg handig! Je klasse blijft de baas over zijn eigen data.


### Opletten met interne aanpassingen

Als je een full property hebt met validatie (bv. controleren op < 0), gebruik dan **ook binnen je eigen klasse** die property!

**FOUT:**
```csharp
public void Reset()
{
    energie = -50; // Oeps, rechtstreeks het field aangepast.
                    // De validatie in de property is omzeild!
}
```

**JUIST:**
```csharp
public void Reset()
{
    Energie = -50;  // Goed! De property voert de checks uit 
                    // en zal deze illegale waarde weigeren.
}
```





### Computed Properties (Transformerende properties)

Je kan properties ook gebruiken om data die je al hebt in een andere vorm te gieten.
Stel dat je `Voornaam` en `Achternaam` hebt. Je wil niet elke keer zelf de volledige naam aan elkaar plakken.

Je kan een property maken die dit "live" berekent telkens je hem opvraagt:

```csharp
internal class Persoon
{
    public string Voornaam { get; set; } // Auto-property
    public string Achternaam { get; set; } // Auto-property

    // Dit is een COMPUTED property. Er is geen 'set'.
    // Hij berekent zijn waarde telkens opnieuw.
    public string VolledigeNaam
    {
        get
        { 
            return $"{Voornaam} {Achternaam}";
        }
    }
}
```
Zie je dat `VolledigeNaam` geen backing field heeft? Hij gebruikt de andere properties om zijn resultaat te maken. Handig!







{% hint style='tip' %}
**Methode of property?**

Een veel gestelde vraag bij beginnende OOP-ontwikkelaars is: *"Moet dit in een property of in een methode geplaatst worden?"*

De regels zijn niet in steen gebeiteld, maar ruwweg kan je stellen dat:

* Betreft het een actie of gedrag: iets dat het object moet doen (tekst tonen, iets berekenen of aanpassen, enz.) dan plaats je het in een **methode**. 
* Betreft het een eigenschap van het object, dan gebruik je een **property** indien het om data gaat die snel verkregen of berekend kan worden. Gaat het om data die zwaardere en/of langere berekeningen vereist dan is een methode nog steeds aangeraden.

{% endhint %}










{% hint style='info' %}
**Nieuw in C# 14: Het `field` keyword**

Vroeger was je verplicht om full properties te schrijven als je validatie wou toevoegen. Sinds C# 14 kan dit veel korter met het `field` keyword.
[Lees er meer over in de appendix](../Bappendix/fieldkeyword.md)
{% endhint %}
