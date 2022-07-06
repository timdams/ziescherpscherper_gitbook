## Het ``base`` keyword

Het **``base``** keyword laat ons toe om bij ``override`` van een methode of property in de child-klasse toch te verplichten om de parent-implementatie toe te passen. Dit kan handig zijn wanneer je in je child-klasse de bestaande implementatie wenst uit te breiden.

Stel dat we volgende 2 klassen hebben:
```java
class Restaurant
{
     protected int kosten = 0;
     public virtual void PoetsAlles()
     {
           kosten += 1000;
     }
}
class Frituur:Restaurant
{
     public override void PoetsAlles()
     {
           kosten += (1000 + 500);  //SLECHT IDEE! Wat als de basiskosten in het restaurant veranderen?
     } 
}
```

Het poetsen van een ``Frituur`` is duurder (1000 basis + 500 voor ontsmetting) dan een gewoon ``Restaurant``. Als we echter later beslissen dat de basisprijs (in ``Restaurant``) moet veranderen dan moet je ook in alle child-klassen doen, wat natuurlijk geen goede programmeerstijl is.

``base`` lost dit voor ons op. De ``Frituur``-klasse herschrijven we naar:

```java
class Frituur:Restaurant
{
     public override void PoetsAlles()
     {
           base.PoetsAlles(); //eerste basiskost wordt opgeteld
           kosten += 500; //kosten eigen aan frituur worden bijgeteld
     }
}
```

Het ``base`` keyword laat ons toe om in onze code expliciet een methode of property van de parent-klasse aan te roepen. Ook al overschrijven we de implementatie van ``PoetsAlles`` toch kan de originele versie van de parent-klasse nog steeds gebruikt worden.

{% hint style='tip' %}
We hebben een soortgelijke werking ook reeds gezien bij de constructors van overgeërfde klassen.
{% endhint %}


Je kan zelf beslissen waar in je code je ``base`` aanroept. Soms doe je dat aan de start van de methode, soms op het einde, soms halverwege. Alles hangt er van af wat je juist nodig hebt.


{% hint style='warning' %}

![](../assets/care.png)
**"Ik denk dat ik een extra voorbeeldje nodig ga hebben."**

Laten we eens kijken. Beeld je in dat je volgende basisklasse hebt:

```java
class Oermens
{
      public virtual int VoorzieVoedsel()
      {
            return 15; //kg
      }
}
```

Wanneer 1 van mijn dorpsgenoten voedsel zoekt (door te jagen) zal hij 15 kg vlees verzamelen.

De moderne mens, die overerft van de oermens, is natuurlijk al iets beter in het maken van voedsel en kan dagelijks standaard 100 kg voedsel maken. 

Echter, er bestaan ook hipsters die houden van de klassieke manier van voedsel verzamelen (maar ze zijn wel gewoon moderne mensen, dus geen klasse apart hier). Uiteraard hebben zij de technieken van de oermens verbeterd en zullen sowieso toch iets meer voedsel nog kunnen verzamelen met de traditionele methoden, namelijk 20 kg bovenop de basishoeveelheid van 15 kg.

```java
class ModerneMens: Oermens
{
      public bool IsHipster {get;  set;}

      public override int VoorzieVoedsel()
      {
            if (IsHipster)
                  return base.VoorzieVoedsel() + 20;
            return 100;
      }
}
```
{% endhint %}


