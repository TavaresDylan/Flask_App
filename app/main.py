from app import app
app.debug = True
import numpy as np
import sklearn.datasets
## Import des données d'exemple depuis les datasets de sklearn
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression # Import du modèle de régression linéaire
from sklearn.model_selection import train_test_split

class Predict:
    def pred(sepal_length,sepal_width,petal_length,petal_width):
        ## Chargement des données splitter en data et target
        X, y = load_iris(return_X_y=True,as_frame=True)
        # Déclaration du modèle
        lr = LinearRegression()
        # Entrainement du modèle
        lr.fit(X, y)
        # Stockage dans un tableau des arguments passer dans l'url
        data_to_pred = [sepal_length,sepal_width,petal_length,petal_width]
        # Prédiction avec les arguments d'url sur le modèle entrainé avec le jeu de données train
        predict = lr.predict([data_to_pred])
        data = load_iris(as_frame=True)
        return data.target_names[int(predict)]

## Import des données d'exemple depuis les datasets de sklearn
#from sklearn.datasets import load_boston
## Chargement des données splitter en data et target
#X, y = load_boston(return_X_y=True)