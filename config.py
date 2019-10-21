import os
class Config:





class Production(Config)
    pass

    
Class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}