import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_KEY = os.environ["OPENAI_KEY"]

GPT_ROLE = "You are a helpful assistant, who know a lot about Python and Data Science. Do never answer non related questions"
SPINNER_TEXT = f"Thinking... 🧠🧠🧠"

langs = ["ESP", "ENG"]


class Tools:
    CONCEPT_ILLUMINATOR = "💡 Concept Illuminator"
    PUZZLE_BUILDER = "🧩 Puzzle Builder"
    DATASET_FINDER = "📊 Dataset Finder"
