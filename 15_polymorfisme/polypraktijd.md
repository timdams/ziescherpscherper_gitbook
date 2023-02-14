## Polymorfisme in de praktijk

Beeld je in dat je een klasse ``EersteMinister`` hebt met een methode ``Regeer`` en je wilt een eenvoudig land simuleren.


De ``EersteMinister`` heeft toegang tot tal van ministers die hem kunnen helpen (inzake milieu, binnenlandse zaken (BZ) en economie). Zonder de voordelen van polymorfisme zou de klasse ``EersteMinister`` er zo kunnen uitzien (**slechte manier**!):

```java
public class EersteMinister
{
    public MinisterVanMilieu Jansens {get;set;} = new MinisterVanMilieu();
    public MinisterBZ Ganzeweel {get;set;} = new MinisterBZ();
    public MinisterVanEconomie VanCent {get;set;} = new MinisterVanEconomie();

    public void Regeer()
    {
        // ministers stappen binnen en zeggen wat er moet gebeuren

        // Jansens: Problematiek aangaande bos dat gekapt wordt
        Jansens.VerhoogBosSubsidies();
        Jansens.OpenOnderzoek();
        Jansens.ContacteerGreenpeace();

        // Ganzeweel advies omtrent rel aan grens met Nederland
        Ganzeweel.VervangAmbassadeur();
        Ganzeweel.RoepTroepenmachtTerug();
        Ganzeweel.VerhoogRisicoZoneAanGrens();

        // Van Cent geeft advies omtrent nakende beurscrash
        VanCent.InjecteerGeldInMarkt();
        VanCent.VerlaagWerkloosheidsPremie();
    }
}
```

{% hint style='tip' %}
Dit voorbeeld is gebaseerd op een briljante StackOverflow post waarin de vraag *"What is polymorphism, what is it for, and how is it used?"* wordt behandeld (**https://stackoverflow.com/questions/1031273/what-is-polymorphism-what-is-it-for-and-how-is-it-used**).
{% endhint %}





De ``MinisterVanMilieu`` zou er zo kunnen uitzien (de methodenimplementatie mag je zelf verzinnen):
```java
class MinisterVanMilieu
{
  public void VerhoogBosSubsidies(){}
  public void OpenOnderzoek(){}
}
```

De ``MinisterVanEconomie``-klasse heeft dan weer heel andere publieke methoden. En de ``MinisterBZ`` ook weer totaal andere.

Je merkt dat de ``EersteMinister`` (of de programmeur van deze klasse) aardig wat specifieke kennis moet hebben van de vele verschillende departementen van het land. Bovenstaande code is dus zeer slecht en vloekt tegen het abstractie-principe van OOP: onze klasse moeten veel te veel weten van andere klassen, wat vermeden moet worden. Telkens er zaken binnen een specifieke ministerklasse wijzigen moet dit ook in de ``EersteMinister`` aangepast worden. **Dankzij polymorfisme en overerving kunnen we dit alles veel mooier oplossen!**

**Ten eerste:** We verplichten alle ministers dat ze overerven van de abstracte klasse ``Minister`` die maar 1 abstracte methode heeft ``Adviseer``:

```java
abstract class Minister
{
  abstract public void Adviseer();
}

class MinisterVanMilieu:Minister
{
  public override void Adviseer()
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

class MinisterBZ:Minister {}
class MinisterVanEconomie:Minister {}
```




**Ten tweede:** Het leven van de EersteMinister wordt plots véél makkelijker. Hij kan gewoon de ``Adviseer`` methode aanroepen van iedere minister:

```java
public class EersteMinister
{
  public MinisterVanMilieu Jansens {get;set;} = new MinisterVanMilieu();
  public MinisterBZ Ganzeweel {get;set;} = new MinisterBZ();
  public MinisterVanEconomie VanCent {get;set;} = new MinisterVanEconomie();
    
  public void Regeer()
  {
      Jansens.Adviseer(); 
      Ganzeweel.Adviseer(); 
      VanCent.Adviseer();
  }
}
```

**En ten derde:** En we kunnen hem nog helpen door met een array of ``List<Minister>`` te werken zodat hij ook niet steeds de "namen" van z'n ministers moet kennen. Dankzij polymorfisme mag dit:

```java
public class EersteMinister
{
  public List<Minister> AlleMinisters {get;set;}= new List<Minister>();
  public EersteMinister()
  {
      AlleMinisters.Add(new MinisterVanMilieu());
      AlleMinisters.Add(new MinisterBZ());
      AlleMinisters.Add(new MinisterVanEconomie());
  }
  public void Regeer()
  {  
      foreach (Minister minister in AlleMinisters)
      {
          minister.Adviseer();
      }
  }
}
```

En wie zei dat het regeren moeilijk was?!

{% hint style='tip' %}
Merk op dat dit voorbeeld ook goed gebruik maakt van **compositie**.
{% endhint %}





