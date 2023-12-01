from flask import jsonify, request, Blueprint
import src.api.__network_formatter__ as nw_formatter
from src.api.__input_manager__ import InputManager
import hashlib
import json


GraphVisualizationController = Blueprint('GraphVisualizationController', __name__)

@GraphVisualizationController.route('/graph-visualization', methods=['POST'])
def visualize_network():
    try:
        input = InputManager(request.files)
        file, file_name, file_hash, columns = input.file, input.file_name, input.file_hash, input.csv_columns       

        graph = nw_formatter.file_to_network(file, columns)
        graph_json = nw_formatter.network_to_json(graph)


        return jsonify({    
                        'network_json': graph_json,
                        'communities': None,
                        'metrics' : None,
                        'category': 'Visualización',
                        'dataset_name': file_name,
                        'dataset_id': file_hash
                    }), 200
    except:
        return jsonify({"errorMessage": "Invalid .csv format"}), 400
