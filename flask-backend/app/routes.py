from flask import render_template, url_for, session, request
from werkzeug.utils import redirect

from app import app
from app.forms import NameForm
from app.models import Leaderboard


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # Create new db entry for current game session with name. Or can do this at the end.
        session['name'] = form.name.data
        session['score'] = 0
        return redirect(url_for("play"))
    return render_template("enter-name.html", form=form)



@app.route('/play', methods=['GET', 'POST'])
def play():
    #if request.method == "POST":

    #else:
        # answer =
        # session['answer'] = answer
    return render_template("play.html")


@app.route('/game-over')
def game_over():
    # Save score THEN reset THEN render page.
    score = session['score']
    name = session['name']
    leaderboard_entry = Leaderboard(name=name, score=score)
    session['score'] = 0
    return render_template("game-over.html")
    
@app.route('/time')
def get_current_time():
    return {'result': "Hello World"}