class config():
    SECRET_KEY = 'my_secret_key'

class configDev(config):
    DEBUG = True

config = {

    'development' : configDev
}