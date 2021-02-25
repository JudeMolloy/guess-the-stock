from flask import render_template, url_for, session
from werkzeug.utils import redirect

from app import app
from app.forms import NameForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # Create new db entry for current game session with name. Or can do this at the end.
        session['name'] = form.name.data
        session['score'] = 0
        return redirect(url_for("play"))
    return render_template("enter-name.html", form=form)


@app.route('/play')
def play():
    return render_template("play.html")

@app.route('/game-over')
def game_over():
    return render_template("game-over.html")