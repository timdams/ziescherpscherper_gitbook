## Exception handling

*Het wordt tijd om de olifant in de kamer te benoemen. Het wordt tijd om een bekentenis te maken... Ben je er klaar voor?! Hier komt ie. Luister goed, maar zeg het niet door: ik heb al de hele tijd informatie voor je achter gehouden! Sorry, het was sterker dan mezelf. Maar ik deed het voor jou. Het was de enige manier om ervoor te zorgen dat je leerde programmeren zonder constant bugs in je code achter te laten. Dus ja, hopelijk neem je het me niet kwalijk?*

Het wordt tijd om **exception handling** er bij te halen! Een essentiële programmeertechniek die ervoor zorgt dat je programma minder snel zal crashen indien er zich **uitzonderingen** tijdens de uitvoer voordoen. 

Wat een dramatische start zeg. Waar was dat voor nodig?! De reden is eenvoudig: exception handling is een tweesnijdend zwaard. Je zou exception handling kunnen gebruiken om al je bugs op te vangen, zodat de eindgebruiker niet ziet hoe vaak je programma zou crashen zonder exception handling. 

Maar uiteindelijk blijf je wel met slechte code zitten en een gouden regel in programmeren is dat slechte code je altijd zal achtervolgen en je ooit dubbel en hard zal straffen voor iedere bug waar je te lui voor was om op te lossen. **Kortom, exception handling is de finale fase van goedgeschreven code.**


### Waarom exception handling?

Veel fouten in je code zijn het gevolg van:

* **Het aanroepen van data die er niet is** : bijvoorbeeld een bestand dat werd verplaatst of hernoemd . Of wat denk je van het wegvallen van het wifi-signaal net wanneer je programma iets van een online database nodig heeft.
* **Foute invoer door de gebruiker** : denk aan de gebruiker die een letter invoert terwijl het programma een getal verwacht.
* **Programmeerfouten** : de ontwikkelaar gebruikt een object dat nog niet met de ``new`` operator werd geïnitialiseerd. Of bijvoorbeeld een deling door nul in een wiskundige berekening.

Voorgaande zaken zijn eigenlijk geen fouten, maar uitzonderingen (**exceptions**). Ze doen zich zelden voor, maar hebben wel een invloed op de correcte uitvoer van je programma. Je programma zal met deze uitzonderingen rekening moeten houden wil je een gebruiksvriendelijk programma hebben. Veel uitzonderingen gebeuren buiten de wil van het programma om (geen wifi , foute invoer, enz.). Door deze uitzonderingen af te handelen (**exception handling**), kunnen we ons programma instructies geven om alternatieve acties uit te voeren wanneer er een uitzondering optreedt.

Je hebt waarschijnlijk al eerder exceptions gezien in je eigen programma's. Als je programma plots een hele hoop tekst toont (waaronder het woord "Exception") en vervolgens direct afsluit, heb je een exception gegenereerd die niet is afgehandeld.

![Een joekel van een foutboodschap die je gebruiker huilend zal wegjagen.](../assets/20_exceptions/exceptcode.png)

Je moet zelfs niet veel moeite doen om uitzonderingen te genereren. Denk maar aan volgende voorbeeld waarbij je een exception kan genereren door een 0 in te geven, of iets anders dan een getal.

```csharp
Console.WriteLine("Geef een getal aub");
int noemer = Convert.ToInt32(Console.ReadLine());
double resultaat = 100/noemer;
Console.WriteLine($"100/{noemer} is gelijk aan {resultaat}");
```

### Exception handling met ``try`` en ``catch``

Het mechanisme om exceptions af te handelen in C# bestaat uit 2 delen:

* Een **``try`` blok**: binnen dit blok staat de code die je wil controleren op uitzonderingen omdat je weet dat die hier kunnen optreden.
* Een of meerdere **``catch``-blokken**: dit blok zal mogelijk exceptions die in het bijhorende try-block voorkomen opvangen. Met andere woorden: in dit blok *staat de code die de uitzondering zal verwerken* zodat het programma op een deftige manier verder kan of meer elegant zichzelf afsluiten (*graceful shutdown*).

De syntax is als volgt (let er op dat de catch blok onmiddellijk na het try-blok komt):

```csharp
try
{
    //code waar exception mogelijk kan optreden
}
catch 
{
    //exception handling code hier
}
```




### Een try catch voorbeeld

In volgend stukje code kunnen uitzonderingen optreden zoals we zonet zagen:

```csharp
string input = Console.ReadLine();
int converted = Convert.ToInt32(input)
```

Een ``FormatException`` zal optreden wanneer de gebruiker tekst of een kommagetal invoert. De ``Convert.ToInt32()`` methode kan niet met andere input dan gehele getallen werken.

Ik toon nu hoe we dit met exception handling kunnen opvangen[^elegant]:

```csharp
try
{
    string input = Console.ReadLine();
    int converted = Convert.ToInt32(input);
}
catch 
{
    Console.WriteLine("Verkeerde invoer!");
}
```

Indien er nu een uitzondering optreedt dan zal de tekst "Verkeerde invoer" getoond worden. Vervolgens gaat het programma verder met de code die mogelijk na het ``catch``-blok staat.

[^elegant]: Merk op dat dit probleem eleganter kan opgelost worden met ``TryParse`` wat in het appendix wordt uitgelegd.


