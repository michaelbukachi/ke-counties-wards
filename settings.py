import os

from gevent import monkey

PORT = os.getenv('PORT', 8004)

monkey.patch_all()

bind = f'0.0.0.0:{PORT}'
worker_class = 'gevent'
workers = 2
loglevel = 'debug'
keepalive = 10
timeout = 3600
preload_app = True

