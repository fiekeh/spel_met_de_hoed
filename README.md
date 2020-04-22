# Spel met de hoed - Webapp

## Start het spel
Om het spel te starten, draai je `spel_met_de_hoed.py`. Te vinden in `src`.    
Pas eventueel de init van de __main__ aan, indien je meer dan twee teams wilt, of een andere team naam.

De applicatie start in Flask en is dus bereikbaar via je webbrowser.

## Voeg kaartjes toe aan de hoed
Om kaartjes toe te voegen aan de hoed ga je naar:
http://127.0.0.1:5000/voeg_woorden_toe

Per keer een kaartje toevoegen. Wijst zich vanzelf.

## Speel het spel
Om het spel te spelen, ga je naar:
http://127.0.0.1:5000/speel_het_spel

De buttons spreken waarschijnlijk voor zich.

Fases in het spel:
* Ronde --> Alle kaartjes terug in hoed, opnieuw beginnen met legen.
* Beurt --> Wisselt tussen team 1 en team 2, speler krijgt achter elkaar een nieuw kaartje uit de hoed. 
Belangrijk voor de puntentelling!!!
* Nieuw kaartje --> Pak een nieuw kaartje uit de hoed en doe je ding.

## Start een nieuw spel
Python script opnieuw opstarten.

## TODO
* [ ] Zorgen dat het kan draaien over het internet, ipv alleen lokaal.
* [ ] Idealiter: timer functionaliteit.
* [ ] Idealiter: geen valsspeel functionaliteit.
* [ ] Idealiter: Nieuw spel functionaliteit.

## Aandachtspunten
Op dit moment draait het alleen nog lokaal. Maar het lijkt geheel te werken.    

Het is erg makkelijk om vals te spelen. Bijvoorbeeld:
- Van beurt wisselen terwijl iemand bezig is.
- Kaartjes in de hoed stoppen, terwijl spel bezig is.
- Nieuwe ronde starten terwijl het spel bezig is.
- etc, etc, etc.

Maar, als je het leuk wilt houden, doe je dat gewoon niet.