from ..extensions import mysql
from flask import Blueprint, request
from flask.json import jsonify

ExperimentsController = Blueprint('ExperimentsController', __name__)

#Main method
@ExperimentsController.route('/save-experiment', methods=['POST'])
def save_experiment():
    # try:
    json = request.get_json()
    print(json.keys())
    #pendiente: extraer info del user y comprobar que esta logeado
    user_id  = 1 #usamos este temporalmente
    experiment_id = json['dataset_hash']

    cursor = mysql.connection.cursor()

    cursor.execute("""INSERT INTO USER_EXPERIMENTS(user_id, experiment_id) VALUES (%s, %s)""", (user_id, experiment_id))

    mysql.connection.commit()

    return jsonify({"successMessage": "File saved", 
                    'Access-Control-Allow-Origin': '*'}), 200
    # except:
    #     return jsonify({"errorMessage": "Invalid .csv format"}), 400