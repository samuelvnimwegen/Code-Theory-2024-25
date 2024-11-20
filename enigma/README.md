# Enigma
Dit document legt de werking van de Enigma kraker uit. De implementatie is gebaseerd op de tweede versie van Turing’s "bombe" machine, ontworpen om Enigma-berichten te kraken. Het programma in Python heeft een runtime van ongeveer 7,5 uur, maar in C++ zou dit zo'n 5-15 minuten duren, aangezien C++ ongeveer 100 keer sneller is dan Python.

## Methode

### Enigma Machine
De eerste stap was het bouwen van een Enigma-machine. Deze machine wordt later in het project gebruikt om verbindingen te maken tussen de rijen van een matrix.

De machine is opgebouwd uit de volgende componenten:
- **Plugboard (Stekkerbord)** – hiermee worden letters onderling verbonden.
- **Rotors** – de draaiende wielen die de letterverschuiving bepalen.
- **Reflector** – kaatst de elektrische stroom terug door de rotors.

We hebben elk van deze componenten geïmplementeerd, maar gaan hier niet in detail in op hun werking.

- De volledige Enigma-machine is te vinden in `enigma/enigma_machine.py`.
- De componenten zijn te vinden in de bestanden `enigma/plugboard`, `enigma/rotor_wheel`, en `enigma/reflector`.

### Enigma Solver
De Enigma solver is gebaseerd op de tweede versie van de Turing bombe, zoals eerder vermeld.

#### Stap 1: Maken van een graaf op basis van de crib
De eerste stap is het maken van een graaf (graph) op basis van de "crib" (het bekende stuk tekst). Dit gebeurt door letters te verbinden en de index van de crib als gewicht (weight) aan de verbinding toe te kennen. Zo ontstaat een graaf die later gebruikt kan worden.

#### Stap 2: Maken van een matrix voor het stekkerbord
De tweede stap is het maken van een matrix voor het stekkerbord. Dit wordt gedaan door eerst alle symmetrische posities te verbinden. Vervolgens worden voor elke verbinding in de graaf de rijen tussen de twee knooppunten (nodes) verbonden met een Enigma-machine. De rotorpositie van deze Enigma-machine komt overeen met het gewicht van de verbinding in de graaf.

#### Stap 3: Controleren of de matrix correct is
De derde stap is om elke matrix te controleren op correctheid. Dit gebeurt door een rij te selecteren van de knoop met de meeste verbindingen in de graaf. Daarna wordt elk vakje in deze rij getest. Een matrix wordt als correct beschouwd als deze voldoet aan de volgende voorwaarden:
- Elke rij bevat maximaal één element.
- Elke kolom bevat maximaal één element.
- De matrix is symmetrisch.
- De matrix bevat ten minste 10 elementen.

Aangezien we vaak maar een deel van de oorspronkelijke tekst hebben, missen we mogelijk een deel van de matrix. Daarom is de regel van ten minste 10 elementen toegevoegd.

### Code
De code is geschreven in Python en te vinden in de `enigma`-map:
- **Enigma-machine**: `enigma/enigma_machine.py`
- **Enigma-graaf**: `enigma/enigma_graph.py`
- **Enigma-matrix**: `enigma/enigma_matrix.py`
- **Enigma-solver**: `enigma/enigma_solver.py`
- **Enigma-solver runnen**: `solve_enigma.py`

## Hoe te runnen
De code kan worden uitgevoerd met het volgende commando, vanuit de root van het project:

```bash
python solve_enigma.py
