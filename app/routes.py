from app import app
from flask import jsonify  # Import librairie permettant de rendre des contenues au format JSON
from flask import render_template # Librairie permettant de rendre une vue html 
from flask import request # Librairie permettant de faire passer des paramètres dans l'url avec la méthode GET
from main import Predict # Appel de la class permettant de faire la prédiction Iris (Régression Linéaire)
import requests

from form import DoubleForm, IrisForm

# Définition de la route Home
@app.route('/')
@app.route('/index')
def index():
    # Rend la vue home HTML dans le dossier templates
    return render_template("home.html", title="Home")

# Définition de la route Predict Iris
@app.route("/predict",methods=['GET','POST'])
def predict():
    form = IrisForm()
    if form.validate_on_submit():
        result = request.form
        sepal_length = float(result["sl_input"])
        sepal_width = float(result["sw_input"])
        petal_length = float(result["pl_input"])
        petal_width = float(result["pw_input"])
        pred = Predict.predIris(sepal_length,sepal_width,petal_length,petal_width)
        return render_template("irisPredict.html", result=result, form=form, pred=pred)
    elif not request.args.get('sepal_length'):
        return render_template("irisPredict.html",form=form)
        #return "Empty parameters in URL, you must specify \"?sepal_length=XXX&sepal_width=XXX&petal_length=XXX&petal_width=XXX\" to predict petal length"
    else:
        # Définition des variables contenant les arguments passés dans l'URL
        sepal_length = float(request.args.get("sepal_length"))
        sepal_width = float(request.args.get("sepal_width"))
        petal_length = float(request.args.get("petal_length"))
        petal_width = float(request.args.get("petal_width"))
        pred = Predict.predIris(sepal_length,sepal_width,petal_length,petal_width)
        # Création d'un dictionnaire pour le parsage en JSON
        pred_json = {
            "success": True,
            "data": pred
        }
        # Retourne un dictionnaire JSON
        #return jsonify(pred_json)
        return render_template("irisPredict.html", json = pred_json,form=form)

# Définition de la route Flask Hello World !
@app.route("/hello")
def hello():
    jsontest = {
        'success': True,
        'data': "Hello World !"
    }
    return jsonify(jsontest)

@app.route("/double",methods=['GET','POST'])
def double():
    form = DoubleForm()
    if form.validate_on_submit():
        result = request.form
        result = int(result['input_nb']) *2
        return render_template("double.html",form=form, result=result)
    elif not request.args.get('number'):
        return render_template("double.html",form=form)
    else:
        data_x2 = int(request.args.get('number')) * 2
        double = {
            "success": True,
            "data": data_x2
        }
        json = jsonify(double)
        return render_template("double.html",form=form, json=json, double=data_x2, number=int(request.args.get('number')))

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

@app.route("/predict-boston", methods=["POST","GET"])
def predictBoston():
    if not request.args.get('zn'):
        return render_template("bostonPredict.html")
    else:
        # Définition des variables contenant les arguments passés dans l'URL
        zn = float(request.args.get("zn"))
        rm = float(request.args.get("rm"))
        b = float(request.args.get("b"))
        pred = Predict.predBoston(zn,rm,b)
        # Création d'un dictionnaire pour le parsage en JSON
        pred_json = {
            "success": True,
            "data": pred
        }
        return render_template("bostonPredict.html", title="Boston Prediction", json = pred)