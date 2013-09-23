import datetime
from todo.model import db


class TodoMemo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    memo = db.Column(db.String(50))
    state = db.Column(db.String(50))
    create_date = db.Column(db.DateTime)

    def __init__(self, user_id, memo, state='incomplete',
                 create_date=datetime.datetime.today()):
        self.user_id = user_id
        self.memo = memo
        self.state = state
        self.create_date = create_date

    def __repr__(self):
        return '<TodoMemo %r>' % self.memo

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

