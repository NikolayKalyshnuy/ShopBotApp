from flask import Flask
from flask import render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import MockCard

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def catalog():
    cards = [
        MockCard(1, "qwe", 123.00, img_src=url_for('static', filename='images/mock/1.jpg')),
        MockCard(2, "asd", 456.86, img_src=url_for('static', filename='images/mock/2.png')),
        MockCard(3, "asd", 456.86, img_src=url_for('static', filename='images/mock/3.jpg')),
        MockCard(4, "asd", 456.86, img_src=url_for('static', filename='images/mock/4.jpg')),
        MockCard(5, "asd", 456.86, img_src=url_for('static', filename='images/mock/5.jpg')),
        MockCard(6, "asd", 456.86, img_src=url_for('static', filename='images/mock/6.jpg')),
        MockCard(7, "asd", 456.86, img_src=url_for('static', filename='images/mock/7.jpg')),
        MockCard(8, "zxc", 789.23, img_src=url_for('static', filename='images/mock/8.png'))]

    return render_template("catalog.html", cards=cards)


if __name__ == '__main__':
    app.run()
