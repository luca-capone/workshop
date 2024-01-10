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

Viene eseguito il blocco di codice corrispondente alla prima condizione che risulta vera. Se nessuna condizione è verificata allora è eseguito il blocco corrispondente alla clausola `else`.

Quando si deve assegnare condizionalmente un valore ad un nome in accordo ad una certa condizione si può abbreviare il codice usando l'**operatore ternario**.

```python
x = 1 if condizione else 0
```

## Looping

Il **looping** è la possibilità di eseguire ripetutamente uno stesso blocco di codice. I cicli `for` consentono di eseguire il codice per un dato numero di volte, mentre i cicli `while` consentono di ripetere l'esecuzione fino a che non si verifica una condizione.

```python
for number in [0, 1, 2, 3, 4]:
    print(number)
```

Notare che non è necessario che la variabile `number` sia stata inizializzata in precedenza. È possibile iterare su qualsiasi sequenza, non necessariamente numerica.

```python
>>for x in 'ciao!':
…        print(x,end = ' ')
…
c i a o !
```

Più in generale l'iterazione è possibile su qualsiasi **iterabile**, ossia qualsiasi oggetto che ha la capacità di restituire i suoi membri uno alla volta. Si può iterare su più indici, ad esempio per iterare su tutte le coppie chiave-valore di un dizionario (l'ordine non è rispettato perchè i dizionari non sono ordinati) .

```python
>>dic = {'A':1,'B':2}
>>for i,j in dic.items():
…     print(i,j)
…
B 2
A 1
```

!!! tip "Variabili di iterazione"
    Notare come nell'esempio precedente si siano violate le convenzioni sui nomi di variabili per le variabili di iterazione `i` e `j` usate nel loop. Questa è una pratica comune, dato che le variabili in questione cessano di essere rilevanti una volta terminato il loop, dunque il fatto che abbiano nomi poco parlanti non influenza la chiarezza del codice che segue.

Si può anche iterare su più sequenze in contemporanea.

```python
people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
for position, person in enumerate(people):
    age = ages[position]
    print(person, age)

for person, age in zip(people, ages):
    print(person, age)
```

Se si vuole eseguire ripetutamente un blocco di codice fino a che una condizione è vera si usa invece un ciclo `while` .

```python
while condizione:
    …
```

Si può arrestare forzatamente un loop tramite `break` , oppure interrompere l'iterazione attuale e saltare a quella successiva con `continue`. Un loop può essere seguito da una clausola `else` che viene eseguita solo se il loop è terminato normalmente (ossia se non è stato interrotto tramite un `break`).

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