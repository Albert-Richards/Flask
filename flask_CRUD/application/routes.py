from application import app, db
from application.models import Games

@app.route('/add')
def add():
    new_game = Games(name="New Game")
    db.session.add(new_game)
    db.session.commit()
    return "Added new game to database"

@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string

@app.route('/update/<name>')
def update(name):
    first_game = Games.query.first()
    first_game.name = name
    db.session.commit()
    return first_game.name

@app.route('/delete')
def delete():
    old_game = Games.query.first()
    db.session.delete(old_game)
    db.session.commit()
    return "You have deleted the first game from database"

@app.route('/number')
def number():
    return str(len(Games.query.all()))
