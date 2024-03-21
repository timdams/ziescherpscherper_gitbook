# Gevorderde klasseconcepten

Nu we weten wat er allemaal achter de schermen gebeurt met onze objecten, wordt het tijd om wat meer geavanceerde concepten van klassen en objecten te bekijken. 

We hebben al ontdekt dat een klasse kan bestaan uit:
* **Instantievariabelen**: variabelen die de toestand van het individuele object bijhouden.
* **Methoden**: om objecten voor ons te laten werken (gedrag).
* **Properties**: om op een gecontroleerde manier toegang tot de interne staat van de objecten te verkrijgen.

Uiteraard is dit niet alles. In dit hoofdstuk bekijken we:
* **Constructors**: een gecontroleerde manier om de beginstaat van een object in te stellen.
* **``static``**: die je de mogelijkheid geeft een (deel van je) klasse te laten werken als een object.
* **Object initializer syntax**: een recente C# aanvulling die het aanmaken van nieuwe objecten vereenvoudigd.

## Constructors

### Werking new operator
Objecten die je aanmaakt komen niet zomaar tot leven. Nieuwe objecten maken we aan met behulp van de ``new`` operator zoals we al gezien hebben:


```csharp
Student frankVermeulen = new Student();
```

 De ``new`` operator doet 3 dingen:

* Het maakt een object aan in het heap geheugen.
* Het roept de **constructor** van het object aan voor eventuele extra initialisatie.
* Het geeft een referentie naar het object in het heap geheugen terug.

Via de constructor van een klasse kunnen we extra code meegeven die moet uitgevoerd worden **telkens een nieuw object van dit type wordt aangemaakt**.

De constructor is een unieke methode die wordt aangeroepen bij het aanmaken van een object, daarom dat we ronde haakjes zetten bij ``new Student()``.

Momenteel hebben we in de klasse ``Student`` de constructor nog niet expliciet beschreven, maar zoals je aan bovenstaande code ziet bestaat deze constructor al wel degelijk...maar doet hij niets extra (de instantievariabelen en properties krijgen gewoon hun default waarde toegekend, afhankelijk van hun type).

{% hint style='danger' %}

De naam "constructor" zegt duidelijk waarvoor het concept dient: *het construeren van objecten*. Constructors mogen maar op 1 moment in het leven van een object aangeroepen worden: tijdens hun geboorte m.b.v. ``new``. 
**Je mag (en kan) een constructor op geen enkel ander moment gebruiken!**
{% endhint %}


### Soorten constructors

Als programmeur van eigen klassen zijn er 3 opties voor je:

* Je gebruikt geen zelfgeschreven constructors: het leven gaat voort zoals het is. Je kunt objecten aanmaken zoals eerder getoond en een *onzichtbare* standaard (default) constructor wordt voor je uitgevoerd.
* Je hebt enkel een **default constructor** nodig. Je kan nog steeds objecten met ``new Student()`` aanmaken, maar je gaat zelf beschrijven wat er moet gebeuren bij de default constructor. De default constructor herken je aan het feit dat je geen parameters meegeeft aan de constructor tijdens de ``new`` aanroep.
* Je wenst gebruik te maken van één of meerdere **overloaded constructors**, hierbij zal je dan actuele parameters kunnen meegeven bij de creatie van een object, bijvoorbeeld: ``new Student(24, "Jos")``.


{% hint style='warning' %}

![](../assets/attention.png)

**Constructors zijn soms gratis, soms niet.** Een lege default constructor voor je klasse krijg je standaard wanneer je een nieuwe klasse aanmaakt. Je ziet deze niet en kan deze niet aanpassen. Je kan echter daarom altijd objecten met ``new myClass()`` aanmaken.**Van zodra je echter beslist om zelf één of meerdere constructors te schrijven zal C# zeggen "Ok, jij je zin, nu doe je alles zelf". De default constructor die je gratis kreeg zal ook niet meer bestaan en heb je die dus nodig dan zal je die dus zelf moeten schrijven!**

*Een nadeel van C# is dat het soms dingen voor ons achter de schermen doet, en soms niet.* Het is mijn taak je dan ook duidelijk te maken wanneer dat wél en wanneer dat net niét gebeurt. Ik vergelijk het altijd met het werken met aannemers: soms ruimen ze hun eigen rommel op nadien, maar soms ook niet. Alles hangt er van af hoe ik die aannemer heb opgetrommeld.

{% endhint %}


### Default constructors

De default constructor is een constructor die geen extra parameters aanvaardt. Een default constructor bestaat ALTIJD uit volgende vorm:

* Iedere constructor is altijd ``public`` .
* Heeft geen returntype, ook niet ``void``.
* Heeft als naam de naam van de klasse zelf.
* Heeft geen extra formele parameters.

Stel dat we een klasse ``Student`` hebben:

```csharp
class Student
{
    public int UurVanInschrijven {private set; get;}
}

```

We willen telkens een Student-object wordt aangemaakt bijhouden op welk uur van de dag dit plaatsvond. Eerst schrijven de default constructor, deze ziet er als volgt uit:

```csharp
class Student
{
    public Student()
    {
        // zet hier de code die bij initialisatie moet gebeuren
    }
    public int UurVanInschrijven {private set; get;}
}
```

Zoals verteld moet de constructor de naam van de klasse hebben, ``public`` zijn en geen returntype definiëren.

Vervolgens voegen we de code toe die we nodig hebben:

```csharp
class Student
{
    public Student()
    {
        UurVanInschrijven = DateTime.Now.Hour;
    }

    public int UurVanInschrijven {private set; get;}
}
```


Telkens we nu een object zouden aanmaken met ``new Student()`` zal deze een ``UurVanInschrijven`` hebben dat afhangt van het moment waarop we de code uitvoeren. Beeld je in dat we dit programma uitvoeren om half twaalf 's morgens:


```csharp
Student eenStudent = new Student();
```

Dan zal de property ``UurVanInschrijven`` van ``eenStudent`` op ``11`` worden ingesteld.


{% hint style='tip' %}
Constructors zijn soms nogal zwaarwichtig indien je enkel een eenvoudige auto-property een startwaarde wenst te geven. Wanneer dat het geval is mag je dit ook als volgt doen:

```csharp
class Student
{
    public int UurVanInschrijven {private set; get;} = 2;
}
```
{% endhint %}
