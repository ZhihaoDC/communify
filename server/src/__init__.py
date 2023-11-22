
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from sqlalchemy.exc import OperationalError
import time

import json

from . import app_config
from src.plugins.SQLAlchemy import db
from src.api.ExperimentController import ExperimentController
from src.api.DatasetController import DatasetController
from src.api.LouvainController import LouvainController
from src.api.GirvanNewmanController import GirvanNewmanController
from src.api.GraphVisualizationController import GraphVisualizationController
from src.models.UserModel import User
from src.models.DatasetModel import Dataset
############################################## APP #################################################


def create_app(env="PROD"):
    app = Flask(__name__)
    app.config.from_object(__name__)

    # Register controller routes
    app.register_blueprint(LouvainController)
    app.register_blueprint(GirvanNewmanController)
    app.register_blueprint(GraphVisualizationController)
    app.register_blueprint(ExperimentController)
    app.register_blueprint(DatasetController)

    # Database config
    app.config['SQLALCHEMY_DATABASE_URI'] = app_config.DATABASE_CONNECTION_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.app_context().push()

    if env != 'TEST':
        # Start app and database
        db.init_app(app)

        #Retry on connection failure
        MAX_RETRIES = 10
        TIME_RETRY_SECS = 5
        retry_count = MAX_RETRIES
        is_db_connected = False
        while retry_count >= 0 and not is_db_connected:
            try:
                db.drop_all()
                db.create_all()
                is_db_connected = True
            except OperationalError:
                print(f"Attempting to reconnect to database... (Retry again in {TIME_RETRY_SECS} seconds...)")
                time.sleep(TIME_RETRY_SECS)
                if retry_count == 0:
                    print(f"Connection failed. (Tried to reconnect {MAX_RETRIES} times")

        # migrate = Migrate(app, db)
        init_database()

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    return app


def init_database():
    default_user = User(username="david19",
        email="david19@gmail.com",
        firstname="david", 
        lastname="fernandez", 
        profile_description="data scientist")
        
    db.session.add(default_user)
    
    # dataset_csv = pd.read_csv("./static/game-of-thrones-books/book1.csv")
    # dataset_json = dataset_csv.to_json("./static/game-of-thrones-books/book1.json", orient='records', indent=2)
    with open("./static/game-of-thrones-books/book1.json") as f:
        book1 = json.load(f)
        default_dataset = Dataset(id="12345678912345678912345678912345", json=json.dumps(book1), user_id=default_user.id)
    db.session.add(default_dataset)

    db.session.commit()


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)