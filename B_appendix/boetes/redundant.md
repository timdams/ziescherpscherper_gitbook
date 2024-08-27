##	Veel onnodige of redundante code (-3 punt max)

*(tot -3 punten)*

Los je de problemen té omslachtig op? Dat kan je tot maximum 3 punten op je totaalscore kosten. 

Enkele typische voorbeelden:

* Geen loops of methoden gebruiken wanneer je bepaalde code meerdere keren na elkaar moet uitvoeren.
* Identieke code op meerdere plekken (tip: ook hier zal een methode handig zijn).

### Uitgewerkte voorbeeld

```csharp
double loop1 = Casino(start, 10);
Console.WriteLine($"Als je 10 keer roulette speelt zou je eindkapitaal {loop1} zijn, dat is een verschil van {loop1-start}");

double loop2 = Casino(start, 100);
Console.WriteLine($"Als je 100 keer roulette speelt zou je eindkapitaal {loop2} zijn, dat is een verschil van {loop2 - start}");

double loop3 = Casino(start, 10000);
Console.WriteLine($"Als je 10000 keer roulette speelt zou je eindkapitaal {loop3} zijn, dat is een verschil van {loop3 - start}");

double loop4 = Casino(start, 1000000);
Console.WriteLine($"Als je 1000000 keer roulette speelt zou je eindkapitaal {loop4} zijn, dat is een verschil van {loop4 - start}");
```

Kan herschreven worden m.b.v. loops en een array:

```csharp

int[] prijzen ={10, 100, 10000, 1000000};

for(int i=0; i<prijzen.Length; i++)
{
    double winst = Casino(start, prijzen[i]);
    Console.WriteLine($"Als je 10 keer roulette speelt zou je eindkapitaal {winst} zijn, dat is een verschil van {winst-start}");
}
```