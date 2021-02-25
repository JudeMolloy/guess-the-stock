from app import db


class Leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    score = db.Column(db.Integer)


    def __repr__(self):
        return '<Leaderboard Entry: {} scored {}>'.format(self.name, self.score)