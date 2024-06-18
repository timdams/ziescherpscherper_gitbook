## Is, as en polymorfisme: een krachtige bende

Dankzij polymorfisme hebben we nu met de ``is`` en ``as`` keywords handige hulpmiddelen om meer "generieke" methoden te schrijven. Herinner je je nog de ``Equals`` methode die we schreven om 2 studenten te vergelijken toen we leerden dat alle klassen van ``System.Object`` overerfden? Laten we deze code er nog eens bijnemen en verbeteren:

```csharp
//In de Student klasse
public override bool Equals(Object o)
{  
    Student temp = (Student)o; 
    return (Geboortejaar == temp.Geboortejaar && Voornaam == temp.Voornaam);
}
```

De eerste lijn waarin we ``o`` casten naar een student kan natuurlijk mislukken. Het is dan ook veiliger om eerst te controleren of we wel mogen casten, voor we het effectief doen. Hierdoor schrijven we een minder foutgevoelige methode:

```csharp
//In de Student klasse
public override bool Equals(Object o)
{  
    if(o is Student)
    { 
        Student temp = o as Student; 
        return (Geboortejaar == temp.Geboortejaar && Voornaam == temp.Voornaam);
    }
    return false;
}
```

Of we kunnen ook het volgende doen:
```csharp
//In de Student klasse
public override bool Equals(Object o)
{  
    Student temp = o as Student; 
    if(temp != null)
    { 
        return (Geboortejaar == temp.Geboortejaar && Voornaam == temp.Voornaam);
    }
    return false;
}
```
Beide zijn geldige oplossingen.

{% hint style='tip' %}
De ``is`` en ``as`` keywords laten toe om meer dynamische code te schrijven. Mogelijk weet je niet op voorhand wat voor datatype je code zal moeten verwerken en wordt polymorfisme je oplossing. Maar dan? Dan komen ``is`` en ``as`` to the rescue!

Je met polymorfisme gevulde lijst van objecten van allerhande typen wordt nu beheersbaarder. Je kan nu met ``is`` een element bevragen of het van een bepaald type is. Vervolgens kan je met ``as`` het element tijdelijk 'omzetten' naar z'n effectieve type. Bijgevolg kan dit element dan doen dan wanneer hij kan in de vermomming is van z'n eigen basistype.
{% endhint %}

