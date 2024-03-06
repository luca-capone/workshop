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
