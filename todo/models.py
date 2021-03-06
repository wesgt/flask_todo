import datetime
from sqlalchemy import Column, Integer, String, DateTime
from todo.database import Base, db_session


class TodoMemo(Base):
    __tablename__ = 'todo_memo'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    memo = Column(String(50))
    state = Column(String(50))
    create_date = Column(DateTime)


    def __init__(self, user_id, memo, state='incomplete',
                 create_date=datetime.datetime.today()):
        self.user_id = user_id
        self.memo = memo
        self.state = state
        self.create_date = create_date

    def __repr__(self):
        return '<TodoMemo %r>' % self.memo

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()
