## Installer maken van je applicatie

Je bent eindelijk klaar. Je hebt de ultieme applicatie gemaakt en bent zo fier als een gieter. Uiteraard wil je je creatie met de wereld delen. Maar hoe?! Hebben je *klanten* ook Visual Studio nodig? Moeten zij ook de .NET runtime hebben? En zo ja, de welke? Veel vragen, die je in principe zou moeten kunnen beantwoorden (tip, de antwoorden in volgorde zijn: "neen", "ja", "hangt af van de runtimeversie waar je naar compileert"). Maar het gelukkig ook veel eenvoudig.

Visual Studio heeft een ingebouwde manier om snel een installer voor je applicatie te maken. Deze installer zal er zelf voor zorgen dat de nodige zaken correct gedownload worden moest jouw applicatie dat nodig hebben om uitgevoerd te kunnen worden. Zo zal de installer zelf kijken of de vereiste .NET runtime op het doelsysteem staat, en indien niet zal de juiste versie eerst geïnstalleerd worden. Ook zal de installer ervoor zorgen dat de gebruiker je applicatie op een mooie manier kan verwijderen en dat je applicatie vanuit het startmenu kan gestart worden.


Maar hoe?! Stay tuned for more!