

### Overloaded constructors

Soms wil je parameters aan een object meegeven bij de creatie ervan. We willen bijvoorbeeld de bijnaam meegeven die het object moet hebben bij het aanmaken.

Met andere woorden, stel dat we dit willen schrijven:


```csharp
Student jos = new Student("Lord Oakenwood");
```

Als we dit met voorgaande klasse uitvoeren , die enkel een default constructor heeft, zal de code een fout geven. C# vindt geen constructor die een ``string`` als actuele parameter aanvaardt.

Net zoals bij overloading van methoden kunnen we ook constructors overloaden. De code is verrassend gelijkaardig aan method overloading:

```csharp
class Student
{
    public Student(string bijnaamIn)
    {
        bijNaam = bijnaamIn;
    }
    public string BijNaam { get; private set;}
}
```

Dat was eenvoudig, hé?

**Maar denk eraan, je hebt een overloaded constructor geschreven en dus heeft C# gezegd: *"Ok, je schrijft zelf constructors? Trek je plan nu maar. De default constructor zal je ook nu zelf moeten schrijven."***

Je kan nu enkel je objecten nog via de overloaded constructors aanmaken. Schrijf je ``new Student()`` dan zal je een error krijgen. Wil je de default constructor toch nog hebben dan zal je die dus ook expliciet moeten schrijven, bijvoorbeeld:


```csharp
class Student
{
    private const string DEFBIJNAAM = "Geen";
    //Default
    public Student() 
    {
       BijNaam = DEFBIJNAAM;
    }
    //Overloaded
    public Student(string bijnaamIn) 
    {
        BijNaam = bijnaamIn;
    }
    public string BijNaam { get; private set;}
}
```


{% hint style='warning' %}

![](../assets/attention.png)

Voorgaande wil ik nog eenmaal herhalen. Herinner je m'n voorbeeld van die aannemers die soms wel en soms niet opruimden? Laten we nog eens samenvatten hoe het zit met constructors in C#:

**Als je geen constructors schrijft krijg je een default constructor gratis. Die doet echter niets extra buiten alle instantievariabelen en properties default waarden geven.**

Van zodra je één constructor zelf schrijft, default of overloaded, krijg je niets meer gratis én zal je dus zelf die constructors moeten bijschrijven die jouw code vereist.
{% endhint %}



#### Meerdere overloaded constructors
Wil je meerdere overloaded constructors dan mag dat ook. Je wilt misschien een constructor die de bijnaam vraagt alsook een ``bool`` om mee te geven of het om een werkstudent gaat:

```csharp
class Student
{
     private const string DEFBIJNAAM = "Geen";
    //Default
    public Student() 
    {
       BijNaam = DEFBIJNAAM;
    }

    //Overloaded 1
    public Student(string bijnaamIn) 
    {
        BijNaam = bijnaamIn;
    }

    //Overloaded 2
    public Student(string bijnaamIn, bool isWerkStudentIn) 
    {
        BijNaam = bijnaamIn;
        IsWerkStudent = isWerkStudentIn
    }

    public string BijNaam { get; private set;}
    public string IsWerkStudent { get; private set;}

}

```

{% hint style='tip' %}
Merk op dat je ook **full properties best aanroept in je constructor** en niet rechtstreeks de achterliggende instantievariabele. Zo kan je ogenblikkelijk de typische controles in een ``set`` in gebruik nemen.

Beeld je in dat het schoolsysteem crasht wanneer een nieuwe student een onbeleefde bijnaam invoert. Wanneer dit gebeurt moet de bijnaam altijd gewoon op "Good boy" gezet worden, ongeacht de effectieve bijnaam van de student. Via een ``set``-controle kunnen we dit doen én vervolgens passen we de auto-property aan naar een full property zodat er een ingebouwde controle kan plaatsvinden:

```csharp
class Student
{
    private const string DEFBIJNAAM = "Good boy";
    //Default
    public Student() 
    {
       bijNaam = DEFBIJNAAM;
    }

    //Overloaded
    public Student(string bijnaamIn) 
    {
        bijNaam = bijnaamIn;
    }

    public string BijNaam
    {
        private set
        {
            if(value == "stommerik") //pardon my french
            {
                bijNaam = DEFBIJNAAM;
            }
            else 
                bijNaam = value;
        }
        get
        {
            return bijNaam;
        }
    }

    private string bijNaam;
}
```

