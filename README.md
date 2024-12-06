<p align="center">
  <img src="docs/logo.jpg" alt="Chatbot de Carrière" width="300"/>
</p>

---

# CarrerBox : Interrogez Votre Fichier

Ce projet fournit une application basée sur **FastAPI** qui permet aux utilisateurs de charger un fichier(CV parexemple) et de poser des questions en langage naturel sur les informations contenues dans ce fichier.

---

## Fonctionnement

### 1. **Téléchargement du fichier**  
L'utilisateur télécharge son CV ou tout autre document dans un format supporté.

### 2. **Extraction du contenu**  
Le texte est extrait du fichier et stocké pour être utilisé dans les requêtes ultérieures.

### 3. **Réponse à la question**  
Les modèles GPT d'OpenAI analysent le contenu et génèrent des réponses aux questions posées par l'utilisateur.

---

## Fonctionnalités

- **Télécharger un fichier** et en extraire le contenu.
- **Répondre à des questions en langage naturel** sur le contenu du fichier téléchargé.
- **Supporte les formats de fichiers suivants** :
  - **PDFs**
  - **Documents Word** (`.docx`)

- **API simple** pour le téléchargement des fichiers et les requêtes de questions.

---

## Prérequis

### Outils requis

- **Python 3.9 ou supérieur**
- **Clé API OpenAI** (pour utiliser des modèles de langage basés sur GPT)

---

## Installation et Configuration

### 1. **Cloner le Dépôt**

```bash
git clone <https://github.com/adjamagatte/CareerChatbox.git>
```

### 2. **Installer les Dépendances**

```bash
pip install -r requirements.txt
```

### 3. **Configurer la Clé API OpenAI**

Pour que votre application puisse interagir avec l'API OpenAI (comme GPT-3 ou GPT-4), vous devez d'abord obtenir une clé API OpenAI, puis la configurer dans votre environnement de travail.

#### a. **Obtenir une clé API OpenAI**

1. Rendez-vous sur la page d'OpenAI : [https://platform.openai.com](https://platform.openai.com).
2. Connectez-vous avec votre compte ou inscrivez-vous si vous n'avez pas encore de compte.
3. Allez dans la section "API Keys" de votre compte.
4. Créez une nouvelle clé API et copiez-la (la clé ressemble à ceci : `sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`).

#### b. **Définir la clé API comme variable d'environnement**

1. Créez un fichier `.env` à la racine de votre projet.
2. Ajoutez-y votre clé API dans ce format :

```bash
OPENAI_API_KEY=your-api-key
```

Remplacez `your-api-key` par la clé API que vous avez obtenue.

---

### 4. **Exécuter Localement**

Lancez le serveur API localement avec **Uvicorn** :

```bash
uvicorn main:app --reload
```

L'option `--reload` permet de recharger automatiquement le serveur après chaque modification du code, sans avoir à redémarrer manuellement.

L'API sera disponible à l'adresse `http://127.0.0.1:8000`.

---

## Exécution des Tests

Pour exécuter les tests unitaires de l'application, utilisez la commande suivante :

```bash
python -m unittest test_utils.py
```

Cela exécutera tous les tests présents dans le fichier `test_utils.py`. Si vous avez plusieurs fichiers de tests, vous pouvez aussi exécuter tous les tests présents dans un répertoire :

---
## CI/CD

CI/CD avec GitHub Action


---
## Hebergement
L'appli a été déployé sur heroku et voici son lien. 
Du moins pendant qu'il est encore déployé 😄😂

```bash
https://career-chatbox-2149ec209e2f.herokuapp.com/

```
---
## Choix des Outils

1. **Python** : pour le développement de l'application.
  
2. **FastAPI** : Framework Python pour développer l'API backend.

3. **HTML et CSS** : pour la mise en forme de l'interface utilisateur.

4. **OpenAI GPT** : Utilisé pour répondre aux questions en langage naturel sur le contenu extrait du fichier.(modele GPT4-mini)

5. **Heroku** : Plateforme d'hébergement pour déployer l'application en ligne.

- - -
## Améliorations Futures

- Améliorer le système de réponse avec des modèles ajustés et finement entraînés pour des questions plus complexes.
- Ajouter le support pour d'autres types de fichiers, comme des fichiers CSV ou des images.
---
## Conclusion
Nous avons choisi d'utiliser l'**API OpenAI** en raison de la qualité des modèles, de la simplicité d'intégration, et du temps limité dont nous disposons pour développer le projet.
