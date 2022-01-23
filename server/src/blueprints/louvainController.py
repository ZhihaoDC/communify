from flask import request, Blueprint
from flask.json import jsonify
import json
from networkx.algorithms.community.quality import modularity as nx_modularity

import src.blueprints.preprocess as preprocess 

#import custom module
from src.scripts import louvain


louvainController = Blueprint('louvainController', __name__)


#Main method
@louvainController.route('/community-detection/louvain', methods=['POST'])
def apply_louvain():
    # try: 
    file = request.files['file']
    if len(request.files) > 1:
        columns_file = request.files['columns']
        columns_bytes = columns_file.read().decode('utf8').replace("'",'"')
        columns_json= json.loads(columns_bytes)
        print(columns_json)
    else:
        columns_json= None
    graph = preprocess.preprocess_network(file, columns_json)

    #Apply louvain method
    supergraph, communities = louvain.Louvain(graph)
    last_community = louvain.last_community(graph, communities)
    modularity = nx_modularity(graph, louvain.dendrogram(last_community))

    #Prepare json
    graph_json = preprocess.preprocess_json(graph, last_community)

    return jsonify({
                    'graph': graph_json,
                    'communities': last_community,
                    'modularity': modularity,
                    'algorithm': 'Louvain'
                }), 200
    # except:
    #     return jsonify({"errorMessage": "Invalid .csv format"}), 400
