### Waar exception handling in code plaatsen?

De plaats in je code waar je je exceptions zal opvangen, heeft invloed op de totale werking van je code. 

Stel dat je volgende stukje code hebt waarin je een methode hebt die een lijst van strings zal beschouwen als urls die moeten gedownload worden.  Indien er echter fouten in de string staan dan zal er een uitzondering optreden bij lijn 16. De tweede url ("http:\\\\www.humo.be") bevat namelijk een bewuste fout: de schuine strepen staan in de verkeerde richting.

{% hint style='tip' %}
Als sneak preview tonen we ook ineens hoe arrays van objecten werken.
{% endhint %}


```java
static void Main(string[] args)
{
    string[] urllist = new string[3];
    urllist[0] = "http://www.ziescherp.be";
    urllist[1] = "http:\\www.humo.be";
    urllist[2] = "timdams.com";
    DownloadAllUris(urllist);
}
 
static public void DownloadAllUris(string[] urls)
{
    System.Net.WebClient webClient = new System.Net.WebClient();
 
    for(int i = 0; i < urls.Length;i++)
    {
        Uri uri = new Uri(urls[i]);
        string result = webClient.DownloadString(uri);
        Console.WriteLine($"{uri} gedownload. Dit is het resultaat {result}");
    }
}
```

{% hint style='tip' %}
De ``WebClient`` is een handige klasse om te interageren met online zaken (websites, restful api's, webservices, enz.). Je kan er bijvoorbeeld heel makkelijk een webscraper mee maken.
{% endhint %}


We bekijken nu een aantal mogelijk try/catch locaties in deze code en zien welke impact deze hebben op de totale uitvoer van het programma.

### Rondom methode-aanroep in z'n geheel

```java
try
{
    DownloadAllUris(urllist);
}
catch (Exception ex)
{
    Console.WriteLine(ex.Message);
}
```

Zal resulteren in:


```text
http://www.ziescherp.be gedownload!
Ongeldige URI: kan de Authority/Host niet parsen.
```

Met andere woorden, zolang de urls geldig zijn zal de download lukken. Bij de eerste fout die optreedt zal de volledige methode echter stoppen. Dit is waarschijnlijk enkel wenselijk indien de code erna de informatie van ALLE urls nodig heeft.

### Rond afzonderlijke elementen in de loop

Mogelijk wil je echter dat je programma blijft werken indien er 1 of meerdere urls niet werken. We plaatsen dan de try catch niet rond de methode ``DownloadAllUris``, maar net binnenin de methode zelf rond het gedeelte dat kan mislukken:

```java
 for(int i = 0; i < urls.Length;i++)
{
    try
    {
        Uri uri = new Uri(urls[i]);
        string result = webClient.DownloadString(uri);
        Console.WriteLine($"{uri} gedownload. Dit is het resultaat {result}");
    }
    catch (Exception ex)
    {
        Console.WriteLine(ex.Message);
    }
}
```

Dit zal resulteren in:


```text
http://www.ziescherp.be gedownload!
Ongeldige URI: kan de Authority/Host niet parsen.
Ongeldige URI: de indeling van de URI kan niet worden bepaald.
```

Met andere woorden, indien een bepaalde url niet geldig is dan zal deze overgeslagen worden en gaat de methode verder naar de volgende. Op deze manier kunnen we alsnog alle urls trachten te downloaden.



### finally 
Soms zal je na een try-catch-blok ook nog een ``finally`` blok zien staan. Dit blok laat je toe om code uit te voeren die ALTIJD moet uitgevoerd worden, ongeacht of er een exception is opgetreden of niet. Je kan dit gebruiken om bijvoorbeeld er zeker van te zijn dat het bestand dat je wou uitlezen terug afgesloten wordt.

```java
try
{
    Uri uri = new Uri(urls[i]);
    string result = webClient.DownloadString(uri);
    Console.WriteLine($"{uri} gedownload. Dit is het resultaat {result}");
}
catch (Exception ex)
{
    Console.WriteLine(ex.Message);
}
finally
{
    //Plaats hier zaken die sowieso moeten gebeuren. 
}
```
