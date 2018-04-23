import os
class Config:
    
    SECRET_KEY = '<potatas>'

    
class ProdConfig(Config):
   SQLALCHEMY_DATABASE_URIN= os.environ.get('DATABASE_URL')

   DEBUG = True

class DevConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://david:somanypasswords@localhost/blog'
    DEBUG = True
config_options ={"production":ProdConfig,"default":DevConfig}

