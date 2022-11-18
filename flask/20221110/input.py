data = input('IDを入力してください')
file = open('data.txt', 'a')
file.write(data)
file.close()