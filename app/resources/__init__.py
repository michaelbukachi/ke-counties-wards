from flask_restplus import Api

from .data import ns as data_ns

api = Api()

api.add_namespace(data_ns)
