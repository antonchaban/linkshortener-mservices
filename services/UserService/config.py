import os

"""
user = 'smjydhpffefdgi'
password = '2ea7743e1fd242f0d1c8fd49b5b21d459f606e67de4316878fc80f62355ee047'
server = 'ec2-176-34-211-0.eu-west-1.compute.amazonaws.com'
database = 'd8ahak39q8951c'
port = '5432'
"""

"""
user = 'dteqfkfrpzxrsv'
password = 'bf4f64740d0d78e09db0ad236dcdf5373f88177468d679841810cc3c6586a2b6'
server = 'ec2-52-30-67-143.eu-west-1.compute.amazonaws.com'
database = 'ddj31rhqjggsgl'
port = '5432'
"""

user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
server = os.getenv('POSTGRES_HOST')
database = os.getenv('POSTGRES_DB')


class Config :
    DEBUG = False
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}' \
                              f'@{server}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
