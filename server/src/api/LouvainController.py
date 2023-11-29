from flask import request, Blueprint
from flask.json import jsonify
import json
import hashlib
from networkx import cytoscape_graph
from werkzeug.utils import secure_filename
import sys


#import custom modules
from src.community_detection import louvain_algorithm as louvain
import src.api.preprocess as preprocess 
from src.models.DatasetModel import Dataset
from src.services import DatasetService
from networkx.algorithms.community.quality import modularity as nx_modularity


LouvainController = Blueprint('LouvainController', __name__)


#Main method
@LouvainController.route('/community-detection/louvain', methods=['POST'])
def apply_louvain():

    try: 
        file = request.files['file']
        dataset_name = secure_filename(file.filename.replace(".csv", ""))

        if (len(request.files) > 1) and ('columns' in request.files):
            columns = request.files['columns'].read().decode('utf8').replace("'",'"')
            columns_json= json.loads(columns)
        else:
            columns_json= None  

        graph = preprocess.file_to_network(file, columns_json)

        #Apply louvain method
        supergraph, communities = louvain.Louvain(graph)
        last_community = louvain.last_community(graph, communities)
        modularity = nx_modularity(graph, louvain.dendrogram(last_community))

        graph_json = preprocess.network_to_json(graph, last_community)

        #Generate dataset hash identifier
        file.seek(0) #reset file pointer
        md5_hash = hashlib.md5(file.read()).hexdigest()

        return jsonify({    
                        'network_json': graph_json,
                        'communities': last_community,
                        'metrics' : {'modularity': modularity},
                        'category': 'Louvain',
                        'dataset_name': dataset_name,
                        'dataset_id': md5_hash
                    }), 200
    except:
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
        graph_json = preprocess.network_to_json(graph, last_community)

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