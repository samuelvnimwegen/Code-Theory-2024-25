# ADFGVX
Dit document legt de werking van de ADFGVX kraker uit. De implementatie is gebaseerd op een bruteforce voor de kolomtranspositie en het hill climbing algoritme voor de Polybius Square. De kolomtranspositie kraken duurt ongeveer 2-5 minuten en het kraken van de Polybius Square duurt enkele seconden voordat er een vrij correcte oplossing is gevonden. Deze is meestal niet volledig correct maar is accuraat genoeg dat je zelf kunt zien wat er nog veranderd moet worden.

## Methode

### Kolomtranspositie

We bruteforcen de kolomtranspositie.\
We berekenen alle mogelijke keys maar zonder letters omdat dit voor duplicate keys kan zorgen. (e.g. de key DBA is equivalent aan de key CBA)\
Onze keys zijn dan van de vorm 012 ipv bv ABC of 201 ipv GEF.\
We gaan ervan uit dat er in de tekst geen cijfers zitten en geven de eerste key dat 26 of minder unieke pairs heeft voor de combinatie van ADFGVX met lengte 2 en herhaling toegestaan.\
Hierdoor kunnen we gewoonweg een key dat 26 of minder unieke pairs heeft gebruiken.

### Hill Climbing

We vullen de Polybius Square met de meest overeenkomende frequenties. (e.g. GV is the most occurring pair in the text and E is the most occurring letter in english --> GV = E)\
De score van onze heuristiek wordt bepaald door de log van de frequentie van een quadgram in het Engels indien dit voorkomt in onze tekst, anders een kleine penalty, dit doen we voor elke keer dat een quadgram voorkomt.\
Tot dat de user het programma interrupt gaan we 2 willekeurige letters switchen in de Polybius Square en berekenen we opnieuw de score. Als de score al eventjes niet is aangepast gaan we terug naar het begin Polybius Square.

### Code
De code is geschreven in Python en te vinden in de `adfgvx`-map:
- **Morse decoder**: `adfgvx/morse.py`
- **Kolom Transpositie**: `adfgvx/column_transposition.py`
- **Frequentie Analyse**: `adfgvx/frequency_analysis.py`
- **Hill Climbing**: `adfgvx/hill_climb.py`
- **Main File**: `adfgvx/run_adfgvx.py`

## Hoe te runnen
De code kan worden uitgevoerd met het volgende commando, vanuit de root van het project:

```bash
python -m adfgvx.run_adfgvx
```