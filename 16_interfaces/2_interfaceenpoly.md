
## Polymorfisme en interfaces

Een object aanmaken van een interface is natuurlijk onmogelijk. Je object zou flinterdun zijn zonder inhoud. Maar, dankzij polymorfisme kunnen we wel variabelen aanmaken van een interfacetype die een referentie hebben naar een object dat die interface heeft:


```csharp
IManager deBaas = new Werknemer();
```

Op dat moment kunnen we via ``deBaas`` aan het gedeelte van het ``Werknemer`` object dat in de ``IManager`` interface beschreven staat. Krachtig toch! 

Beeld je in dat je een complexe klasse ``DiskWriter`` hebt die je programma gebruikt om data van en naar de harde schijf te schrijven. De klasse implementeert een interface ``IData`` die twee methoden heeft (``LeesData()`` en ``SchrijfData``):

```csharp
interface IData
{
    string LeesData();
    void SchrijfData(string towrite);
}

internal class DiskWriter : IData
{
    public string LeesData()
    {
        //Lees van harde schijf
    }

    public void SchrijfData(string towrite)
    {
        //Schrijf naar harde schijf
    }
    //Allerlei andere zaken
}
```



Als je later beslist om je data naar een online server te schrijven in plaats van naar de harde schijf, dan kan je gewoon die klasse bijmaken. Bijvoorbeeld door de klasse``InternetWriter`` te schrijven en vervolgens ook de ``IData`` interface te implementeren: 

```csharp
internal class InternetWriter: IData
{
    public string LeesData()
    {
        //Lees van internet
    }

    public void SchrijfData(string towrite)
    {
        //Schrijf naar internet
    }
}
```

Al je andere code moet dan niet aangepast worden! Je andere klassen kunnen gewoon ``LeesData`` en ``SchrijfData`` blijven aanroepen en weten misschien zelfs niet dat hun data niet meer naar de harde schijf maar naar het internet wordt gestuurd. Nu maken we een klasse die effectief die writer gebruikt. De truc zit hem er in dat deze klasse met ``IData`` werkt via compositie en dus niet weet naar waar alles zal geschreven worden. 

Beter zelfs: de klasse weet het niet, en hoeft dat ook niet te weten. Je kan vervolgens volgens de compositie regels instellen welk object ``IData`` krijgt. Hier doen we dit in de setters van een ``Offline`` property zodat we van buiten aan de klasse kunnen vertellen of het internet wel of niet beschikbaar is:

```csharp
internal class BackupSystem
{
    private IData writer = new DisWriter();
    public bool Offline //No internet
    {
        set
        {
            if(value)
                writer = new DiskWriter();
            else
                writer = new InternetWriter();
        }
    }
    public void MaakBackup(string backup)
    {
        writer.SchrijfData(backup);
    }
}
```




In volgend voorbeeld maken we een ``Logboek`` klasse aan die ook een ``IData`` interface in zich heeft. Echter, via de constructor stellen we nu in hoe ieder object informatie moet wegschrijven: 

```csharp
internal class Logboek
{
    private IData datadoel;
    public Logboek(IData doel)
    { 
        datadoel = doel; 
    }
    public void Schrijf(string log)
    {
        datadoel.SchrijfData(log);
    }
    //enz.
}
```

Vanaf nu kan je ``Logboek``-objecten aanmaken die naar verschillende plekken schrijven/lezen zonder dat je IN ``Logboek`` moet weten naar waar dat gebeurt[^depin]:

```csharp
Logboek naarlokalefile = new Logboek(new DiskWriter());
naarlokalefile.Schrijf();
Logboek naarInternet = new Logboek(new InternetWriter());
naarInternet.Schrijf();
```

[^depin]: Voor de geïnteresseerden: dit concept is een eerste stap naar *Dependency Injection*. Dit is een erg krachtig concept dat je nog veel zal tegenkomen in je verdere programmeercarrière.


