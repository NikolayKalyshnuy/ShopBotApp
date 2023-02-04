from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import MockCard

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def catalog():
    cards = [MockCard(1, "qwer", 123.00), MockCard(2, "asd", 456.86), MockCard(3, "zxc", 789.23)]
    return render_template("catalog.html", cards=cards)


if __name__ == '__main__':
    app.run()
