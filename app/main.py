from app import app
## Import des données d'exemple depuis les datasets de sklearn
from sklearn.datasets import load_boston
# Chargement des données splitter en data et target
X, y = load_boston(return_X_y=True)