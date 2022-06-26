from src import db

class UserExperiment(db.Model):
    __tablename__ = 'USER_EXPERIMENTS'
    user_id = db.Column(db.Integer, db.ForeignKey("USERS.id"))
    experiment_id = db.Column(db.String(32), primary_key=True)
    user = db.relationship('User')


class User(db.Model):
 __tablename__ = 'USERS'
 id = db.Column(db.Integer, auto_increment=True, primary_key=True)
 username = db.Column(db.String(25), nullable=False)
 email = db.Column(db.String(50), nullable=False)
 firstname = db.Column(db.String(50), nullable=False)
 lastname = db.Column(db.String(100))
 profile_description = db.Column(db.String(250))