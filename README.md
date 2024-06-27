# CheckMyNumber - Projet Flask 🔍📱

Ce projet permet d'héberger localement un outil qui utilise l'API NumVerify pour vérifier les informations d'un numéro de téléphone suspect.

## Installation 🚀

Pour utiliser ce projet, suivez ces étapes :

1. **Clonez le dépôt :**

    ```
    git clone https://github.com/ZeyKii/CheckMyNumber.git
    
    cd .\CheckMyNumber\
    ```

2. **Installez les dépendances :**

    Assurez-vous d'avoir Python et pip installés. Ensuite, installez les dépendances nécessaires en exécutant :

    ```
    pip install -r requirements.txt
    ```

## Configuration ⚙️

Avant de démarrer l'application, vous devez configurer votre clé API NumVerify dans le fichier `app.py`.

1. Obtenez une clé API NumVerify sur [NumVerify](https://numverify.com/).

2. Remplacez `YOUR_API_KEY` dans `app.py` par votre clé API NumVerify :

```python
NUMVERIFY_API_KEY = 'YOUR_API_KEY'
```

## Utilisation 🎯

Pour lancer l'application, exécutez le fichier app.py :

```
python app.py
```

L'application sera accessible à l'adresse http://localhost:5000.

## Fonctionnalités

- **Validation de numéro :** Vérifie la validité d'un numéro de téléphone.

- **Informations supplémentaires :** Fournit des détails comme le format local et international, le pays, et le type de ligne.

## Structure du projet 📂

- **app.py :** Contient le code principal de l'application Flask.

- **index.html :** Fichier HTML pour l'interface utilisateur.

- **static/ :** Répertoire contenant les fichiers statiques (CSS, JavaScript).

- **templates/ :** Répertoire contenant les templates Jinja2 pour les pages HTML.

## Dépendances principales 🛠️

- **Flask :** Framework web utilisé pour le développement de l'application.

- **Requests :** Pour effectuer des requêtes HTTP vers l'API NumVerify.

- **Jinja2 :** Moteur de templates utilisé avec Flask.