Deze manier voorkomt dat de constructors verantwoordelijk zijn opdat properties de juiste waarden krijgen. Leg steeds de verantwoordelijk bij het element zelf. Door dit te doen hoef je ook niet in iedere constructor te controleren doorgegeven parameters wel geldig zijn. Ook hier blijft de regel gelden: als je dubbele code dicht bij elkaar ziet staan dan is de kans groot dat je dit kan vereenvoudigen.

{% endhint %}


### Constructors hergebruiken met ``this()``

Beeld je in dat je volgende klasse hebt:

```csharp
class Microfoon
{
    public Microfoon(string merkIn, bool isUitverkochtIn)
    {
        IsUitverkocht = isUitverkochtIn;
        Merk = merkIn;
    }

    public Microfoon(string merkIn)
    {
        IsUitverkocht = false;
        Merk = merkIn;
    }

    public Microfoon()
    {
        Merk = "Onbekend";
        isUitverkocht = true;
    }

    public string Merk { get; set;}
    public bool IsUitverkocht {get; set;}
}
```

Bij voorgaande code gaat er mogelijk bij sommige van jullie een alarmbelletje af vanwege de kans op quasi dezelfde code in de verschillende constructors. En dat is een terecht alarm! Om te voorkomen dat we steeds dezelfde toewijzingen moeten schrijven in constructors laat C# toe dat je een andere constructor kunt aanroepen bij een constructor call. We gebruiken hier een speciale methode aanroep ``this()`` bij de constructorsignatuur. Via deze aanroep kunnen we dan eventueel parameters meegeven, afhankelijk wat we nodig hebben. De compiler zal aan de hand van de parameters (of het ontbreken) er aan beslissen welke constructor nodig is met behulp van de klassieke *method overload resolution* regels en de **betterness** regel toepassen.




Voorgaande klasse gaan we herschrijven zodat alle constructors de bovenste overloaded constructor gebruiken en zo voorkomen dat we te veel dubbele code hebben:

```csharp
class Microfoon
{
    public Microfoon(string merkIn, bool isUitverkochtIn)
    {
        IsUitverkocht = isUitverkochtIn;
        Merk = merkIn;
    }

    public Microfoon(string merkIn): this(merkIn, false)
    {  }

    public Microfoon(): this ("Onbekend", true)
    {  }

    public string Merk { get; set;}
    public bool IsUitverkocht {get; set;}
}
```

Bij de tweede overloaded constructor geven we de binnenkomende parameter ``merkIn`` gewoon door naar de ``this()`` aanroep en voegen er nog een tweede literal, ``false``, aan toe. De compiler zal nu via **method overload resolution** op zoek gaan naar de best passende constructor, wat in dit geval de bovenste overloaded constructor zal zijn.

Uiteraard ben je vrij om in de constructor zelf nog steeds code te plaatsen. Het is gewoon belangrijk dat je de volgorde begrijpt waarin de constructor-code wordt doorlopen. Stel dat we volgende constructor toevoegen:

```csharp
public Microfoon(bool isUitverkochtIn): this("Bovarc", isUitverkochtIn)
{
    Merk = "Wit Product";
}
```

Wanneer we een object aanmaken als volgt ``new Microfoon(true)`` dan zal uiteindelijk dit object van het merk ``Wit Product`` zijn. Er gebeurt namelijk het volgende:

1. De overloaded constructor ``Microfoon(bool isUitverkochtIn)`` wordt aangeroepen.
2. Ogenblikkelijk wordt de meegegeven actuele parameter ``isUitverkochtIn`` doorgegeven om de overloaded constructor ``Microfoon(string merkIn, bool isUitverkochtIn)`` te benaderen.
3. Deze constructor zal het ``Merk`` op ``Bovarc`` zetten en ``IsUitverkocht`` op ``true`` (daar we die parameter doorgeven).
4. We keren nu terug naar de contructor ``Microfoon(bool isUitverkochtIn)`` en voeren de code hiervan uit. Bijgevolg wordt de waarde in ``Merk`` overschreven met ``Wit Product``. 






