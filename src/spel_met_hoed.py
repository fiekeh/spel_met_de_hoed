from flask import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField

import numpy as np
import random

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class VerzamelAlleWoorden(Form):
    woord_in_hoed = StringField('woord_in_hoed', default=False)
    speler = StringField('speler', default=False)


class SpeelHetSpel(Form):
    submit_button = BooleanField('submit_button')


class AdminPage(Form):
    submit_button = BooleanField('submit_button', default=False)
    team_naam = StringField('team_naam', default=False)


class SpelMetDeHoed:
    def __init__(self, teams=['A', 'B']):
        self.teams = teams
        self.leeg_de_hoed()
        self.start_nieuw_spel()

    def nieuw_woord(self):
        """Funtie om nieuw woord op te vragen in een beurt.
        --> Geef nieuw woord, verwijder laatste woord uit de huidige ronde lijst.
        """
        if self.last_woord is not None and len(self.woorden_in_ronde) > 0:
            self.woorden_in_ronde.remove(self.last_woord)
            self.team_scores[self.team_index_aan_beurt] += 1  # Houdt de score bij

        if len(self.woorden_in_ronde) > 0:
            nieuw_woord = random.choice(self.woorden_in_ronde)
            self.last_woord = nieuw_woord  # Onthoudt laatste woord om straks te kunnen verwijderen
        else:
            return None

        return nieuw_woord

    def start_nieuwe_ronde(self, count_up=True):
        """Functie om een nieuwe ronde te starten.
        --> Reset de woorden in ronde naar alle woorden in hoed."""
        self.woorden_in_ronde = self.woorden_in_hoed.copy()
        self.last_woord = None
        if count_up:
            self.ronde_count += 1

    def start_nieuwe_beurt(self):
        """Functie om een nieuwe beurt te krijgen.
        --> wissel van team dat aan de beurt is. Door naar de volgende.
        """
        self.team_index_aan_beurt += 1
        if self.team_index_aan_beurt >= len(self.teams):
            self.team_index_aan_beurt = 0
        self.last_woord = None

    def start_nieuw_spel(self):
        """Functie om nieuw spel te starten
        Puntentelling resetten. index_aan_beurt op random. Weergeven welk team mag starten.
        """
        self.team_scores = np.zeros(len(self.teams))
        self.team_index_aan_beurt = np.random.randint(len(self.teams))
        self.ronde_count = 1
        self.last_woord = None

    def leeg_de_hoed(self):
        """Functie om hoed leeg te maken. Kans voor nieuwe kaartjes."""
        self.woorden_in_hoed = []
        self.woorden_in_ronde = []


@app.route("/setup_spel", methods=['GET', 'POST'])
def setup_spel():
    form = VerzamelAlleWoorden(request.form)

    if request.method == 'POST':  # Er moet een woord extra in de hoed
        woord = request.form['woord_in_hoed']
        if woord is not '':
            flash('Yeah, je woord zin in de hoed! ' + woord)
            spel.woorden_in_hoed.append(woord)
            spel.start_nieuwe_ronde(count_up=False)
        else:
            flash('Enter een valide woord! Dit is geen woord..')

    return render_template('setup_spel.html', form=form)


@app.route("/speel_het_spel", methods=['GET', 'POST'])
def speel_het_spel():
    form = SpeelHetSpel(request.form)

    if request.method == 'POST':
        if request.form['submit_button'] == 'Alles terug in de hoed':
            spel.start_nieuwe_ronde()
            flash('Alle kaartjes zitten weer in de hoed. Tijd voor ronde nummer {}!! '
                  'Team {} is aan de beurt!'.format(spel.ronde_count, spel.teams[spel.team_index_aan_beurt]))

        if request.form['submit_button'] == 'Wissel van beurt':
            spel.start_nieuwe_beurt()
            flash('Team {} is aan de beurt!'.format(spel.teams[spel.team_index_aan_beurt]))

        if request.form['submit_button'] == 'Pak een woord':
            nieuw_woord = spel.nieuw_woord()
            if nieuw_woord is not None:
                flash('Je nieuwe woord is: ' + nieuw_woord)
            else:
                flash('Einde van de ronde is bereikt. Druk op "Alles terug in de hoed" voor nog een ronde!')

        if request.form['submit_button'] == 'Tussenstand':
            tussenstand_string = 'De tussenstand is: \n'
            for team, score in zip(spel.teams, spel.team_scores):
                tussenstand_string += 'Team {}: {}\n'.format(team, int(score))
            flash(tussenstand_string)

        if request.form['submit_button'] == 'Start nieuw spel':
            spel.start_nieuw_spel()
            flash('Team {} mag het spel starten! Veel plezier!'.format(spel.teams[spel.team_index_aan_beurt]))

        if request.form['submit_button'] == 'Leeg de hoed(!)':
            spel.leeg_de_hoed()
            flash('De hoed is weer leeg. Ga naar XXXXXX om woorden in de hoed te stoppen.')

    return render_template('speel_het_spel.html', form=form)

# TODO: Timer functionality??
# TODO: Teams functionality??


if __name__ == "__main__":
    spel = SpelMetDeHoed()
    app.run()
