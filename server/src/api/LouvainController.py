from flask import request, Blueprint
from flask.json import jsonify
import hashlib
from networkx import cytoscape_graph
import sys


#import custom modules
from src.community_detection import louvain_algorithm as louvain
import src.api.__network_formatter__ as nw_formatter
from src.api.__input_manager__ import InputManager
from src.models.DatasetModel import Dataset
from src.services import DatasetService
from networkx.algorithms.community.quality import modularity as nx_modularity


LouvainController = Blueprint('LouvainController', __name__)


#Main method
@LouvainController.route('/community-detection/louvain', methods=['POST'])
def apply_louvain():

    try: 
        input = InputManager(request.files)
        file, file_name, file_hash, columns = input.file, input.file_name, input.file_hash, input.csv_columns       

        graph = nw_formatter.file_to_network(file, columns)

        #Apply louvain method
        supergraph, communities = louvain.Louvain(graph)
        last_community = louvain.last_community(graph, communities)
        modularity = nx_modularity(graph, louvain.dendrogram(last_community))

        graph_json = nw_formatter.network_to_json(graph, last_community)


        return jsonify({    
                        'network_json': graph_json,
                        'communities': last_community,
                        'metrics' : {'modularity': modularity},
                        'category': 'Louvain',
                        'dataset_name': file_name,
                        'dataset_id': file_hash
                    }), 200
    except Exception as e:
        print(e, file=sys.stderr)
        return jsonify({"errorMessage": "Invalid .csv format"}), 500


@LouvainController.route("/community-detection/louvain/<user_id>/<dataset_id>", methods=['GET'])
def apply_louvain_to_dataset(user_id, dataset_id):
    try:
        dataset = DatasetService.get_by_id(Dataset, user_id, dataset_id)
        
        graph = cytoscape_graph(dataset['json'])

        #Apply louvain method
        supergraph, communities = louvain.Louvain(graph)
        last_community = louvain.last_community(graph, communities)
        modularity = nx_modularity(graph, louvain.dendrogram(last_community))
        graph_json = nw_formatter.network_to_json(graph, last_community)

        # print(dataset['id'], file=sys.stderr) #depurar

        return jsonify({    
                        'network_json': graph_json,
                        'communities': last_community,
                        'metrics' : {'modularity': modularity},
                        'category': 'Louvain',
                        'dataset_name': dataset['name'],
                        'dataset_id': dataset['id']
                    }), 200
    except Exception as e:
        return jsonify({"errorMessage": "Error interno del servidor" + str(e)}), 500

    
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()