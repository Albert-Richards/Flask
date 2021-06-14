from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:fBraswjAuGuFBhOs@34.89.97.233/flaskdb"

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0')