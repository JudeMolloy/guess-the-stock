import random

from flask import render_template, url_for, session, request
from werkzeug.utils import redirect

from app import app
from app.forms import NameForm
from app.models import Leaderboard, StockData
from sqlalchemy import func
from guess import Data


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

    if request.method == "POST":
        data = request.form
        selected_answer= data.get('selected_answer')
        print(selected_answer)

        if selected_answer == session['answer']:
            session['score'] += 1
            return redirect(url_for('play'))
        else:
            return redirect(url_for('game_over'))

    score = session['score']
    stock = StockData.query.order_by(func.random()).first_or_404()
    answer = stock.name
    session['answer'] = answer
    stocks = [x for x in Data.stocks if x != answer]
    options = random.sample(stocks, 3)
    options.append(answer)
    random.shuffle(options)

    return render_template("play.html", score=score, stock_json_string=stock.json_string,
                           a=options[0], b=options[1], c=options[2], d=options[3])


@app.route('/game-over')
def game_over():
    # Save score THEN reset THEN render page.
    score = session['score']
    name = session['name']
    leaderboard_entry = Leaderboard(name=name, score=score)
    session['score'] = 0
    return render_template("game-over.html", name=name, score=score)
