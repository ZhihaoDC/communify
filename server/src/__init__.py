from . import app_config
from flask import Flask
from flask_cors import CORS
from src.extensions.SQLAlchemy import db
from src.api.LouvainController import LouvainController
from src.api.GirvanNewmanController import GirvanNewmanController
from src.api.GraphVisualizationController import GraphVisualizationController
from src.api.ExperimentsController import ExperimentsController
############################################## APP #################################################


def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)
    app.register_blueprint(LouvainController)
    app.register_blueprint(GirvanNewmanController)
    app.register_blueprint(GraphVisualizationController)
    app.register_blueprint(ExperimentsController)

    app.config['SQLALCHEMY_DATABASE_URI'] = app_config.DATABASE_CONNECTION_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.app_context().push()

    db.init_app(app)
    db.create_all()

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)