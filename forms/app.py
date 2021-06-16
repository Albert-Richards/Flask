from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField, DateField, SelectField
from os import getenv
app = Flask(__name__)

app.config['SECRET_KEY'] = getenv('SKEY')

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    age = IntegerField('Your age')
    date = DateField('Enter the date')
    height = DecimalField('Your height', places=2)
    colour = SelectField('Your favourite colour', choices=[('blue','Blue'),('yellow','Yellow'),('red','Red')])
    submit = SubmitField('Add Name')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        age = form.age.data
        date = form.date.data
        height = form.height.data
        clolour = form.colour.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        else:
            return f'thank_you {first_name} {last_name}'

    return render_template('home.html', form=form, message=error)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')