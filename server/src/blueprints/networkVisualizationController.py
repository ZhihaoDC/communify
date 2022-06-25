from flask import jsonify, request, Blueprint
import src.blueprints.preprocess as preprocess 
import hashlib


networkVisualizationController = Blueprint('networkVisualizationController', __name__)

@networkVisualizationController.route('/community-detection/network-visualization', methods=['POST'])
def visualize_network():
    try:
        file = request.files['file']

        graph = preprocess.preprocess_network(file)

        graph_json = preprocess.preprocess_json(graph)

        #Generate dataset hash identifier  
        md5_hash = hashlib.md5(file.read()).hexdigest() 

        return jsonify({'graph': graph_json, 
                        'algorithm':'network-visualization', 
                        'dataset_hash': md5_hash}), 200
    except:
        return jsonify({"errorMessage": "Invalid .csv format"}), 400
