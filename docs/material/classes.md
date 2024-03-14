---
icon: material/code-block-parentheses
---

# Classi
## Programmazione Orientata agli Oggetti

Python è un linguaggio di programmazione che supporta la **programmazione orientata agli oggetti** (object oriented programming, **OOP**). Per capire questo concetto, immaginate un oggetto come una scatola che contiene informazioni e strumenti. Le informazioni sono chiamate **attributi**, mentre gli strumenti sono le **funzioni** o **metodi**.

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

## Esercizi

### Esercizio 1
Definisci una classe `Auto` con due attributi di istanza, `marca` e `modello`. Aggiungi un metodo `mostra_info` che stampi marca e modello dell'auto.

??? info "Soluzione"
    ```python
    class Auto:
        def __init__(self, marca, modello):
            self.marca = marca
            self.modello = modello

        def mostra_info(self):
            print(f"Marca: {self.marca}, Modello: {self.modello}")


    mia_auto = Auto("Fiat", "500")
    mia_auto.mostra_info()  # Output: Marca: Fiat, Modello: 500
    ```

### Esercizio 2
Crea una classe `Libro` con gli attributi `titolo` e `autore` e un metodo `get_dettagli` che restituisca una stringa con titolo e autore del libro.

??? info "Soluzione"
    ```python
    class Libro:
        def __init__(self, titolo, autore):
            self.titolo = titolo
            self.autore = autore

        def get_dettagli(self):
            return f"Titolo: {self.titolo}, Autore: {self.autore}"


    mio_libro = Libro("Il Signore degli Anelli", "J.R.R. Tolkien")
    print(
        mio_libro.get_dettagli()
    )  # Output: Titolo: Il Signore degli Anelli, Autore: J.R.R. Tolkien
    ```

### Esercizio 3
Definisci una classe `Punto` con due attributi, `x` e `y`, rappresentanti le coordinate in uno spazio bidimensionale. Aggiungi un metodo `mostra` che stampi le coordinate del punto.

??? info "Soluzione"
    ```python
    class Punto:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def mostra(self):
            print(f"Punto({self.x}, {self.y})")


    punto = Punto(5, 10)
    punto.mostra()  # Output: Punto(5, 10)
    ```

### Esercizio 4
Crea una classe `Contatore` con un attributo di classe `count` inizializzato a 0. Aggiungi un metodo `incrementa` che aumenti `count` di 1 ogni volta che viene chiamato.

??? info "Soluzione"
    ```python
    class Contatore:
        count = 0

        def incrementa(self):
            self.count += 1


    Contatore.incrementa()
    Contatore.incrementa()
    print(Contatore.count)  # Output: 2
    ```


### Esercizio 5
Definisci una classe `Cerchio` con l'attributo di istanza `raggio`. Aggiungi metodi per calcolare l'area e la circonferenza del cerchio.

??? info "Soluzione"
    ```python
    import math


    class Cerchio:
        def __init__(self, raggio):
            self.raggio = raggio

        def area(self):
            return math.pi * self.raggio**2

        def circonferenza(self):
            return 2 * math.pi * self.raggio


    cerchio = Cerchio(3)
    print(f"Area: {cerchio.area()}")
    print(f"Circonferenza: {cerchio.circonferenza()}")
    ```

### Esercizio 6
Crea una classe `Banca` con due attributi di istanza: `nome` e `bilancio`. Implementa i metodi `deposita` e `preleva` per modificare il bilancio e un metodo `mostra_bilancio` per visualizzare il bilancio attuale.

??? info "Soluzione"
    ```python
    class Banca:
        def __init__(self, nome, bilancio):
            self.nome = nome
            self.bilancio = bilancio

        def deposita(self, importo):
            self.bilancio += importo

        def preleva(self, importo):
            if importo > self.bilancio:
                print("Fondi insufficienti")
            else:
                self.bilancio -= importo

        def mostra_bilancio(self):
            print(f"Bilancio attuale: {self.bilancio}")


    conto = Banca("Luca", 1000)
    conto.deposita(500)
    conto.mostra_bilancio()  # Output: Bilancio attuale: 1500
    conto.preleva(200)
    conto.mostra_bilancio()  # Output: Bilancio attuale: 1300
    ```

### Esercizio 7
Definisci una classe `Animale` con un metodo `emetti_suono`. Crea due sottoclassi, `Cane` e `Gatto`, che ereditino da `Animale` e ognuna con una propria implementazione di `emetti_suono`.

??? info "Soluzione"
    ```python
    class Animale:
        def emetti_suono(self):
            pass


    class Cane(Animale):
        def emetti_suono(self):
            return "Bau"


    class Gatto(Animale):
        def emetti_suono(self):
            return "Miao"


    cane = Cane()
    gatto = Gatto()
    print(cane.emetti_suono())  # Output: Bau
    print(gatto.emetti_suono())  # Output: Miao
    ```

### Esercizio 8
Crea una classe `Frazione` che rappresenti una frazione matematica. La classe deve avere due attributi, `numeratore` e `denominatore`. Aggiungi un metodo `riduci` che riduca la frazione ai minimi termini.

??? info "Soluzione"
    ```python
    def mcd(a, b):
        while b:
            a, b = b, a % b
        return a


    class Frazione:
        def __init__(self, numeratore, denominatore):
            self.numeratore = numeratore
            self.denominatore = denominatore

        def riduci(self):
            divisore = mcd(self.numeratore, self.denominatore)
            self.numeratore //= divisore
            self.denominatore //= divisore

        def __str__(self):
            return f"{self.numeratore}/{self.denominatore}"


    frazione = Frazione(150, 100)
    frazione.riduci()
    print(frazione)  # Output: 3/2
    ```
