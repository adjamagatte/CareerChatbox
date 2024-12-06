from dotenv import load_dotenv
import os
import openai
import PyPDF2
import docx



from dotenv import load_dotenv
import os

def fetch_openai_apikey():
    """
    Récupère la clé API d'OpenAI à partir des variables d'environnement.

    Cette fonction utilise le module `dotenv` pour charger les variables
    d'environnement à partir d'un fichier `.env` si celui-ci est présent.
    Elle tente ensuite de récupérer la valeur de la variable `OPENAI_API_KEY`.

    Retourne :
        str : La clé API si elle est trouvée, ou un message indiquant que la clé est introuvable.

    Exceptions :
        - Cette fonction gère les cas d'erreur et ne lève aucune exception.
    """
    # Charger les variables d'environnement depuis un fichier .env
    load_dotenv()
    try:
        # Récupérer la clé API d'OpenAI
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key is None:
            return "Clé API introuvable."
    except Exception as e:
        return f"Une erreur est survenue : {e}"
    
    print("Clé API chargée avec succès.")
    return api_key


def extract_text(file_path):
    """
    Extrait le texte d'un fichier PDF ou DOCX.
    Args:
        file_path (str): Chemin du fichier.
    Returns:
        str: Texte extrait du fichier.
    Raises:
        ValueError: Si le format du fichier n'est pas supporté.
    """
    if file_path.endswith(".pdf"):
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            return ''.join(page.extract_text() for page in reader.pages)
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return '\n'.join(para.text for para in doc.paragraphs)
    else:
        raise ValueError("Format de fichier non supporté.")


def answer_question(cv_text, question):
    """
    Utilise GPT pour répondre à une question sur un CV.
    Args:
        cv_text (str): Texte brut du CV.
        question (str): Question en langage naturel.
    Returns:
        str: Réponse générée par GPT.
    """
    prompt = f"""
    Le texte suivant est un CV :
    {cv_text}

    Répondez à cette question de manière concise : {question}
    """

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    message_content = response.choices[0].message.content
    return message_content.strip()


