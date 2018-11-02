# coding:utf-8

from flask import Flask, render_template
from models import db
from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)

# デバック
app.config['DEBUG'] = True

# 秘密キー
app.secret_key = 'development key'

# データベースを指定
app.config['SQLALCHEMY_DATABASE_URI'] = 'SQLite:///diary.db'
app.config['SQLALCHEMY_NATIVE_UNICODE'] = 'utf-8'
db.init_app(app)
db.app = app

@app.route("/")
def hello():
    return render_template("index.html")

migrate = Migrate(app, db)
manager = Manager(app)

if __name__ == "__main__":
    manager.run()