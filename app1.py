from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/squared/<int:number>', methods=['GET','POST'])
def squared(number):
    return str(number**2)

if __name__ == "__main__":
    app.run(debug=True)