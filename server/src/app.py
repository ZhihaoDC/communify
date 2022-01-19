from flask import Flask, request, jsonify
from flask_cors import CORS
from src.blueprints.louvainController import louvainController
from src.blueprints.girvanNewmanController import girvanNewmanController
from src.blueprints.networkVisualizationController import networkVisualizationController

############################################## APP #################################################


def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)
    app.register_blueprint(louvainController)
    app.register_blueprint(girvanNewmanController)
    app.register_blueprint(networkVisualizationController)

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()