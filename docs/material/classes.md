# Classi
## Programmazione Orientata agli Oggetti

Python è un linguaggio di programmazione che supporta la **programmazione orientata agli oggetti** (**o**bject **o**riented **p**rogramming, **OOP**). Per capire questo concetto, immaginate un oggetto come una scatola che contiene informazioni e strumenti. Le informazioni sono chiamate **attributi**, mentre gli strumenti sono le **funzioni** o **metodi**.

Una classe è come un **modello** (*template*) per creare oggetti. Per definire una classe, si utilizza la parola chiave `class`, seguita dal nome della classe e due punti. All'interno della classe, si definiscono le variabili ed i metodi che appartengono alla classe.

```python
class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def mostra_info(self):
        print(f"Nome: {self.nome}, Età: {self.eta}")
```

Per creare un oggetto della classe, si chiama il nome della classe con i parametri definiti nel metodo `__init__` (il costruttore della classe).

```python
persona1 = Persona("Luca", 32)
persona1.mostra_info()  # Output: Nome: Luca, Età: 32
```

Le classi sono, a loro volta, oggetti e sono istanze di `type`. Ogni istanza della classe eredita attributi e metodi della classe. I metodi possono agire sulla specifica istanza tramite l'argomento speciale `self`.

```python
class Square:
    # `side` è un attributo di `Square`
    side = 8

    # `area` è un metodo di `Square`
    def area(self):
        return self.side**2


sq = Square()
isinstance(sq, Square)
print(sq.area())
print(Square.area(sq))
```

## Attributi e Metodi

Un oggetto può essere qualcosa di semplice come un numero o una stringa, o più complesso come una data o un file. Ogni oggetto ha:

1. **attributi**: Sono come le caratteristiche o le proprietà dell'oggetto. Per esempio, in un oggetto che rappresenta una data, gli attributi potrebbero essere il giorno, il mese e l'anno.
2. **metodi**: Sono come le azioni che l'oggetto può eseguire. Se pensate a un oggetto che rappresenta un file, un metodo potrebbe essere l'apertura o la chiusura del file.

Una variabile definita all'interno di un metodo è propria della singola istanza, mentre una variabile definita al di fuori del metodo è comune a tutte le istanze di quella classe. Si parla quindi di **variabili di classe** e **variabili di istanza**.

```python
class MyClass:
    # Variabile di classe
    z = 4

    def __init__(self, x, y):
        # Variabili di istanza
        self.x = x
        self.y = y
```

## Identità

Ogni oggetto in Python ha un identificativo unico, un tipo e vive in uno **spazio dei nomi**. Lo spazio dei nomi è come un grande elenco che tiene traccia di tutti gli oggetti e dei loro nomi. L'operatore `.` è usato per accedere agli attributi e ai metodi degli oggetti, permettendoci di "navigare" nello spazio dei nomi.

Quando assegniamo un valore a una variabile, in realtà stiamo collegando un nome a un oggetto. Se cambiamo il valore della variabile, stiamo collegando quel nome a un nuovo oggetto. Possiamo vedere questo attraverso la funzione `id()`, che mostra l'identificativo unico di un oggetto.

```python
x = 2
print(id(x))  # Mostra l'ID di x
x = 3
print(id(x))  # Mostra un nuovo ID perché x ora si riferisce a un oggetto diverso
```

## Confronto tra oggetti

Quando confrontiamo due oggetti, possiamo usare `==` per vedere se hanno lo stesso valore o `is` per vedere se sono lo stesso oggetto (ovvero hanno lo stesso identificativo).

```python
a = 1000
b = 1000
print(a == b)  # True, perché i valori sono uguali
print(a is b)  # False, perché sono due oggetti separati

a = b
print(a == b)  # True, i valori sono uguali
print(a is b)  # True, ora a e b si riferiscono allo stesso oggetto
```

## Ereditarietà

Le classi possono ereditare proprietà e metodi da altre classi. Questo concetto è noto come **ereditarietà** e aiuta a ridurre la duplicazione del codice.

```python
class Studente(Persona):
    def __init__(self, nome, eta, anno_di_studio):
        super().__init__(nome, eta)
        self.anno_di_studio = anno_di_studio

    def mostra_info_studente(self):
        print(
            f"Nome: {self.nome}, Età: {self.eta}, Anno di Studio: {self.anno_di_studio}"
        )
```

In questo esempio, la classe `Studente` eredita da `Persona` e aggiunge ulteriori funzionalità.
