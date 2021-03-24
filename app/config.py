import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    IMAGE_UPLOADS = "/Users/dylantavares/Documents/IA/Briefs/2021-03-19apidylan_tavares/app/static/img/"
