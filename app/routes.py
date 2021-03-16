from app import app
from flask import jsonify  # Import librairie permettant de rendre des contenues au format JSON
from flask import render_template # Librairie permettant de rendre une vue html 
from flask import request # Librairie permettant de faire passer des paramètres dans l'url avec la méthode GET
@app.route('/')
@app.route('/index')
def index():
    # Rend une vue HTML dans le dossier templates
    return render_template("home.html")

@app.route("/predict",methods=['GET'])
def predict():
    if not request.args.get('sepal_length'):
        return "Empty parameters in URL, you must specify \"?sepal_length=XXX&sepal_width=XXX&petal_length=XXX&petal_width=XXX\" to predict petal length"
    else:
        import numpy as np
        import sklearn.datasets
        ## Import des données d'exemple depuis les datasets de sklearn
        from sklearn.datasets import load_iris
        ## Chargement des données splitter en data et target
        X, y = load_iris(return_X_y=True,as_frame=True)

        from sklearn.linear_model import LinearRegression
        from sklearn.model_selection import train_test_split

        # Déclaration du modèle
        lr = LinearRegression()
        # Entrainement du modèle
        lr.fit(X, y)
        data_to_pred = [float(request.args.get("sepal_length")),float(request.args.get("sepal_width")),float(request.args.get("petal_width")),float(request.args.get("petal_length"))]
        predict = lr.predict([data_to_pred])
        data = load_iris(as_frame=True)
        pred_json = {
            "success": True,
            "data": data.target_names[int(predict)]
        }
        return jsonify(pred_json)

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
