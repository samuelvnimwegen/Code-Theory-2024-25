# Vigenère
Dit project bevat de oplossing van de Vigenère code. De code is geschreven in Python en bevat een extra kolom-transpositie.

## Methode
### Kolomtranspositie
De kolomtranspositie is de eerste stap voor het decrypten. Hiervoor was het moeilijke vooral het zoeken naar een manier om de oplossing te herkennen.

#### Oplossing herkennen
We weten van Vigenère code wel 1 ding. De key lengte is te achterhalen omdat er een groot aantal herhalingen is van 3-letter fragmenten met een veelvoud van de key-lengte hiertussen.
Uit deze informatie was er dus indirect af te leiden dat vigenere code veel meer terugkomende zelfde 3-letter sequenties heeft dan random text.
Met deze informatie was het mogelijk om de vigenère code te achterhalen.


#### Methode
De methode is eigenlijk vrij simpel. We nemen de tekst en splitsen deze op in kolommen. Hiermee contrueren we dan de Vigenère text. 
We weten dat deze juist is als deze veel meer herhalingen heeft van 3-letter sequenties dan random text.

We houden de top 50 opties die maximaal 10% van elkaar liggen bij en kijken naar de volgende stap.

### Vigenère
Deze methode werd in de les vermeld, maar toch zijn er zaken die nog extra aandacht nodig hebben.

De Vigenère code is een code die werkt met een key. 
Deze key wordt gebruikt om de tekst te encrypten. 

#### De key lengte achterhalen
De key lengte is te achterhalen door te kijken naar de herhalingen van 3-letter sequenties.
Deze meeste herhalingen zijn een veelvoud van de key lengte.
Op deze manier is de key lengte te achterhalen.

#### De key achterhalen
Je kan nu per item in de tekst die onder hetzelfde character van de key zit de key achterhalen. 
Als de sleutel lengte 3 heeft bijvoorbeeld, en de crypt `1234567` is, dan weet je dat character 1, 4 en 7 onder hetzelfde character van de key zitten.

Als je nu deze characters in groepen opdeelt op basis van het key character, dan kan je de key achterhalen.

Per groep ga je per taal kijken met welke verschuiving je het dicht bij een mogelijk taal kan komen. 
Dit doe je met de frequentietabellen van de talen. Als deze zo dicht mogelijk overeenkomen, is de key value waarschijnlijk juist.
Dit doen we met de **Chi-kwadraat** test. 

Als deze waarde minimaal is, dan is de key value waarschijnlijk juist. Dit herhalen we dan voor elke key value.

#### Decrypten
Als de key bekend is, dan is het decrypten van de tekst vrij simpel. Je shift nu gewoon de andere kant op dan bij encrypten.


## Code
De code is geschreven in Python en is te vinden in de map `vigenere`.

De code is te runnen met het volgende commando:

Vanuit de root van het project:
```bash
python solve_vignere_column.py
```