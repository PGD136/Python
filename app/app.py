from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/1')
def One():
    return '{msg:"1  Page}'

@app.route('/2')
def Two():
    return '{msg:"2  Page}'


if __name__ == '__main__':
    app.run(debug=True)