### Een exception genereren met ``throw``

Je kan ook zelf eender waar in je code een uitzondering **opwerpen**. Je doet dit met het **``throw``** keyword. De werking is quasi dezelfde als het ``return`` keyword. Alleen zal bij een ``throw`` je *terug gaan* tot de eerste plek waar een ``catch`` klaarstaat om de uitzondering op te vangen. Om een uitzondering op te werpen dien je eerst een ``Exception`` object aan te maken en daar de nodige informatie in te plaatsen. In hoofdstuk 14 ga ik hier nog wat dieper op in, maar hier alvast een voorbeeldje:

```csharp
//Een error treedt op
throw new Exception("Wow, dit loopt fout");
```

Afhankelijk van het soort fout kunnen we echter ook andere soort uitzonderingen opwerpen. Draai daarom snel deze pagina om en ontdek hoe dit kan!

<!-- \newpage -->



### Meerdere catchblokken

`Exception` is een klasse van het .NET framework. Er zijn van deze basis-klasse meerdere Exception-klassen afgeleid die een specifieke uitzondering behelzen. Enkele veelvoorkomende zijn:

| Klasse | Omschrijving |
|--------|-----------|
|`Exception`|	Basisklasse|
|`SystemException`|	Klasse voor uitzonderingen die niet al te belangrijk zijn en die mogelijk verholpen kunnen worden.|
|`IndexOutOfRangeException`|	De index is te groot of te klein voor de benadering van een array|
|`NullReferenceException`|	Benadering van een niet-geïnitialiseerd object |


Je kan in het catch blok aangeven welke soort exceptions je wil vangen in dat blok. Als je bijvoorbeeld alle Exceptions wil opvangen schrijf je:

```csharp
catch (Exception e)
{
}
```

Hiermee vangen we dus **alle** Exceptions op, daar alle Exceptions van de klasse `Exception` afgeleid zijn en dus ook zelf een `Exception` zijn. De identifier ``e`` kies je zelf en wordt gebruikt om vervolgens in het ``catch`` block de nodige informatie uit het opgevangen Exception object (``e``) uit te lezen. Ik leg dit zo meteen uit.

We kunnen nu echter ook specifieke exceptions opvangen. De truc is om de meest algemene exception onderaan te zetten en naar boven toe steeds specifieker te worden. We maken een *fallthrough mechanisme* (wat we ook in een ``switch`` al hebben gezien). 

Stel bijvoorbeeld dat we weten dat de `FormatException` kan voorkomen en we willen daar iets mee doen. Volgende code toont hoe dit kan:

```csharp
try
{
    //...
}
catch (FormatException e)
{
    Console.WriteLine("Verkeerd invoerformaat");
}
catch (Exception e)
{
    Console.WriteLine("Exception opgetreden");
}
```

Indien een ``FormatException`` optreedt dan zal het eerste catch-blok uitgevoerd worden, in alle andere gevallen het tweede. Het tweede blok zal niet uitgevoerd worden indien een ``FormatException`` optreedt.




### Welke exceptions worden gegooid?

De online .NET documentatie is de manier om te weten te komen welke exceptions een methode mogelijk kan opgooien. Gaan we bijvoorbeeld naar de documentatie van de ``Int32.Parse``-methode[^intparsedoc] dan zien we daar een sectie "Exceptions" waar klaar en duidelijk wordt beschreven wanneer welke exception wanneer wordt opgeworpen.



![Een deel van de documentatie. ](../assets/20_exceptions/msdn.png)<!--{width=60%}-->


[^intparsedoc]: Zie [docs.microsoft.com/dotnet/api/system.int32.parse](https://docs.microsoft.com/dotnet/api/system.int32.parse).

<!-- \newpage -->


### Werken met de exception parameter

De Exceptions die worden opgegooid door een methode zijn objecten van de Exception-klasse. Deze klasse bevat standaard een aantal interessante zaken, die je kan oproepen in je code.

**Bovenaan de declaratie van het ``catch``-blok geef je aan hoe het exception object in het blok zal heten.** In de vorige voorbeelden was dit altijd `e` (standaardnaam).

Alle ``Exception``-objecten bevatten volgende informatie:

| Element	|Omschrijving|
|----|----|
|`Message`|	Foutmelding in relatief eenvoudige taal.|
|`StackTrace`|	Lijst van methoden die de exception hebben doorgegeven.|
|`TargetSite`|	Methode die de exception heeft gegenereerd (staat bij StackTrace helemaal bovenaan).|
|`ToString()`	|Geeft het type van de exception, Message en StackTrace terug als string.|


We kunnen via deze parameter meer informatie uit de opgeworpen uitzondering uitlezen en bijvoorbeeld aan de gebruiker tonen:

```csharp
catch (Exception e)
{
    Console.WriteLine("Exception opgetreden");
    Console.WriteLine("Message:"+e.Message);
 
    Console.WriteLine($"Targetsite: {e.TargetSite}");
    Console.WriteLine("StackTrace: {e.StackTrace}");
}
```


{% hint style='danger' %}
Vanuit een security standpunt is het zelden aangeraden om Exception informatie zomaar rechtstreeks naar de gebruiker te sturen. Mogelijk bevat de informatie gevoelige informatie en zou deze door kwaadwillige gebruikers kunnen misbruikt worden om bugs in je programma te vinden.
{% endhint %}





