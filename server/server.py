from flask import Flask, request, jsonify
from flask_cors import CORS
from louvainController import louvainController
from girvanNewmanController import girvanNewmanController

############################################## APP #################################################
app = Flask(__name__)
app.config.from_object(__name__)
app.register_blueprint(louvainController)
app.register_blueprint(girvanNewmanController)
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong')

if __name__ == '__main__':
    app.run()