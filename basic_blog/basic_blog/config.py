class Configuration(object):
    DEBUG = True

    SECRET_KEY = 'qwerty'

    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'bcrypt'

    POSTGRES_USER = 'postgres'
    POSTGRES_PW = ''
    POSTGRES_URL = 'localhost'
    POSTGRES_DB = 'olmol-flask'

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2' \
        f'://{POSTGRES_USER}' \
        f':{POSTGRES_PW}' \
        f'@{POSTGRES_URL}' \
        f'/{POSTGRES_DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
