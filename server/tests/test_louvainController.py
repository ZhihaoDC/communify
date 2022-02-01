from io import BytesIO


def test_apply_louvain(client):
    """
    GIVEN backend listens in route: "community-detection/louvain"
    WHEN a POST request with file is sent to the same route "community-detection/louvain"
    THEN backend must respond with a json that contains the graph resulting from louvain algorithm
        AND contains graph's edges
        AND contains graph's nodes
        AND contains communities
        AND contains modularity
    """
    #create mock csv for POST request
    mock_csv = BytesIO(b"""\
                from,to,weight
                node_1,node_2,2
                node_1,node_4,1
                node_2,node_3,4
                node_4,node_5,5
                node_4,node_2,3
                    """)
    data = dict()
    data['file'] = (mock_csv, 'edge_list.csv')

    #Mock request
    rv = client.post("/community-detection/louvain",
                    data= data,
                    content_type='multipart/form-data')

    response = rv.json #convert response to json

    assert "graph" in response
    assert "nodes" in response["graph"]["elements"]
    assert "edges" in response["graph"]["elements"]
    assert "communities" in response
    assert "modularity" in response