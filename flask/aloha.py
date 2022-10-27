from flask import Flask, render_template, request
 
app = Flask(__name__, static_folder='./templates/images')

# 表示するため、routingする
@app.route('/')
def start():
    return 'ALOHA!'
   
 # http://127.0.0.1:5000/hello
@app.route('/hello')
def hello():
    msg = 'こんにちは'
    return msg

# http://127.0.0.1:5000/weather
@app.route('/weather')
def weather():
    msg = '雨がふっています'
    return msg

# HTMLファイルを表示する
# http://127.0.0.1:5000/me
@app.route('/me')
def me():
    return render_template('me.html')
 
 # http://127.0.0.1:5000/favorite
@app.route('/favorite')
def favorite():
    return render_template('favorite.html')

# http://127.0.0.1:5000/form
@app.route('/form')
def form():
    return render_template('form.html')

#データをもらう＆表示する
@app.route('/result', methods=['POST'])
def result():
    #データをもらう
     id = request.form['id']
    #データを表示する
     return id

if __name__=='__main__':
    app.run(debug=True)
