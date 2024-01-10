
# Introduzione

## Perché Python?

Python è un linguaggio di programmazione potente e flessibile, famoso per la sua leggibilità e semplicità. È utilizzato sia da principianti che da esperti in svariati campi, dalla scienza dei dati all'intelligenza artificiale, passando per lo sviluppo web e molto altro. La sua versatilità ed immediatezza rendono Python il linguaggio ideale per iniziare.

## Cosa devo sapere prima di iniziare?

Niente. Questo corso è stato pensato e strutturato appositamente per chi non ha alcuna esperienza precedente con la programmazione. Se vi sentite completamente a digiuno di nozioni in questo ambito, siete nel posto giusto.

## Come si leggono i riquadri?

WARNING: **Attenzione**
Riquadri come questo contengono informazioni a cui si deve prestare particolare attenzione perché possono causare bug o comportamenti indesiderati nel codice.

TIP: **Consiglio da esperti**
Riquadri come questo contengono informazioni un po' più avanzate, non fondamentali alla comprensione del testo ma preziose da conoscere.

SUCCESS: **Esempio positivo**
Riquadri come questo contengono esempi positivi da imitare.

FAILURE: **Esempio negativo**
Riquadri come questo contengono esempi di codice scritto male o addirittura non funzionante.

# Ambiente di sviluppo

## Installazione di Python

La prima cosa di cui abbiamo bisogno, chiaramente, è Python stesso.

