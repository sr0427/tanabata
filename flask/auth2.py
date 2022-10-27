from flask import Flask, render_template, request

# webアプリをつくる
app = Flask(__name__)


# routeをつくる
@app.route('/auth2')
def auth2():
    return render_template('auth2.html')


@app.route('/output2', methods=['POST'])
def output2():
    # IDとパスワードをもらう
    id = request.form['id']
    pwd = request.form['pwd']

    # データファイル（id.txt）を開いて、IDとパスワードを確認する
    file = open('id.txt', 'r')

    flag = 0

    for line in file:
        if id in line and pwd in line:
            flag = 1
            break
        else:
            flag = 0

    # 確認した結果を、表示する
    if flag == 1:
        kekka = 'IDとパスワード、OKです。'
    else:
        kekka = 'IDかパスワードが、違います！'

    # ファイルを閉じる
    file.close()

    return kekka


# 実行する
if __name__ == '__main__':
    app.run(debug=True)

