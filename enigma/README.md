# Enigma
Dit document bevat uitleg over de werking van de Enigma kraker. 
De code is gebaseerd op de tweede Turing bombe.
De runtime van het programma is ongeveer 7.5 uur. 
Als we dit in c++ zouden schrijven, zou dit ongeveer 5-15 minuten duren wetende dat c++ ongeveer 100 keer sneller is dan python.

## Methode
### Enigma Machine
De eerste stap was om een Enigma machine te bouwen. 
Deze wordt later nog in het project gebruikt voor de connectie tussen rijen.

Het bouwen zelf gebeurde op basis van de componenten.
- Plugboard
- Rotors
- Reflector

We gaan niet uitleggen hoe deze allemaal werken, maar we hebben ze wel geïmplementeerd.

De volledige enigma machine is te vinden in `enigma/enigma_machine.py`.

De componenten zijn te vinden in `enigma/plugboard`, `enigma/rotor_wheel`, `enigma/reflector`.

### Enigma solver
De Enigma solver is gebaseerd op de tweede Turing bombe zoals eerder vermeld.

#### Stap 1: Maken van een graaf op basis van de crib
De eerste stap is om een graaf te maken op basis van de crib.
Dit gebeurt door de letters te connecteren en dan de index te nemen van de crib als weight van deze link.
Op deze manier hebben we een graph die we later kunnen gebruiken.

#### Stap 2: Maken van een matrix voor het stekkerbord
De tweede stap is om een matrix te maken voor het stekkerbord. 
Dit gebeurd door eerst alle symmetrische vakjes met elkaar te verbinden.
Hierna worden voor elke link in de graph de rijen tussen de 2 node verbonden met een enigma machine.
Deze enigma machine zal een rotorpositie hebben van de weight van de link in de graph.

#### Stap 3: Voor elke matrix voor elke rotorpositie checken of deze correct is
De derde stap is om voor elke matrix te checken of deze correct is.
Dit gebeurt door een rij te kiezen van de node met de meeste connecties in de graph.
Nu wordt er per vakje in de rij getest of deze correct is.
Een matrix is correct (in de code) als:
- Elke rij maximaal 1 element heeft
- Elke kolom maximaal 1 element heeft
- De matrix symmetrisch is
- De matrix minstens 10 elementen heeft

We vaak kunnen niet de hele matrix ontdekken omdat we maar een deel van de echte text hebben.
Dit zal er voor zorgen dat we vaak een deel van de matrix zullen missen.
Daarom is de regel van minstens 10 elementen toegevoegd.

#### Code:
De code is geschreven in Python en is te vinden in de map `enigma`.
- Enigma machine: `enigma/enigma_machine.py`
- Enigma graph: `enigma/enigma_graph.py`
- Enigma matrix: `enigma/enigma_matrix.py`
- Enigma solver: `enigma/enigma_solver.py`
- Enigma solver runnen: `solve_enigma.py`


## Hoe te runnen
De code is te runnen met het volgende commando vanuit de root van het project:
```bash
python solve_enigma.py
```