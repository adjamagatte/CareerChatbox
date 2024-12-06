import unittest
from unittest import mock
import os
from unittest.mock import patch, mock_open
import PyPDF2
import docx
from utils import *  

class TestFetchOpenAIAPIKey(unittest.TestCase):
    
    @patch('os.getenv')
    def test_fetch_openai_apikey_key_found(self, mock_getenv):
        """
        Teste que la fonction retourne la clé API lorsqu'elle est définie dans les variables d'environnement.
        """
        # Simuler la présence de la clé API dans les variables d'environnement
        mock_getenv.return_value = "cle_api_test_123"
        
        # Appeler la fonction et vérifier qu'elle retourne la clé correcte
        resultat = fetch_openai_apikey()
        self.assertEqual(resultat, "cle_api_test_123")
    
    @patch('os.getenv')
    def test_fetch_openai_apikey_key_not_found(self, mock_getenv):
        """
        Teste que la fonction retourne un message d'erreur si la clé API est absente.
        """
        # Simuler l'absence de la clé API dans les variables d'environnement
        mock_getenv.return_value = None
        
        # Appeler la fonction et vérifier qu'elle retourne le message d'erreur
        resultat = fetch_openai_apikey()
        self.assertEqual(resultat, "Clé API introuvable.")


# Test extract_text fonction 
class TestExtractText(unittest.TestCase):

    def setUp(self):
        self.pdf_file = "docs/pdfFile.pdf"
        self.docx_file = "docs/docxfile.docx"
        self.invalid_file = "docs/textfile.txt"
        self.expected_text = (
            "Elle est Data Scientist / Data Engineer, spécialisée dans le développement de solutions de traitement et "
            "d'analyse de données, ainsi que dans la création et la mise en production de modèles d'apprentissage machine. "
            "Elle travaille également sur des projets liés à l'architecture des données, à l'ingestion et au traitement des "
            "données, et à l'utilisation d'outils de Business Intelligence."
        )
       
    def test_extract_text_pdf(self):
        """
        Teste l'extraction de texte depuis un fichier PDF réel.
        """
     
        # Extraire le texte du fichier pdf
        result = extract_text(self.pdf_file)
        result = ' '.join(result.replace("\n", " ").split())
        self.assertEqual(result.strip(), self.expected_text)

    def test_extract_text_docx(self):
        """
        Teste l'extraction de texte depuis un fichier DOCX réel.
        """
        # Extraire le texte du fichier DOCX
        result = extract_text(self.docx_file)
        self.assertEqual(result.strip(), self.expected_text)
        
    def test_extract_text_invalid_format(self):
        with self.assertRaises(ValueError):
            extract_text(self.invalid_file)


# test answer question

class TestAnswerQuestion(unittest.TestCase):
    
    def setUp(self):
        """
        Prépare les données avant chaque test.
        """
        self.cv_text = "Elle est Data Scientist, spécialisée dans le développement de solutions de traitement et d'analyse de données."
        self.question = "Quel est le métier de cette personne ?"
        self.expected_answer = "Data Scientist"

    def test_answer_question(self):
        """
        Teste la fonction answer_question sans appeler réellement l'API OpenAI.
        """
        # Patch de l'environnement pour éviter que la clé API soit requise
        with mock.patch.dict('os.environ', {'OPENAI_API_KEY': 'fake-api-key'}), \
             mock.patch('openai.chat.completions.create') as mock_openai:
            
            # Définir ce que le mock doit retourner
            mock_openai.return_value = mock.Mock(
                choices=[mock.Mock(message=mock.Mock(content=self.expected_answer))]
            )
            
            # Appeler la fonction answer_question avec les arguments nécessaires
            result = answer_question(self.cv_text, self.question)
            
            # Vérification que le résultat correspond à la réponse attendue
            self.assertEqual(result, self.expected_answer)

if __name__ == '__main__':
    unittest.main()





