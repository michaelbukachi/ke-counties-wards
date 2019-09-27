import click
from werkzeug.middleware.proxy_fix import ProxyFix

from .defaults import get_counties_and_wards
from .errors import before_send
from .factory import Factory


def create_app(environment='development'):
    # if environment != 'testing' and os.getenv('LOCAL', None) is None:
    #     sentry_sdk.init(
    #         dsn='https://9830cf0816d5497dbf606114a0edc4f1@report.mobidev-sandbox.com/14',
    #         integrations=[FlaskIntegration()],
    #         before_send=before_send
    #     )
    f = Factory(environment)
    f.set_flask()
    f.set_api()

    app = f.flask

    if app.config['TESTING']:  # pragma: no cover
        # Setup app for testing
        @app.before_first_request
        def initialize_app():
            pass

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE')

        return response

    app.wsgi_app = ProxyFix(app.wsgi_app)

    @app.cli.command()
    @click.argument('command')
    def setup(command):
        pass

    return app
