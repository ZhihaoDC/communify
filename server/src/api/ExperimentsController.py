from flask import Blueprint, request
from flask import json
from src.models.ExperimentModel import Experiment
from src.services import ExperimentService
import base64
from codecs import encode

ExperimentsController = Blueprint('ExperimentsController', __name__)


@ExperimentsController.route('/save-experiment', methods=['POST'])
def save_experiment():
    request_json = request.get_json()

    default_values = {'experiment_name': request_json["dataset_name"],
                    'description': ""}
    for key, value in default_values.items():
        if key not in request_json:
            request_json[key] = value

    if 'dataset_hash' in request_json:
        ExperimentService.add_instance(Experiment,
                                        user_id=1,
                                        experiment_name = request_json['experiment_name'],
                                        network_json=request_json['network_json'],
                                        category=request_json['category'],
                                        metrics=request_json['metrics'],
                                        dataset_name = request_json['dataset_name'],
                                        dataset_hash = request_json['dataset_hash'],
                                        thumbnail= base64.decodebytes(encode(request_json['thumbnail'])),
                                        # description=bytes("Descripcion introducida por el usuario", encoding='utf-8') #hardcodeado
                                        description = request_json['description']
                                        )
                                                                
        return json.jsonify({"successMessage": "File saved",
                             'Access-Control-Allow-Origin': '*'}), 200
    else:
        return json.jsonify({"errorMessage": "Invalid .csv format"}), 400


@ExperimentsController.route('/get-experiments/<user_id>', methods=['GET'])
def get_experiments(user_id):
    data = ExperimentService.get_all_by_user_id(
        Experiment,
        user_id=user_id
    )
    # print(dict({k: v for k, v in data}))
    return json.jsonify({'status': 'success',
                        'experiments': data}), 200
