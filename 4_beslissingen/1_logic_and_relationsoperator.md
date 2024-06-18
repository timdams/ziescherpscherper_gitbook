## Relationele en logische operators

Om beslissingen te kunnen nemen in C# hebben we een nieuw soort operators nodig. Operators waarmee we kunnen testen of iets waar of niet waar is. Met C# kun je een actie uitvoeren als een voorwaarde waar is, en iets anders doen (of een stap overslaan) als de voorwaarde niet waar is. 

Dit doen we met de zogenaamde **relationele operators** en **logische operators**.

### Booleaanse expressies

**Een booleaanse expressie is een stuk C# code dat een ``bool`` als resultaat zal geven.** De logische en relationele operators die ik hierna bespreek zijn operators die een ``bool`` teruggeven. Ze zijn zogenaamde test-operators: ze testen of iets waar is of niet.

### Relationele operators

Relationele operators zijn het hart van booleaanse expressies. En guess what, je kent die al van uit het lager onderwijs. Enkel de "gelijk aan" ziet er iets anders uit dan we gewoon zijn uit onze lessen wiskunde:

| Operator| Betekenis| 
| ---------| ---------|
| ``>`` |groter dan| 
| ``<`` |kleiner dan| 
| ``==`` |gelijk aan | 
| ``!=`` |niet gelijk aan| 
| ``<=`` |kleiner dan of gelijk aan| 
| ``>=`` |groter dan of gelijk aan| 

Deze operators hebben steeds twee operanden nodig en geven **een bool als resultaat terug**. Beide operanden  **moeten van hetzelfde datatype zijn**. Je kan geen appelen met peren vergelijken!

Daar dit operators zijn kan je deze dus gebruiken in eender welke expressie. Het resultaat van de expressie ``12 > 6`` zal ``true`` als resultaat hebben daar 12 groter is dan 6. Eenvoudig toch.

{% hint style='tip' %}
We weten al dat je het resultaat van een expressie altijd in een variabele kunt bewaren. Ook bij het gebruik van relationele operators kan dat dus:

```csharp
bool isKleiner = 65 > 67 ;
Console.WriteLine(isKleiner);
```

Er zal `false` als output op het scherm verschijnen.
{% endhint %}


{% hint style='warning' %}
Er is een groot verschil tussen de ``=`` operator en de ``==`` operator. De eerste is de toekenningsoperator en zal de rechtse operand aan de linkse operand toewijzen. De tweede zal de linkse met de rechtse operand op gelijkheid vergelijken en een ``bool`` teruggeven.
{% endhint %}


### Logische operators

Vaak wil je meer complexe keuzes maken, zoals :*"ga verder indien je hongerig bent EN je genoeg geld bijhebt"*. Dit doen we met de zogenaamde **logische operators**. 

Er zijn 3 (booleaanse) operators die je hiervoor kunt gebruiken:

* ``&&`` (*EN*) : Geeft enkel ``true`` als beide operanden ``true`` zijn
* ``||`` (*OF*) : Geeft ``true`` indien minstens 1 operand ``true`` is
* ``!`` (*NIET*) : Inverteert de waarde van de expressie (``true`` wordt ``false`` en omgekeerd)

De logische operators geven ook steeds een ``bool`` terug **maar verwachten enkel operanden van het type ``bool``**. Als je dus schrijft ``true || false``  zal het resultaat ``true`` zijn.

De *EN* en *OF* operators verwachten 2 operanden. Maar de *NIET*-operator verwacht maar 1 operand.

Aangezien onze relationele operators ``bool`` als resultaat geven, kunnen we dus de uitvoer van deze operators gebruiken als operanden voor de logische operators. We gebruiken hierbij haakjes om zeker de volgorde juist te krijgen:


```csharp
bool result = (4 < 6) && ("ja" == "nee");
```

De haakjes zorgen ervoor dat eerste die delen worden berekend. Voorgaande zal dus in een tussenstap (die jij niet ziet) tijdens de uitvoer er als volgt uitzien:

```csharp
bool result = true && false;
```

Vervolgens wordt dan de logische EN getest en krijgen we finaal ``false`` in ``result``.

#### Niet-operator

Je kan de niet-operator voor een expressie zetten om het resultaat van de expressie te inverteren.  Bijvoorbeeld:


```csharp
bool result = !(0==2) 
```

Eerst wordt weer het resultaat tussen de haakjes berekend. Dit geeft ``false`` (daar 0 niet gelijk is aan 2). Vervolgens passen we de NIET-operator toe op dit resultaat en zal er dus  ``true`` bewaard worden.

Merk op dat we deze code ook kunnen schrijven als:

```csharp
bool result = (0!=2) 
```


{% hint style='warning' %}
Alhoewel we voorgaande ook zonder haakjes kunnen schrijven, raad ik dit af. Haakjes zorgen ervoor dat je code leesbaarder wordt. Maar nog belangrijker: het maakt de volgorde van bewerkingen explicieter. Als je niet zeker weet welke operator voorrang heeft, kun je haakjes gebruiken om de juiste volgorde af te dwingen. Dit helpt je om logische fouten te voorkomen die kunnen ontstaan door verkeerde veronderstellingen.
{% endhint %}


#### Volgorde van bewerkingen

De volgorde van bewerkingen wordt nu belangrijk[^volgorde]! In C# hebben de operatoren die we al kennen volgende volgorde:

1. **Logische NIET: ``!``**
2. Delen en vermenigvuldigen: ``*``, ``/``, ``%``
3. Optellen en aftrekken: ``+``, ``-``
4. **Relationele operators: ``<``, ``<=``, ``>``, ``>=``**
5. **Gelijkheid: ``==``, ``!=``**
6. **Logische EN: ``&&``**
7. **Logische OF: ``||``**

Wil je deze volgorde dus veranderen in een samengestelde expressie, dan moet je gebruik maken van haakjes.



[^volgorde]: Bekijk zeker de tabel op [docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators) waar de volgorde van alle operators wordt beschreven.



### Test jezelf

Wat zal de uitkomst zijn van volgende expressies?

* ``3>2 ``
* ``4!=4`` 
* ``4<5 && 4<3``
* ``"a"=="A" || 4>=3``
* ``(3==3 && 2<1) || 5!=4``
* ``!(4<=3)``
* ``true || false``
* ``!true && false``


