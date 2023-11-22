from src import db


class User(db.Model):
    __tablename__ = 'USER'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(100))
    profile_description = db.Column(db.String(250))

    datasets = db.relationship('Dataset', passive_deletes=True)

    def serialize(self):
        return{
            "user_id": self.id,
            "username": self.username
        }