from flask import Flask, render_template, request
  
  # appを作る
app = Flask(__name__)
  
  # routeを作る
@app.route('/')
def start():
    return 'Good morning.'
  
  # 「メッセージを入力するページ」のrouteを作る
@app.route('/msg')
def msg():
    return render_template('msg.html')
  
  # もらったメッセージを、表示するための、routeを作る
@app.route('/output', methods=['POST'])
def output():
      # データをもらう; 名前は msg
    msg = request.form['msg']
    if msg=='hello':
        kekka = 'こんにちは'
    else
        kekka = msg
      # データを出力する（表示する）
    return kekka
  
  
  # 実行する（必ず、いちばん下に書く）
if __name__=='__main__':
    app.run(debug=True)