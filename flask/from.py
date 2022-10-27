from flask import Flask, render_template, request
  ...
  ...
  ...
  
@app.route('/result', methods=['POST'])
def result():
    # データをもらう
  id = request.form['id']
    
    # データを表示する
  return id
