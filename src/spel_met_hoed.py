from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

import numpy as np
import random

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class VerzamelAlleWoorden(Form):
    woord_in_hoed = StringField('woord_in_hoed')


class SpelMetDeHoed:
    def __init__(self, teams=['Team A', 'Team B']):
        self.teams = teams
        self.team_scores = np.zeros(len(self.teams))
        self.woorden_in_hoed = []
        self.woorden_in_ronde = []
        self.team_index_aan_beurt = 0
        self.ronde_count = 0
        self.last_woord = None

    def nieuw_woord(self):
        """Funtie om nieuw woord op te vragen in een beurt.
        --> Geef nieuw woord, verwijder laatste woord uit de huidige ronde lijst.
        """
        if self.last_woord is not None:
            self.woorden_in_ronde.remove(self.last_woord)
        nieuw_woord = random.choice(self.woorden_in_ronde)
        self.last_woord = nieuw_woord
        return nieuw_woord

    def start_nieuwe_ronde(self):
        """Functie om een nieuwe ronde te starten.
        --> Reset de woorden in ronde naar alle woorden in hoed."""
        self.woorden_in_ronde = self.woorden_in_hoed
        self.ronde_count += 1

    def start_nieuwe_beurt(self):
        """Functie om een nieuwe beurt te krijgen.
        --> wissel van team dat aan de beurt is. Door naar de volgende.
        """
        self.team_index_aan_beurt += 1
        if self.team_index_aan_beurt >= len(self.teams):
            self.team_index_aan_beurt = 0



@app.route("/voeg_woorden_toe", methods=['GET', 'POST'])
def verzamel_de_input():
    form = VerzamelAlleWoorden(request.form)

    if request.method == 'POST':
        woord = request.form['woord_in_hoed']
        if woord is not '':
            flash('Ja, je woord zin in de hoed! ' + woord)
            spel.woorden_in_hoed.append(woord)

            if len(spel.woorden_in_hoed) == 3:
                spel.start_nieuwe_ronde()
                while len(spel.woorden_in_ronde) > 1:
                    print(len(spel.woorden_in_ronde))
                    print(spel.nieuw_woord())
        else:
            flash('Enter een valide woord! Dit is geen woord..')
    return render_template('verzamel_woorden.html', form=form)


if __name__ == "__main__":
    spel = SpelMetDeHoed()
    app.run()












# app = Flask(__name__)
#
# @app.route('/test')
# @app.route('/')
# def index():
#     return 'Index Page'
#
# def test():
#     return 'test2'
#
# @app.route('/hello')
# def hello():
#     return 'Hello, World'
#
# @app.route("/sign-up", methods=["GET", "POST"])
# def sign_up():
#
#     if request.method == "POST":
#
#         req = request.form
#
#         return redirect(request.url)
#
#     return render_template("public/sign_up.html")



if __name__ == "__main__":
    app.run()