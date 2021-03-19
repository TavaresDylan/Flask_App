# Importation du framework flask
from flask import Flask
from config import Config
# Déclaration de l'application
app = Flask(__name__)
app.config.from_object(Config)
# Import du module de gestion des routes de flask
from app import routes