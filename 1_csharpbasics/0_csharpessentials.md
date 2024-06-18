# De basisconcepten van C\# <!--\label{ch:2}-->


Om een werkend C#-programma te maken moeten we de C#-taal beheersen. Net zoals iedere taal bestaat ook C# uit:

* grammatica: in de vorm van de **C# syntax** 
* woordenschat: in de vorm van gereserveerde **keywords**.

Een C#-programma bestaat uit een opeenvolging van instructies, **statements** genoemd. **Statements eindigen steeds met een puntkomma**. Net zoals ook in het Nederlands een zin meetal eindigt met een punt. Ieder statement kan je vergelijken als één lijn in ons recept, het algoritme.

De volgorde van de woorden in C# zijn niet vrijblijvend en moeten aan grammaticale regels voldoen '(de syntax). Enkel indien alle statements correct zijn zal het programma gecompileerd worden naar een werkend programma.

Enkele belangrijke regels van C#:

* **Hoofdlettergevoelig**: C# is hoofdlettergevoelig. Dat wil zeggen dat hoofdletter ``R`` en kleine letter ``r`` totaal verschillende zaken zijn voor C#. ``Reinhardt`` en ``reinhardt`` zijn dus ook niet hetzelfde.
* **Statements afsluiten met puntkomma ( **``;``** )**: Doe je dat niet dan zal C# denken dat de regel gewoon op de volgende lijn doorloopt en zal deze dan als één (fout) geheel proberen te compileren.
* **Witruimtes**: Spaties, tabs en enters worden door de C# compiler genegeerd. Je kan ze dus gebruiken om de layout van je code (*bladspiegel*) te verbeteren. De enige plek waar witruimtes wél een verschil geven is tussen aanhalingstekens ``"      "`` die we later zullen leren gebruiken.
* **Commentaar toevoegen kan**: door ``//`` voor een enkele lijn te zetten zal deze lijn genegeerd worden door de compiler. Je kan ook meerdere lijnen code in commentaar zetten door er ``/*`` voor en ``*/`` achter te zetten.
* **Je code begint altijd in de ``Main``-methode!!!**
* **Van boven naar onder**: je code wordt van boven naar onder uitgevoerd en zal enkel naar andere plaatsen springen als je daar expliciet in je code om vraagt.

## Keywords: de woordenschat

C# bestaat zoals gezegd niet enkel uit grammaticale regels. Grammatica zonder woordenschat is nutteloos. Er zijn binnen C# dan ook momenteel 80 woorden, zogenaamde **reserved keywords** die de woordenschat voorstellen. Het spreekt voor zich dat deze keywords een eenduidige, specifieke betekenis hebben en dan ook enkel voor dat doel gebruikt kunnen worden. 

In dit boek zullen we stelselmatig deze keywords leren kennen en gebruiken op een correcte manier om zo werkende code te maken. 

Deze keywords zijn:

|   |     |     |   |
|------|------|-------|------|
|*abstract*|*as*|*base*|**bool**|
|**break**|**byte**|**case**|*catch*|
|**char**|checked|*class*|**const**|
|continue|**decimal**|*default*|delegate|
|**do**|**double**|**else**|**enum**|
|event|explicit|extern|**false**|
|finally|fixed|**float**|**for**|
|*foreach*|goto|**if**|implicit|
|*in*|**int**|*interface*|*internal*|
|*is*|lock|**long**|**namespace**|
|*new*|*null*|*object*|*operator*|
|**out**|*override*|params|*private*|
|*protected*|*public*|readonly|**ref**|
|**return**|**sbyte**|*sealed*|**short**|
|sizeof|stackalloc|*static*|**string**|
|*struct*|**switch**|*this*|*throw*|
|**true**|*try*|typeof|**uint**|
|**ulong**|unchecked|unsafe|**ushort**|
|*using*|using static|*virtual*|**void**|
|volatile|**while**| | |



De keywords in **vet** zijn keywords die we in het eerste deel van dit boek zullen bekijken (hoofdstukken 1 tot en met 8). Die in **cursief** in het tweede deel  (9 en verder). De overige zal je zelf moeten ontdekken ... of mogelijk zelfs nooit in je carrière gebruiken vanwege hun soms obscure nut.


{% hint style='tip' %}
C# is een levende taal. Soms verschijnen er dan ook nieuwe keywords. De afspraak is echter dat de lijst hierboven niet verandert. Nieuwe keywords maken deel uit van de *contextual keywords* en zullen nooit gereserveerde keywords worden. We zullen enkele van deze "nieuwere" keywords tegenkomen waaronder: ``get``, ``set``, ``value`` en ``var``.
{% endhint %}





>![](../assets/gotopolice.png)Aandacht, aandacht! Step away from the keyboard! I repeat. Step away from the keyboard. Hierbij wil ik u attent maken op een belangrijke, onbeschreven, wet voor C# programmeurs: "**NEVER EVER USE GOTO**"
>
>Het moet hier alvast even uit m'n systeem. ``goto`` is weliswaar een officieel C# keyword, toch zal je het in dit boek **nooit** zien terugkomen in code. Je kan alle problemen in je algoritmes oplossen zonder ooit ``goto`` nodig te hebben. 
>
>Voel je toch de drang: **don't!** Simpelweg, don't. Het is het niet waard. Geloof me.
>
>**NEVER USE GOTO**.
>
>Enneuh, ik hou je in't oog hoor!




## Variabelen, identifiers en naamgeving

Variabelen zijn nodig om tijdelijke data in op te slaan, zoals gebruikersinput, zodat we deze later in het programma kunnen gebruiken.

