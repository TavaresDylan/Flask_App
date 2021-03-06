from app import app
from flask import jsonify  # Import librairie permettant de rendre des contenues au format JSON
from flask import render_template # Librairie permettant de rendre une vue html 
from flask import request # Librairie permettant de faire passer des paramètres dans l'url avec la méthode GET
from main import Predict # Appel de la class permettant de faire la prédiction Iris (Régression Linéaire)
import requests
import os
import config
from PIL import Image


from form import DoubleForm, IrisForm, BostonForm

# Définition de la route Home
@app.route('/')
@app.route('/index')
def index():
    # Rend la vue home HTML dans le dossier templates
    return render_template("home.html", title="Home")

# Définition de la route Predict Iris
@app.route("/predict",methods=['GET','POST'])
def predict():
    ##POST METHOD
    form = IrisForm()
    if form.validate_on_submit():
        result = request.form
        sepal_length = float(result["sl_input"])
        sepal_width = float(result["sw_input"])
        petal_length = float(result["pl_input"])
        petal_width = float(result["pw_input"])
        pred = Predict.predIris(sepal_length,sepal_width,petal_length,petal_width)
        return render_template("irisPredict.html", result=result, form=form, pred=pred, title="Iris Classification")
    elif not request.args.get('sepal_length'):
        return render_template("irisPredict.html",form=form, title="Iris Classification")
        #return "Empty parameters in URL, you must specify \"?sepal_length=XXX&sepal_width=XXX&petal_length=XXX&petal_width=XXX\" to predict petal length"
    else:
        ## GET METHOD
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
        return render_template("irisPredict.html", json = pred_json,form=form, title="Iris Classification")

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
    title_boston = "Boston Prediction"
    form = BostonForm()
    if not request.args.get('zn'):
        return render_template("bostonPredict.html", title=title_boston, form=form)
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

@app.route("/axios", methods=["POST","GET"])
def axiosPage():
    axios_title = "Axios"
    return render_template("axios.html", title=axios_title)

# Route MNIST
@app.route("/mnist", methods=["POST","GET"])
def mnistPage():
    mnist_title = "Mnist"
    # Conditions pour l'upload de l'image
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            img_load = Image.open(app.config["IMAGE_UPLOADS"]+image.filename)
            return render_template("mnist.html", title=mnist_title, image=img_load, img_name=image.filename, img_path=app.config["IMAGE_UPLOADS"]+image.filename)
    return render_template("mnist.html", title=mnist_title)