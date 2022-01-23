from pandas import DataFrame, Series, read_csv
from json import loads
from networkx import from_pandas_edgelist, get_node_attributes
from networkx.relabel import convert_node_labels_to_integers
from networkx.classes.function import set_node_attributes, set_edge_attributes
from networkx.readwrite.json_graph import cytoscape_data
from matplotlib.cm import get_cmap
from matplotlib.colors import rgb2hex


#Prepare file, return networkx graph
def preprocess_network(file, input_columns=None):
    #Prepare dataframe
    edge_list = read_csv(file)
    edge_list.columns = edge_list.columns.str.lower()
    # edge_list.dropna(how='any', axis='index', inplace=True)
    # edge_list['id'] = edge_list.index
    # edge_list = edge_list.filter(['from', 'to', 'source', 'taget'],axis='columns')
    possible_weights = ['weight', 'weights', 'value', 'values']
    #Generate graph
    if input_columns:
        graph = from_pandas_edgelist(edge_list, 
                                        source=str(input_columns['source']).lower(), 
                                        target=str(input_columns['target']).lower(), 
                                        edge_attr=str(input_columns['weight']).lower())
        print('Using weights inserted by user')
    elif any(column in possible_weights for column in edge_list.columns):
        is_desired_column_name =  [column in possible_weights for column in edge_list.columns]
        desired_column_name_index = is_desired_column_name.index(True)
        graph = from_pandas_edgelist(edge_list, 
                                        source=edge_list.columns[0], 
                                        target=edge_list.columns[1],
                                        edge_attr=edge_list.columns[desired_column_name_index])
        
        print('Found weight-alike column in ', desired_column_name_index)
    else:
        graph = from_pandas_edgelist(edge_list, 
                                        source=edge_list.columns[0], 
                                        target=edge_list.columns[1])
        print('No weights found')

    graph = convert_node_labels_to_integers(graph, first_label=0, label_attribute='name')

    return graph


#Convert graph to json 
def preprocess_json(graph, communities=None):
    #add color to communities and label them
    if communities is not None:
        colors = get_community_colors(graph, communities)
        set_node_attributes(graph, colors, name='background_color')
        set_node_attributes(graph, communities, name='community')
    
    #add degree
    degrees = dict(graph.degree)
    set_node_attributes(graph, degrees, name="degree")

    #add node size based on degree centrality
    MIN_NODE_SIZE = 20
    size = {node: MIN_NODE_SIZE + degree for node, degree in degrees.items()} #add MIN_NODE_SIZE to every degree
    set_node_attributes(graph, size, name="size")

    #add font-size based on degree centrality, up lo a limit of MAX_FONT_INCREASE
    MIN_FONT_SIZE = 12
    MAX_DEGREE = max(degrees.values())
    MIN_DEGREE = min(degrees.values())
    MAX_FONT_INCREASE = 10
    font_size = {node: MIN_FONT_SIZE + MAX_FONT_INCREASE*((degree - MIN_DEGREE)/(MAX_DEGREE - MIN_DEGREE)) for node, degree in degrees.items()} #add MIN_NODE_SIZE to every degree
    set_node_attributes(graph, font_size, "font_size")

    #set edge id (important for cytoscape usage!)
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
