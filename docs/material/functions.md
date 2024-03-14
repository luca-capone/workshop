# Funzioni

Una **funzione** è un blocco di codice che viene eseguito solo quando viene chiamato. Le funzioni sono utili per scomporre compiti complessi in parti più piccole e gestibili, rendendo il codice più organizzato, riutilizzabile e più facile da testare.

## Definizione e Chiamata

Per definire una funzione in Python, si utilizza la parola chiave `def`, seguita dal nome della funzione e una coppia di parentesi. All'interno delle parentesi, si possono definire i parametri (o argomenti) che la funzione può accettare.

```python
def saluta(nome):
    print(f"Ciao, {nome}!")
```

Per chiamare una funzione, si utilizza il nome della funzione seguito dalle parentesi contenenti eventuali argomenti necessari.

```python
saluta("Luca")  # Output: Ciao, Luca!
```

## Valori di ritorno

Le funzioni possono anche restituire valori. Per farlo, si utilizza la parola chiave `return`. Il valore dopo `return` sarà il risultato della funzione.

```python
def somma(a, b):
    return a + b


risultato = somma(5, 3)  # risultato è 8
```

## Passare argomenti

Passare un argomento alla funzione significa sostanzialmente assegnare un nome locale ad un oggetto. Qui, `x` è un oggetto immutabile (un intero). Quando passiamo `x` alla funzione `mostra_valore`, `a` diventa semplicemente un altro nome per lo stesso valore a cui `x` fa riferimento, cioè 10. Tuttavia, qualsiasi modifica a `a` all'interno della funzione non influenzerà `x`.

```python
def mostra_valore(a):
    print("Valore all'interno della funzione:", a)


x = 10
mostra_valore(x)  # Output: Valore all'interno della funzione: 10
```

Possiamo verificare che quanto detto sia vero usando l'operatore `is`:

```python
def ritorna_valore(a):
    return a


x = 10
y = ritorna_valore(x)

print(y is x)  # True
```

Ora, osserviamo cosa accade quando passiamo un oggetto mutabile, come una lista:

```python
lista = [1, 2, 3]


def modifica_lista(l):
    l[0] = 99
    print("Lista all'interno della funzione:", l)


modifica_lista(lista)
print("Lista dopo la chiamata della funzione:", lista)
```

Output:

```
Lista all'interno della funzione: [99, 2, 3]
Lista dopo la chiamata della funzione: [99, 2, 3]
```

In questo esempio, `lista` è una lista (un oggetto mutabile). Quando passiamo `lista` alla funzione `modifica_lista`, il parametro `l` all'interno della funzione punta allo stesso oggetto a cui punta `lista`. Pertanto, qualsiasi modifica fatta a `l` (come `l[0] = 99`) si rifletterà direttamente su `lista` nel contesto globale.

Questo comportamento sottolinea l'importanza di essere consapevoli del tipo di oggetti (mutabili vs. immutabili) quando si lavora con funzioni in Python, in quanto ciò determina se le modifiche all'interno della funzione avranno effetti sulle variabili nel contesto esterno.

## Tipi di Argomenti

Ci sono diverse modalità di passaggio degli argomenti:

1. **Argomenti Posizionali**: Il valore di ogni argomento è basato sulla sua posizione.
2. **Argomenti con Parola Chiave (Keyword Arguments)**: È possibile passare argomenti utilizzando il nome del parametro, rendendo l'ordine degli argomenti irrilevante.

    ```python
    def descrivi_animali(tipo, nome):
        print(f"Tipo: {tipo}, Nome: {nome}")


    descrivi_animali(nome="Fido", tipo="Cane")  # L'ordine degli argomenti non conta
    ```

3. **Argomenti Predefiniti**: Possiamo assegnare valori predefiniti ai parametri. Se un argomento per quel parametro non viene fornito nella chiamata, verrà usato il valore predefinito.

    ```python
    def descrivi_libro(titolo, autore="Sconosciuto"):
        print(f"Libro: {titolo}, Autore: {autore}")


    descrivi_libro("Il Grande Gatsby")  # Autore sarà "Sconosciuto"
    ```

4. **Argomenti Variadici**: A volte non sappiamo in anticipo quanti argomenti verranno passati alla funzione. In questi casi, usiamo *args (per liste di argomenti) e **kwargs (per dizionari di argomenti).

    ```python
    def somma(*numeri):
        return sum(numeri)


    print(somma(1, 2, 3, 4))  # Possiamo passare quanti numeri vogliamo
    ```

