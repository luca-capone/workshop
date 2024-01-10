

# Fondamenti
## Commenti

La prima cosa da sapere quando si studia un linguaggio di programmazione è la sintassi per i commenti. Un commento in programmazione è come una nota che si inserisce nel codice per spiegare cosa fa una parte specifica di quel codice. Queste annotazioni non vengono eseguite quando il programma è in esecuzione ma sono utili per aiutare i programmatori a comprendere meglio il codice. In Python, è possibile inserire un commento inserendo il carattere cancelletto `#`

```python
# Questo è un commento "in testa"
x = 0

y = 1  # questo invece è un commento "in coda"

```

## Variabili

Le **variabili** sono una componente fondamentale di Python, possono essere pensate come contenitori per memorizzare dati di vario tipo da utilizzare durante l'esecuzione del programma. Come si intuisce dal nome, il valore di una variabile cambia nel corso dell'esecuzione per effetto dell'applicazione di **operatori**, il più fondamentale dei quali è l'**operatore di assegnazione** `=` che cambia il valore della variabile a sinistra dell'operatore con il valore alla sua destra.

```python
x = 5  # assegna il valore intero 5 alla variabile x
```

Python è un linguaggio cosiddetto **a tipizzazione dinamica**, vale a dire che non è necessario dichiarare esplicitamente il tipo della variabile prima di utilizzarla, inoltre si può cambiare il tipo della variabile quante volte si desidera

```python
y = 10     # assegna il valore intero 10 alla variabile
y = "ciao" # ora y diventa una stringa
```

Un programma complesso fa uso di un gran numero di variabili, dunque è importante scegliere con cura i nomi delle variabili per evitare confusione. Le regole del linguaggio per i nomi sono:

- il nome può contenere solo lettere, cifre ed il carattere underscore `_`
- il nome non può iniziare con una cifra
- il nome è case sensitive, i.e. `var` e `VAR` sono due variabili differenti

La convenzione è quella di scegliere nomi più lunghi di due caratteri, scritti tutti in minuscolo ed in formato **snake case**, ovvero con gli `_` a rimpiazzare gli spazi. Esistono due eccezioni a queste regole, rappresentate dalle **costanti** e dalle **variabili di iterazione**, che vedremo più avanti.

!!! warning "Nomi riservati"
    Ci sono alcuni nomi che, sebbene soddisfino tutte le regole e le convenzioni sopra descritte, non andrebbero usati perché ci sono alcune variabili **built-in**, cioè variabili necessarie a Python per funzionare, con lo stesso nome e.g., `type`, `hash`, `input`, `file`.
    Se proprio dovesse piacervi l'idea di chiamare una variabile in questo modo, potete risolvere aggiungendo un `_` in coda e.g., `type_`.

### Esempio 1

Supponiamo di dover scegliere i nomi di alcune variabili che devono contenere informazioni anagrafiche di un cliente.

!!! success "Nomi di variabili"
    `nome_utente`, `data_registrazione`, `codice_fiscale`

I nomi nel riquadro verde sono delle buone scelte in quanto sono, come si suol dire, **parlanti** ovvero non è in dubbio a cosa esattamente facciano riferimento. Sono inoltre scritti tutti in minuscolo, in snake case e sufficientemente lunghi.

### Esercizio 1

Nel riquadro rosso trovi dei nomi di variabili che sono sconsigliabili, sei in grado di dire quale è il problema di ciascun nome?

!!! failure "Nomi di variabili"
    `cf`, `nomeUtente`, `data`, `DATA_NASCITA`

## Costanti

Le **costanti** in Python sono molto semplici da comprendere, dato che non esistono. Sebbene il linguaggio non preveda esplicitamente la possibilità di creare delle costanti, si possono usare delle normali variabili facendo attenzione a che il valore non venga mai alterato dopo l'assegnazione iniziale. Per facilitare questo compito, si usa assegnare loro nomi che seguono tutte le convenzioni sui nomi delle variabili eccetto una: sono tutti in maiuscolo invece che in minuscolo.

```python
PI_GRECO = 3.14159  # costante di Archimede
ALPHA = 1/137       # costante di struttura fine
```

## Tipi di dati

Il **tipo di dato** (*datatype*) di una variabile stabilisce le operazioni che è possibile effettuare su di essa. I tipi fondamentali in Python sono:

1. **int**: rappresenta i numeri interi;
2. **float**: rappresenta i numeri decimali in virgola mobile (*floating point*, da cui il nome);
3. **complex**: rappresenta i numeri complessi, l'unità immaginaria è indicata con `j`;
4. **bool**: rappresenta un valore di verità (`True` oppure `False`);
5. **stringa**: rappresenta una sequenza di caratteri racchiusa tra apici singoli `'` o doppi `"`.

### Tipi numerici

Nel riquadro sotto un esempio di assegnazione di variabili di tipo numerico.

```python
a = 5           # numero intero
b = 3.14        # numero decimale in floating point
c = 2 + 3j      # numero complesso

d = 0xabcdef    # numero intero in esadecimale
e = .6532       # lo 0 non è indispensabile nei floating point
f = 1e6         # numero floating point in notazione esponenziale
g = 10_000_000  # gli _ sono ignorati ma aumentano la leggibilità
```

I tipi numerici possono essere manipolati con gli **operatori aritmetici** che eseguono le operazioni aritmetiche fondamentali.

```python
c = a + b   # Addizione
c = a - b   # Sottrazione
c = a * b   # Moltiplicazione
c = a / b   # Divisione
c = a ** b  # Potenza
c = a % b   # Modulo (resto della divisione)
c = a // b  # Divisione intera
```

### Tipo bool

