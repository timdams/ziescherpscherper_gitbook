## Interfaces in de praktijk

In het vorige hoofdstuk gaf ik een voorbeeld van een klasse ``EersteMinister`` die enkele ``Minister``-klassen gebruikte om hem of haar te helpen.

Een nadeel van die aanpak is dat al onze Ministers maar 1 "job" kunnen hebben: ze erven allemaal over van ``Minister`` en kunnen nergens anders van overerven (geen *multiple inheritance* is toegestaan in C#). Je wordt uiteraard niet geboren als Minister.  Het zou dus handig zijn dat ook andere mensen Minister kunnen worden, zonder dat ze hun bestaande expertise moeten weggooien. 

Via interfaces kunnen we dit oplossen. Een ``Minister`` gaan we dan eerder als een "bij-job" beschouwen en niet de hoofdreden van een klasse.

We definiëren daarom eerst een nieuwe interface ``IMinister``:
```csharp
interface IMinister
{
    void Adviseer();
}
```

Vanaf nu kan eender *wie* die deze interface implementeert de ``EersteMinister`` advies geven. Hoera! En daarnaast kan die klasse echter ook nog tal van andere zaken doen. Beeld je in dat een CEO van een bedrijf ook minister bij de EersteMinister wilt zijn, zoals deze:

```csharp
internal class Ceo
{
    public void MaakJaarlijkseOmzet()
    { 
       Console.WriteLine("Geld!!!");
    }
    public void OntslaDepartement()
     { 
       Console.WriteLine("You're all fired!");
    }
}
```

Nu we de interface ``IMinister`` hebben kunnen we deze klasse aanvullen met deze interface zonder dat de bestaande werking van de klasse moet aangepast worden:

```csharp
internal class Ceo: IMinister
{ 
    public void Adviseer()
    { 
        Console.WriteLine("Vrijhandel is essentieel!");
    }
    //gevolgd door de reeds bestaande methoden
```
De CEO kan dus z'n bestaande job blijven uitoefenen maar ook als Minister optreden. 

<!-- \newpage -->


Ook de ``EersteMinister`` moet aangepast worden om nu met een lijst van ``IMinister`` ipv ``Minister`` te werken. Dankzij polymorfisme is dat erg eenvoudig! 

```csharp
internal class MisterEersteMinister
{
    public void Regeer()
    {
        List<IMinister> AlleMinisters = new List<IMinister>();
        AlleMinisters.Add(new Ceo); 
        foreach (IMinister minister in AlleMinisters)
        {
            minister.Adviseer();
        }
    }
}
```

De eerder beschreven ``MinisterVanMilieu``, ``MinisterBZ`` en ``MinisterVanEconomie`` dienen ook niet meer van de abstracte klasse ``Minister`` over te erven en kunnen gewoon de interface implementeren. Enkel lijn 1 moet hierbij aangepast worden:

```csharp
internal class MinisterVanMilieu:IMinister
{
    public void Adviseer()
    {
        VerhoogBosSubsidies();
        OpenOnderzoek();
        ContacteerGreenpeace();
    }

    private void VerhoogBosSubsidies(){ ... }
    private void OpenOnderzoek(){ ... }
    private void ContacteerGreenpeace(){ ... }
    }
}
```

En bij deze hebben we dankzij interfaces, compositie en polymorfisme, ervoor gezorgd dat eender wie ``Minister`` kan worden zonder dat dat die daarvoor z'n bestaande job moet *opzeggen*. OOP laat ons echt toe de realiteit zo dicht mogelijk te benaderen!