#### Welke constructors moet ik nu eigenlijk allemaal voorzien? 

Dit hangt natuurlijk af van de soort klasse dat je maakt. Een constructor is minimaal nodig om ervoor te zorgen dat alle variabele die essentieel zijn in je klasse een beginwaarde hebben. Beeld je volgende klasse voor die een breuk voorstelt:

```csharp
class Breuk
{
    public int Noemer {get; private set;}
    private int Teller {get; private set;}
    public double BerekenBreuk()
    {
        return (double)Teller/Noemer;
    }
}
```

De methode zal een ``DivideByZeroException`` opleveren als ik de methode ``BerekenBreuk`` zou aanroepen nog voor de ``Noemer`` een waarde heeft gekregen (deling door nul, weet je wel):

```csharp
Breuk eenBreuk = new Breuk();
int resultaat = eenBreuk.BerekenBreuk(); //BAM!Een exception! 
```

Via een constructor kunnen we dit soort bugs voorkomen. We beschermen ontwikkelaars hiermee dat ze jouw klasse foutief gebruiken. Door een overloaded constructor te schrijven die een noemer en teller vereist verplichten we de ontwikkelaar jouw klasse correct te gebruiken (en kunnen geen breuk-objecten met de default constructor aangemaakt worden). 

Eerst veranderen we de auto-property ``Noemer`` naar een full property:

```csharp
private int noemer;
public int Noemer 
{
    get 
    { 
        return noemer;
    }
    private set
    {
        if(value != 0)
            noemer = value; 
        else
            noemer = 1; //of werp Exception op zoals eerder uitgelegd.
    }
}
```



En vervolgens voegen we een overloaded constructor toe:

```csharp
public Breuk(int tellerIn, int noemerIn)
{
    Teller = tellerIn;
    Noemer = noemerIn
}
```

Finaal wordt dan onze klasse:

```csharp
class Breuk
{
    public Breuk(int tellerIn, int noemerIn)
    {
        Teller = tellerIn;
        Noemer = noemerIn
    }    
    private int Teller {get; private set;}

    private int noemer;
    public int Noemer 
    {
        get 
        { 
            return noemer;
        }
        private set
        {
            if(value != 0)
                noemer = value; 
            else
                noemer = 1; //of werp Exception op zoals eerder uitgelegd.
        }
    }
}
```

Hierdoor kan ik geen ``Breuk`` objecten meer als volgt aanmaken:``Breuk eenBreuk = new Breuk();`` Maar ben ik verplicht deze als volgt aan te maken:

``Breuk eenBreuk = new Breuk(21,8);``






### Pong met constructors
We zullen deze nieuwe informatie gebruiken om onze ``Pong``-klasse uit het eerste hoofdstuk te verbeteren door deze de nodige constructors te geven. Namelijk een default die een balletje aanmaakt dat naar rechtsonder beweegt, en één overloaded constructor die toelaat dat we zelf kunnen kiezen wat de beginwaarden van ``X``, ``Y``, ``VectorX`` en ``VectorY`` zullen zijn:

```csharp
class Balletje
{
    public Balletje(int xin, int yin, int vxIn, int vyIn)
    {
        X = xin;
        Y = yin;
        VectorX = vxIn;
        VectorY = vyIn;
    }

    public Balletje(): this(5,5,1,1)
    {

    }

    //...
```

We kunnen nu op 2 manieren balletjes aanmaken:
```csharp
Balletje bal1 = new Balletje();
Balletje bal2 = new Balletje(10,8,-2,1);
```

{% hint style='tip' %}
Je zou ook kunnen overwegen om in de default constructor het balletje een willekeurige locatie en snelheid te geven:

```csharp
static Random rng =new Random();
public Balletje()
{
    X = rng.Next(0, Console.WindowWidth);
    Y = rng.Next(0, Console.WindowWidth);
    VectorX = rng.Nex(-2,3);
    VectorY = rng.Nex(-2,3);
}
```
{% endhint %}




