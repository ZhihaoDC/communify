from flask import Blueprint, request
from flask import json, jsonify
import hashlib
from werkzeug.utils import secure_filename

import src.api.preprocess as preprocess 
from src.models.DatasetModel import Dataset
from src.services import DatasetService

DatasetController = Blueprint('DatasetController', __name__)


@DatasetController.route('/get-datasets/<user_id>', methods=['GET'])
def get_datasets(user_id):
    data = DatasetService.get_all_by_user_id(
        Dataset,
        user_id=user_id
    )
    return json.jsonify({'status': 'success',
                        'experiments': data}), 200


@DatasetController.route('/save-dataset', methods=['POST'])
def save_dataset():
    try:
        file = request.files['file']
        dataset_name = secure_filename(file.filename.replace(".csv", ""))

        if (len(request.files) > 1) and ('columns' in request.files):
            columns = request.files['columns'].read().decode('utf8').replace("'",'"')
            columns_json= json.loads(columns)
        else:
            columns_json= None

        graph = preprocess.file_to_network(file, columns_json)

        #Generate dataset hash identifier
        file.seek(0) #reset file pointer
        md5_hash = hashlib.md5(file.read()).hexdigest()

        added_dataset = DatasetService.add_instance(Dataset,
            id=md5_hash,
            name=dataset_name,
            json=graph
        )
        
        return jsonify(added_dataset), 200
    
    except:
        return jsonify({"errorMessage": "Invalid .csv format"}), 400

