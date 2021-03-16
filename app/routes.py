from app import app
from flask import jsonify  # Import librairie permettant de rendre des contenues au format JSON
from flask import render_template # Librairie permettant de rendre une vue html 
from flask import request # Librairie permettant de faire passer des paramètres dans l'url avec la méthode GET
@app.route('/')
@app.route('/index')
def index():
    return render_template("home.html")

@app.route("/predict")
def predict():
    return "Prediction Page"

@app.route("/hello")
def hello():
    jsontest = {
        'success': True,
        'data': "hello world"
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
