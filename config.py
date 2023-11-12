import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_KEY = os.environ["OPENAI_KEY"]

GPT_MODEL = "gpt-4-1106-preview"
GPT_ROLE = "Eres un experto en Python y Data Science. Nunca respondas a preguntas no relacionadas. En tus respuestas usas markdown. Tu respuesta empieza siempre con un encabezado de nivel 3. "
MESSAGE_RANDOM_CONCEPT = "Elige un concepto de análisis de datos / python / machine leqarning. Sé creativo al elegir el concepto, no siempre lo mismo. Explícalo. "

SPINNER_TEXT = f"Pensando... 🧠🧠🧠"
SPINNER_TEXT_IMAGINE = f"Imaginando... ✨✨✨"
SPINNER_TEXT_EXERCISE = f"Generando... 🧩🧩🧩 puede llevar hasta 2 minutos..."

language_code_to_name = {
    "ESP": "Spanish",
}

explanation_length_code_to_name = {
    "XS": "Muy corta",
    "S": "Corta",
    "M": "Mediana",
    "L": "Larga",
}


class Tools:
    CONCEPT_ILLUMINATOR = "💡 Faro del Saber"
    PUZZLE_BUILDER = "🧩 Puzzle Generator"
    DATASET_FINDER = "📊 Dataset Finder"
    ABOUT = "ℹ️ About"
