from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:fBraswjAuGuFBhOs@34.89.97.233/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False, unique=True)
    rating = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(20))

if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')