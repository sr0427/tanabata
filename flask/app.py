from flask import Flask

app = Flask(__name__)



@app.route('/hello')
def hello():
    return '<h1>hello!<h1>'


@app.route('/ciao')
def ciao():
    return '<h1>Ciao!<h1>'



if __name__=='__main__':
    app.run(debug=True)
