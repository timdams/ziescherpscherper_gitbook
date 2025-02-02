<!-- \frontmatter -->

# Welkom

{% hint style='danger' %}
Ben je een leerkracht middelbaar of hoger onderwijs? Gebruik je dit handboek in je lessen (of als voorbereiding er op)? Graag krijg ik meer inzicht op wie je bent en hoe je dit boek gebruikt. Vul daarom even deze korte enquête in:
[Hier zo!](https://forms.office.com/Pages/ResponsePage.aspx?id=PM_YMxQvwEia1l0oJVM2c4aMAk4NbYhHgqINmEfA8iBUQTc0NUhLN0Q1WTNGMjlSNllWRDRMQzlHTi4u)

Alvast bedankt!

PS Niet bang zijn, het boek blijft voor eeuwig en altijd gratis beschikbaar, ongeacht uw antwoorden :)
{% endhint %}

Je vraagt je misschien af waarom dit allemaal verteld wordt? Waarom wordt deze geschiedenisles gegeven? De reden is heel eenvoudig. Je gaat zeker geregeld zaken op het internet willen opzoeken tijdens het (leren) programmeren en zal dan ook vaker op artikels stuiten met de oude(re) naamgeving en dan mogelijks niet kunnen volgen. 


Zo, je hebt besloten om C# te leren? Je bent hier aan het juiste adres. Dit boek is ontstaan als handboek voor de opleidingen professionele bachelor elektronica-ict en toegepaste informatica van de AP Hogeschool. Ondertussen wordt het ook in tal van andere hogescholen en middelbare scholen gebruikt. Ik ga je op een laagdrempelige manier leren programmeren in C#, waarbij geen voorkennis vereist is.

Eerst zullen we de fundering leggen en zaken behandelen zoals variabelen, loops methoden en arrays. Vervolgens zal de wonderlijke wereld van het *object georiënteerd programmeren* uit de doeken gedaan worden.

Je vraagt je misschien af hoe up-to-date dit boek is? Wel, het is origineel samengesteld tijdens de lockdowns in 2020... Mmm, het jaar 2020 als kwaliteitslabel gebruiken is een beetje zoals zeggen dat je wijn maakt met rioolwater. Toen eind 2021 een nieuwe versie van Visual Studio verscheen werd het tijd om dit boek grondig te updaten. De versie die je nu in handen hebt werd geüpdatet in de zomer van 2024, na reeds een grote herziening in 2022.

Net zoals spreektalen, evolueert ook de programmeertaal C# constant. Terwijl ik dit schrijf zijn we aan versie 10.0 van C# en staat versie 11 in de startblokken. Bij iedere nieuwe C#-versie worden bepaalde concepten plots veel eenvoudiger of zelfs gewoon overbodig. Een goed programmeur moet natuurlijk zowel met de oude als de nieuwe constructies kunnen werken. 

Ik heb getracht een gezonde mix tussen oud en nieuw te zoeken, waarbij de nadruk ligt op maximale bruikbaarheid in je verdere professionele carrière. Je zal hier dus geen stoere, state-of-the-art C# innovaties terugvinden die enkel in heel specifieke projecten bruikbaar zijn. Integendeel. Ik hoop dat als je aan het laatste hoofdstuk bent, je een zodanige basis hebt, dat je ook zonder problemen in andere 'zustertalen' durft te duiken (zoals Java, C en C++, maar ook zelfs Python of JavaScript).

Dit boek ambieert niet om de volledige C#-taal en alles dat daar rond hangt aan te leren. Het boek daarentegen is gericht op eender wie die interesse heeft in de wondere wereld van programmeren, maar mogelijk nog nooit één letter code effectief heeft geprogrammeerd. Bepaalde concepten die ik te ingewikkeld acht voor een beginnende programmeur werden dan ook weg gelaten. Beschouw wat je gaat lezen dus maar als een *gateway drug* naar meer C#, meer programmeertalen en vooral meer programmeerplezier! U weze gewaarschuwd.


## Wat je kunt verwachten

Voor we verder gaan wil ik je wel even waarschuwen. Dit boek gaat uit van geen enkele kennis van programmeren, laat staan C#. Daarom beginnen we bij het prille begin. Verwacht echter niet dat je aan het einde van dit boek supercoole grafische applicaties of games kunt maken. Het is zelfs zo dat we hoegenaamd geen woord gaan reppen over "windows applicaties", met knoppen en menu's enz. 

Alles dat in dit boek gemaakt wordt zal uitgevoerd "in de console".  Die oeroude DOS-schermen - ook wel een *shell* genoemd - die je nu nog vaak in films ziet wanneer hackers proberen in een erg beveiligd systeem in te breken. Deze aanpak helpt je te focussen op de essentie van het probleem, zonder afgeleid te worden door visuele elementen.  


![De "console". Qua zwarte inkt-verspilling zal deze afbeelding de hoofdprijs winnen!](../assets/0_intro/introconsole.png)<!--{width=50%}-->


## Over de bronnen

Dit boek is het resultaat van bijna een decennium C# doceren aan de AP Hogeschool (eerst nog Hogeschool Antwerpen, dan Artesis Hogeschool, dan Artesis Plantijn Hogeschool, enz.). De eerste schrijfsels verschenen op een eigen gehoste blog ("Code van 1001 Nacht", die ondertussen ter ziele is gegaan) en vervolgens kreeg deze een iets strakkere, eenduidige vorm als gitbook cursus. 

Deze cursus, alsook een hele resem oefeningen en andere nuttige extra's kan je terugvinden op **ziescherp.be**. De inhoud van die cursus loopt integraal gelijk aan die van dit boek. Uiteraard is de kans bestaande dat er in de online versie ondertussen weer wat minder schrijffoutjes staan. 


Waarom deze korte historiek? Wel, de kans is bestaande dat er hier en daar flarden tekst, code voorbeelden, of oefeningen niet origineel de mijne zijn. Ik heb getracht zo goed mogelijk aan te geven wat van waar komt, maar als ik toch iets vergeten ben, aarzel dan niet om me er op te wijzen. 




## Benodigdheden

Alle codevoorbeelden in deze cursus kan je zelf (na)maken met de gratis **Visual Studio 2022 Community** editie die je kan downloaden op [visualstudio.microsoft.com](https://visualstudio.microsoft.com).

<!-- \newpage -->

## Dankwoord

Aardig wat mensen - grotendeels mijn eerstejaars studenten van de professionele bachelor Elektronica-ICT  en Toegepaste Informatica van de AP Hogeschool - hebben me met deze cursus geholpen. Hen allemaal afzonderlijk bedanken zou me een extra pagina kosten, en ik heb de meeste al nadrukkelijk bedankt in de vorige editie van dit boek. 

Een speciale dank nogmaals aan Maarten Wachters die de originele pixel-art van me maakte waar ik vervolgens enkele varianten op heb gemaakt.

Ook een bos bloemen voor collega's Olga Coutrin en Walter Van Hoof om de ondankbare taak op zich te nemen mijn vele dt-fouten uit de vorige editie te halen op nog geen week voor de deadline. Bedankt!

De trainers van Multimedi BV. die dit handboek ook gebruiken wil ik expliciet bedanken voor hun nuttige feedback op de eerste versie van dit boek, alsook om mij een extra reden te geven om dit boek in de eerste plaats uit te brengen.

Als laatste, in deze 2024 editie, een shoutout naar de leerkrachten van het middelbaar die sinds de laatste onderwijshervorming C# en OOP aan hun leerlingen mogen onderwijzen! 

![](../assets/me.png)

Veel lees-en programmeerplezier,

Tim Dams 
Zomer 2024
