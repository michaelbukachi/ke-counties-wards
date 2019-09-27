from gevent import monkey

monkey.patch_all()

import logging

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handler = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
