from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from os import getenv 

app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI_flask')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    purchase_list = db.relationship('Purchase_list', backref='customer') 

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float(10,2), nullable=False)
    purchase_list = db.relationship('Purchase_list', backref='product')

class Purchase_list(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)

if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')