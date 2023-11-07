import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_KEY = os.environ["OPENAI_KEY"]

GPT_ROLE = "You are helpful teacher, who knows a lot about Python and Data Science. Do never answer non related questions. "
MESSAGE_RANDOM_CONCEPT = "Choose a data/python/machine learning concept. Then give an explanation. Put a header3 as title using markdown. Be creative choosing the concept. "
SPINNER_TEXT = f"Thinking... 🧠🧠🧠"
SPINNER_TEXT_IMAGINE = f"Imagining... ✨✨✨"

langs = ["ESP", "ENG"]


class Tools:
    CONCEPT_ILLUMINATOR = "💡 Concept Illuminator"
    PUZZLE_BUILDER = "🧩 Puzzle Builder"
    DATASET_FINDER = "📊 Dataset Finder"
    ABOUT = "ℹ️ About"


random_concepts = ["Decorators", "Regular Expressions", "Gradient Descent", "Bayesian Inference", "Support Vector Machines", "Pandas DataFrame", "Monte Carlo Simulation", "Cross-Validation", "Principal Component Analysis", "Generators", "Deep Learning", "Scikit-learn", "Time Series Analysis", "Natural Language Processing", "K-means Clustering", "Neural Networks", "Confidence Intervals", "Multi-threading", "Lambda Functions", "Convolutional Neural Networks", "Variables", "Lists", "Dictionaries", "For Loops", "If Statements", "Functions", "Modules", "Data Types", "String Formatting", "Boolean Logic"]
