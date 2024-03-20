---
icon: material/arrow-decision-outline
---

# Flusso di controllo
## Indentazione

Prima ancora di iniziare a vedere gli elementi fondamentali che costituiscono un programma, è fondamentale capire il ruolo che l'indentazione gioca in Python. A differenza di altri linguaggi che utilizzano le parentesi o le graffe per definire i blocchi di codice, Python utilizza l'indentazione per organizzare e delimitare i blocchi di istruzioni. L'indentazione per convenzione è fatta con quattro spazi:

```python
def mia_funzione():
    for elemento in lista:
        # Operazioni all'interno del for loop
        if condizione:
            print("Condizione soddisfatta")
        else:
            print("Condizione non soddisfatta")
```

## Branching

Il **branching** è la possibilità di esecuzione condizionale del codice, vale a dire la possibilità di deviare l'esecuzione del codice verso percorsi alternativi:

```python
if condizione_1:
    print("Condizione 1 soddisfatta")
elif condizione_2:
    print("Condizione 1 non soddisfatta, ma condizione 2 soddisfatta")
else:
    print("Nessuna condizione soddisfatta")
```

Viene eseguito il blocco di codice corrispondente alla prima condizione che risulta vera. Se nessuna condizione è verificata allora è eseguito il blocco corrispondente alla clausola `else`. Ad esempio:

```python
età = 18
if età < 18:
    print("Minorenne")
elif età >= 18 and età < 65:
    print("Adulto")
else:
    print("Anziano")
```

Quando si deve assegnare condizionalmente un valore ad un nome in accordo ad una certa condizione si può abbreviare il codice usando l'**operatore ternario**.

```python
messaggio = "Buongiorno" if ora < 12 else "Buonasera"
print(messaggio)
```


## Looping

Il **looping** è la possibilità di eseguire ripetutamente uno stesso blocco di codice. I cicli `for` consentono di eseguire il codice per un dato numero di volte, mentre i cicli `while` consentono di ripetere l'esecuzione fino a che non si verifica una condizione.

```python
for number in [0, 1, 2, 3, 4]:
    print(number)

# Stesso risultato del ciclo precedente ma usando la funzione `range` che restituisce la collezione
# dei numeri da 0 al numero passato come argomento, escluso il numero stesso.
for i in range(5):
    print(number)

for lettera in "Python":
    print(lettera.upper())
```

Notare che non è necessario che la variabile `number` sia stata inizializzata in precedenza. È possibile iterare su qualsiasi sequenza, non necessariamente numerica.

```python
for x in "ciao!":
    print(x, end=" ")
```

Anche gli oggetti più complessi come le liste di liste possono essere iterati:

```python
liste_numeri = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for lista in liste_numeri:
    for numero in lista:
        print(numero)
```

Più in generale l'iterazione è possibile su qualsiasi **iterabile**, ossia qualsiasi oggetto che ha la capacità di restituire i suoi membri uno alla volta. Si può iterare su più indici, ad esempio per iterare su tutte le coppie chiave-valore di un dizionario (l'ordine non è rispettato perchè i dizionari non sono ordinati) .

```python
dic = {"A": 1, "B": 2}
for i, j in dic.items():
    print(i, j)
```

!!! tip "Variabili di iterazione"
    Notare come nell'esempio precedente si siano violate le convenzioni sui nomi di variabili per le variabili di iterazione `i` e `j` usate nel loop. Questa è una pratica comune, dato che le variabili in questione cessano di essere rilevanti una volta terminato il loop, dunque il fatto che abbiano nomi poco parlanti non influenza la chiarezza del codice che segue.

Si può anche iterare su più sequenze in contemporanea.

```python
people = ["Jonas", "Julio", "Mike", "Mez"]
ages = [25, 30, 31, 39]
for position, person in enumerate(people):
    age = ages[position]
    print(person, age)

for person, age in zip(people, ages):
    print(person, age)
```

Se si vuole eseguire ripetutamente un blocco di codice fino a che una condizione specificata rimane vera si usa invece un ciclo `while` .
Il ciclo seguente continua a stampare il valore di `numero` finché non diventa 0, decrementando `numero` di 1 ad ogni iterazione.

