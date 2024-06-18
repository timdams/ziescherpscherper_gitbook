## String.Format()
String interpolatie met het $-teken is een nieuwe C# aanwinst. Je zal echter geregeld documentatie en online code tegenkomen die nog met ``String.Format`` werkt (ook zijn er nog zaken waar het te verkiezen is om ``String.Format`` te gebruiken i.p.v. 1 van vorige manieren). Om die reden bespreken we dit nog in dit boek.

``String.Format`` is een ingebouwde methode die string-interpolatie toelaat op een iets minder intuïtieve manier, als volgt:


```csharp
string result = String.Format("Ik ben {0} en ik ben {1} jaar.", naam, leeftijd);
```

Het getal tussen de accolades geeft aan welke parameter op die plek moet komen. 0 betekent de eerste, 1 betekent de tweede, enzovoort.
 De eerste parameter is ``naam``, de tweede is ``leeftijd``.

Volgende code zal een ander resultaat geven:


```csharp
string result = String.Format("Ik ben {1} en ben {1} jaar.", naam, leeftijd);
```

Namelijk: ``Ik ben 13 en ik ben 13 jaar oud.``

{% hint style='tip' %}
Je kan deze vorm van formateren ook toepassen in ``Console.WriteLine`` zonder dat je expliciet ``String.Format`` hiervoor moet aanroepen:


```csharp
Console.WriteLine("Gratis formateren. {0} maal hoera voor .NET!", 3);
```
{% endhint %}