Il tipo bool è di fondamentale importanza per manipolare l'ordine in cui le istruzioni di un programma vengono eseguite, il cosiddetto **flusso di controllo** (*control flow*). Le variabili di tipo bool possono essere manipolate tramite **operatori logici**, che eseguono le operazioni fondamentali della logica simbolica, ed **operatori di confronto**, che vengono utilizzati per confrontare valori e determinare relazioni tra di essi.

| operazione             | sintassi |
| ---------------------- | -------- |
| congiunzione           | `and`    |
| negazione              | `not`    |
| disgiunzione inclusiva | `or`     |
| uguaglianza            | `is`     |
| equivalenza            | `==`     |
| non equivalenza        | `!=`     |

Nel codice sottostante alcuni esempi di utilizzo di operatori su variabili booleane.

```python
# Operatori logici
print(True and False)        # False
print(not True)              # False
print(True or False)         # True

# Operatori di confronto
a = 5
b = 5
c = 10/2
print(a is b)                # True
print(a is c)                # False
print(a == b)                # True
print(a == c)                # True
print(a != b)                # False
```

Altre caratteristiche del tipo bool sono le seguenti:

- `False` e `True` sono alias rispettivamente per `0` ed `1`;
- un'espressione numerica è falsa se è uguale a `0`, altrimenti è vera;
- sequenze e dizionari vengono valutate a `True` (ma non sono uguali né equivalenti ad esso) se contengono almeno un elemento.

### Stringhe

Le stringhe in Python sono semplicemente collezioni ordinate di caratteri, che possono essere delimitate da `'` o da `"`. Sebbene la scelta sia indifferente, il fatto che il carattere `'` potrebbe servire all'interno della stringa, dato che rappresenta anche l'apostrofo, rende più conveniente usare `"`.

```python
stringa_apici_singoli = 'Questo è un esempio di stringa con gli apici singoli.'

stringa_apici_doppi = "Questo è un esempio di stringa con gli apici doppi."
```

Racchiudendo una stringa con tripli apici, siano essi singoli o doppi, è possibile farla spaziare su più righe:

```python
stringa_tripli_apici_singoli = '''Questo è un esempio 
di stringa con tripli apici singoli su 
più righe.'''

stringa_tripli_apici_doppi = """Questo è un esempio 
di stringa con tripli apici doppi su 
più righe."""
```

La formattazione delle stringhe in Python è un concetto fondamentale per manipolare e presentare dati in modo leggibile e strutturato.

```python
nome = "Luca"
eta = 32

# Utilizzo del metodo format() per inserire valori in una stringa
saluto = "Ciao, mi chiamo {} e ho {} anni.".format(nome, eta)
```

Nell'esempio sopra, `{}` è un segnaposto all'interno della stringa. Quando chiamiamo il metodo `format()` sulla stringa `saluto` e passiamo le variabili `nome` e `eta`, i valori vengono inseriti nei rispettivi segnaposto. Il risultato sarà:

```
Ciao, mi chiamo Luca e ho 32 anni.
```

Il metodo `format()` offre molta flessibilità. È possibile specificare l'ordine dei valori, utilizzare segnaposto numerati o nominati e applicare formattazioni più complesse per numeri, stringhe e altri tipi di dati. Ad esempio:

```python
# Utilizzo di segnaposti nominati
saluto = "Ciao, mi chiamo {nome} e ho {eta} anni.".format(nome="Luca", eta=32)
```

Esiste però un metodo molto più conveniente per la formattazione delle stringhe, vale a dire l'utilizzo delle cosiddette **f-string**:

```python
nome = "Luca"
eta = 32
saluto = f"Ciao, mi chiamo {nome} e ho {eta} anni."
```

Un'altra operazione frequente sulle stringhe è la concatenazione, ottenuta con l'operatore `+`:

```python
frase_iniziale = "Il cielo è "
colore = "blu"
punteggiatura = "."

frase_completa = frase_iniziale + colore + punteggiatura

print(frase_completa)  # Il cielo è blu.
```

!!! warning "Concatenazione silente"
    In effetti, è sufficiente mettere due stringhe vicine per ottenere una concatenazione, proprietà detta **concatenazione silente**. Fare estremamente attenzione a questa particolare funzionalità di Python, dato che è una fonte inesauribile di bug.

## Collezioni

Le collezioni sono strutture dati che servono a contenere più oggetti al loro interno. Si distinguono in **mutabili** ed **immutabili**, a seconda che possano essere modificate dopo la loro creazione o meno. Una sequenza può essere ordinata o non avere un ordine.

La tabella sottostante riassume le proprietà di ogni tipo di collezione:

| tipo          | mutabile | ordinata  | duplicati | struttura |
|---------------|:--------:|:---------:|:---------:|:---------:|
| dizionario    | sì       | no | no        | `{a:m, b:n}`   |
| tupla       | no       | sì        | sì        | `(a, b)`  |
| lista         | sì       | sì        | sì        | `[a, b]`  |
| insieme           | no       | no        | no        | `{a, b}`  |
| stringa       | no       | sì        | sì        | `ciao`    |

## Continuazione di linea

Quando si scrive del codice lungo, è possibile **continuare una linea** utilizzando il carattere di **continuazione `\`** alla fine della linea da spezzare. Tuttavia, all'interno di parentesi (tonde, quadre o graffe), Python consente la continuazione automatica senza la necessità di utilizzare il carattere `\`, semplificando la scrittura di codice su più righe senza compromettere la leggibilità.

```python
lunga_stringa = "Questa è una lunga stringa che possiamo " \
                "continuare su più righe utilizzando il carattere di continuazione."

lunga_lista = [
    "elemento1",
    "elemento2",
    "elemento3",
    "elemento4",
    "elemento5",
]
```