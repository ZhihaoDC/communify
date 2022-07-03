from src import db
from sqlalchemy.sql import func


class UserExperiment(db.Model):
    __tablename__ = 'USER_EXPERIMENTS'
    __table_args__ = {'extend_existing': True}

    user_id = db.Column(db.Integer, db.ForeignKey("USERS.id"))
    experiment_id = db.Column(db.String(32), primary_key=True)
    creation_date = db.Column(db.Date, server_default=func.now(), nullable=False)
    category = db.Column(db.String(50))
    description = db.Column(db.String(300))
    network_json = db.Column(db.JSON, nullable=False)
    metrics = db.Column(db.JSON)
    
    user = db.relationship('User')

    @property
    def serialized(self):
        """Return object data in serializeable format"""
        return {
            'user_id': self.user_id,
            'experiment_id': self.experiment_id,
        }



class User(db.Model):
    __tablename__ = 'USERS'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(100))
    profile_description = db.Column(db.String(250))

    def serialize(self):
        return{
            "user_id": self.id,
            "username": self.username
        }