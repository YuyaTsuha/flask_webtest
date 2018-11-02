# coding: utf-8
from flask import Flask, render_template

app = Flask(__name__)

# 内容に変更があると自動で変更される
app.config['DEBUG'] = True


@app.route('/') # ルートにアクセスすると以下のプログラムが実行される
def hello():
    return render_template("index.html") # テンプレートからHTMLファイルを読み込む


if __name__ == '__main__':
    app.run()
