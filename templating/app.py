from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ben')
def ben():
    return render_template('ben.html')

@app.route('/harry')
def harry():
    return render_template('harry.html')

@app.route('/letterb')
def letterb():
    return render_template('letter_b.html')

if __name__ == "__main__":
    app.run(debug=True)