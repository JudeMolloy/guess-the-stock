from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from jinja2 import Environment

env = Environment()

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.template_filter('pluralize')
def pluralize(number, singular = '', plural = 's'):
    if number == 1:
        return singular
    else:
        return plural


from app import routes, models