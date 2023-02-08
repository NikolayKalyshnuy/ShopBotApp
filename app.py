from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import models, routes





if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