```python
numero = 5
while numero > 0:
    print(numero)
    numero -= 1
```

Un loop può essere seguito da una clausola `else` che viene eseguita solo se il loop è terminato normalmente (ossia se non è stato interrotto tramite un `break`).
Il ciclo seguente stampa i numeri 3, 2, 1 e poi "Raggiunto zero".

```python
numero = 3
while numero > 0:
    print(numero)
    numero -= 1
else:
    print("Raggiunto zero")
```

Si può arrestare forzatamente un loop tramite `break` , oppure interrompere l'iterazione attuale e saltare a quella successiva con `continue`.
In questo esempio, il numero 5 viene saltato a causa di `continue`, e il ciclo si interrompe quando `numero` è uguale a 3, quindi 3 non viene stampato.

```python
numero = 10
while numero > 0:
    numero -= 1
    if numero == 5:
        continue
    if numero == 3:
        break
    print(numero)
```

## Comprensioni di lista
Le **comprensioni di lista** (*list comprehensions*) sono un modo potente e conciso in Python per creare nuove collezioni (come liste, dizionari, insiemi) a partire da collezioni esistenti. Ad esempio, possiamo creare una lista con i quadrati dei numeri da 1 a 10:

```python
quadrati = [x**2 for x in range(1, 11)]
```

Nonostante il nome, le comprensioni di lista possono essere usate per creare collezioni di qualsiasi tipo, ad esempio possiamo creare un dizionario
che mappa i numeri dispari fino a 10 ai rispettivi quadrati.

```python
quadrati_dispari = {x: x**2 for x in range(1, 11) if x % 2 != 0}
```

Anche gli **insiemi** possono essere creati tramite comprensioni. Per esempio, possiamo generare un insieme dei resti della divisione per 5 di numeri da 1 a 10:

```python
resti = {x % 5 for x in range(1, 11)}
```

Le comprensioni sono uno degli strumenti più potenti di Python perché consentono di scrivere cicli in maniera estremamente coincisa.


## Bonus: Eccezioni

Le **eccezioni** in Python sono eventi che si verificano durante l'esecuzione del programma e che interrompono il normale flusso delle istruzioni. Quando si verifica un errore nel codice, Python genera un'eccezione. Questo può accadere per vari motivi, come un accesso a un indice di una lista che non esiste, la divisione per zero, o un errore di sintassi.

Le eccezioni sono importanti perché permettono ai programmatori di gestire gli errori in modo controllato e di prevenire il blocco o il comportamento imprevisto del programma. Python offre la possibilità di gestire le eccezioni attraverso i blocchi `try` e `except`.

```python
try:
    # Codice che potrebbe generare un'eccezione
    risultato = 10 / 0
except ZeroDivisionError:
    # Codice eseguito in caso di ZeroDivisionError
    print("Non è possibile dividere per zero")
```

Nell'esempio sopra, se il codice all'interno del blocco `try` causa un'eccezione `ZeroDivisionError`, il programma non si blocca, ma esegue il codice all'interno del blocco `except`.

È possibile gestire più tipi di eccezioni in un unico blocco `except` o avere più blocchi `except` per gestire diversi tipi di eccezioni.

```python
try:
    # Codice che potrebbe generare diverse eccezioni
    lista = [1, 2, 3]
    print(lista[3])
except IndexError:
    print("Indice non presente nella lista")
except Exception as e:
    print("Errore: ", e)
```

In questo esempio, se il codice nel blocco `try` genera un'eccezione `IndexError`, verrà eseguito il primo blocco `except`. Se si verifica un altro tipo di eccezione, verrà catturato dal secondo blocco `except`, che stampa un messaggio generico.

Infine, è possibile utilizzare anche i blocchi `else` e `finally` in combinazione con `try` e `except`. Il blocco `else` viene eseguito se non si verifica nessuna eccezione, mentre `finally` viene eseguito sempre, sia che si verifichi un'eccezione, sia che non si verifichi, utilizzato spesso per operazioni di pulizia, come la chiusura di file o connessioni a database.

