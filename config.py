import os
class Config:
    '''
    General configuration parent class
    '''
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://acces:Access@localhost/pitches'

    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
   
   
    pass