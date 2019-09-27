from flask_restplus import Namespace, Resource, fields

from ..utils import PlainField

ns = Namespace('demo', description='Examples')

demo_model = ns.model('Demo', {
    'message': PlainField
})


@ns.route('', endpoint='index')
class IndexPage(Resource):

    @ns.marshal_with(demo_model)
    def get(self):
        """
        Example url
        """
        return 'County - Wards utils'
