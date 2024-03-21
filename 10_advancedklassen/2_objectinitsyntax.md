## Object initializer syntax

Het is niet altijd duidelijk hoeveel overloaded constructors je juist nodig hebt. Meestal beperken we het tot de default constructor en 1 of 2 heel veel gebruikte overloaded constructors. 

Dankzij **object initializer syntax** kan je ook parameters tijdens de aanmaak van objecten meegeven zonder dat je hiervoor een specifieke constructor moet schrijven.

**Object initializer syntax laat je toe om tijdens (eigenlijk direct er na) creatie van een object, properties beginwaarden te geven.**

{% hint style='tip' %}
Object initializer syntax is een eerste glimp in het feit waarom properties zo belangrijk zijn in C#. Je kan object initializer syntax enkel gebruiken om via properties je object extra beginwaarden te geven.
{% endhint %}


Stel dat we volgende klasse hebben waarin we enkele auto-properties gebruiken. Merk op dat dit evengoed full properties mochten zijn. Voor object initializer syntax maakt dat niet uit, het ziet toch enkel maar het ``public`` gedeelte van de klasse:

```csharp
class Meting
{
    public double Temperatuur {get;set;}
    public bool IsGeconfirmeerd {get;set;}
}
```


We kunnen deze properties beginwaarden geven via volgende initializer syntax:


```csharp
Meting meting = new Meting() { Temperatuur = 3.4, IsGeconfirmeerd = true};
```

Object initializer syntax bestaat er uit dat je een object aanmaakt met de **default constructor** en dat je dan tussen accolades een lijst van properties en hun beginwaarden kunt meegeven. Object initializer werkt enkel indien het object een default constructor heeft (je hoeft deze niet expliciet te maken indien je klasse geen andere constructors heeft zoals in een eerder hoofdstuk al besproken). 

{% hint style='tip' %}
Bovenstaande code mag ook iets korter nog:


```csharp
Meting meting = new Meting { Temperatuur = 3.4, IsGeconfirmeerd = true};
```

Zie je het verschil? De ronde haakjes van de default constructor mag je dus achterwege laten.
{% endhint %}


De volgorde waarin je code wordt uitgevoerd is wel belangrijk. Je ziet het niet duidelijk, maar sowieso wordt eerst nu de default constructor aangeroepen. Pas wanneer die klaar is zullen de properties de waarden krijgen die je meegeeft tussen de accolades. Als je dus zelf een default constructor in ``Meting`` had geschreven dan had eerst die code uitgevoerd zijn geweest. Voorgaande voorbeeld zal intern eigenlijk als volgt plaatsvinden:

```csharp
Meting meting = new Meting();
meting.Temperatuur = 3.4;
meting.IsGeconfirmeerd = true;
```

{% hint style='tip' %}
Je bent niet verplicht alle properties via deze syntax in te stellen, enkel de zaken die je wilt meegeven tijdens de objectcreatie.
{% endhint %}


# `required` properties

Object initializer syntax werd ontwikkeld om de wildgroei aan overloaded constructors in te perken. Echter, dit bracht een nieuw probleem met zich mee. Met behulp van overloaded constructors kan je gebruikers van je klasse verplichten om bepaalde begininformatie van het object bij de creatie mee te geven. Object initializer syntax werkt enkel met een default constructor, en dus was een nieuw keyword vereist. Welkom `required`! 

Door `required` voor een property te plaatsen kan je aangeven dat deze property verplicht moet ingesteld worden wanneer je een object aanmaakt met object initializer syntax: 

```csharp
class Meting
{
    public double Temperatuur {get;set;}
    public required bool IsGeconfirmeerd {get;set;}
}
```

Wanneer we nu een `Meting` als volgt aanmaken:

```csharp
Meting meting = new Meting { Temperatuur = 0.7};
```

Dan krijgen we een foutboodschap: *Required member 'Meting.IsGeconfirmeerd' must be set in the object initializer or attribute constructor.* Enkel als we dus minstens `IsGeconfirmeerd` ook instellen zal onze code werken:

```csharp
Meting meting = new Meting { IsGeconfirmeerd = true};
```

{% hint style='danger' %}
Het `required` keyword werd pas geïntroduceerd in C# 11.0 en zal enkel werken indien je applicaties ontwikkelt in .NET 7 of nieuwer.
{% endhint %}


{% hint style='tip' %}
Attribute constructors worden niet in dit boek behandeld.
{% endhint %}