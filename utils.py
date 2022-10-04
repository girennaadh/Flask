import os
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:admin@localhost/coursedb')
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False)
postgres_host = os.getenv('postgres_host', 'postgres')
postgres_port = os.getenv('postgres_port', '5432')
postgres_user = os.getenv('postgres_user', 'postgres')
postgres_pwd = os.getenv('postgres_pwd', 'root')
database = os.getenv('database', 'coursedb')


