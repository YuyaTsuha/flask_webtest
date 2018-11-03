# coding: utf-8

from flask import Flask, render_template
from models import *
from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)
#デバッグ
app.config['DEBUG'] = True
#秘密キー
app.secret_key = 'development key'
#データベースを指定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_NATIVE_UNICODE'] = 'utf-8'
db.init_app(app)
db.app = app

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/book/index")
def book_index():
    """
    書籍一覧
    """
    a = Book.query.order_by(Book.id.asc())
    return render_template("book/index.html",
                            books=a)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='localhost', port='8080'))

if __name__ == "__main__":
    manager.run()