import streamlit as st

from config import langs, Tools, SPINNER_TEXT
from gpt import ask_gpt


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
    use_case = st.sidebar.selectbox("Tool", ('Home', Tools.CONCEPT_ILLUMINATOR, Tools.PUZZLE_BUILDER, Tools.DATASET_FINDER),
                                    key="use_case", index=0)

    st.session_state.language = st.sidebar.radio("Response Language", options=langs, index=0)
    st.sidebar.markdown("done by [sheriff](https://linkedin.com/in/sheriff-data)")

    if use_case == "Home":
        page_index()
    elif use_case == Tools.CONCEPT_ILLUMINATOR:
        page_concept()
    elif use_case == Tools.PUZZLE_BUILDER:
        page_exercise()
    elif use_case == Tools.DATASET_FINDER:
        page_dataset()


def page_index():
    st.header("Welcome to PyData Mentor 🧑‍🏫️")
    st.subheader("A series of tools to help you learn Python and Data Science")
    st.markdown(f"""
    - {Tools.CONCEPT_ILLUMINATOR}: review a concept and ask for real world examples
    
    - {Tools.PUZZLE_BUILDER}: generate an exercise to test your knowledge
    
    - {Tools.DATASET_FINDER}: find a dataset to practice your skills
    """)


def build_concept_query(concept, explanation_type: str, explanation_length: str, is_with_use_case: bool):
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

    query_llm += "I will write the explanation using markdown. So please use markdown syntax, especially for bold and italic."

    return query_llm


def ask_for_concept_inputs():
    concept = st.text_input('Ask about any Python/Data related concept')

    col1, col2 = st.columns(2)
    explanation_type = col1.radio('Explanation level', options=['5 year old', 'Basic', 'Intermediate', 'Expert'],
                                  index=1)
    explanation_length = col2.radio('Explanation length', options=['Very short', 'Short', 'Medium', 'Long'], index=1)
    is_with_use_case = st.checkbox('Add a real world example')

    return concept, explanation_type, explanation_length, is_with_use_case


def page_concept():
    st.header(Tools.CONCEPT_ILLUMINATOR)

    concept, explanation_type, explanation_length, is_with_use_case = ask_for_concept_inputs()

    if st.button('GO'):
        query_llm = build_concept_query(concept, explanation_type, explanation_length, is_with_use_case)

        with st.spinner(SPINNER_TEXT):
            explanation = ask_gpt(
                user_message=query_llm,
                language_response=st.session_state.language
            )

        st.subheader("Explanation")
        st.markdown(explanation)


def ask_for_exercise_inputs():
    topic = st.text_input('Ask for an exercise on the topic you want')

    col1, col2 = st.columns(2)
    difficulty_level = col1.radio('Difficulty level', options=['Basic', 'Intermediate', 'Expert'], index=0)

    exercise_type = col2.radio('Exercise type', options=['Multiple-choice', 'Fill-in-the-blank', 'Code-writing', 'Debugging'], index=0)

    return topic, difficulty_level, exercise_type


def build_puzzle_query(topic, difficulty_level, exercise_type):
    query_llm = f"Build an exercise of difficulty level: {difficulty_level}. "
    query_llm += f"Exercise must be exercise about topic: {topic}. "
    query_llm += f"Exercise must be of type: {exercise_type}. "
    query_llm += "Do not write intros or explanations. Just the exercise. "
    query_llm += "You will add an extra line at the end with the exact syntax: '--Solution--' followed by the solution with an explanation."

    return query_llm


def page_exercise():
    st.header(Tools.PUZZLE_BUILDER)
    topic, difficulty_level, exercise_type = ask_for_exercise_inputs()

    query_llm = build_puzzle_query(topic, difficulty_level, exercise_type)

    if st.button('GO'):
        with st.spinner(SPINNER_TEXT):
            response = ask_gpt(
                user_message=query_llm,
                language_response=st.session_state.language
            )

            puzzle, solution = response.split("--Solution--")

        st.subheader("Puzzle")
        st.markdown(puzzle)

        with st.expander("Show solution"):
            st.markdown(solution)


def page_dataset():
    st.header(Tools.DATASET_FINDER)


if __name__ == "__main__":
    main()
