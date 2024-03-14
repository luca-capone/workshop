---
icon: material/view-list-outline
---

# Collezioni

## Ordine e mutabilità
Le collezioni sono strutture dati che servono a contenere più oggetti al loro interno. Si distinguono in **mutabili** ed **immutabili**, a seconda che possano essere modificate dopo la loro creazione o meno. Una sequenza può essere ordinata o non avere un ordine.

La tabella sottostante riassume le proprietà di ogni tipo di collezione:

| tipo          | mutabile | ordinata  | duplicati | struttura |
|---------------|:--------:|:---------:|:---------:|:---------:|
| dizionario    | sì       | no | no        | `{a:m, b:n}`   |
| tupla       | no       | sì        | sì        | `(a, b)`  |
| lista         | sì       | sì        | sì        | `[a, b]`  |
| insieme           | no       | no        | no        | `{a, b}`  |
| stringa       | no       | sì        | sì        | `ciao`    |

Ecco alcuni esempi di collezioni:

```python
# Lista
lista_spesa = ["pane", "latte", "uova"]

# Dizionario
info_utente = {"nome": "Luca", "età": 32, "email": "luca@example.com"}

# Insieme
insieme_numeri = {1, 2, 3, 4, 5}
```

## Accesso agli elementi

In Python, l'accesso agli elementi di una collezione varia a seconda del tipo di collezione. I tipi di collezione principali in Python includono liste, tuple, dizionari e insiemi.

### Liste e Tuple

**Liste** e **tuple** sono collezioni ordinate, il che significa che ogni elemento ha un indice basato sulla sua posizione. Gli indici partono da `0` per il primo elemento, `1` per il secondo, e così via.

Esempio di accesso a una lista:

```python
lista = ["mela", "banana", "ciliegia"]
print(lista[0])  # stampa 'mela'
print(lista[1])  # stampa 'banana'
print(lista[-1])  # stampa 'ciliegia', -1 indica l'ultimo elemento
```

Esempio di accesso a una tupla:

```python
tupla = ("lunedì", "martedì", "mercoledì")
print(tupla[0])  # stampa 'lunedì'
```

### Dizionari

I **dizionari** in Python sono collezioni non ordinate di coppie chiave-valore. L'accesso agli elementi di un dizionario avviene tramite le chiavi:

```python
dizionario = {"nome": "Luca", "età": 30}
print(dizionario["nome"])  # stampa 'Luca'
```

Se si tenta di accedere a una chiave inesistente, Python solleverà un'eccezione `KeyError`. Per evitare questo, si può usare il metodo `get`, che restituisce `None` (o un valore predefinito) se la chiave non esiste.

```python
print(dizionario.get("professione", "Non specificato"))
```

### Insiemi

Gli **insiemi** (*sets*) sono collezioni non ordinate e non indicizzate. Non si può accedere agli elementi di un insieme tramite un indice o una chiave. Tuttavia, è possibile iterare su di essi o verificare se un elemento esiste all'interno dell'insieme.

Esempio di iterazione su un insieme:

```python
insieme = {1, 2, 3}
for numero in insieme:
    print(numero)
```

Verificare la presenza di un elemento:

```python
if 2 in insieme:
    print("2 è presente nell'insieme")
```

### Slicing
Lo slicing è una caratteristica in Python che permette di accedere a una sotto-sequenza da una sequenza come una lista, una tupla o una stringa. Lo slicing si effettua utilizzando la sintassi sequenza[inizio:fine:passo], dove inizio è l'indice iniziale (incluso), fine è l'indice finale (escluso), e passo è il numero di elementi da saltare.

```python
# Liste
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slicing di base
sottolista = lista[2:5]  # [2, 3, 4]

# Slicing con passo
sottolista_con_passo = lista[1:8:2]  # [1, 3, 5, 7]

# Slicing negativo
sottolista_negativa = lista[-5:-2]  # [5, 6, 7]

# Slicing con indice di inizio o fine omesso
inizio_omesso = lista[:4]  # [0, 1, 2, 3]
fine_omessa = lista[6:]  # [6, 7, 8, 9]

# Stringhe
stringa = "Python Programming"

# Slicing di base su una stringa
sottostringa = stringa[7:18]  # "Programming"

# Slicing con passo su una stringa
sottostringa_con_passo = stringa[0:6:2]  # "Pto"

# Tuple
tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Slicing di base su una tupla
sottotupla = tupla[3:7]  # (3, 4, 5, 6)

# Slicing inverso su una tupla
sottotupla_inversa = tupla[::-1]  # (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
```


## Continuazione di linea

Quando si scrive del codice lungo, è possibile **continuare una linea** utilizzando il carattere di **continuazione** `\` alla fine della linea da spezzare. Tuttavia, all'interno di parentesi (tonde, quadre o graffe), Python consente la continuazione automatica senza la necessità di utilizzare il carattere `\`, semplificando la scrittura di codice su più righe senza compromettere la leggibilità.

```python
lunga_stringa = (
    "Questa è una lunga stringa che possiamo "
    "continuare su più righe utilizzando il carattere di continuazione."
)

lunga_lista = [
    "elemento1",
    "elemento2",
    "elemento3",
    "elemento4",
    "elemento5",
]
```

## Esercizi

### Esercizio 1

Crea una tupla contenente i mesi dell'anno e un insieme contenente i giorni della settimana.

??? info "Soluzione"
    ```python
    # Tupla dei mesi
    mesi = (
        "gennaio",
        "febbraio",
        "marzo",
        "aprile",
        "maggio",
        "giugno",
        "luglio",
        "agosto",
        "settembre",
        "ottobre",
        "novembre",
        "dicembre",
    )

    # Insieme dei giorni
    giorni = {"lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"}
    ```

### Esercizio 2

Dato il seguente dizionario e lista, accedi a specifici elementi come indicato:

```python
# Dizionario
studente = {"nome": "Giovanni", "età": 21, "corso": "Informatica"}

# Lista
numeri = [10, 20, 30, 40, 50]

# Accesso agli elementi:
# 1. Stampa l'età dello studente dal dizionario
# 2. Stampa il terzo elemento della lista numeri
```

??? info "Soluzione"
    ```python
    # Soluzione 1
    print(studente["età"])

    # Soluzione 2
    print(numeri[2])
    ```

### Esercizio 3

Stampa il penultimo carattere della stringa `"Python"`.

??? info "Soluzione"
    ```python
    parola = "Python"
    print(parola[-2])  # Stampa 'o'
    ```

### Esercizio 4

Crea una lista contenente i primi cinque numeri pari e usa lo slicing per stampare gli ultimi tre elementi.

??? info "Soluzione"
    ```python
    numeri_pari = [2, 4, 6, 8, 10]
    print(numeri_pari[-3:])  # Stampa [6, 8, 10]
    ```

### Esercizio 5

Dato il dizionario `{"Italia": "Roma", "Francia": "Parigi", "Germania": "Berlino"}`, accedi al valore associato alla chiave `"Francia"`.

??? info "Soluzione"
    ```python
    capitali = {"Italia": "Roma", "Francia": "Parigi", "Germania": "Berlino"}
    print(capitali["Francia"])  # Stampa 'Parigi'
    ```

### Esercizio 6

Dato l'insieme `{1, 3, 5, 7, 9}`, verifica se il numero `4` è presente nell'insieme.

??? info "Soluzione"
    ```python
    numeri = {1, 3, 5, 7, 9}
    print(4 in numeri)  # Stampa False
    ```