### Windows
- Vai al sito ufficiale di Python: [python.org](https://www.python.org/).
- Nella sezione "Downloads", trova la versione per Windows e clicca per scaricarla.
- Esegui il file scaricato (`.exe`).
- Seleziona "Add Python to PATH" all'inizio dell'installazione. Questo passaggio è cruciale per eseguire Python da qualsiasi prompt dei comandi.
- Clicca su "Install Now".
- Apri il Prompt dei comandi (CMD) o PowerShell.
- Digita `python --version` e premi Enter. Dovrebbe mostrare la versione di Python installata.

### Mac
- Visita il sito ufficiale di Python: [python.org](https://www.python.org/).
- Nella sezione "Downloads", seleziona la versione per macOS e clicca per scaricarla.
- Apri il file `.pkg` scaricato per avviare l'installazione.
- Segui le istruzioni sullo schermo per installare Python. Potrebbe essere necessario inserire la password dell'account amministratore.
- Una volta completata l'installazione, apri il Terminal.
- Digita `python3 --version` e premi Enter per verificare l'installazione. Dovrebbe mostrare la versione di Python installata.

### Linux
- La maggior parte delle distribuzioni Linux viene con Python già installato. Per verificare, apri il terminale.
- Digita `python3 --version` e premi Enter. Se Python è installato, dovrebbe mostrare la versione.
- Se Python non è installato, usa il gestore pacchetti della tua distribuzione. Per esempio, su Debian o Ubuntu, usa `sudo apt-get install python3`.
- Segui le istruzioni sullo schermo per completare l'installazione.
- Dopo l'installazione, verifica nuovamente la versione di Python con `python3 --version` nel terminale.

## Installazione di Visual Studio Code

Per sviluppare in Python, ci serve un ambiente dove scrivere, testare e gestire il codice. Le opzioni possibili sono numerose, ma si distinguono approssimativamente in due categorie: **editor di testo** ed **ambienti di sviluppo integrati** (***I**ntegrated **D**evelopment **E**nvironment*, **IDE**).

- **Editor di Testo**: Sono programmi focalizzati sulla scrittura e modifica del codice sorgente. Offrono funzionalità come l'evidenziazione della sintassi e il completamento automatico del codice. Esempi includono **Notepad++** e **Sublime Text**.
- **IDE**: Un IDE è un ambiente più completo che integra diverse funzionalità: editor di testo, debugger, compilatore/interprete, e altri strumenti utili. Esempi sono **PyCharm** e **Eclipse**.

**Visual Studio Code (VSCode)** si posiziona a metà strada, in quanto è tecnicamente un editor di testo ma offre un sistema di estensioni che consentono di aggiungere le funzionalità di un IDE. Questo lo rende ideale in quanto è complesso esattamente quanto necessario e non di più.

TIP: **Command palette**
VSCode è dotato di una **Command Palette**. Accessibile tramite `Ctrl+Shift+P` su Windows/Linux o `Cmd+Shift+P` su MacOS, questa funzionalità permette di accedere rapidamente a comandi e funzioni del programma. Potete cercare comandi, installare estensioni, aprire file, e molto altro, tutto da un'unica interfaccia. La Command Palette è uno strumento essenziale, usatelo!

### Windows
- Vai al sito ufficiale di VSCode: [code.visualstudio.com](https://code.visualstudio.com/).
- Scarica la versione per Windows.
- Esegui il file scaricato (`.exe`).
- Segui le istruzioni per completare l'installazione.
- Installa [questa](https://marketplace.visualstudio.com/items?itemName=ms-python.python) estensione
- Crea una cartella `python_workshop` da qualche parte sul tuo computer
- Apri la cartella `python_workshop` in VSCode da `File` `Open Folder`
- Apri un nuovo file in VSCode.
- Scrivi `print("Hello, world!")`
- Salva il file con estensione `.py`
- Esegui lo script premendo `Ctrl + F5` e seleziona Python come ambiente di esecuzione.
### Mac
- Visita il sito ufficiale di Visual Studio Code: [code.visualstudio.com](https://code.visualstudio.com/).
- Scarica la versione per macOS.
- Apri il file `.zip` scaricato e trascina l'icona di Visual Studio Code nella cartella Applicazioni.
- Apri Visual Studio Code dal Finder o dalla Launchpad.
- Installa l'estensione Python dal [marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
- Crea una cartella `python_workshop` da qualche parte sul tuo computer
- Apri la cartella `python_workshop` in VSCode da `File` `Open Folder`
- Apri un nuovo file in VSCode.
- Digita `print("Hello, world!")`.
- Salva il file con estensione `.py`.
- Esegui lo script premendo `Cmd + F5` e scegli Python come ambiente di esecuzione.

### Linux
- Visita il sito ufficiale di Visual Studio Code: [code.visualstudio.com](https://code.visualstudio.com/).
- Scarica la versione per Linux (Debian, Ubuntu, Fedora, Red Hat o SUSE).
- Segui le istruzioni specifiche per la tua distribuzione per installare il pacchetto scaricato.
- Una volta installato, apri Visual Studio Code dal menu delle applicazioni o dal terminale.
- Installa l'estensione Python dal [marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
- Crea una cartella `python_workshop` da qualche parte sul tuo computer
- Apri la cartella `python_workshop` in VSCode da `File` `Open Folder`
- Crea un nuovo file in VSCode.
- Scrivi `print("Hello, world!")`.
- Salva il file con estensione `.py`.
- Esegui lo script premendo `Ctrl + F5` e seleziona Python come ambiente di esecuzione.

## Installazione di Poetry

**Poetry** è uno strumento per la gestione di progetti Python che aiuta a semplificare e ottimizzare diverse attività cruciali, come la gestione delle dipendenze e la configurazione degli strumenti di sviluppo. Ci servirà più avanti.

### Windows
1. Apri il Prompt dei comandi (CMD) o PowerShell.
2. Esegui il comando per scaricare e installare Poetry:

   ```
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
   ```

3. Dopo l'installazione, riavvia il Prompt dei comandi o PowerShell.
4. Verifica l'installazione con il comando `poetry --version`.

### Mac
1. Apri il terminale.
2. Usa il comando curl per scaricare e installare Poetry:

   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Chiudi e riapri il terminale.
4. Verifica l'installazione con `poetry --version`.

### Linux
1. Apri il terminale.
2. Per installare Poetry, usa il comando:

   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Una volta completata l'installazione, chiudi e riapri il terminale.
4. Controlla che Poetry sia stato installato correttamente con `poetry --version`.

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

WARNING: **Nomi riservati**
Ci sono alcuni nomi che, sebbene soddisfino tutte le regole e le convenzioni sopra descritte, non andrebbero usati perché ci sono alcune variabili **built-in**, cioè variabili necessarie a Python per funzionare, con lo stesso nome e.g., `type`, `hash`, `input`, `file`.
Se proprio dovesse piacervi l'idea di chiamare una variabile in questo modo, potete risolvere aggiungendo un `_` in coda e.g., `type_`.

### Esempio 1

Supponiamo di dover scegliere i nomi di alcune variabili che devono contenere informazioni anagrafiche di un cliente.

SUCCESS: **Nomi di variabili**
`nome_utente`, `data_registrazione`, `codice_fiscale`

I nomi nel riquadro verde sono delle buone scelte in quanto sono, come si suol dire, **parlanti** ovvero non è in dubbio a cosa esattamente facciano riferimento. Sono inoltre scritti tutti in minuscolo, in snake case e sufficientemente lunghi.

### Esercizio 1

Nel riquadro rosso trovi dei nomi di variabili che sono sconsigliabili, sei in grado di dire quale è il problema di ciascun nome?

FAILURE: **Nomi di variabili**
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

WARNING: **Concatenazione silente**
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

TIP: **Variabili di iterazione**
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

# Classi
## Programmazione Orientata agli Oggetti

Python è un linguaggio di programmazione che supporta la **programmazione orientata agli oggetti** (***o**bject **o**riented **p**rogramming*, **OOP**). Per capire questo concetto, immaginate un oggetto come una scatola che contiene informazioni e strumenti. Le informazioni sono chiamate **attributi**, mentre gli strumenti sono le **funzioni** o **metodi**.

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
class Square():
    # `side` è un attributo di `Square`
    side = 8
    # `area` è un metodo di `Square`
    def area(self):                
        return self.side ** 2

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
        print(f"Nome: {self.nome}, Età: {self.eta}, Anno di Studio: {self.anno_di_studio}")
```

In questo esempio, la classe `Studente` eredita da `Persona` e aggiunge ulteriori funzionalità.

# Ecosistema Python
## Librerie

Quando si sviluppa un progetto in Python, solo una piccola parte del codice viene scritto dallo sviluppatore per lo specifico progetto. La maggior parte del codice è invece costituito dalle **librerie**.

Una libreria è un insieme di codice riutilizzabile condiviso da terze parti che offre funzioni, classi e metodi che afferiscono ad uno stesso argomento, come l'analisi dei dati, la grafica, o la comunicazione di rete. Ad esempio, `matplotlib` è una libreria per la creazione di grafici.

Le librerie sono composte da moduli, organizzati in pacchetti. L'insieme delle librerie usate da un progetto costituiscono le sue **dipendenze**.

## Moduli

Un **modulo** è un file Python (con estensione `.py`) che contiene definizioni e implementazioni di funzioni, classi e variabili. I moduli possono essere importati e utilizzati in altri moduli o script Python. Ad esempio, il modulo `math` in Python fornisce accesso a funzioni matematiche.

## Pacchetti

Un **pacchetto** è una raccolta di moduli Python. Mentre un modulo è un singolo file Python, un pacchetto è una directory che contiene file Python e un file speciale chiamato `__init__.py`. Questo file indica che la directory è un pacchetto Python, che può includere sotto-pacchetti e moduli. Per esempio, `numpy` è un pacchetto popolare per il calcolo numerico.

## Gestore di pacchetti

Un **gestore di pacchetti** (*package manager*) è uno strumento che automatizza il processo di installazione, aggiornamento, configurazione e rimozione di pacchetti software da un archivio di pacchetti. In Python, il gestore di pacchetti più comune è `pip`. Con `pip`, è possibile installare pacchetti da [PyPI (Python Package Index)](https://pypi.org/), un repository di software per la programmazione in Python.

```shell
# Installs matplotlib
pip install matplotlib
```

## Versionamento

Le librerie vengono costantemente modificate, dunque è importante considerare la versione di una libreria che si sta utilizzando. La versione è tipicamente espressa secondo una convenzione detta di **versionamento semantico**, che prevede di assegnare a ciascuna versione un numero nel formato seguente:

```text
major.minor.patch
```

Una **patch version** introduce solo fix di bug, una **minor version** introduce nuove funzionalità mentre una **major version** segnala cambiamenti radicali che possono introdurre regressioni.

## Ambienti virtuali

Il versionamento delle librerie fa emergere un problema: cosa succede se si lavora a più di un progetto sulla stessa macchina? Supponiamo di sviluppare due progetti `A` e `B` e che entrambi abbiano bisogno della libreria `mylib`. Immaginiamo che la libreria `mylib` venga aggiornata e passi dalla versione `1.2.3` alla versione `2.0.0`, dalle regole del versionamento semantico sappiamo che questo significa che potrebbero esserci regressioni. Come ci si deve comportare se il progetto `A` non può aggiornare la libreria perché impattato da tali regressioni mentre il progetto `B` vuole aggiornare la libreria per avvantaggiarsi delle nuove funzionalità introdotte?

L'esempio sopra fa intuire come ciascun progetto debba essere accompagnato da una copia di tutte le librerie di cui ha bisogno, ciascuna libreria alla specifica versione che meglio risponde alle esigenze del progetto. Non basta: Python stesso deve essere alla specifica versione di cui il progetto ha bisogno, dato che il discorso fatto sulle librerie si estende al linguaggio stesso.

Un **ambiente virtuale** (**virtual environment** o **venv**) è uno strumento che permette di mantenere separate le dipendenze richieste da diversi progetti. In parole semplici, è come avere un cassetto per ciascun progetto, ciascuno dei quali può contenere i suoi propri strumenti, indipendentemente dal contenuto degli altri. Gli ambienti virtuali sono gestiti da uno strumento apposito, per esempio `conda`, `virtualenv` o `pyenv`.

Poetry, che abbiamo installato all'inizio, consente di creare facilmente ambienti virtuali. Per farlo apriamo il terminale integrato in VSCode (`Terminal` `New terminal`) quindi eseguiamo i seguenti comandi:

```shell
# Creiamo un nuovo progetto
poetry new myproject
# Spostiamoci all'interno della cartella del progetto
cd myproject
# Entriamo nell'ambiente virtuale
poetry shell
# Installiamo qualche libreria
poetry add matplotlib pandas
```

## Jupyter

Un notebook **Jupyter** è un documento composto da una serie di "celle", che possono contenere codice, testo formattato, equazioni o visualizzazioni. Contrariamente ad uno script, che viene eseguito per intero quando lanciato, un notebook Jupyter viene eseguito una cella per volta. Una cella può essere eseguita più volte, cancellata, spostata, ignorata, etc. Per lavorare con i notebook Jupyter in VSCode, installare la relativa [estensione](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter). Per eseguire una cella di codice, premere il pulsante "Run Cell" che appare quando si passa il mouse sopra la cella o premere `Shift + Enter`.
