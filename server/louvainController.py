from flask import request, Blueprint
from flask.json import jsonify
import pandas as pd
import networkx as nx
import louvain #custom module
import matplotlib.cm
import matplotlib.colors
import json


louvainController = Blueprint('louvain_Controller', __name__)


#Main method
@louvainController.route('/community-detection/louvain', methods=['POST'])
def apply_louvain():

    file = request.files['file']
    print("Archivo recibido!")

    #Prepare dataframe
    edge_list = pd.read_csv(file)
    edge_list.columns = edge_list.columns.str.lower()
    
    #Generate graph
    graph = nx.from_pandas_edgelist(edge_list, 
                                    source=edge_list.columns[0], 
                                    target=edge_list.columns[1])

    graph = nx.relabel.convert_node_labels_to_integers(graph, first_label=1, label_attribute='label')
    #Apply louvain method
    supergraph, communities = louvain.Louvain(graph)
    last_community = louvain.last_community(graph, communities)
    modularity = nx.algorithms.community.quality.modularity(graph, louvain.dendrogram(last_community))

    colors = get_community_colors(graph, last_community)
    nx.classes.function.set_node_attributes(graph, colors, name='color')
    # node_list['label'] = node_list.applymap(lambda x: id_to_labels[x])
    # node_list['color'] = node_list.applymap(lambda x: colors[x])
    return jsonify({
                    'graph': nx.readwrite.json_graph.node_link_data(graph,
                                                                    attrs={'source':'from', 'target':'to', 'name':'id', 'link':'edges'}),
                    'communities': last_community,
                    'modularity': modularity
                })





#Helper method
def get_community_colors(graph, community):
	""" 
	Draws the graph using colors as community identifier
	"""
	num_comms = len(set(community.values()))
	cmap = matplotlib.cm.get_cmap('tab10', max(community.values()) + 1)
	norm = matplotlib.colors.Normalize(vmin=0, vmax=num_comms)
	colors = dict()

	for node in graph.nodes:
		colors.update({node:matplotlib.colors.rgb2hex(cmap(community[node]))})

	return colors

