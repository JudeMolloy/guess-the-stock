from app import db


class Leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    score = db.Column(db.Integer)

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return '<Leaderboard Entry: {} scored {}>'.format(self.name, self.score)


class StockData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    json_string = db.Column(db.String)

    def __init__(self, name, json_string):
        self.name = name
        self.json_string = json_string