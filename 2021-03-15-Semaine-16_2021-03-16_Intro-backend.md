# Intro to API

## Objectifs

- Créer une application backend en python avec Flask

* Effectuer des requêtes HTTP

## Consignes

Réaliser une application backend qui expose les routes suivantes

- GET /hello
  - renvoie un json
  ```json
  {
    success: true,
    data: “Hello world”
  }
  ```
- GET /double?number=X

  - renvoie un json

  ```json
  {
    "success": true,
    "data": YYY
  }
  ```

  - où data est le double du paramètre “number” issu de la requête

- GET /predict?sepal_length=XXX&sepal_width=XXX&petal_length=XXX&petal_width=XXX

  - renvoie la prédiction d’un modèle (basique) entraîné sur les données du iris dataset : https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html

  ```json
  {
    "success": true,
    "data": XXX
  }
  ```

- GET /users

  - renvoie une liste d’utilisateurs récupérée après un appel HTTP vers https://jsonplaceholder.typicode.com/users

  ```json
  {
    "success": true,
    "data": [...]
  }
  ```

## Ressources

- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
- https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/
- Client HTTP PostMan
