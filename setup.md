---
hide:
  - navigation
---

# Ambiente di sviluppo

## Installazione di Python

La prima cosa di cui abbiamo bisogno, chiaramente, è Python stesso.

=== "Windows"
    - Vai al sito ufficiale di Python: [python.org](https://www.python.org/).
    - Nella sezione "Downloads", trova la versione per Windows e clicca per scaricarla.
    - Esegui il file scaricato (`.exe`).
    - Seleziona "Add Python to PATH" all'inizio dell'installazione. Questo passaggio è cruciale per eseguire Python da qualsiasi prompt dei comandi.
    - Clicca su "Install Now".
    - Apri il Prompt dei comandi (CMD) o PowerShell.
    - Digita `python --version` e premi Enter. Dovrebbe mostrare la versione di Python installata.

=== "Mac"
    - Visita il sito ufficiale di Python: [python.org](https://www.python.org/).
    - Nella sezione "Downloads", seleziona la versione per macOS e clicca per scaricarla.
    - Apri il file `.pkg` scaricato per avviare l'installazione.
    - Segui le istruzioni sullo schermo per installare Python. Potrebbe essere necessario inserire la password dell'account amministratore.
    - Una volta completata l'installazione, apri il Terminal.
    - Digita `python3 --version` e premi Enter per verificare l'installazione. Dovrebbe mostrare la versione di Python installata.

=== "Linux"
    - La maggior parte delle distribuzioni Linux viene con Python già installato. Per verificare, apri il terminale.
    - Digita `python3 --version` e premi Enter. Se Python è installato, dovrebbe mostrare la versione.
    - Se Python non è installato, usa il gestore pacchetti della tua distribuzione. Per esempio, su Debian o Ubuntu, usa `sudo apt-get install python3`.
    - Segui le istruzioni sullo schermo per completare l'installazione.
    - Dopo l'installazione, verifica nuovamente la versione di Python con `python3 --version` nel terminale.

## Installazione di Visual Studio Code

Per sviluppare in Python, ci serve un ambiente dove scrivere, testare e gestire il codice. Le opzioni possibili sono numerose, ma si distinguono approssimativamente in due categorie **editor di testo** ed **ambienti di sviluppo integrati** (Integrated Development Environments, **IDE**).

- **Editor di Testo**: Sono programmi focalizzati sulla scrittura e modifica del codice sorgente. Offrono funzionalità come l'evidenziazione della sintassi e il completamento automatico del codice. Esempi includono **Notepad++** e **Sublime Text**.
- **IDE**: Un IDE è un ambiente più completo che integra diverse funzionalità: editor di testo, debugger, compilatore/interprete, e altri strumenti utili. Esempi sono **PyCharm** e **Eclipse**.

**Visual Studio Code (VSCode)** si posiziona a metà strada, in quanto è tecnicamente un editor di testo ma offre un sistema di estensioni che consentono di aggiungere le funzionalità di un IDE. Questo lo rende ideale in quanto è complesso esattamente quanto necessario e non di più.

!!! tip "Command palette"
    VSCode è dotato di una **Command Palette**. Accessibile tramite `Ctrl+Shift+P` su Windows/Linux o `Cmd+Shift+P` su MacOS, questa funzionalità permette di accedere rapidamente a comandi e funzioni del programma. Potete cercare comandi, installare estensioni, aprire file, e molto altro, tutto da un'unica interfaccia. La Command Palette è uno strumento essenziale, usatelo!

=== "Windows"
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

=== "Mac"
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

=== "Linux"
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

=== "Windows"
     1. Apri il Prompt dei comandi (CMD) o PowerShell.
     2. Esegui il comando per scaricare e installare Poetry:

        ```
        (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
        ```

     3. Dopo l'installazione, riavvia il Prompt dei comandi o PowerShell.
     4. Verifica l'installazione con il comando `poetry --version`.

=== "Mac"
     1. Apri il terminale.
     2. Usa il comando curl per scaricare e installare Poetry:

        ```
        curl -sSL https://install.python-poetry.org | python3 -
        ```

     3. Chiudi e riapri il terminale.
     4. Verifica l'installazione con `poetry --version`.

=== "Linux"
     1. Apri il terminale.
     2. Per installare Poetry, usa il comando:

        ```
        curl -sSL https://install.python-poetry.org | python3 -
        ```

     3. Una volta completata l'installazione, chiudi e riapri il terminale.
     4. Controlla che Poetry sia stato installato correttamente con `poetry --version`.
