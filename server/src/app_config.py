import os

host = os.environ.get('MYSQL_HOST', default='localhost')
port = os.environ.get('MYSQL_PORT', default='3306')
user = os.environ.get('MYSQL_USER', default='user')
password = os.environ.get('MYSQL_PASSWORD', default='pwd12345')
database = os.environ.get('MYSQL_DATABASE', default='Networkly')

DATABASE_CONNECTION_URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
