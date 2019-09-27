import os


class Config:
    ERROR_404_HELP = False

    SECRET_KEY = os.getenv('APP_SECRET', '7b9b943f4dab6aa1573d8ea8b995112553b6d3706474bbb43bff200209498e75')
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))  # refers to application_top
    APP_STATIC = os.path.join(APP_ROOT, 'static')
    SRC_FILE = os.path.join(APP_STATIC, 'src.csv')

    DEPLOYED = bool(os.getenv('DEPLOYED', False))


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig
}
