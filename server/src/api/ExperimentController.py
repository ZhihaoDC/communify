from flask import Blueprint, request
from flask import json
from src.models.ExperimentModel import Experiment
from src.api.DatasetController import save_dataset
from src.services import ExperimentService
import base64
from codecs import encode

ExperimentController = Blueprint('ExperimentController', __name__)


@ExperimentController.route('/save-experiment/<user_id>', methods=['POST'])
def save_experiment(user_id):
    request_json = request.get_json()

    default_values = {
                    'experiment_id' : None,
                    'experiment_name': request_json["dataset_name"],
                    'description': ""
                    }

    for key, value in default_values.items():
        if key not in request_json:
            request_json[key] = value

    if 'dataset_id' in request_json:
        added_dataset = save_dataset(user_id=user_id)
        
        added_experiment = ExperimentService.add_instance(Experiment,
                                        user_id=user_id,
                                        experiment_id=request_json['experiment_id'],
                                        experiment_name = request_json['experiment_name'],
                                        network_json=request_json['network_json'],
                                        category=request_json['category'],
                                        metrics=request_json['metrics'],
                                        dataset_id = added_dataset['id'],
                                        dataset_name = added_dataset['name'],
                                        thumbnail= base64.decodebytes(encode(request_json['thumbnail'])),
                                        description = request_json['description']
                                        )                                                      
        return json.jsonify({"successMessage": "File saved",
                             'Access-Control-Allow-Origin': '*',
                             'experiment': added_experiment}), 200
    else:
        return json.jsonify({"errorMessage": "Invalid .csv format"}), 400


@ExperimentController.route('/get-experiments/<user_id>', methods=['GET'])
def get_experiments(user_id):
    data = ExperimentService.get_all_by_user_id(
        Experiment,
        user_id=user_id
    )
    # print(dict({k: v for k, v in data}))
    return json.jsonify({'status': 'success',
                        'experiments': data}), 200


@ExperimentController.route('/delete-experiment/<user_id>/<experiment_id>', methods=['DELETE'])
def delete_experiments(user_id, experiment_id):
    deleted_experiment = ExperimentService.delete_by_id(Experiment, experiment_id)
    return json.jsonify({'status': 'success',
                        'experiments': deleted_experiment}), 200