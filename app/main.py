from app import app
import numpy as np
import joblib

## Import des données d'exemple depuis les datasets de sklearn
import sklearn.datasets
from sklearn.datasets import load_iris
from sklearn.datasets import load_boston

from sklearn.linear_model import LinearRegression # Import du modèle de régression linéaire
from sklearn.linear_model import LogisticRegression # Import du modèle de régression logistique
from sklearn.model_selection import train_test_split

class Predict:
    def predIris(sepal_length,sepal_width,petal_length,petal_width):
        ## Chargement des données splitter en data et target
        X, y = load_iris(return_X_y=True)
        # Déclaration du modèle
        lr = LogisticRegression()
        # Entrainement du modèle
        lr.fit(X, y)
        # Stockage dans un tableau des arguments passer dans l'url
        data_to_pred = [sepal_length,sepal_width,petal_length,petal_width]
        # Prédiction avec les arguments d'url sur le modèle entrainé avec le jeu de données train
        predict = lr.predict([data_to_pred])
        data = load_iris()
        return data.target_names[int(predict)]

    def predBoston(zn,rm,b):
        ## Chargement des données splitter en data et target
        X, y = load_boston(return_X_y=True)
        # splitting des données
        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=42)
        # Définition du modèle
        lr = LinearRegression()
        # Entrainement du modèle
        lr.fit(X_train, y_train)
        # Tableau des variables à prédire (récupérées depuis l'url)
        data_to_pred = [zn,rm,b]
        # Prédiction avec le modèle précedement entrainé
        #predict = lr.predict([data_to_pred])
        # Score sur le jeu de test
        test_score = lr.score(X_test,y_test).round(2)
        train_score = lr.score(X_train,y_train).round(2)

        #predict = lr.predict([data_to_pred])

## 3 features MODEL PREDICT
        loaded_model = joblib.load("../ZN_RM_B_lrModel.joblib")
        predict_loaded_model = loaded_model.predict([data_to_pred])
        return [test_score,train_score,predict_loaded_model]