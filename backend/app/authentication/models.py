from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(18), index = True, unique = True)
    email = db.Column(db.String(64), index = True, unique = True)
    password = db.Column(db.String(64))
    account_number = db.Column(db.String(18))
    balance = db.Column(db.Integer)

    def __repr__(self):
        return 'User {}'.format(self.user_name)