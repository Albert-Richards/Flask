from flask import Flask

squared = Flask(__name__)

@squared.route('/')
@squared.route('/home/<int:number>', methods=['GET','POST'])
def home(number):
    return str(number**2)

if __name__ == "__main__":
    squared.run(debug=True)