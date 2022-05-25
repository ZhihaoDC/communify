import pytest
from src import create_app
from io import StringIO
from csv import writer, QUOTE_NONNUMERIC


@pytest.fixture(scope='module')
def client():
    app = create_app()
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        yield client


@pytest.fixture(scope='function')
def csv_file():
    mock_csv = [
                ['from','to','weight'],
                ['node_1','node_2','2'],
                ['node_1','node_4','1'],
                ['node_2','node_3','4'],
                ['node_4','node_5','5'],
                ['node_4','node_2','3'],
                ]
    csv_file = StringIO("")
    csv_writer = writer(csv_file, delimiter=",", quoting=QUOTE_NONNUMERIC)

    for row in mock_csv:
        csv_writer.writerow(row)

    csv_file.seek(0) #point to the beginning of file

    with csv_file:
        yield csv_file
        