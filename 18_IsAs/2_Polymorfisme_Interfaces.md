## Alles samen : Polymorfisme, interfaces en is/as

De eigenschappen van polymorfisme en interfaces combineren kan tot zeer krachtige code resulteren. Wanneer we dan ook nog eens de ``is`` en ``as`` keywords gebruiken is het hek helemaal van de dam. Als afsluiter van deze lange reis in OOP-land zal ik daarom een voorbeeld geven waarin de verschillende OOP-concepten samenkomen om ... vloekende mensen op het scherm te tonen.


### Vloekende mensen: Opstart

Het idee is het volgende: mensen kunnen spreken. Leraars, studenten, politieker, en ja zelfs advocaten zijn mensen. Echter, enkel politiekers en advocaten hebben ook de interface ``IVloeker`` die hen toelaat eens goed te vloeken. Brave leerkrachten en studenten doen dat niet (*kuch*). We willen een programma dat lijsten van mensen bevat waarbij we de vloekers kunnen doen vloeken zonder complexe code te moeten schrijven.

We hebben volgende klasse-structuur:

![Klasse-schema van de vloekende mensen.](../assets/12_isas/polyinterface.png)


Als basis klasse ``Mens`` hebben we:

```csharp
internal class Mens
{
    public void Spreek()
    {
        Console.WriteLine("Hoi!");
    }
}
```



Voorts definiëren we de interface ``IVloeker`` als volgt:

```csharp
interface IVloeker
{
    void Vloek();
}
```

We kunnen nu de nodige child-klassen maken:

1. De niet-vloekers: ``Leraar`` en ``Student``
2. De vloekers: ``Advocaat`` en ``Politieker``

```csharp
internal class Leraar:Mens {} //moet niets speciaal doen

internal class Student:Mens{} //ook studenten doen niets speciaal

internal class Politieker: Mens, IVloeker
{
    public void Vloek()
    {
        Console.WriteLine("Godvermiljaardedju, zei de politieker");
    }
}

internal class Advocaat: Mens, IVloeker
{
    public void Vloek()
    {
        Console.WriteLine("SHIIIIT, zei de advocaat");
    }
}
```

### Vloekende mensen: Het probleem
We maken een array van mensen aan waarin we van iedere type een vertegenwoordiger plaatsen (uiteraard had dit ook in een ``List<Mens>`` kunnen gebeuren):

```csharp
Mens[] mensjes = new Mens[4];
mensjes[0] = new Leraar();
mensjes[1] = new Politieker();
mensjes[2] = new Student();
mensjes[3] = new Advocaat();
for(int i = 0; i < mensjes.Length; i++)
{
    //NOW WHAT?
```

**Het probleem:** hoe kan ik in de array van studenten, leraren, advocaten en politiekers **enkel de vloekers laten vloeken?**

<!-- \newpage -->


### Oplossing 1: ``is`` to the rescue
De eerste oplossing is door gebruik te maken van het ``is`` keyword.
We zullen de array doorlopen en steeds aan het huidige object vragen of dit object de ``IVloeker`` interface bezit, als volgt:
```csharp
for(int i = 0; i<mensjes.Length; i++)
{
    if(mensjes[i] is IVloeker)
    {
        //NOW WHAT?
    }
    else
    {
        mensjes[i].Spreek();
    }
}
```
Vervolgens kunnen we binnen deze ``if`` het huidige object tijdelijk omzetten (casten) naar een ``IVloeker`` object en laten vloeken:

```csharp
if(mensjes[i] is IVloeker)
{
    IVloeker tijdelijk = (IVloeker)mensjes[i];
    tijdelijk.Vloek();
}
```

### Oplossing 2: ``as`` to the rescue

Het ``as`` keyword kan ook een toffe oplossing geven. Hierbij zullen we het object proberen om te zetten via ``as`` naar een ``IVloeker``. Als dit lukt (het object is verschillend van ``null``) dan kunnen we het object laten vloeken:
```csharp
for(int i = 0; i<mensjes.Length; i++)
{
    IVloeker tijdelijk = mensjes[i] as IVloeker;
    if(tijdelijk != null)
    {
        tijdelijk.Vloek();
    }
    else
    {
        mensjes[i].Spreek();
    }
}
```


<!-- \newpage -->


>![](../assets/attention.png)Hopelijk hebben voorgaande voorbeelden je een beetje hebben kunnen doen proeven van de kracht van interfaces. Gedaan met ons druk te maken wat er allemaal in een klasse gebeurt. Werk gewoon 'tegen' de interfaces van een klasse en we krijgen de ultieme black-box revelatie! *See what I did there?*



