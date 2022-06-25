from flask import request, Blueprint
from flask.json import jsonify
import json
import hashlib

#import custom modules
from src.scripts import louvain
import src.blueprints.preprocess as preprocess 
from networkx.algorithms.community.quality import modularity as nx_modularity


louvainController = Blueprint('louvainController', __name__)


#Main method
@louvainController.route('/community-detection/louvain', methods=['POST'])
def apply_louvain():
    # try: 
        file = request.files['file']
        if (len(request.files) > 1) and ('columns' in request.files):
            columns_file = request.files['columns']
            columns_bytes = columns_file.read().decode('utf8').replace("'",'"')
            columns_json= json.loads(columns_bytes)
        else:
            columns_json= None
        graph = preprocess.preprocess_network(file, columns_json)

        #Apply louvain method
        supergraph, communities = louvain.Louvain(graph)
        last_community = louvain.last_community(graph, communities)
        modularity = nx_modularity(graph, louvain.dendrogram(last_community))

        #Prepare json
        graph_json = preprocess.preprocess_json(graph, last_community)

        #Generate dataset hash identifier
        file.seek(0) #reset file pointer
        md5_hash = hashlib.md5(file.read()).hexdigest()

        return jsonify({    
                        'graph': graph_json,
                        'communities': last_community,
                        'modularity': modularity,
                        'algorithm': 'Louvain',
                        'dataset_hash': md5_hash
                    }), 200
    # except:
    #     return jsonify({"errorMessage": "Invalid .csv format"}), 400

    
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()