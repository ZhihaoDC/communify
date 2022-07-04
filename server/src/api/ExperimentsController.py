from flask import Blueprint, request
from flask import json
from src.models.models import UserExperiment
from src.services import experiment_service
import base64

ExperimentsController = Blueprint('ExperimentsController', __name__)


@ExperimentsController.route('/save-experiment', methods=['POST'])
def save_experiment():
    request_json = request.get_json()
    # if all(keys in request_json for keys in ['user_id', 'dataset_hash']):
    if 'dataset_hash' in request_json:
        experiment_service.add_instance(UserExperiment,
                                        user_id=1,
                                        experiment_id=request_json['dataset_hash'],
                                        category=request_json['algorithm'],
                                        metrics=request_json['metrics'],
                                        network_json=request_json['graph'],
                                        thumbnail=request_json['thumbnail'],
                                        description=bytes("prueba", encoding='utf-8')
                                        )
        return json.jsonify({"successMessage": "File saved",
                             'Access-Control-Allow-Origin': '*'}), 200
    else:
        return json.jsonify({"errorMessage": "Invalid .csv format"}), 400


@ExperimentsController.route('/get-experiments/<user_id>', methods=['GET'])
def get_experiments(user_id):
    data = experiment_service.get_all_by_user_id(
        UserExperiment,
        user_id=user_id
    )
    print(dict({k: v for k, v in data}))
    return json.jsonify({'status': 'success',
                        'experiments': data}), 200


# @ExperimentsController.route('/save-experiment', methods=['POST'])
# def save_experiment():
#     # try:
#     json = request.get_json()
#     print(json.keys())
#     #pendiente: extraer info del user y comprobar que esta logeado
#     user_id  = 1 #usamos este temporalmente
#     experiment_id = json['dataset_hash']

#     cursor = db.connection.cursor()

#     cursor.execute("""INSERT INTO USER_EXPERIMENTS(user_id, experiment_id) VALUES (%s, %s)""", (user_id, experiment_id))

#     db.connection.commit()

#     return jsonify({"successMessage": "File saved",
#                     'Access-Control-Allow-Origin': '*'}), 200
#     # except:
#     #     return jsonify({"errorMessage": "Invalid .csv format"}), 400
