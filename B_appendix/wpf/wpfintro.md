# Windows Presentation Foundation (WPF)

In den beginnen bestond er  Windows Forms (kort *Winforms*). Nu nog steeds zal je in aardig wat bedrijven grafische, bureaubladapplicaties vinden die werden geschreven in Winforms. Als je als Windows-ontwikkelaar  in de nillies (2000-2010) grafische applicaties wilde maken dan deed je dat in Winforms. Het liet je toe om zogenaamde **Graphical User Interface** (GUI) applicaties te ontwikkelen in C#, VB en andere .NET talen. Het voorzag een hele hoop standaard *controls* om te gebruiken zoals knoppen (``Button``), tekstvelden (``TextBox`` en ``Label``), afbeeldingen (``Image``, ``Canvas``), etc. zonder dat je je als programmeur nog druk moest maken over de interne werking van een knop of combobox.

Hoe geliefkoosd deze .NET technologie ook was, ze raakte snel verouderd naarmate onze computers evolueerden en we grotere én kleinere schermen kochten. Er was nood aan bureaubladapplicaties die grafisch veel straffere dingen konden, zoals animaties, en die ook op gigantische HD en UHD (4K) schermen er nog steeds *crisp* uitzagen. 

Windows Presentation Foundation (WPF) was de oplossing. Het werd de opvolger van Winforms en is nog steeds de basis voor veel grafische .NET applicaties op je computer. Je huidige Visual Studio is bijvoorbeeld ook in WPF ontwikkeld. 

De belangrijkste verschillen met Winforms zijn:

* Betere scheiding tussen de grafische front-end code (in *xaml*, zie verder) en effectieve code-behind (in C#).
* Schaalbare user interfaces omdat WPF met vector-gebaseerde controls werkt.

## Xaml

