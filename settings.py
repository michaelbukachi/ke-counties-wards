import gunicorn
from gevent import monkey

monkey.patch_all()

bind = '0.0.0.0:8004'
worker_class = 'gevent'
workers = 2
loglevel = 'debug'
keepalive = 10
timeout = 3600
preload_app = True
worker_tmp_dir = '/dev/shm'

gunicorn.SERVER_SOFTWARE = 'Microsoft-IIS/6.0'
