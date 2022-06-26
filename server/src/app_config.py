import os

os.environ['MYSQL_ROOT_PASSWORD'] = 'root'
os.environ['MYSQL_DATABASE'] = 'Networkly'
os.environ['MYSQL_USER'] = 'user'
os.environ['MYSQL_PASSWORD'] = 'pwd12345'
os.environ['MYSQL_HOST'] = 'localhost'
os.environ['MYSQL_PORT'] = '3306'

user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
host = os.environ['MYSQL_HOST']
database = os.environ['MYSQL_DATABASE']
port = os.environ['MYSQL_PORT']

DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}:{port}/{database}'