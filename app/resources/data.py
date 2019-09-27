from flask_restplus import Namespace, Resource, fields

from app import get_counties_and_wards

ns = Namespace('data', 'County-Ward operations')

single_model = ns.model('Name', {
    'name': fields.String
})


@ns.route('/counties')
class GetCounties(Resource):

    @ns.marshal_list_with(single_model)
    def get(self):
        """
        Get all counties
        """
        counties = get_counties_and_wards()
        return [{'name': key} for key in counties.keys()]


@ns.route('/counties/<string:county>/wards')
class GetCountyWards(Resource):

    @ns.marshal_list_with(single_model)
    def get(self, county):
        """
        Get all wards of a county
        """
        counties = get_counties_and_wards()
        county = county.title()
        wards = counties.get(county, [])
        return [{'name': ward} for ward in wards]