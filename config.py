import os

class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://student:peninah@localhost/pitches'
    SECRET_KEY = '3550026850074f58a9c1198b6fb64e1c'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    pass


class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://student:peninah@localhost/pitches'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}    