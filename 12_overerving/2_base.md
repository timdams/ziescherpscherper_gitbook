## Het ``base`` keyword

Het **``base``** keyword laat ons toe om bij ``override`` van een methode of property in de child-klasse toch te verplichten om de parent-implementatie toe te passen. Dit kan handig zijn wanneer je in je child-klasse de bestaande implementatie wenst uit te breiden.

Stel dat we volgende 2 klassen hebben:
```csharp
internal class Restaurant
{
     protected int kosten = 0;
     public virtual void PoetsAlles()
     {
           kosten += 1000;
     }
}
internal class Frituur:Restaurant
{
     public override void PoetsAlles()
     {
           kosten += (1000 + 500);  //SLECHT IDEE! Wat als de basiskosten in het restaurant veranderen?
     } 
}
```

Het poetsen van een ``Frituur`` is duurder (1000 basis + 500 voor ontsmetting) dan een gewoon ``Restaurant``. Als we echter later beslissen dat de basisprijs (in ``Restaurant``) moet veranderen dan moet je ook in alle child-klassen doen, wat natuurlijk geen goede programmeerstijl is.

``base`` lost dit voor ons op. De ``Frituur``-klasse herschrijven we naar:

```csharp
internal class Frituur:Restaurant
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

<!-- \newpage -->


Je kan zelf beslissen waar in je code je ``base`` aanroept. Soms doe je dat aan de start van de methode, soms op het einde, soms halverwege. Alles hangt er van af wat je juist nodig hebt.





>![](../assets/care.png)**"Ik denk dat ik een extra voorbeeldje nodig ga hebben."**

Laten we eens kijken. Beeld je in dat je volgende basisklasse hebt:

```csharp
internal class Oermens
{
      public virtual int VoorzieVoedsel()
      {
            return 15; //kg
      }
}
```

Wanneer 1 van mijn dorpsgenoten voedsel zoekt door te jagen zal hij 15 kg vlees verzamelen.

De moderne mens, die overerft van de oermens, is natuurlijk al iets beter in het maken van voedsel en kan dagelijks standaard 100 kg voedsel maken. 

Echter, er bestaan ook jagers die nog op de klassieke manier voedsel kunnen verzamelen (maar ze zijn wel gewoon moderne mensen, dus geen klasse apart hier). Uiteraard hebben zij de technieken van de oermens verbeterd en zullen sowieso toch iets meer voedsel nog kunnen verzamelen met de traditionele methoden, namelijk 20 kg bovenop de basishoeveelheid van 15 kg.

```csharp
internal class ModerneMens: Oermens
{
      public bool IsJager {get;  set;}

      public override int VoorzieVoedsel()
      {
            if (IsJager)
                  return base.VoorzieVoedsel() + 20;
            return 100;
      }
}
```

<!-- \newpage -->


### Een wereld met OOP: Pong overerving

Dankzij overerving zijn we nu in staat om Pong uit te breiden met andere soort balletjes. De eerste vraag die je je moet stellen is dan "welke werking in de klasse ``Balletje`` gaan we potentiëel willen aanpassen?". Laten we veronderstellen dat we enkel de ``Update`` mogelijk willen veranderen. We voegen daarom het ``virtual`` keyword aan die methode toe:

```csharp
virtual public void Update()
```

Voor de rest passen we hier niets aan. Dankzij overerving kunnen we de klasse ``Balletje`` nu onaangeroerd laten en onze nieuwe functionaliteit toevoegen via child-klassen. 

Stel dat we een nieuw ``Balletje`` willen ontwikkelen, genaamd ``CentreerBalletje``. Dit balletje heeft als eigenschappen dat het terug naar het midden van het scherm *teleporteert* wanneer het de linker- of rechterzijde van het scherm raakt. Dit zal er zo uitzien:

```csharp
internal class CentreerBalletje : Balletje
{
      public override void Update()
      {
            if(X+VX >= Console.WindowWidth || X+VX < 0)
            {
                  X = Console.WindowWidth / 2;
                  Y = Console.WindowHeight / 2;
            }         
            base.Update();
      }     
}
```

We hoeven nu enkel in het hoofdprogramma alle ``Balletje``-variabelen te vervangen door  ``CentreerBalletje``.

{% hint style='tip' %}
Dankzij polymorfisme verderop gaan we ontdekken dat zelfs dit eigenlijk mag!

```csharp
Balletje bal1 = new CentreerBalletje();
```

{% endhint %}