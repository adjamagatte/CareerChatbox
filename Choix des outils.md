
# Installation et Configuration
## Lancez le serveur API localement

### 1. **Cloner le Dépôt**

```bash
git clone https://github.com/adjamagatte/CareerChatbox.git
```

### 2. **Installer les Dépendances**

```bash
pip install -r requirements.txt
```

### 3. **Configurer la Clé API OpenAI**

Pour que votre application puisse interagir avec l'API OpenAI (comme GPT-3 ou GPT-4), vous devez d'abord obtenir une clé API OpenAI, puis la configurer dans votre environnement de travail dans un fichier.env .
### 4. **Exécuter Localement**

Lancez le serveur API localement avec **Uvicorn** :

```bash
uvicorn main:app --reload
```
### Interface Web
L'API sera disponible à l'adresse `http://127.0.0.1:8000`

## Sur le cloud
L'appli a été déployé sur heroku et voici son lien. 
Du moins pendant qu'il est encore déployé 😄😂

```bash
https://career-chatbox-2149ec209e2f.herokuapp.com/

```