from werkzeug.middleware.proxy_fix import ProxyFix

from .factory import Factory
from .utils import get_counties_and_wards


def create_app(environment='development'):
    f = Factory(environment)
    f.set_flask()
    f.set_api()

    app = f.flask

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET')

        return response

    app.wsgi_app = ProxyFix(app.wsgi_app)

    return app
