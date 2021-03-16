# Importation du framework flask
from flask import Flask
# Déclaration de l'application
app = Flask(__name__)

# Import du module de gestion des routes de flask
from app import routes