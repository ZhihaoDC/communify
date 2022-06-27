from . import app_config
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from src.plugins.SQLAlchemy import db
from src.api.LouvainController import LouvainController
from src.api.GirvanNewmanController import GirvanNewmanController
from src.api.GraphVisualizationController import GraphVisualizationController
from src.api.ExperimentsController import ExperimentsController
############################################## APP #################################################


def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)

    # Register controller routes
    app.register_blueprint(LouvainController)
    app.register_blueprint(GirvanNewmanController)
    app.register_blueprint(GraphVisualizationController)
    app.register_blueprint(ExperimentsController)

    # Database config
    app.config['SQLALCHEMY_DATABASE_URI'] = app_config.DATABASE_CONNECTION_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.app_context().push()

    # Start app and database
    db.init_app(app)
    # db.create_all()
    
    migrate = Migrate(app, db)

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)