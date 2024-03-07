## Oefeningen

### Prijzen met foreach

Maak een array die tot 20 prijzen (``double``) kan bewaren. Vraag aan de gebruiker om 20 prijzen in te voeren en bewaar deze in de array. Doorloop vervolgens m.b.v. een ``foreach``-lus de volledige array en toon enkel de elementen op het scherm wiens prijs hoger of gelijk is aan €5.00. Toon op het einde van het programma het gemiddelde van alle prijzen (dus inclusief de lagere prijzen).

### Speelkaarten

Maak een klasse ``Speelkaart`` die je kan gebruiken om een klassieke speelkaart met getal en "kleur" voor te stellen. Een kaart heeft 2 eigenschappen:

1. Een getal van 1 tot en met 13 (boer=11, koningin= 12, heer= 13).
2. Een soort, de zogenaamde ``suite``. Deze stel je voor via een enumtype en kan als waarden Schoppen, Harten, Klaveren of Ruiten zijn.


Schrijf nu met behulp van 2 loops die de 52 kaarten van een standaard pak in een ``List<SpeelKaart>`` lijst plaatst.

Maak een applicatie die telkens een willekeurige kaart uit de *stapel* trekt en deze aan de gebruiker toont. De kaart wordt na het tonen ook uit de lijst verwijderd. Door met een willekeurig getal te werken hoef je dus je deck niet te schudden.

### Computer-winkel*

Een firma heeft een grote lijst met computeronderdelen en wil hier de nodige filters op kunnen toepassen.

#### ComputerOnderdeel
De klasse ``ComputerOnderdeel`` bestaat uit volgende auto-properties:

* Prijs (``int``)
* ID (``int``)
* InDoos (``bool``)

Voorts heeft de klasse een default constructor die voorgaande auto-properties op willekeurige waarden instelt (prijs positief tot max 1000, ID een getal tussen 100 en 999)

De klasse heeft 1 methode ``ToonInfo`` die de 3 waarden van het object naar het scherm stuurt:


```text
Prijs: 845, ID: 45, InDoos: true
```

#### Filteren

Maak in je hoofdprogramma een ``List<ComputerOnderdeel>`` dat je vult met 100 willekeurige  aangemaakte objecten.
Vervolgens:

* Roep de ``ToonInfo`` methode aan van ieder computeronderdeel in de lijst aan.
* Roep de ``ToonInfo`` methode aan van ieder computeronderdeel met een prijs boven de 400.
* Idem nu voor alle onderdelen die in een doos zitten.
* Idem nu voor alle onderdelen die een even ID hebben én wiens prijs onder de 200 ligt.

Tussen iedere filter toon je op het scherm wat de volgende lijst juist voorstelt (bv "Nu tonen we alle onderdelen in een doos").

#### Managen

Vraag nu aan de gebruiker wat er met de lijst moet gebeuren:

1. Alle objecten in een doos verwijderen
2. Alle objecten met een prijs kleiner dan 100 verwijderen.

Toon het resultaat van de aangepaste lijst (door de ``ToonInfo`` van ieder object in de lijst aan te roepen.)

#### Finale

