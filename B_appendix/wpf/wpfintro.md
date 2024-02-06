# Windows Presentation Foundation (WPF)

In den beginnen bestond er  Windows Forms (kort *Winforms*). Nu nog steeds zal je in aardig wat bedrijven grafische, bureaubladapplicaties vinden die werden geschreven in Winforms. Als je als Windows-ontwikkelaar  in de *nillies* (2000-2010) grafische applicaties wilde maken dan deed je dat in Winforms. Het liet je toe om zogenaamde **Graphical User Interface** (GUI) applicaties te ontwikkelen in C#, VB en andere .NET talen. Het voorzag een hele hoop standaard *controls* om te gebruiken zoals knoppen (``Button``), tekstvelden (``TextBox`` en ``Label``), afbeeldingen (``Image``, ``Canvas``), etc. zonder dat je je als programmeur nog druk moest maken over de interne werking van een knop of combobox.

Hoe geliefkoosd deze .NET technologie ook was, ze raakte snel verouderd naarmate onze computers evolueerden en we grotere én kleinere schermen kochten. Er was nood aan bureaubladapplicaties die grafisch veel straffere dingen konden, zoals animaties, en die ook op gigantische HD en UHD (4K) schermen er nog steeds *crisp* uitzagen. 

Windows Presentation Foundation (WPF) was de oplossing. Het werd de opvolger van Winforms en is nog steeds de basis voor veel grafische .NET applicaties op je computer. Je huidige Visual Studio is bijvoorbeeld ook in WPF ontwikkeld. 

De belangrijkste verschillen met Winforms zijn:

* Betere scheiding tussen de grafische front-end code (in *Xaml*, zie verder) en effectieve code-behind (in C#).
* Schaalbare user interfaces omdat WPF met vector-gebaseerde controls werkt.


## Is WPF nog relevant?

Alhoewel we in de praktijk niet zo vaak nog "pure WPF" op de markt zien verschijnen, zijn er toch meerdere goede argumenten om deze technologie in de vingers te krijgen, namelijk:

* De achterliggende "technologiestack"  (de combinatie  C# en xaml) wordt toegepast in meerdere moderne .NET frameworks waaronder .NET MAUI en UWP. Het grote voordeel bij WPF is dat deze laagdrempeliger is en dus de ideale opstap indien je van plan bent om te leren hoe moderne (crossplatform) grafische applicaties te ontwikkelen zoals met .NET MAUI.
* Het laat toe om snel krachtige bureaubladapplicaties te ontwikkelen zonder al te veel gedoe en je hoeft geen UX expert (*user experience*) te zijn. Stel dat je dus een handige console-applicatie hebt ontwikkeld, dan kan je daar snel een grafische front-end *overgooien* om zo een toegankelijkere app te krijgen. 

## Je eerste WPF applicatie!

Om een WPF-applicatie in Visual Studio te maken moeten we bij het projecttemplate uiteraard nu kiezen voor **WPF Application** tijdens het aanmaken van de solution (en project)

![Keuze van projecttype](../assets/wpf/wpfkeuze.png)

Je wordt nu echter door een heel ander beeld begroet dan dat je gewoon bent bij Console-applicaties. Waar is de C# code?! Wees gerust, hij is er nog, maar laten we eerst een kijkje nemen naar wat je nu te zien krijgt: de UI-designer en bijhorende XAML-code (via het menu Window->Reset Window layout klikken indien je niet hetzelfde beeld krijgt als hieronder)

![Klaar voor een eerste grafische applicatie! Spannend.](../assets/wpf/startvsbeeld.png)

In het bovenste gedeelte zien we een pre-render van hoe je finale grafische user interface er zal uitzien. Eronder zie je de effectieve *code* die resulteert in de UI die je ziet. Deze code lijkt erg hard op HTML en dat is niet toevallig, het is **XAML** en behoort tot dezelfde familie. Meer daarover later.

Aan de linkerzijde je een tabknop "Toolbox". Hier staan alle **controls** die je op je UI kan plaatsen. Kijk wat er gebeurt wanneer je vanuit de toolbox een element sleept naar de grafische prerender van de UI. Er gebeuren 2 zaken:

1. De control wordt getoond in de grafische render.
2. In de onderliggende xaml-code wordt de effectieve code geschreven.

Je kan nu je applicatie uitvoeren en je zal merken dat je applicatie er net zo uitziet zoals de prerender in VS. Uiteraard zal de applicatie nog niet veel doen, dat komt nog.

## Xaml

Zoals reeds verteld vereist het schrijven van grafische applicatie dat je naast C# ook een andere taal beheerst, xaml. We hebben echter ook net ontdekt dat zo te zien VS voor ons aardig wat xaml code kan schrijven, dus dat is mooi meegenomen.

Xaml staat voor *"eXtensible Application Markup Language"* en dus een zogenaamde *markup*-taal zoals ook HTML. Markup-talen zijn talen die beschrijven hoe tekst en beeld moet opgemaakt worden. Je kan met andere woorden beschrijven hoe de effectieve uitvoer van een bepaalde element moet zijn naar het scherm toe (vet, cursief, in het rood, etc.). Xaml doet voor grafische bureaubladapplicaties, wat HTML doet voor websites: het beschrijft de grafische gebruikers interface. 


## Code-behind

(hoe er geraken via VS)