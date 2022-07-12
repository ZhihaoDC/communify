from flask import request, Blueprint
from flask.json import jsonify
import hashlib
import json
from werkzeug.utils import secure_filename


#Import custom modules
import src.api.preprocess as preprocess
from src.community_detection import girvan_newman_algorithm as gn


GirvanNewmanController = Blueprint('GirvanNewmanController', __name__)


#Main method
@GirvanNewmanController.route("/community-detection/girvan-newman", methods=['POST'])
def apply_girvan_newman():
    try:
        file = request.files['file']
        dataset_name = secure_filename(file.filename.replace(".csv", ""))
        if (len(request.files) > 1) and ('columns' in request.files):
            columns = request.files['columns'].read().decode('utf8').replace("'",'"')
            columns_json= json.loads(columns)
        else:
            columns_json= None

        #Preprocess network from file
        graph = preprocess.file_to_network(file, columns_json)

        #Apply girvan-newman method
        dendrogram, modularity = gn.Girvan_Newman_2004(graph)
        GN_communities = gn.dendrogram_to_community(dendrogram)

        graph_json = preprocess.network_to_json(graph, GN_communities)

        #Generate dataset hash identifier  
        file.seek(0)
        md5_hash = hashlib.md5(file.read()).hexdigest() 

        return jsonify(
                        {'network_json': graph_json,
                        'communities': GN_communities,
                        'metrics' : {'modularity': modularity},
                        'category' : 'Girvan-Newman',
                        'dataset_hash': md5_hash,
                        'dataset_name': dataset_name
                        }), 200
    except:
        return jsonify({"errorMessage": "Invalid .csv format"}), 400
