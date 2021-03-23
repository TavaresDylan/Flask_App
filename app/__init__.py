# Importation du framework flask
from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
# Déclaration de l'application
app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)
# Import du module de gestion des routes de flask
from app import routes