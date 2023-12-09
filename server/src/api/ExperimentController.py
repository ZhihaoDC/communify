from flask import Blueprint, request
from flask import json
import src.api.__network_formatter__ as nw_formatter
from src.models.ExperimentModel import Experiment
from src.models.DatasetModel import Dataset
from src.services import DatasetService
from src.services import ExperimentService
import sys
import base64
from codecs import encode

ExperimentController = Blueprint('ExperimentController', __name__)


@ExperimentController.route('/save-experiment/<user_id>', methods=['POST'])
def save_experiment(user_id):
    def __apply_default_values__(request_json, default_values):
        for key, value in default_values.items():
            if key not in request_json:
                request_json[key] = value
        return request_json
        

    request_json = request.get_json()
    
    request_json = __apply_default_values__(request_json, 
                                            default_values={
                                                'experiment_id': None,
                                                'experiment_name': request_json["dataset_name"],
                                                'description': ""
                                            }
    )
    keys_to_check = ['network_json', 'dataset_id', 'dataset_name']

    if all(request_json.get(key) for key in keys_to_check):
    
        added_dataset = DatasetService.add_instance(Dataset,
                                                    id=request_json['dataset_id'],
                                                    name=request_json['dataset_name'],
                                                    json=request_json['network_json'],
                                                    user_id=user_id)

        added_experiment = ExperimentService.add_instance(Experiment,
                                        user_id=user_id,
                                        experiment_id=request_json['experiment_id'],
                                        experiment_name = request_json['experiment_name'],
                                        network_json=request_json['network_json'],
                                        category=request_json['category'],
                                        metrics=request_json['metrics'],
                                        visualization_params=request_json['visualization_params'],
                                        dataset_id = added_dataset['id'],
                                        dataset_name = added_dataset['name'],
                                        thumbnail= base64.decodebytes(encode(request_json['thumbnail'])),
                                        description = request_json['description']
                                        )
                                     
        return json.jsonify({"successMessage": "File saved",
                             'Access-Control-Allow-Origin': '*',
                             'experiment': added_experiment}), 200
    else:
        return json.jsonify({"errorMessage": "Invalid experiment format. Please try again."}), 400


@ExperimentController.route('/get-experiments/<user_id>', methods=['GET'])
def get_experiments(user_id):
    data = ExperimentService.get_all_by_user_id(
        Experiment,
        user_id=user_id
    )
    return json.jsonify({'status': 'success',
                        'experiments': data}), 200


@ExperimentController.route('/delete-experiment/<user_id>/<experiment_id>', methods=['DELETE'])
def delete_experiments(user_id, experiment_id):
    deleted_experiment = ExperimentService.delete_by_id(Experiment, user_id, experiment_id)
    return json.jsonify({'status': 'success',
                        'experiments': deleted_experiment}), 200


