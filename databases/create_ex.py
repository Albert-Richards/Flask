from app_ex import db, Customers, Products, Purchase_list

db.drop_all()
db.create_all() # Creates all table classes defined

db.session.commit()