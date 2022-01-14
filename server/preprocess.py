from pandas import DataFrame, read_csv

from networkx import from_pandas_edgelist, get_node_attributes
from networkx.relabel import convert_node_labels_to_integers
from networkx.classes.function import set_node_attributes
from networkx.readwrite.json_graph import node_link_data

from matplotlib.cm import get_cmap
from matplotlib.colors import rgb2hex


#Prepare file, return networkx graph
def preprocess_network(file):
    
    #Prepare dataframe
    edge_list = read_csv(file)
    edge_list.columns = edge_list.columns.str.lower()
    
    #Generate graph (take first two columns)
    graph = from_pandas_edgelist(edge_list, 
                                    source=edge_list.columns[0], 
                                    target=edge_list.columns[1])

    graph = convert_node_labels_to_integers(graph, first_label=0, label_attribute='label')

    return graph


#Preprocess community detection results for front-end consumption
def preprocess_json(graph, communities):
    colors = get_community_colors(graph, communities)
    set_node_attributes(graph, colors, name='color')

    degrees = dict(graph.degree)
    set_node_attributes(graph, degrees, name='value')
    
    set_node_attributes(graph, communities, name='group')

    labels = dict(get_node_attributes(graph,"label"))
    set_node_attributes(graph, labels, name='title')

    graph_json = node_link_data(graph,
                                attrs={ 'source':'from', 
                                        'target':'to', 
                                        'name':'id', 
                                        'link':'edges',
                                        'title': 'title' })
    return graph_json


#Helper method
def get_community_colors(graph, community):
	""" 
	Draws the graph using colors as community identifier
	"""
	num_comms = len(set(community.values()))
	cmap = get_cmap('tab10', max(community.values()) + 1)
	# norm = matplotlib.colors.Normalize(vmin=0, vmax=num_comms)
	colors = dict()

	for node in graph.nodes:
		colors.update({node: rgb2hex(cmap(community[node]))})

	return colors