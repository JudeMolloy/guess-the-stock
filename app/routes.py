import random

from flask import render_template, url_for, session, request
from werkzeug.utils import redirect

from app import app
from app.forms import NameForm
from app.models import Leaderboard, StockData
from sqlalchemy import func, desc
from guess import Data


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # Create new db entry for current game session with name. Or can do this at the end.
        session['name'] = form.name.data
        session['score'] = 0
        return redirect(url_for("play"))
    leaderboard_data = Leaderboard.query.order_by(desc(Leaderboard.score)).limit(10).all()
    print(leaderboard_data)
    return render_template("enter-name.html", form=form, leaderboard=leaderboard_data)



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


    stock = StockData.query.order_by(func.random()).first_or_404()
    answer = stock.name
    session['answer'] = answer
    stocks = [x for x in Data.stocks if x != answer]
    options = random.sample(stocks, 3)
    options.append(answer)
    random.shuffle(options)
    score = session['score']

    return render_template("play.html", score=score, stock_json_string=stock.json_string,
                           a=options[0], b=options[1], c=options[2], d=options[3])


@app.route('/game-over')
def game_over():
    # Save score THEN reset THEN render page.
    score = session['score']
    name = session['name']
    leaderboard_entry = Leaderboard(name=name, score=score)
    leaderboard_entry.save_to_db()
    session['score'] = 0

    img = "elon-cry.gif"
    message = "That was so bad you made Elon cry."

    if score > 9:
        img = "jordan.gif"
        message = "You are The Wolf of Wall Street."
    elif score > 4:
        img = "mark-cuban.gif"
        message = "Mark Cuban thinks you have potential."
    elif score > 0:
        img = "zucc.webp"
        message = "Go back to eating toast without butter like Zucc."


    return render_template("game-over.html", name=name, score=score, img=img, message=message)
