# Geheugenbeheer <!--\label{ch:10}-->

In dit hoofdstuk duiken we onder de motorkap van C#.
Als programmeur moet je weten wat er gebeurt als je een object aanmaakt.
Waarom gedraagt een `int` zich anders dan een `Student` object?
Waarom crasht mijn code met een `NullReferenceException`?

Het antwoord ligt in het geheugen: **Stack vs Heap**.


## Geheugenbeheer in C\#

In hoofdstuk 8 deed ik reeds uit de doeken dat variabelen op 2 manieren in het geheugen kunnen leven:

* **Value types**: waren variabelen wiens waarde rechtstreeks op de geheugenplek stonden waar de variabele naar verwees. Dit gold voor alle bestaande, ingebakken datatypes zoals ``int``, ``bool``, ``char`` enz. alsook voor ``enum`` types.
* **Reference types**: deze variabelen bevatten als inhoud een geheugenadres naar een andere plek in het geheugen waar de effectieve waarde van deze variabele stond. We zagen dat dit voorlopig enkel bij arrays gebeurde.

**Ook objecten zijn reference types.** Hoofdstuk 8 liet uitschijnen dat vooral value type variabelen veelvuldig in programma's voorkwamen. Wel je zal nu ontdekken dat reference types véél meer voorkomen: **simpelweg omdat alles in C# een object is** (en dus ook arrays van objecten én zelfs valuetypes, enz.).

Om goed te begrijpen waarom reference types zo belangrijk zijn, zullen we nu eerst eens inzoomen op hoe het geheugen van een C# applicatie werkt. 

### Stack en Heap: De Rugzak en het Magazijn

Je computer heeft twee soorten geheugen die C# gebruikt. Het verschil snappen is cruciaal om te weten waarom `int` zich anders gedraagt dan `Student`.

#### 1. De Stack (Je Rugzak)

* **Wat is het?**: Een klein, supersnel geheugen dat netjes geordend is.
* **Analogie**: Je rugzak. Je kan er snel iets instoppen en uithalen.
* **Wat zit erin?**: **Value Types** (Eenvoudige waarden).
* **Gedrag**: Als je een `int` aanmaakt, zit de waarde (bv. `10`) *effectief in je rugzak*.

#### 2. De Heap (Het Magazijn)

* **Wat is het?**: Een gigantische, rommelige opslagruimte.
* **Analogie**: Een enorm Amazon-magazijn. Er is plaats voor alles, maar het is trager om iets te vinden.
* **Wat zit erin?**: **Reference Types** (Objecten, Arrays...).
* **Gedrag**: Als je een `new Student()` maakt, wordt de student **in het magazijn** gezet. In je rugzak (Stack) krijg je enkel een **papiertje met de locatie** (het adres) van die student.

---

### Value Types vs Reference Types

Dit fundamentele verschil bepaalt hoe de `=` (toekenning) werkt.

#### Kopie bij Value Types (Kopieer het blad)

Value types (int, bool, double...) zitten direct in de stack.
Als je schrijft `a = b`, neem je de waarde van `b`, maak je er een fotokopie van, en geef je die aan `a`.

```csharp
int getalA = 10;
int getalB = getalA; // KOPIE!
getalB = 999;

Console.WriteLine(getalA); // Nog steeds 10!
```
Je hebt op je eigen kopie geschreven. Het origineel blijft intact.

#### Kopie bij Reference Types (Kopieer de sleutel)
Reference types (alle klassen!) zitten in de Heap.
In de stack zit enkel de **verwijzing** (het adres/de sleutel).
Als je schrijft `studentA = studentB`, kopieer je **enkel het adres**.

**Je hebt nu twee papiertjes die naar dezelfde student in het magazijn wijzen!**

```csharp
Student a = new Student(); 
a.Naam = "Ken";

Student b = a; // KOPIE VAN HET ADRES!
b.Naam = "Barbie";

Console.WriteLine(a.Naam); // Barbie!
```
Omdat `a` en `b` naar **hetzelfde object** wijzen, zien ze elkaars wijzigingen.

![Stack en Heap visualisatie](../assets/5_arrays/gc1.png)<!--{width=75%}-->



### Het geheugen in actie

Laten we eens stap voor stap kijken wat er gebeurt als je een object maakt.

```csharp
Student stud = new Student();
```

1.  **Heap**: `new Student()` reserveert plaats in de Heap (het magazijn) en maakt het object aan.
2.  **Stack**: Er wordt een variabele `stud` gemaakt in de Stack (je rugzak). Een leeg papier.
3.  **Koppeling**: De *locatie* van het object in de Heap wordt opgeslagen in `stud`. We schrijven de locatie in het magazien op het papiertje.

`stud` bevat dus letterlijk **een "pijltje" naar het object**.

![Visualisatie van de referentie](../assets/6_klassen/memzoom3.png)<!--{width=80%}-->

#### De grote verwisseltruc

Omdat variabelen enkel pijltjes zijn, kan je vreemde situaties krijgen.

```csharp
Student a = new Student("Abba");
Student b = new Student("Queen");
```
Je hebt nu twee objecten in het magazijn, en twee pijltjes in je rugzak.

```csharp
b = a;
```
Je zegt nu: "Kopieer de inhoud van `a` naar `b`".
De inhoud van `a` is **het adres van Abba**.
`b` vergeet dus zijn eigen adres (naar Queen) en bevat nu óók het adres van Abba.

**Gevolg:**
1.  Zowel `a` als `b` wijzen naar "Abba".
2.  Niemand wijst nog naar "Queen".
3.  Als je `b` aanpast, past `a` ook aan (want het is hetzelfde object!).

![Twee variabelen, één object](../assets/5_arrays/queenabba2.png)<!--{width=60%}-->


<!-- \newpage -->


### De Garbage Collector (De kuisploeg)

Wat gebeurde er met het "Queen" object in het vorige voorbeeld? Iedereen wijst nu naar "Abba".
"Queen" staat nog wel in het Magazijn (Heap), maar **niemand heeft het adres nog**. Het is onbereikbaar.

Dit is waar de **Garbage Collector (GC)** in actie komt.
Dit is een automatisch proces (een soort robotstofzuiger) dat constant door de Heap rijdt.
De GC checkt: *"Is er nog iemand in de Stack die een verwijzing naar dit object heeft?"*
* **JA**: Object mag blijven.
* **NEE**: Weg ermee! Het geheugen wordt vrijgegeven.

In C# hoef je dus (bijna) nooit zelf geheugen op te kuisen. De GC doet het vuile werk.

![De Garbage Collector ruimt orphaned objects op](../assets/5_arrays/gc2.png)<!--{width=60%}-->

---

### NullReferenceException: De lege hand

Wat als een variabele in de stack *nergens* naar verwijst?
In C# noemen we dat `null`.

```csharp
Student joske; // Nog geen 'new Student()' gedaan!
// joske is nu 'null'. Zijn 'pijltje' wijst naar niets.
```

Als je nu probeert dat object te gebruiken:
```csharp
joske.Naam = "Jos"; // BOEM! CRASH!
```

Dan krijg je de beruchte **NullReferenceException**.
Je probeert iets in het magazijn te leggen, maar je hebt geen adres. Je gooit het dus in het luchtledige.

{% hint style='tip' %}
Zie je een `NullReferenceException`? Check dan altijd of je ergens een object probeert te gebruiken dat nog `null` is (dus waar je nog geen `new` voor hebt gedaan).
{% endhint %}



