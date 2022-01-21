from pandas import DataFrame, Series, read_csv

from networkx import from_pandas_edgelist, get_node_attributes
from networkx.relabel import convert_node_labels_to_integers
from networkx.classes.function import set_node_attributes, set_edge_attributes
from networkx.readwrite.json_graph import cytoscape_data
from matplotlib.cm import get_cmap
from matplotlib.colors import rgb2hex
import networkx as nx


#Prepare file, return networkx graph
def preprocess_network(file):
    #Prepare dataframe
    edge_list = read_csv(file)
    edge_list.columns = edge_list.columns.str.lower()
    # edge_list.dropna(how='any', axis='index', inplace=True)
    # edge_list['id'] = edge_list.index
    # edge_list = edge_list.filter(['from', 'to', 'source', 'taget'],axis='columns')
    
    #Generate graph (take first two columns)
    graph = from_pandas_edgelist(edge_list, 
                                    source=edge_list.columns[0], 
                                    target=edge_list.columns[1], 
                                    edge_attr=['weight'])

    graph = convert_node_labels_to_integers(graph, first_label=0, label_attribute='name')

    return graph


#Convert graph to json 
def preprocess_json(graph, communities=None):

    if communities is not None:
        colors = get_community_colors(graph, communities)
        set_node_attributes(graph, colors, name='background_color')
        set_node_attributes(graph, communities, name='community')

    degrees = dict(graph.degree)
    set_node_attributes(graph, degrees, name='degree')
    set_edge_attributes(graph, [], name="id")

    for u,v in graph.edges:
        graph[u][v]['id'] = str(u)+'-'+str(v)

    graph_json = dict(cytoscape_data(graph, name="name", ident="id"))
    
    return graph_json


#Helper method
def get_community_colors(graph, community):
	""" 
	Draws the graph using colors as community identifier
	"""
	num_comms = len(set(community.values()))
	cmap = get_cmap('tab20', max(community.values()) + 1)
	# norm = matplotlib.colors.Normalize(vmin=0, vmax=num_comms)
	colors = dict()

	for node in graph.nodes:
		colors.update({node: "#"+rgb2hex(cmap(community[node]))[1]
                                    +rgb2hex(cmap(community[node]))[3] 
                                    +rgb2hex(cmap(community[node]))[5]})
    
	return colors


def remap_communities(communities):
    """"Remap community identifier by count"""
    comms_sort = Series(communities.values()).value_counts()
    reorder_map = dict(zip(comms_sort.index, list(comms_sort.reset_index().index)))
    return Series(communities.values()).map(reorder_map)
