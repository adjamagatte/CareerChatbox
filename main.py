from fastapi import FastAPI, File, Form, UploadFile, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import utils 
import openai
import os

app = FastAPI()

# Configurer Jinja2 pour les templates
templates = Jinja2Templates(directory="templates")

# Route statique si nécessaire
app.mount("/static", StaticFiles(directory="static"), name="static")

# Variable globale pour stocker le chemin du fichier téléchargé
uploaded_file_path = None

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Affiche la page principale avec le formulaire.
    """
    return templates.TemplateResponse("index.html", {
        "request": request,
        "answer": None,
        "reponse_a_question_suivante": None,
        "uploaded_file_path": uploaded_file_path
    })

@app.post("/", response_class=HTMLResponse)
async def handle_form(
    request: Request,
    cv_file: UploadFile = File(None),  # Champ pour charger un fichier
    question: str = Form(...),
    reponse_a_question_suivante: str = Form(None)  # Nouveau champ pour la réponse de continuer à poser des questions
):
    global uploaded_file_path

    if cv_file:  # Si un fichier est téléchargé
        # Sauvegarde temporaire du fichier
        uploaded_file_path = f"uploaded_{cv_file.filename}"
        with open(uploaded_file_path, "wb") as buffer:
            buffer.write(await cv_file.read())
    
    # Vérification si un fichier est déjà chargé
    if uploaded_file_path:
        # Extraire le texte du CV
        cv_text = utils.extract_text(uploaded_file_path)

        # Connexion à OpenAI
        openai.api_key = utils.fetch_openai_apikey()

        # Répondre à la question posée
        answer = utils.answer_question(cv_text, question)

        # Si l'utilisateur souhaite poser une autre question, on passe à l'étape suivante
        if reponse_a_question_suivante == "oui":
            return templates.TemplateResponse("index.html", {
                "request": request,
                "answer": answer,
                "reponse_a_question_suivante": "oui",
                "uploaded_file_path": uploaded_file_path  # Garde le chemin du fichier
            })
        else:
            return templates.TemplateResponse("index.html", {
                "request": request,
                "answer": answer,
                "reponse_a_question_suivante": "non",
                "uploaded_file_path": uploaded_file_path  # Garde le chemin du fichier
            })
    
    # Si aucun fichier n'a été téléchargé et qu'il y a une question
    return templates.TemplateResponse("index.html", {
        "request": request,
        "answer": "Veuillez d'abord télécharger un fichier.",
        "reponse_a_question_suivante": "non",
        "uploaded_file_path": uploaded_file_path
    })
