# Playfair

Dit project bevat de code om een playfair cipher te kraken. De code is geschreven in Python 
en deze file bevat de verdere informatie om met de code te werk te gaan.

## Methode

De methode van Playfair is in de klas uitgelegd. Enkele opmerkingen:
 * Tekst is alijd in hoofdletters, zonder spaties en leestekens
 * Gebruik geen 'J' in de tekst, maar vervang met 'I'
 * Na decryptie, zullen al de X's verwijderd worden uit het resultaat. 
   *  Aangezien in het proces de letters X worden toegevoegd om de letter herhaling in eenzelfde pairs te splitsen,
        is het op het einde moeilijk te bepalen welke letters X van de oorspronkelijke tekst zijn en welke zijn toegevoegd in het proces.

## Solving Playfair

### Starting point
Start in de file `solve_playfair.py` om de ciphertext te kraken. Gebruik methode `cracking(...)` met volgende parameters:
* path naar file met input string (tekst dat wordt gekraakt)
* functie van de heuristiek die wordt gebruikt om tekst een score te geven
* path naar file om de output te schrijven

### Resultaat

Het resultaat is te vinden in de file `solutions/02-OPGAVE-playfair.txt`.

Het zal onwaarschijnlijk zijn om dit resultaat een tweede maal te bekomen, aangezien het algoritme gebruikt om het te kraken (simulated annealing) een groot deel geluk nodig heeft.  


## Code
De code is geschreven in Python en is te vinden in de map `playfair`.

De code is te runnen met het volgende commando:

Vanuit de root van het project:
```bash
python playfair/solve_playfair.py
```