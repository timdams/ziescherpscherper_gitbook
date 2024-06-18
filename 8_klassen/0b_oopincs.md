
## OOP in C\#

In C# kunnen we geen objecten aanmaken zonder eerst een klasse te definiëren. Een klasse beschrijft de algemene eigenschappen (properties en instantievariabelen) en het gedrag (methoden) van die objecten.


### Klasse maken

Een klasse heeft minimaal de volgende vorm:

```csharp
class ClassName
{

}
```

{% hint style='danger' %}
De naam die je een klasse geeft moet voldoen aan de identifier regels uit hoofdstuk 2. Het is echter een goede gewoonte om **klassenamen altijd met een hoofdletter te laten beginnen**.
{% endhint %}



Volgende code beschrijft de klasse ``Auto`` in C#

```csharp
class Auto
{

}
```

Binnen het codeblock dat bij deze klasse hoort zullen we verderop dan de werking via properties en methoden beschrijven.

### Klassen in Visual Studio toevoegen

Je kan "eender waar" een klasse aanmaken in een project, maar het is een goede gewoonte om per klasse **een apart bestand** te gebruiken. Dit kan op 2 manieren.

Manier 1:

* In de solution Explorer, rechterklik op je project.
* Kies "Add".
* Kies "Class..".
* Geef een goede naam voor je klasse.

<!-- \newpage -->


Manier 2:

* Klik in de menubalk bovenaan op "Project".
* Kies "Add class..." .

![Manier 2 is de snelste. Tip: of maak een eigen toetsenbord shortcut, dat is nog sneller natuurlijk.](../assets/6_klassen/addclass.png)

Je zal zien dat nieuw toegevoegde klassen in Visual Studio ook nog het keyword ``internal`` voor ``class`` krijgen. Dit is een zogenaamde **access modifier** en leg ik zo meteen uit.

### Objecten aanmaken

Je kan nu objecten aanmaken van de klasse die je hebt gedefinieerd. Dit kan op alle plaatsen in je code waar je in het verleden ook al variabelen kon declareren, bijvoorbeeld in een methode of je ``Main``-methode.

Je doet dit door eerst een variabele te definiëren en vervolgens een object te **instantiëren** met behulp van het ``new`` keyword. De variabele heeft als datatype ``Auto``:

```csharp
Auto mijnEersteAuto = new Auto();
Auto mijnAndereAuto = new Auto();
```

We hebben nu **twee objecten aangemaakt van het type Auto** die we verderop zouden kunnen gebruiken.

Let goed op dat je dus op de juiste plekken dit alles doet:

* Klassen maak je aan als aparte bestanden in je project.
* Objecten creëer je in je code op de plekken waar je deze nodig hebt, bijvoorbeeld in je ``Main`` methode bij een Console-applicatie.

<!-- \newpage -->


### De ``new`` operator

In het volgende hoofdstuk leg ik uit wat er allemaal gebeurt in het geheugen wanneer we een object met ``new`` aanmaken. Het is echter nu al belangrijk te beseffen dat objecten niet kunnen gemaakt worden zonder ``new``. 

De ``new`` operator vereist dat je aangeeft van welke klasse (het type) je een object wilt aanmaken, gevolgd door ronde haakjes. Bijvoorbeeld:

```csharp
new Student();
```

Deze lijn code doet niets nuttig. We roepen hier weliswaar een constructor aan (zie verder) die het object in het geheugen zal aanmaken. Vervolgens geeft ``new`` een adres terug waar het object zich bevindt. We doen nog niets met dit adres. 

Het is dit adres dat we vervolgens kunnen bewaren in een variabele die links van de toekenningsoperator (``=``) staat:

```csharp
Student hetEersteStudentObject = new Student();
```

Test eens wat er gebeurt als je volgende code probeert te compileren:

```csharp
Auto mijnEersteAuto = new Auto();
Auto mijnAndereAuto;
Console.WriteLine(mijnEersteAuto);
Console.WriteLine(mijnAndereAuto);
```

Je zal een ``"Use of unassigned local variable mijnAndereAuto"`` foutboodschap krijgen. Inderaad, je hebt nog geen object aangemaakt met ``new`` en ``mijnAndereAuto`` is dus voorlopig een lege doos (**het heeft de waarde ``null``**).

{% hint style='warning' %}
Dit concept is dus fundamenteel verschillend van de klassieke *valuetypes* die we al kenden (``int``, ``double``, enz.). Daar zal volgende code wél werken:

```csharp
int balans;
Console.WriteLine(balans);
```

{% endhint %}


<!-- \newpage -->


### Klassen zijn gewoon nieuwe datatypes

In hoofdstuk 2 leerden we dat er allerlei datatypes bestaan. We maakten vervolgens variabelen aan van een bepaald datatype zodat deze variabele als inhoud enkel zaken kon bevatten van dat ene datatype. 

Zo leerden we toen volgende categorieën van datatypes:

* **Valuetypes** zoals ``int``, ``char`` en ``bool``.
* Het **``enum``** keyword liet ons toe om een nieuw datatype te maken dat maar een eindig aantal mogelijke waarden (values) kon hebben. Intern bewaarden variabelen van zo'n enum-datatype hun waarde als een ``int``.
* **Arrays** waren het laatste soort datatypes. Je ontdekte dat je arrays kon maken van eender welk datatype (valuetypes en enums).

**Wel nu, klassen zijn niet meer dan een nieuw soort datatypes**. Kortom: telkens je een klasse aanmaakt, kunnen we in dat project variabelen en arrays aanmaken met dat datatype. We noemen variabelen die een klasse als datatype hebben **objecten**.

Het grote verschil dat deze objecten zullen hebben is dat ze vaak veel complexer zijn dan de eerdere datatypes die we kennen:

* Ze zullen meerdere "waarden" tegelijk kunnen bewaren (een ``int`` variabele kan maar één waarde tegelijkertijd in zich hebben).
* Ze zullen methoden hebben die we kunnen aanroepen om het object *voor ons te laten werken*.



>![](../assets/care.png)Het blijft ingewikkeld hoor. Heel boeiend om de theorie van een speer te leren, maar ik denk dat ik toch beter een paar keer met een speer naar een mammoet werp om echt te voelen wat OOP is. 
>
>Ik onthoud nu alvast **"klassen zijn gewoon een nieuwe vorm van complexere datatypes"** dan diegene die ik totnogtoe heb geleerd? Ok?
>
>**Correct. Er verandert dus niet veel. Enkel je variabelen worden krachtiger!**












