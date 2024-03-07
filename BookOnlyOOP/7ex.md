## Oefeningen

### Politiek
Maak een programma om de politieke situatie van een land te simuleren.

Maak volgende klassen:
* ``Land``
* ``Minister``
* ``President``

**``Minister``**

Een ``Minister`` heeft geen speciale eigenschappen. Enkel een auto-property om de ``Naam`` van de minister in bij te houden

**``President``**

Een ``President`` is een ``Minister`` maar met 1 extra property met private setter: hij heeft een teller die start op 4 alsook een methode `JaarVerder`die deze teller met 1 iedere aanroep verlaagt.

**``Land``**

* Een ``Land`` heeft 0 of 1 ``President`` (of koning, dictator kies zelf).
* Een ``Land`` heeft 0 of 1 "eerste minister" (m.b.v. een ``eersteMinister`` instantievariabele).
* Een ``Land`` heeft 0 tot 4 ministers (via een ``List<Minister>``).

Al deze compositieobjecten zijn private.
Een land heeft volgende publieke methoden:

**``MaakRegering``**

Deze methode aanvaardt volgende parameters:
  
1. 1 ``President`` object die aan de private president variabele wordt toegekend.
  
2. Een ``List<Minister>`` object waarin tussen de 1 tot 5 ministers in staan: de eerste minister in de lijst wordt toegewezen aan de ``eersteMinister`` instantievariabele. De overige ministers in de lijst worden aan de private lijst van ministers toegewezen.

Deze methode zal enkel iets doen indien er geen president in het land is (``null``). Indien er reeds een regering is dan zal er een foutboodschap verschijnen.

**``JaarVerder``**

Deze methode aanroepen zal de ``JaarVerder`` aanroepen op de president indien deze er is (en dus niet ``null`` is). Deze methode controleert ook of de teller van de president na deze aanroep op 0 staat. Als dat het geval is dan worden alle ministers en president in het land op ``null`` gezet.

#### Eindfase

Controleer je klasse Land door enkele ministers en een president te maken en deze in een object van het type Land via ``MaakRegering`` door te geven. Test dan wat er gebeurt indien je enkele malen ``JaarVerder`` op het land aanroept.
    

### Moederbord

Maak een klasse ``Moederbord`` die een, je raadt het nooit, moederbord van één computer voorstelt. Kies een van de vele moederborden die je online vindt en bekijk uit welke delen een moederbord bestaat (*heeft een*).

Maak voor ieder deel een aparte klasse. Voorzie vervolgens via compositie de nodige objecten in je moederbord. Denk er aan dat je bijvoorbeeld 2 (of 4) RAM-slots hebt en dus hier ofwel een array moet voorzien van het type ``List<RAM>``, oftewel twee aparte delen ``RAMSlot1`` en ``RAMSlot2``.

Maak een methode ``TestMoederbord`` in de klasse ``Moederbord``. Wanneer je deze aanroept zal deze weergeven welke onderdelen nog leeg zijn (``==null``).

Voorzie een default constructor die alle datavelden initialiseert.

Iedere module moet via een property langs buiten ingesteld worden (beeld je in dat je effectief een moederbord in elkaar knutselt):

```java
Moederbord Z390E_GAMING = new Moederbord();
Z390E_GAMING.AGP= new AGPSlot("GeForceRTX2080");
Z390E_GAMING.CPU= new CPUSlot("IntelCorei9_9900K");
//enz.
```

Kan je zelf een computer samenstellen door enkele objecten van verschillende types aan te maken en deze aan je moederbord-object toe te wijzen? 