## Esercizi

### Esercizio 1
Scrivi una funzione chiamata `doppio` che prenda un numero come argomento e restituisca il suo doppio.

??? info "Soluzione"
     ```python
     def doppio(numero):
         return numero * 2


     # Esempio di chiamata della funzione
     print(doppio(4))  # Output: 8
     ```

### Esercizio 2
Crea una funzione `saluta_mondo` che non accetta argomenti e stampa semplicemente "Ciao Mondo!".

??? info "Soluzione"
    ```python
    def saluta_mondo():
        print("Ciao Mondo!")


    saluta_mondo()  # Output: Ciao Mondo!
    ```

### Esercizio 3
Definisci una funzione `massimo` che prenda due numeri come argomenti e restituisca il maggiore dei due.

??? info "Soluzione"
    ```python
    def massimo(a, b):
        return a if a > b else b


    print(massimo(3, 7))  # Output: 7
    ```

### Esercizio 4
Scrivi una funzione `presentati` che prenda due argomenti, nome e cognome, e stampi "Mi chiamo [nome] [cognome]".

??? info "Soluzione"
    ```python
    def presentati(nome, cognome):
        print(f"Mi chiamo {nome} {cognome}")


    presentati("Mario", "Rossi")  # Output: Mi chiamo Mario Rossi
    ```

### Esercizio 5
Crea una funzione `media` che prenda un numero arbitrario di valori numerici e restituisca la loro media. Usa gli argomenti variadici.

??? info "Soluzione"
    ```python
    def media(*numeri):
        return sum(numeri) / len(numeri) if numeri else 0


    print(media(1, 2, 3, 4, 5))  # Output: 3.0
    ```

### Esercizio 6
Definisci una funzione `saluta_opzionale` che accetti un nome come argomento e un argomento opzionale `messaggio`, con valore predefinito "Ciao". La funzione deve stampare "[messaggio], [nome]!".

??? info "Soluzione"
    ```python
    def saluta_opzionale(nome, messaggio="Ciao"):
        print(f"{messaggio}, {nome}!")


    saluta_opzionale("Luca")  # Output: Ciao, Luca!
    saluta_opzionale("Luca", "Benvenuto")  # Output: Benvenuto, Luca!
    ```

### Esercizio 7
Scrivi una funzione `conta_vocali` che prenda una stringa come argomento e restituisca il numero totale di vocali (sia maiuscole che minuscole) in quella stringa.

??? info "Soluzione"
    ```python
    def conta_vocali(testo):
        vocali = "aeiouAEIOU"
        return sum(1 for lettera in testo if lettera in vocali)


    print(conta_vocali("Ciao Mondo"))  # Output: 5
    ```

### Esercizio 8
Crea una funzione `e_primo` che determini se un numero è primo o meno. La funzione prende un numero intero come input e restituisce `True` se il numero è primo, altrimenti `False`.

??? info "Soluzione"
    ```python
    def e_primo(numero):
        if numero <= 1:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True


    print(e_primo(11))  # Output: True
    print(e_primo(4))  # Output: False
    ```

### Esercizio 9
Scrivi una funzione `cifra_numeri` che prenda una stringa come input e sostituisca ogni cifra numerica (0-9) nella stringa con il corrispondente numero in parole. Per esempio, "ho 2 gatti e 1 cane" diventa "ho due gatti e uno cane".

??? info "Soluzione"
    ```python
    def cifra_numeri(testo):
        numeri_parole = [
            "zero",
            "uno",
            "due",
            "tre",
            "quattro",
            "cinque",
            "sei",
            "sette",
            "otto",
            "nove",
        ]
        return "".join(numeri_parole[int(c)] if c.isdigit() else c for c in testo)


    print(cifra_numeri("ho 2 gatti e 1 cane"))  # Output: ho due gatti e uno cane
    ```

### Esercizio 10
Crea una funzione `frequenza_parole` che prenda una stringa come input e restituisca un dizionario con ogni parola unica nella stringa come chiave e il numero di volte in cui appare quella parola come valore. Assume che le parole siano separate da spazi e che la punteggiatura non sia importante.

??? info "Soluzione"
    ```python
    def frequenza_parole(testo):
        parole = testo.lower().split()
        frequenze = {}
        for parola in parole:
            frequenze[parola] = frequenze.get(parola, 0) + 1
        return frequenze


    print(frequenza_parole("Ciao mondo ciao mondo"))  # Output: {'ciao': 2, 'mondo': 2}
    ```