Kan je hier een volledige applicatie van maken die een computerfirma als een soort inventaristool kan gebruiken (en dus met de nodige menu's en mogelijkheden om bijvoorbeeld een nieuw onderdeel toe te voegen)? Kijk zeker eens naar volgende oefening daaromtrent.

### Bookmark Manager*

Maak een "bookmark manager". Deze tool zal in de console aan de gebruiker 5 favoriete sites vragen: ``naam`` en ``url``. Vervolgens zal de tool alle sites in een lijst tonen met een nummer ervoor. De gebruiker kan dan de nummer intypen en de tool zal automatisch de site in een vereenvoudigde versie op het scherm tonen. 

Je opdracht:

1. Maak een array of ``List`` waarin je 5 bookmark objecten kan plaatsen. 
2. Vul de applicatie aan zodat de gebruiker een bestaand bookmark kan verwijderen en een bestaand bookmark kan aanpassen.
3. De gebruiker kan een bookmark selecteren (door de index ervan in te geven) en vervolgens zal deze site getoond worden op het scherm.

Hierna volgen enkele zaken die je zal nodig hebben.



```java
class BookMark
{
    public BookMark(string naamIn, urlIn)
    {
        Naam = naamIn;
        URL = urlIn;
    }

    public string Naam { get; set; }
    public string URL { get; set; }
    public string DownloadSite()
    {
        var wc = new WebClient();
        string result = wc.DownloadString(URL);
        return GetPlainTextFromHtml(result);
    }
    
    private string GetPlainTextFromHtml(string html)
    {
        string htmlTagPattern = "<.*?>";
        string reg = "(\\<script(.+?)\\</script\\>)|(\\<style(.+?)\\</style\\>)";
        var regCss = 
            new Regex(reg, RegexOptions.Singleline|RegexOptions.IgnoreCase);
        html = regCss.Replace(html, string.Empty);
        html = Regex.Replace(html, htmlTagPattern, string.Empty);
        html = Regex.Replace(html, @"^\s+$[\r\n]*", "", RegexOptions.Multiline);
        html = html.Replace("&nbsp;", " ");
        return html;
    }
}
```

De ``GetPlanTextFromHtml()`` methode komt van volgende post:: **www.mercator.eu/mercator/std/info_aruba/reporting-hoe-gegevens-afdrukken-met-html-tags.html**.


Voorbeeld van hoe de ``Bookmark`` klasse zal werken:

```java
BookMark u = new BookMark("Google", "https://www.google.be" );
Console.WriteLine(u.DownloadSite());
```

Kan je je eigen "console browser" maken?



### Voortplanten en generaties

We gaan de voortplantings-simulator uit hoofdstuk 10 uitbreiden. Voorzie volgende constructors in de klasse ``Mens``:
* Een default constructor die bovenstaande eigenschappen op willekeurige waarden instelt. Bij maxlengte is deze waarde 90% van de tijd tussen 150 en 210. 5% van de tijd is deze een getal tussen 40 en 150. 5% van de tijd een getal tussen 210 en 240.
* Een overloaded constructor waarbij de 3 eigenschappen als parameter kunnen doorgegeven worden.

Maak 12 willekeurige mensen en plaats deze in een List. De eerste 6 mensen zijn vrouwen, de laatste 6 mensen zijn mannen. Alle mensen hebben willekeurige eigenschappen, enkel het geslacht is dus al bepaald.
Laat nu de mensen voortplanten.
* De eerste helft mensen in de List zoeken een willekeurige partner van het andere geslacht in de andere helft lijst. En maakt hier een nieuwe mens mee. De man wordt meegegeven als parameter aan de Plantvoort methode van de vrouw.
* Plaats deze nieuwe mens in de lijst achteraan.

#### Generaties

Voeg een property Generatie toe aan je ``Mens`` die toelaat om te onthouden wanneer Mens is aangemaakt. Je kan deze via de constructor instellen. De eerste 12 mensen zijn generatie 1. Een nieuw mens krijgt als generatie de generatie van z'n ouder + 1 . Indien beide ouders van een verschillende generatie waren, dan krijgt het kind de generatie+1 van z'n ouder met de hoogste generatie van beide.

Herhaal de voortplantingscyclus voor 10 generaties (merk op dat ouders dus vermoedelijk kinderen zullen maken met hun eigen kinderen/kleinkinderen. Niet over nadenken) en bekijk wat de resultaten zijn. Plaats deze simulatie in een ``static`` methode ``Simuleer`` die een List van mensen als parameter aanvaardt, alsook een getal dat aangeeft hoeveel generaties moet getest worden. 

Houdt bij iedere Mens die je aanmaakt om welke generatie het gaat.

Toon aan de gebruiker hoeveel de gemiddelde lengte is, hoeveel percent welke kleur ogen heeft, etc.

Maak een applicatie waarbij de gebruiker experimenten kan doen om te zien wat er gebeurt na x generaties. Bijvoorbeeld:
* Wat als mannen erg klein zijn, vrouwen erg lang.
* Wat als mensen met blauwe ogen steeds die kleur aan hun kinderen doorgeven, na hoeveel generaties heeft iedereen blauwe ogen.
