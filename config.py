import os
class Config:
    
    SECRET_KEY = '<Flask WTF Secret Key>'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://david:somanypasswords@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
config_options ={"production":ProdConfig,"default":DevConfig}

