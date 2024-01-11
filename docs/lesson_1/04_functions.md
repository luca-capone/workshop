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
