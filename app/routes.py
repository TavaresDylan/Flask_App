from app import app
from flask import jsonify  # Import librairie permettant de rendre des contenues au format JSON
from flask import render_template # Librairie permettant de rendre une vue html 
from flask import request # Librairie permettant de faire passer des paramètres dans l'url avec la méthode GET
from main import Predict # Appel de la class permettant de faire la prédiction Iris (Régression Linéaire)
import requests

# Définition de la route Home
@app.route('/')
@app.route('/index')
def index():
    # Rend la vue home HTML dans le dossier templates
    return render_template("home.html")

# Définition de la route Predict Iris
@app.route("/predict",methods=['GET'])
def predict():
    if not request.args.get('sepal_length'):
        return "Empty parameters in URL, you must specify \"?sepal_length=XXX&sepal_width=XXX&petal_length=XXX&petal_width=XXX\" to predict petal length"
    else:
        # Définition des variables contenant les arguments passés dans l'URL
        sepal_length = float(request.args.get("sepal_length"))
        sepal_width = float(request.args.get("sepal_width"))
        petal_length = float(request.args.get("petal_length"))
        petal_width = float(request.args.get("petal_width"))
        pred = Predict.pred(sepal_length,sepal_width,petal_length,petal_width)
        # Création d'un dictionnaire pour le parsage en JSON
        pred_json = {
            "success": True,
            "data": pred
        }
        # Retourne un dictionnaire JSON
        return jsonify(pred_json)

# Définition de la route Flask Hello World !
@app.route("/hello")
def hello():
    jsontest = {
        'success': True,
        'data': "Hello World !"
    }
    return jsonify(jsontest)

@app.route("/double",methods=['GET'])
def double():
    if not request.args.get('number'):
        return "Empty parameters in URL, you must specify \"?number=x\" to multiply number x by 2"
    else:
        data_x2 = int(request.args.get('number')) * 2
        double = {
            "success": True,
            "data": data_x2
        }
        return jsonify(double)

@app.route("/triple",methods=['GET'])
def triple():
    if not request.args.get('number'):
        return "Empty parameters in URL, you must specify \"?number=x\" to multiply number x by 3"
    else:
        data_x3 = int(request.args.get('number')) * 3
        triple = {
            "success": True,
            "data": data_x3
        }
        return jsonify(triple)

@app.route("/users")
def users():
    data_users = requests.get("https://jsonplaceholder.typicode.com/users")
    return jsonify(data_users.json())