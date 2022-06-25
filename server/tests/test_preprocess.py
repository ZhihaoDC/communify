from dataclasses import dataclass
import json
from pandas import read_csv
from csv import writer, QUOTE_NONNUMERIC
import networkx
import src.api.preprocess as preprocess


def test_preprocess_network(csv_file):
    """
    GIVEN a .csv file from the body of a http POST request
    WHEN function preprocess_network is called
    THEN function preprocess_network returns formatted networkx.Graph Object
    """

    result = preprocess.preprocess_network(csv_file)

    assert isinstance(result, networkx.Graph)
    assert not networkx.classes.function.is_empty(result)

    #assert that node labels are integers 
    assert all([isinstance(i, int) for i in result.nodes()])

    #assert that label is a node attribute (storing old name)
    assert all(['name' in result.nodes(data=True)[i] for i in range(result.number_of_nodes())]) 

    #assert that weight is an edge attribute
    assert all(['weight' in data for u, v, data  in result.edges(data=True)])



def test_preprocess_json(csv_file):
    """
    GIVEN that we have executed one of the community detection algorithms on a networkx.Graph Object
    WHEN we obtain the networkx.Graph Object and a dict() of communities
    THEN we format the Graph to have the desired attribute names
    AND we return a json of the Graph
    """
    graph = preprocess.preprocess_network(csv_file)

    communities = {0:1, 1:1, 2:2, 3:1, 4:3} #mock communities

    result = preprocess.preprocess_json(graph, communities)

    assert isinstance(result, dict)
    assert all(['name' in node['data'] for node in result['elements']['nodes']])
    assert all(['background_color' in node['data'] for node in result['elements']['nodes']])
    assert all(['community' in node['data'] for node in result['elements']['nodes']])
    assert all(['degree' in node['data'] for node in result['elements']['nodes']])


def test_preprocess_json_visualization(csv_file):
    """
    GIVEN that we have transformed our .csv file to a networkx.Graph Object for plain visualization
    WHEN we obtain the networkx.Graph Object and no communities
    THEN we format the Graph to have the desired attribute names
    AND we return a json of the Graph
    """
    graph = preprocess.preprocess_network(csv_file)

    result = preprocess.preprocess_json(graph)

    assert isinstance(result, dict)
    assert all(['name' in node['data'] for node in result['elements']['nodes']])
    assert all(['degree' in node['data'] for node in result['elements']['nodes']])