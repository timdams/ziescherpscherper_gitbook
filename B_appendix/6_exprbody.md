## Expression bodied members

Wanneer je methoden, constructors of properties schrijft waar **exact 1 expressie** (*1 lijn code* die een resultaat teruggeeft) nodig is dan kan je gebruik maken van de **expression bodied member syntax** (EBM). Deze is van de vorm:


```text
member => expression
```

Dankzij EBM kan je veel kortere code schrijven.

We tonen telkens een voorbeeld hoe deze origineel is en hoe deze naar EBM syntax kan omgezet worden.

### Methoden en EBM

Origineel:

```java
public void ToonGeboortejaar(int geboortejaarIn)
{
    Console.WriteLine(geboortejaarIn);
}
```

Met EBM:

```java
public void ToonGeboortejaar(int geboortejaarIn)
                     => Console.WriteLine(geboortejaarIn);
```

Nog een voorbeeld, nu met een return. Merk op dat we return niet moeten schrijven:

```java
public int GeefGewicht()
{
    return 4 * 34;
}
```

Met EBM:


```java
public int GeefGewicht() => 4 * 34;
```



### Constructors en EBM
Ook constructors die maar 1 expressie bevatten kunnen korter nu. Origineel:
```java
class Student
{
    public int Geboortejaar {get;set;}
    public Student(int geboorteJaarIn)
    {
        Geboortejaar = geboorteJaarIn;
    }
}
```

Met EBM wordt dit:
```java
class Student
{
    public int Geboortejaar {get;set;}
    public Student(int geboorteJaarIn) => Geboortejaar = geboorteJaarIn;
}
```

### Full Properties met EBM
Properties worden een soort mengeling tussen full en auto-properties:

```java
private int name;
public int Name
{
    get => name;
    set => name = value;
}
```


### Read-only properties met EBM
Bij read-only properties hoeft het ``get`` keyword zelfs niet meer getypt te worden bij EBM:

```java
private int name;
public int Name => name;
```

{% hint style='tip' %}
Uiteraard had voorgaande zelfs nog korter geweest met behulp van een auto-property.
{% endhint %}
