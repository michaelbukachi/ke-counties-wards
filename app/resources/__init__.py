from flask_restplus import Api

from .demo import ns as index_ns
from .data import ns as data_ns

api = Api()

api.add_namespace(index_ns)
api.add_namespace(data_ns)