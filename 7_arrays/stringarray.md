## String en arrays

Het type ``string`` is niet meer dan een arrays van karakters, ``char[]``. Het is dan ook logisch dat we dit erg belangrijke datatype even apart toelichten en enkele nuttige methoden tonen om strings te manipuleren.

### String naar char array

Om de aparte karakters van een ``string`` te bewerken zet je deze best om naar een *char-array* . Dit kan gebruikmakend van ``.ToCharArray()`` als volgt:

```csharp
string origineleZin = "Ik ben Tom";
char[] karakters = origineleZin.ToCharArray();
karakters[8] = 'i';
```

De array zal nu het volgende bevatten:``Ik ben Tim``. Willen je dit nu terug als ``string``, dan lees je snel verder!

### Char array naar string

Ook de omgekeerde weg is mogelijk. De werking is iets anders en maakt gebruik van ``new string()``. Let vooral op hoe we de char array doorgeven als argument bij het aanmaken van een nieuwe ``string`` in lijn 3:

```csharp
char[] alleKarakters = {'h', 'a', 'l', 'l', 'o'};
alleKarakters[2] = 'x';
string woord = new string(alleKarakters);
Console.WriteLine(woord);
```

De uitvoer van deze code zal zijn: ``haxlo``.

### Andere nuttige methoden met strings

Volgende methoden kan je rechtstreeks op string-variabelen oproepen:

#### Length
Geeft het totaal aantal karakters in de string wat logisch is, daar het om een array gaat:

```csharp
string myName = "Tim";
Console.WriteLine(myName.Length); //er verschijnt 3 op het scherm
```



#### IndexOf

Deze methode geeft een ``int`` terug die de index bevat waar de string die je als parameter meegaf begint. Je kan deze index gebruiken om te ontdekken of een bepaald woord bijvoorbeeld in een grote lap tekst voorkomt zoals volgend voorbeeld toont:

```csharp
string boek = "Ik ben Reinhardt";
int index = boek.IndexOf("ben");
Console.WriteLine(index); 
```

Er zal ``3`` verschijnen op scherm. De substring "ben" start op positie 3. "ik" staat op positie 0 en 1, gevolgd door een spatie op positie 2. Indien de string niet gevonden werd, zal ``index`` de waarde -1 krijgen.

#### Trim

``Trim()`` verwijdert alle onnodige spaties en andere onzichtbare tekens vooraan en achteraan de string. Deze methode geeft de opgekuiste string terug als resultaat. Dit resultaat moet je dus bewaren als je er nog iets mee wilt doen. In het volgende voorbeeld overschrijven we de originele string met z'n opgekuiste versie:

```csharp
string boek = "   Ik ben Reinhardt   ";
Console.WriteLine(boek);
boek = boek.Trim();
Console.WriteLine(boek);
```

Dit zal de output op het scherm zijn (de spaties achteraan op lijn 1 zie je niet, maar zijn er dus wel):


```text
   Ik ben Reinhardt   
Ik ben Reinhardt
```



#### ToUpper en ToLower

``ToUpper`` zal de meegegeven string naar ALLCAPS omzetten en geeft de nieuwe string als resultaat terug. ``ToLower()``doet het omgekeerde.

```csharp
string boek = "Ik ben Reinhardt";
Console.WriteLine(boek.ToUpper());
Console.WriteLine(boek.ToLower());
```

Output op het scherm:


```csharp
IK BEN REINHARDT
ik ben reinhardt
```



#### Replace

``Replace(string old, string news)`` zal in de string alle substrings die gelijk zijn aan ``old`` vervangen door de meegegeven ``news`` string. Vervolgens zal de nieuwe string als resultaat worden teruggeven. 

Volgende voorbeeld toont dit en zal "Mercy" vervangen door "Reinhardt":

```csharp
string boek = "Ik ben Mercy";
boek = boek.Replace("Mercy","Reinhardt");
Console.WriteLine(boek);
```

{% hint style='tip' %}
``Replace`` kan je ook misbruiken om bijvoorbeeld alle woorden uit een stuk tekst te verwijderen door deze te vervangen door een lege ``string`` met de waarde ``""``. Volgende code zal alle ``"e"``'s uit de tekst verwijderen:

```csharp
string boek = "Ik ben Mercy";
boek = boek.Replace("e", "");
Console.WriteLine(boek);
```

Waardoor we ``Ik bn Mrcy`` op het scherm krijgen.
{% endhint %}


#### Remove

``Remove(int start, int lengte)`` zal op de index ``start`` alle ``lengte`` volgende karakters in de ``string`` verwijderen en een nieuwe, kortere ``string`` als resultaat geven.

Volgend voorbeeld zal het stukje "ben " uit de ``string`` weghalen:

```csharp
string boek = "Ik ben Mercy";
boek = boek.Remove(3,4);
Console.WriteLine(boek);
```

Output op het scherm:


```text
Ik Mercy
```

In voorgaande voorbeeld gaven we de methode ``Remove`` de opdracht: *"verwijder alles vanaf het element met index 3 (de ``b``) en dit gedurende 4 tekens (dus tot en mét de spatie na ``ben``)"*.

<!-- \newpage -->


#### Split

{% hint style='tip' %}
Volgende twee methoden zijn ``static`` en moet je  via de klasse ``String`` doen en niet via de objecten zelf. Ik leg in hoofdstuk 11 uit waarom dat is.
{% endhint %}

 De ``Split`` methode laat toe een string te splitsen op een bepaald teken. Het resultaat is steeds een **array van strings**.

```csharp
string data = "12,13,20";
string[] gesplitst = data.Split(',');

for(int i = 0; i<gesplitst.Length;i++)
{
    Console.WriteLine(gesplitst[i]);
}
```

Uiteraard kan je dit gebruiken om op eender welk ``char`` te splitsen. 

#### Join

Via ``Join`` kunnen we een array van strings terug samenvoegen. Het resultaat is een nieuwe string.

Volgende voorbeeld zal de eerder gesplitste array van het vorige voorbeeld opnieuw samenvoegen maar nu met telkens een ``;`` tussen iedere string:


```csharp
string joined = String.Join(";", gesplitst);
```






