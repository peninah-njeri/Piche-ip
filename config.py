import os
class Config:


     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://student:peninah@localhost/pitches'


class Production(Config)
    pass

    
Class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}