## De ``is`` en ``as`` keywords
Dankzij polymorfisme kunnen we dus child en parent-objecten door elkaar gebruiken. De keywords ``is`` en ``as`` gaan ons helpen om door het bos van objecten het bos nog te zien. 

### Het ``is`` keyword
Het ``is`` keyword is een operator die je kan gebruiken om te weten te komen of:
* Een object van een bepaalde datatype is.
* Een object een bepaalde interface bevat (zie volgende hoofdstuk).

De ``is`` operator heeft twee operanden nodig en geeft een ``bool`` terug als resultaat. De linkse operator moet een variabele zijn, de rechtse een datatype. Bijvoorbeeld:


```csharp
bool ditIsEenStudent = mijnStudent is Student;
```

#### ``is`` voorbeeld 
Stel dat we volgende drie klassen hebben:
```csharp
class Voertuig {}

class Auto: Voertuig{}

class Persoon {}
```
Een Auto **is** een Voertuig.
Een Persoon **is géén** Voertuig.

Stel dat we enkele variabelen hebben als volgt:
```csharp
Auto mijnAuto = new Auto();
Persoon rambo = new Persoon();
```

We kunnen nu de objecten met ``is`` bevragen of ze van een bepaalde type zijn:
```csharp
if(mijnAuto is Voertuig)
{
    Console.WriteLine("mijnAuto is een Voertuig");
}
if(rambo is Voertuig)
{
    Console.WriteLine("rambo is een Voertuig");
}
```

De uitvoer zal worden: ``mijnAuto is een Voertuig``. 



Met polymorfisme wordt dit voorbeeld echter interessanter. Wat als we een hoop objecten in een lijst van voertuigen plaatsen en nu enkel met de auto's iets willen doen, dan kan dat:

```csharp
List<Voertuig> alleMiddelen = new List<Voertuig>();
alleMiddelen.Add(new Voertuig());
alleMiddelen.Add(new Auto());
alleMiddelen.Add(new Voertuig());

foreach (var middel in alleMiddelen)
{
    if(middel is Auto)
    {
        //Doe iets met het huidige voertuig
    }
}
```

### ``as`` keyword met voorbeeld
Wanneer we objecten van het ene naar het andere type willen omzetten dan doen we dit vaak met behulp van casting:

```csharp
Student fritz = new Student();
Mens jos = (Mens)fritz;
```

Het probleem bij casting is dat dit niet altijd lukt. Indien de conversie niet mogelijk is zal een uitzondering gegenereerd worden en je programma zal crashen als je niet aan exception handling doet.

Het ``as`` keyword lost dit op. Het keyword zegt aan de compiler **"probeer dit object te converteren. Als het niet lukt, zet het dan op ``null`` in plaats van een uitzondering op te werpen."**
 
De code van daarnet herschrijven we dan naar:

 ```csharp
Student fritz = new Student();
Mens jos = fritz as Mens;
```

Indien nu de casting niet lukt (omdat ``Student`` misschien geen childklasse van ``Mens`` blijkt te zijn) dan zal ``jos`` de waarde ``null`` hebben gekregen.

We kunnen dan vervolgens schrijven:
 ```csharp
Student fritz = new Student();
Mens jos = fritz as Mens;
if(jos != null)
{
    //Doe Mens-zaken 
}
```



