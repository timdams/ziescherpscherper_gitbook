# Polymorfisme

Naast het blackbox-, abstractie- en overervingsprincipe, is polymorfisme (*polymorphism*) de vierde grote peiler van object georiënteerd programmeren. 

De latijnse naam polymorfisme bestaat uit 2 delen: *poly* en *morfisme*, letterlijk dus "meerdere vormen". En geloof het of niet, deze naam dekt de lading ongelooflijk goed. 

Polymorfisme laat ons toe dat objecten kunnen behandeld worden als objecten van de klasse waar ze van overerven. Dit klinkt logisch, maar zoals je zo meteen zal zien zal je hierdoor erg krachtige code kunnen schrijven. Anderzijds zorgt polymorfisme er ook voor dat het ``virtual`` en ``override`` concept bij methoden en properties ook effectief werkt. Het is echter vooral de eerste eigenschap waar we in dit hoofdstuk dieper op in zullen gaan.



## De "is een"-relatie in actie

Dankzij overerving kunnen we "is een"-relaties beschrijven. Soms is het echter handig dat we alle child-objecten als hetzelfde type, dat van hun parent, kunnen beschouwen. Beeld je in dat je een gigantische klasse-hiërarchie hebt gemaakt, maar finaal wil je wel dat alle objecten een bepaalde property aanpassen die ze gemeenschappelijk hebben. Zonder polymorfisme is dat een probleem. 

Stel dat we een een aantal van ``Dier`` afgeleide klassen hebben die allemaal op hun eigen manier een geluid voortbrengen:
```java
abstract class Dier
{
   public abstract string MaakGeluid();
}
class Paard: Dier
{
  public override string MaakGeluid()
  { 
      return "Hinnikhinnik";
  }
}
class Varken: Dier
{
  public override string MaakGeluid()
  { 
      return "Oinkoink";
  }
}
```

**Dankzij polymorfisme kunnen we nu elders objecten van Paard en Varken in een variabele van het type ``Dier`` bewaren**, maar toch hun eigen geluid laten reproduceren:

```java
Dier someAnimal = new Varken();
Dier anotherAnimal = new Paard();
Console.WriteLine(someAnimal.MaakGeluid()); //Oinkoink
Console.WriteLine(anotherAnimal.MaakGeluid()); //Hinnikhinnik
```

**Alhoewel er een volledig ``Varken`` en ``Paard`` object in de heap wordt aangemaakt (en blijft bestaan), zullen variabelen van het type ``Dier`` enkel die dingen kunnen aanroepen die in de klasse ``Dier`` gekend zijn. Dankzij ``override`` zorgen we er echter voor dat ``MaakGeluid`` wel die code uitvoert die specifiek bij het child-type hoort.**

![Het gearceerde deel is  niet bereikbaar voor de 2 variabelen in de stack daar deze van het type ``Dier`` zijn.](../assets/7_overerving/varkenpaard.png)


{% hint style='tip' %}
Het is belangrijk te beseffen dat ``someAnimal`` en ``anotherAnimal`` van het type ``Dier`` zijn en dus enkel die dingen kunnen die in ``Dier`` beschreven staan. Enkel zaken die ``override`` zijn in de child-klasse zullen met de specialisatie-code werken.
{% endhint %}




### Objecten en polymorfisme

Kortom, polymorfisme laat ons toe om referenties naar objecten van een child-type, toe te wijzen aan een variabele van het parent-type.

Dit wil ook zeggen dat dit mag (daar alles overerft van ``System.Object``):


```java
System.Object mijnObject = new Varken();
```

Alhoewel ``mijnObject`` effectief een ``Varken`` is (in het geheugen), kunnen we enkel aan dat gedeelte dat in de klasse ``System.Object`` staat beschreven, zijnde de klassieke 4 methoden (``ToString``, ``Equals`` enz.). Als we het varken toch geluid willen laten maken, dan zal dat niet werken!



## Arrays en polymorfisme

Arrays en lijsten laten heel krachtige code toe dankzij polymorfisme. Je kan een lijst van de basis-klasse maken en deze vullen met allerlei objecten van de basis-klasse **én de child-klassen**. 

Een voorbeeld:

```java
List<Dier> zoo = new List<Dier>();
zoo.Add(new Varken());
zoo.Add(new Paard());
foreach(var dier in zoo)
{
  Console.WriteLine(dier.MaakGeluid());
}
```

We hebben nu een manier gevonden om onze objecten op de juiste momenten even als één geheel te gebruiken, zonder dat we verplicht zijn dat ze allemaal van hetzelfde type zijn!


{% hint style='warning' %}

![](../assets/care.png)

Polymorfisme is een heel krachtig concept. Door een referentie naar objecten te bewaren in een variabele van hun basistype en, wanneer nodig, ze als 'zichzelf' te gebruiken wordt je code een pak eenvoudiger.
Vaak weet je niet op voorhand wat voor elementen je in je lijst wilt plaatsen. Via polymorfisme lossen we dit op. Stel bijvoorbeeld dat je een lijst van Personen hebt (``List<Person>``) waar echter elementen van subklassen in terecht kunnen komen (``Bakker``, ``Student``, etc) , dan laat polymorfisme dit gewoon toe om ook deze elementen in die lijst te plaatsen.

{% endhint %}


