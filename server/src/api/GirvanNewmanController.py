from flask import request, Blueprint
from flask.json import jsonify
import hashlib
import json
from networkx import cytoscape_graph
from werkzeug.utils import secure_filename


#Import custom modules
import src.api.__network_formatter__ as nw_formatter
from src.api.__input_manager__ import InputManager
from src.community_detection import girvan_newman_algorithm as gn
from src.models.DatasetModel import Dataset
from src.services import DatasetService


GirvanNewmanController = Blueprint('GirvanNewmanController', __name__)


#Main method
@GirvanNewmanController.route("/community-detection/girvan-newman", methods=['POST'])
def apply_girvan_newman():
    try:
        input = InputManager(request.files)
        file, file_name, file_hash, columns = input.file, input.file_name, input.file_hash, input.csv_columns        

        #Preprocess network from file
        graph = nw_formatter.file_to_network(file, columns)

        #Apply girvan-newman method
        dendrogram, modularity = gn.Girvan_Newman_2004(graph)
        GN_communities = gn.dendrogram_to_community(dendrogram)

        graph_json = nw_formatter.network_to_json(graph, GN_communities)

        return jsonify(
                        {'network_json': graph_json,
                        'communities': GN_communities,
                        'metrics' : {'modularity': modularity},
                        'category' : 'Girvan-Newman',
                        'dataset_name': file_name,
                        'dataset_id': file_hash
                        }), 200
    except:
        return jsonify({"errorMessage": "Invalid .csv format"}), 400



@GirvanNewmanController.route("/community-detection/girvan-newman/<dataset_id>", methods=['GET'])
def apply_girvan_newman_to_dataset(dataset_id):
    try:
        dataset = DatasetService.get_by_id(Dataset, dataset_id)
        graph = cytoscape_graph(dataset['json'])

        #Apply girvan-newman method
        dendrogram, modularity = gn.Girvan_Newman_2004(graph)
        GN_communities = gn.dendrogram_to_community(dendrogram)
        graph_json = nw_formatter.network_to_json(graph, GN_communities)

        return jsonify(
                        {'network_json': graph_json,
                        'communities': GN_communities,
                        'metrics' : {'modularity': modularity},
                        'category' : 'Girvan-Newman',
                        'dataset_name': dataset['name'],
                        'dataset_id': dataset['id']
                        }), 200
    except:
        return jsonify({"errorMessage": "Invalid .csv format"}), 400
        

