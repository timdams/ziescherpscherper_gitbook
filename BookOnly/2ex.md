## Oefeningen

### UNICODE-kunst

Genereer je naam in UNICODE-kunst met een van de vele online generators. Kan je deze in een console-applicatie visualiseren?

Of pittiger: Gebruik je kennis van het verschil tussen `Console.Write` en `Console.WriteLine`, alsook de werking van kleuren in console-applicaties, om je naam van kleur te voorzien. Zorg ervoor dat minstens 1 letter in een andere kleur is dan de andere.


### Systeeminformatie

Maak een applicatie die de belangrijkste computer-informatie (geheugen, etc) aan de gebruiker toont m.b.v. de ``Environment`` bibliotheek.
Zoals je ziet wordt het geheugen in bytes teruggegeven. Zorg ervoor dat het geheugen steeds in mega of gigabytes op het scherm wordt getoond.

Formateer de informatie met behulp van de $-notatie zodat deze deftig getoond worden in een tabel (inclusief mooie met UNICECODE getekende randen!) en de gebruiker snel de belangrijke informatie over z'n systeem te zien krijgt.

### Shell-starter 

``Process.Start`` laat je toe om vanuit je applicatie andere programma's op de computer te starten. Je kan de output van een ``Process.Start()`` programma naar je console scherm sturen. Dit vereist wat meer code. 

Volgend voorbeeld zal de output van het commando ``ipconfig /all`` op het scherm tonen:

```java
System.Diagnostics.Process process = new System.Diagnostics.Process();
process.StartInfo.FileName = "ipconfig";
process.StartInfo.Arguments = "/all"; 
process.StartInfo.UseShellExecute = false;
process.StartInfo.RedirectStandardOutput = true;
process.StartInfo.RedirectStandardError = true;
process.Start(); //start process

// Lees de output van het process
string output = process.StandardOutput.ReadToEnd(); //normale output
Console.WriteLine(output);
string err = process.StandardError.ReadToEnd(); //error output (indien die er is)
Console.WriteLine(err);
//Ga verder
Console.WriteLine("Klaar");
```


Maak enkele kleine C# programma's die bepaalde shell-commando's zullen uitvoeren, eventueel na input van de gebruiker.



Enkele nuttige shell-commando's in de netwerk-sfeer zijn bijvoorbeeld:


```text
hostname
arp -a
getmac
nslookup google.com
netstat
```

Andere toffe commando's kunnen zijn:


```text
chrome.exe timdams.com
notepad mytest.txt
```

Je kan ook een bestand openen door gewoon het volledige path naar het betand mee te geven aan ``Process.Start``. Het bestand zal dan geopend worden in de standaardapp die je voor dat soort bestandstype hebt ingesteld (bv. `docx` zal Word openen als dat op je computer staat):


```text
c:\Temp\mydocument.docx
```
