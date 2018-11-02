from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Unicode, UnicodeText, ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import datetime

db = SQLAlchemy()

class Book(db.Model):
    """
    書籍モデル
    """
    # SQLに"books"テーブルを作成
    __tablename__ = "books"
    id = Column(Integer, primary_key=True) # idのカラムに整数値が入るように設定
    title = Column(Unicode(225)) # titleのカラムに255字以内のUnicodeを取ることができる
    auther = Column(Unicode(225))
    publisher = Column(Unicode(225))

    # 初期化(生成された時に呼び出される)
    def __init__ (title, auther, publisher):
        self.title = title.tiele()
        self.auther = auther.title()
        self.publisher = publisher.title()

class Diary(db.Model):
    """
    感想モデル
    """
    # SQLに"diaries"テーブルを作成
    __tabkename__ = "diaries"
    id = Column(Integer, primary_key=True) # idのカラムに整数値が入るように設定
    date = Column(Unicode(225)) # dateのカラムに255字以内のUnicodeを取ることができる
    book_title = Column(Unicode(225), ForeignKey("books.title")) # booksテーブルのtitleとリレーションを定義
    implession = Column(UnicodeText)

    # 書籍とのリレーションを作成
    book = relationship("Book", backref=backref('diaries', order_by=id))

    #初期化
    def __init__(book_title, impression):
        self.date = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        self.book_title = book_title.title()
        self.impression = impression.title()