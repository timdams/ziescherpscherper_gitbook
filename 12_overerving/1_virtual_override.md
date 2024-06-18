## Virtual en Override

Het is fijn dat onze child-klasse alles kan dat onze parent-klasse doet. Maar soms is dat beperkend:

* Mogelijk wil je een bestaande methode van de parent-klasse uitbreiden/aanvullen met extra functionaliteit.
* Soms wil je gewoon de volledige implementatie van een methode of property herschrijven in je child-klasse.

**De keywords ``virtual`` en ``override`` gaan je hiermee kunnen helpen.**

### De werking van child-klassen aanpassen

Om te voorkomen dat child-klassen zomaar eender welke methode of property van de parent-klasse kunnen aanpassen gaan we de hulp van het ``virtual`` keyword inroepen. Standaard is het geen goede gewoonte om de bestaande werking van een klasse in de child-klasse aan te passen: beeld je in dat je een essentieel stuk code aanpast waardoor je hele klasse plots niet meer werkt!

Soms willen we echter kunnen aangeven dat de werking van een property of methode door een child-klassen mag aangepast worden. Dit geven we aan met het **``virtual``** keyword. 

Vervolgens dient de child-klasse het keyword ``override`` te gebruiken om expliciet aan te geven dat er een methode of property komt wiens werking die van de parent-klasse zal wijzigen.

{% hint style='tip' %}
Enkel indien een element met ``virtual`` werd aangeduid, kan je deze dus met ``override`` aanpassen. Uiteraard ben je niet verplicht om elke *virtueel* element ook effectief te *overriden*. **``virtual`` geeft enkel aan dat dit een mogelijkheid is, geen verplichting.**
{% endhint %}

<!-- \newpage -->


### Een voorbeeld met vliegende objecten

Stel je voor dat je een applicatie hebt met 2 klassen, ``Vliegtuig`` en ``Raket``. Een raket is een vliegtuig, maar kan veel hoger vliegen dan een vliegtuig. Omdat we weten dat potentiële childklassen op een andere manier zullen willen vliegen, zullen we de methode ``Vlieg`` ``virtual`` zetten:

```csharp
internal class Vliegtuig
{
   public virtual void Vlieg()
   {
      Console.WriteLine("Het vliegtuig vliegt door de wolken.");
   }
}
internal class Raket: Vliegtuig
{ 

}
```

{% hint style='tip' %}
Merk op dat we het keyword ``virtual`` mee opnemen in de methodesignatuur op lijn 3, en dat deze dus niets te maken heeft met het returntype en de zichtbaarheid van de methode. Dit zou bijvoorbeeld een perfect legale methodesignatuur kunnen zijn: ``protected virtual int SayWhatNow()``. 

Terzijde: ``static`` methoden kunnen niet ``virtual`` gezet worden.
{% endhint %}


Stel dat we 2 objecten aanmaken en laten vliegen:

```csharp
Vliegtuig topGun = new Vliegtuig();
Raket spaceX1 = new Raket();
topGun.Vlieg();
spaceX1.Vlieg();
```

De uitvoer zal dan zijn twee maal dezelfde zin tonen: ``Het vliegtuig vliegt door de wolken.``


{% hint style='danger' %}
Enkel ``public`` methoden en properties kan je ``virtual`` instellen.
{% endhint %}


<!-- \newpage -->


Momenteel doet het ``virtual`` keyword niets. Het is enkel een signaal aan mede-programmeurs: *"hey, als je wilt mag je de werking van deze methode aanpassen als je van deze klasse overerft."*

Een raket is een vliegtuig, toch vliegt het anders. We willen dus de methode ``Vlieg`` anders uitvoeren voor een raket. Daar hebben we **override** voor nodig. Door override voor een methode in de child-klasse te plaatsen zeggen we "gebruik deze implementatie en niet die van de parent klasse."

```csharp
internal class Raket:Vliegtuig
{
   public override void Vlieg()
   {
      Console.WriteLine("De raket verdwijnt in de ruimte.");
   }     
}
```

De uitvoer van volgende code zal nu anders zijn:
```csharp
Vliegtuig topGun = new Vliegtuig();
Raket spaceX1 = new Raket();
topGun.Vlieg();
spaceX1.Vlieg();
```

Uitvoer:

```text
Het vliegtuig vliegt door de wolken.
De raket verdwijnt in de ruimte.
```

{% hint style='tip' %}
Indien je iets ``override`` moet de signatuur van je methode of property  identiek zijn aan deze van de parent-klasse. Het enige verschil is dat je het keyword ``virtual`` vervangt door ``override``.

Als je in VS override begint te typen in een child-klassen dan kan je met behulp van de tab-toets heel snel de overige code van de signatuur schrijven. 
{% endhint %}




