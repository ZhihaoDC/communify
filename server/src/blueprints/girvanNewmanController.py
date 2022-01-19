from flask import request, Blueprint
from flask.json import jsonify
import src.blueprints.preprocess as preprocess

#Import custom module
import src.scripts.girvan_newman as gn

girvanNewmanController = Blueprint('girvanNewmanController', __name__)

#Main method
@girvanNewmanController.route("/community-detection/girvan-newman", methods=['POST'])
def apply_girvan_newman():
    file = request.files['file']
    print("Archivo recibido!")

    #Preprocess network from file
    graph = preprocess.preprocess_network(file)

    #Apply girvan-newman method
    dendrogram, modularity = gn.Girvan_Newman_2004(graph)
    GN_communities = gn.dendrogram_to_community(dendrogram)

    graph_json = preprocess.preprocess_json(graph, GN_communities)

    return jsonify(
                    {'graph': graph_json,
                    'communities': GN_communities,
                    'modularity': modularity}
                    )