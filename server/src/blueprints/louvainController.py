from flask import request, Blueprint
from flask.json import jsonify

from networkx.algorithms.community.quality import modularity as nx_modularity

import src.blueprints.preprocess as preprocess 

#import custom module
from src.scripts import louvain


louvainController = Blueprint('louvainController', __name__)


#Main method
@louvainController.route('/community-detection/louvain', methods=['POST'])
def apply_louvain():
    try: 
        file = request.files['file']
        print("Archivo recibido!")

        graph = preprocess.preprocess_network(file)

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
    except:
        return jsonify({"errorMessage": "Invalid .csv format"}), 500
