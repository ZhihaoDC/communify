from flask import jsonify, request, Blueprint
import src.api.preprocess as preprocess 
import hashlib
import json


GraphVisualizationController = Blueprint('GraphVisualizationController', __name__)

@GraphVisualizationController.route('/community-detection/graph-visualization', methods=['POST'])
def visualize_network():
    try:
        file = request.files['file']
        if (len(request.files) > 1) and ('columns' in request.files):
            columns = request.files['columns'].read().decode('utf8').replace("'",'"')
            columns_json= json.loads(columns)
        else:
            columns_json= None

        graph = preprocess.file_to_network(file, columns_json)

        graph_json = preprocess.network_to_json(graph)

        #Generate dataset hash identifier  
        md5_hash = hashlib.md5(file.read()).hexdigest() 

        return jsonify({'network_json': graph_json, 
                        'category':'network-visualization', 
                        'dataset_id': md5_hash}), 200
    except:
        return jsonify({"errorMessage": "Invalid .csv format"}), 400
