from flask import Flask
from flask import render_template
from models import MockCard

app = Flask(__name__)


@app.route('/')
def catalog():
    cards = [MockCard(1, "qwer", 123), MockCard(2, "asd", 456), MockCard(3, "zxc", 789)]
    return render_template("catalog.html", cards=cards)


if __name__ == '__main__':
    app.run()
