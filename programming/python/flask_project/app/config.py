import os

base_dir = os.path.abspath('db/')


class Configuration(object):
    DEBUG = True
    CAPTCHA_ENABLE = True
    CAPTCHA_LENGTH = 5
    CAPTCHA_WIDTH = 150
    CAPTCHA_HEIGHT = 50
    SESSION_TYPE = 'sqlalchemy'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'base.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = ''