We doen hetzelfde in ons hoofd wanneer we bijvoorbeeld zeggen "tel 3 en 4 op en vermenigvuldig dat resultaat met 5". Eerst zullen we het resultaat van "3+4" in een variabele moeten bewaren. Vervolgens zullen we de inhoud van die variabele vermenigvuldigen met 5 en dat nieuwe resultaat ook in een nieuwe variabele opslaan.

Wanneer we een variabele aanmaken, zal deze moeten voldoen aan enkele afspraken. Zo moeten we minstens 2 zaken meegeven:

* De **identifier** waarmee we snel aan de variabele-waarde kunnen. Dit is de gebruiksvriendelijke naam die we geven aan een geheugenplek.
* Het **datatype** dat aangeeft wat voor soort data we wensen op te slaan. Enkel en alleen dat soort type data zal in deze variabele kunnen bewaard worden. 


### Regels voor identifiers

De code die we gaan schrijven moet voldoen aan een hoop regels. Wanneer we in onze code zelf namen (**identifiers**) geven aan variabelen (en later ook methoden, objecten, enz.) dan moeten we een aantal regels volgen:

* **Hoofdlettergevoelig**: de identifiers ``tim`` en ``Tim`` zijn verschillend zoals reeds vermeld.
* **Geen keywords**: identifiers mogen geen gereserveerde C# keywords zijn. De keywords van 2 pagina's terug mogen dus niet. Varianten waarbij de hoofdletters anders zijn mogen wel.  ``gOTO`` en ``stRINg`` mogen dus wel, maar niet ``goto`` of ``string`` want dat zijn gereserveerde keywords. Een ander voorbeeld ``INT`` mag bijvoorbeeld wel, maar ``int`` niet.
* **Eerste karakter-regel**: het eerste karakter van de identifier mag een  **kleine of grote letter**, of een **liggend streepje** (``_``) zijn.
* **Alle andere karakters-regels**: de overige karakters volgende de eerste karakter-regel, maar mogen ook cijfers zijn.
* **Lengte**: Een legale identifier mag zo lang zijn als je wenst, maar je houdt het best leesbaar.



Volg je voorgaande regels niet dan zal je code niet gecompileerd worden en zal VS de identifiers in kwestie als een fout aanduiden. Of beter, als een hele hoop foutboodschappen. Schrik dus niet als je bijvoorbeeld het volgende ziet:


![Zoals je ziet raakt VS volledig de kluts kwijt als je je niet houdt aan de identifier regels.](../assets/1_csharpbasics/frerror.png)

<!-- \newpage -->


#### Enkele voorbeelden

Enkele voorbeelden van toegelaten en niet toegelaten identifiers:

| Identifier | Toegelaten? | Uitleg indien niet toegelaten |
|-----|----|------------|
|werknemer| ja |  |
|kerst2018| ja |  |
|pippo de clown| neen| geen spaties toegestaan|
|4dPlaats| neen| mag niet starten met een cijfer|
|_ILOVE2022| ja| |
|Tor+Bjorn| neen| enkel cijfers, letters en liggende streepjes toegestaan|
|ALLCAPSMAN| ja |  |
|B_A_L| ja| |
|class | neen| gereserveerd keyword|
|WriteLine| ja|  |
|______| ja|  | (liggende streepjes)

### Naamgeving afspraken

Er zijn geen vaste afspraken over hoe je je variabelen moet noemen toch hanteren we enkele **coding richtlijnen**:

* **Duidelijke naam**: de identifier moet duidelijk maken waarvoor de identifier dient. Schrijf dus liever ``gewicht`` of ``leeftijd`` in plaats van ``a`` of ``meuh``.
* **Camel casing**: gebruik camel casing indien je meerdere woorden in je identifier wenst te gebruiken. Camel casing wil zeggen dat ieder nieuw woord terug met een hoofdletter begint. Een goed voorbeeld kan dus zijn ``leeftijdTimDams`` of ``aantalLeerlingenKlas1EA``. Merk op dat we liefst het eerste woord met kleine letter starten. Uiteraard zijn er geen spaties toegelaten.


<!-- \newpage -->

## Commentaar

Soms wil je misschien extra commentaar bij je code zetten. Op die manier kan je extra informatie aan jezelf of andere *lezers* van je code geven.

### Enkele lijn commentaar

Eén lijn commentaar geef je aan door de lijn te starten met twee voorwaartse slashes ``//``. Uiteraard mag je ook meerdere lijnen op deze manier in commentaar zetten. Zo wordt dit ook vaak gebruikt om tijdelijk een stuk code "uit te schakelen". Ook mogen we commentaar *achter* een stuk C# code plaatsen zoals we hieronder tonen. 

``//`` zal alle tekens die volgen tot aan de volgende witregel in commentaar zetten:

```csharp
//De start van het programma
int getal = 3;
//Nu gaan we rekenen
int result = getal * 5;
// result = 3*5;
Console.WriteLine(result); //We tonen resultaat op scherm: 15
```

### Blok commentaar

We kunnen een stuk tekst als commentaar aangeven door voor de tekst ``/*`` te plaatsen en ``*/`` achteraan. Een voorbeeld:

```csharp
/*
    Een blok commentaar
    Een heel verhaal, dit wordt mooi
    Is dit een haiku?
*/
int leeftijd = 0;
```


Je kan ook code in VS selecteren en dan met de comment/uncomment-knoppen in de menubalk heel snel lijnen of hele blokken code van commentaar voorzien, of deze net weghalen:

![De linkse knop voegt comment tags toe, de andere verwijdert ze.](../assets/1_csharpbasics/comments.png)


