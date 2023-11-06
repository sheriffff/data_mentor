import openai
import streamlit as st

from config import langs
from gpt import ask_gpt


# load keys from file keys.txt


def main():
    set_page_config()
    build_sidebar()


def set_page_config():
    st.set_page_config(
        page_title="PyData Mentor",
        page_icon="🧑‍🏫️",
        layout="centered",
    )


def build_sidebar():
    st.sidebar.header("PyData Mentor 🧑‍🏫")
    # no selection by default in selectbox
    use_case = st.sidebar.selectbox("Tool", ('Home', 'Concept Illuminator', 'Puzzle Builder', 'Dataset Finder'),
                                    key="use_case", index=0)

    st.session_state.language = st.sidebar.radio("Response Language", options=langs, index=0)
    st.sidebar.markdown("done by [Sheriff](https://linkedin.com/in/sheriff-data)")

    if use_case == "Home":
        page_index()
    elif use_case == "Concept Illuminator":
        page_concept()
    elif use_case == "Puzzle Builder":
        page_exercise()
    elif use_case == "Dataset Finder":
        page_dataset()


def page_index():
    st.header("Welcome to PyData Mentor 🧑‍🏫️")
    st.subheader("A series of tools to help you learn Python and Data Science")


def page_concept():
    st.header("Concept Illuminator 💡")

    concept = st.text_input('Concept')

    col1, col2 = st.columns(2)
    explanation_type = col1.radio('Explanation level', options=['5 year old', 'Basic', 'Intermediate', 'Expert'], index=1)
    explanation_length = col2.radio('Explanation length', options=['Very short', 'Short', 'Medium', 'Long'], index=1)
    is_with_use_case = st.checkbox('Add a real world example')
    lang_response = st.session_state.language

    if st.button('GO'):
        query_llm = f"Explain the concept of {concept}"

        if explanation_type == '5 year old':
            query_llm += " as if I were five years old."
        elif explanation_type == 'Basic':
            query_llm += " in simple terms."
        elif explanation_type == 'Intermediate':
            query_llm += " at an intermediate level of complexity."
        elif explanation_type == 'Expert':
            query_llm += " with expert level detail."

        query_llm += f"The explanation length should be: {explanation_length}."
        if explanation_length != 'Very short':
            query_llm += " Please provide the explanation in several distinct lines."

        if is_with_use_case:
            query_llm += " Include a real-world example of how this concept is applied."

        query_llm += f" Please provide the explanation in {lang_response}."
        query_llm += "I will write the explanation using markdown. So please use markdown syntax, especially for bold and italic."

        with st.spinner(f"Thinking... 🧠🧠🧠"):
            explanation = ask_gpt(
                system_role="You are a helpful assistant, who know a lot about Python and Data Science. Do never answer non related questions",
                user_messages=[query_llm]
            )

        st.subheader("Explanation")
        st.markdown(explanation)


def page_exercise():
    st.header("Puzzle Builder 🧩")
    concept = st.text_input('Topic')

    col1, col2 = st.columns(2)
    difficulty_level = col1.radio('Difficulty level', options=['Basic', 'Intermediate', 'Expert'], index=0)

    exercise_type = col2.radio('Exercise type', options=['Multiple-choice', 'Fill-in-the-blank', 'Code-writing', 'Debugging'], index=0)

    if st.button('Generate Exercise'):
        pass


def page_dataset():
    st.header("Dataset Finder 📊")


if __name__ == "__main__":
    main()
