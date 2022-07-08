from src import db
import base64

class Experiment(db.Model):
    __tablename__ = 'EXPERIMENTS'
    __table_args__ = {'extend_existing': True}

    user_id = db.Column(db.Integer, db.ForeignKey("USERS.id"))
    experiment_id = db.Column(db.String(32), primary_key=True)
    creation_date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    network_json = db.Column(db.JSON, nullable=False)
    category = db.Column(db.String(50))
    description = db.Column(db.String(300))
    metrics = db.Column(db.JSON)
    thumbnail = db.Column(db.BLOB, nullable=False)
    
    user = db.relationship('User', passive_deletes=True)

    @property
    def serialized(self):
        """Return object data in serializeable format"""
        return {
            'user_id': self.user_id,
            'experiment_id': self.experiment_id,
            'creation_date' : self.creation_date.strftime("%Y/%m/%d, %H:%M"),
            'network_json' : self.network_json,
            'category' : self.category,
            'description' : self.description,
            'metrics': self.metrics,
            'thumbnail': base64.encodebytes(self.thumbnail).decode('utf-8')
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