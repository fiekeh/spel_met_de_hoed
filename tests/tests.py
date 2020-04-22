

class Tests:
    def __init__(self):
        # Init

    def test_loading_files(self):
        # Do test

    def do_tests(self):
        self.test_loading_files()
        # Etc.


if __name__ == "__main__":
    tests = Tests()
    tests.do_tests()


"""
Ideeen:
- Folder met txts met op elke lijn een nieuwe entry van de inzending

Fases in het spel:
Ronde --> Alle kaartjes terug in hoed, opnieuw beginnen met legen
Beurt --> Wisselt tussen team 1 en team 2, speler krijgt achter elkaar een nieuw kaartje uit de hoed

Keys: 
r   -   Start nieuwe ronde. Alle kaartjes gaan opnieuw in de hoed. Vraag om tijd die hoort bij de ronde in sec
b   -   Wissel van beurt, ga naar volgend team.
n   -   Vorig kaartje is goed geraden, pak een nieuw kaartje

Wat moet in de init
- N teams + teamnamen. Default ['team_1', 'team_2']


Maken
- Automatische puntentelling
- Key input lezen
- Timer
- Functie die iedere keer een kaartje geeft

Hoe te spelen met mensen zonder python??
Hoe speel je dit met meerdere spelers via internet??
"""