```python
try:
    # Codice che potrebbe generare un'eccezione
    numero = int("abc")
except ValueError:
    print("Errore di conversione")
else:
    print("Nessuna eccezione")
finally:
    print("Esecuzione blocco finally")
```

La gestione delle eccezioni è un aspetto cruciale nella scrittura di codice robusto e resistente agli errori, specialmente in applicazioni complesse o che interagiscono con sistemi esterni dove i comportamenti imprevisti sono comuni.

!!! quote " "
    A software engineer walks into a bar. Orders a beer. Orders 0 beers. Orders 99999999999 beers. Orders a lizard. Orders -1 beers. Orders a ueicbksjdhd.

    First real customer walks in and asks where the bathroom is. The bar bursts into flames, killing everyone.

## Esercizi

### Esercizio 1
Riesci a capire cosa fa ciascun ciclo?

```python
for i in range(5):
    print(i)
    if i == 2:
        break
```

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

```python
for i in range(5):
    print(i)
else:
    print("Loop terminato normalmente")
```

??? info "Soluzione"
    - Il primo ciclo stampa i numeri da 0 a 2 e poi si interrompe a causa del break.
    - Il secondo ciclo salta il numero 2 grazie al continue e stampa gli altri numeri da 0 a 4.
    - Nel terzo ciclo, viene stampato ogni numero da 0 a 4, e poi, poiché il ciclo termina normalmente, viene stampato il messaggio.

### Esercizio 2
Scrivi un programma che trova il numero massimo in una lista di numeri. La lista può essere definita direttamente nel codice.
Non utilizzare funzioni predefinite.

Esempio di lista: `numeri = [3, 5, 7, 2, 8, 10, 1]`

??? info "Soluzione"
    ```python
    numeri = [3, 5, 7, 2, 8, 10, 1]
    numero_massimo = numeri[0]

    for numero in numeri:
        if numero > numero_massimo:
            numero_massimo = numero

    print(f"Il numero massimo nella lista è: {numero_massimo}")
    ```

### Esercizio 3
Scrivi un programma che conta quante vocali (a, e, i, o, u) ci sono nella stringa `"Ciao, benvenuto nel mondo della programmazione!"`.

??? info "Soluzione"
    ```python
    testo = "Ciao, benvenuto nel mondo della programmazione!"
    vocali = "aeiou"
    conteggio = 0

    for carattere in testo:
        if carattere.lower() in vocali:
            conteggio += 1

    print(f"Ci sono {conteggio} vocali nella stringa.")
    ```

### Bonus: Esercizio 4
Crea un semplice gioco che genera un numero casuale tra 1 e 10 e chiede all'utente di indovinarlo utilizzando la funzione `input()`. Il programma deve dare un feedback all'utente dopo ogni tentativo, indicando se il numero indovinato è troppo alto o troppo basso. Il gioco termina quando l'utente indovina il numero o dopo 3 tentativi.

!!! tip "Validazione degli input"
    La funzione `input()` è utilizzata per raccogliere l'input dell'utente. Quando chiami `input()`, il programma si ferma e attende che l'utente digiti qualcosa e prema invio. La stringa inserita dall'utente viene poi restituita dalla funzione e può essere convertita in un altro tipo di dato se necessario, ad esempio in un intero con `int()`. Ma come assicurarsi che l'utente abbia inserito un numero? Dobbiamo usare un blocco `except` che intercetti un eventuale `ValueError`.

??? info "Soluzione"
    ```python
    NUMERO_SEGRETO = 7  # Modificare per cambiare la soluzione
    tentativi = 0

    while tentativi < 3:
        try:
            guess = int(input("Indovina il numero (tra 1 e 10): "))
            tentativi += 1

            if guess == NUMERO_SEGRETO:
                print(f"Hai indovinato! Il numero era {NUMERO_SEGRETO}.")
                break
            elif guess < NUMERO_SEGRETO:
                print("Troppo basso!")
            else:
                print("Troppo alto!")
        except ValueError:
            print("Per favore, inserisci un numero valido.")

        if tentativi == 3:
            print(f"Hai finito i tentativi. Il numero era {NUMERO_SEGRETO}.")
    ```
