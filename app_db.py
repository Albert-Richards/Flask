from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI_local')

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0')