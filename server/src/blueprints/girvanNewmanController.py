from flask import request, Blueprint
from flask.json import jsonify
import src.blueprints.preprocess as preprocess
import hashlib


#Import custom module
import src.scripts.girvan_newman as gn

girvanNewmanController = Blueprint('girvanNewmanController', __name__)

#Main method
@girvanNewmanController.route("/community-detection/girvan-newman", methods=['POST'])
def apply_girvan_newman():
    try:
        file = request.files['file']

        #Preprocess network from file
        graph = preprocess.preprocess_network(file)

        #Apply girvan-newman method
        dendrogram, modularity = gn.Girvan_Newman_2004(graph)
        GN_communities = gn.dendrogram_to_community(dendrogram)

        graph_json = preprocess.preprocess_json(graph, GN_communities)

        #Generate dataset hash identifier  
        md5_hash = hashlib.md5(file.read()).hexdigest() 

        return jsonify(
                        {'graph': graph_json,
                        'communities': GN_communities,
                        'modularity': modularity,
                        'algorithm' : 'Girvan-Newman',
                        'dataset_hash': md5_hash
                        }), 200
    except:
        return jsonify({"errorMessage": "Invalid .csv format"}), 400
