import streamlit as st

from config import Tools, SPINNER_TEXT, language_code_to_name, SPINNER_TEXT_EXERCISE, explanation_length_code_to_name
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


def ask_for_response_language():
    language_codes = list(language_code_to_name.keys())
    n_langs = len(language_codes)
    if n_langs > 1:
        st.session_state.language_code = st.sidebar.radio("Lenguaje de respuesta", options=language_codes, index=0)
    else:
        st.session_state.language_code = list(language_code_to_name.keys())[0]


def build_sidebar():
    st.sidebar.header("PyData Mentor 🧑‍🏫")
    # no selection by default in selectbox
    use_case = st.sidebar.selectbox(
        "Herramienta", (
            Tools.CONCEPT_ILLUMINATOR,
            Tools.PUZZLE_BUILDER,
            # Tools.DATASET_FINDER,
            Tools.ABOUT
        ),
        key="use_case", index=0
    )

    ask_for_response_language()

    st.sidebar.markdown("by [sheriff](https://linkedin.com/in/sheriff-data)")

    if use_case == Tools.CONCEPT_ILLUMINATOR:
        page_concept()
    elif use_case == Tools.PUZZLE_BUILDER:
        page_exercise()
    elif use_case == Tools.DATASET_FINDER:
        page_dataset()
    elif use_case == Tools.ABOUT:
        page_index()


def page_index():
    st.header("Bienvenid@ a PyData Mentor 🧑‍🏫️")
    st.subheader("Una serie de herramientas para ayudarte a aprender Python y Data Science")
    st.markdown(f"""
    - {Tools.CONCEPT_ILLUMINATOR}: explica un concepto y proporciona ejemplos del mundo real
    
    - {Tools.PUZZLE_BUILDER}: genera un ejercicio para poner a prueba tus conocimientos
    
    
    Creado por [sheriff](https://linkedin.com/in/sheriff-data)
    """)

    # - {Tools.DATASET_FINDER}: find a dataset to practice your skills


def build_concept_query(concept, explanation_type: str, explanation_length_code: str, is_with_use_case: bool):
    query_llm = f"Explica el concepto de {concept}"

    if explanation_type == '5 años':
        query_llm += " como si tuviera 5 años. "
    elif explanation_type == 'Básico':
        query_llm += " a un nivel básico. "
    elif explanation_type == 'Intermedio':
        query_llm += " a un nivel intermedio. "
    elif explanation_type == 'Experto':
        query_llm += " a un nivel experto. "

    query_llm += f"La longitud de la explicación debe ser: {explanation_length_code_to_name[explanation_length_code]}. "

    if explanation_length_code != 'XS':
        query_llm += "Por favor, no hagas párrafos muy largos. "

    if is_with_use_case:
        query_llm += "Por favor, incluye un ejemplo del mundo real de cómo se aplica este concepto. "

    return query_llm


def ask_for_concept_inputs():
    concept = st.text_input(
        '¿Qué concepto quieres entender/repasar?',
        # placeholder=random_concept.lower()
    )

    col1, col2 = st.columns(2)
    explanation_type = col1.radio('Nivel de la explicación', options=['5 años', 'Básico', 'Intermedio', 'Experto'],
                                  index=1)
    explanation_length = col2.radio('Longitud de la explicación', options=['XS', 'S', 'M', 'L'], index=1)

    if explanation_length in ['M', 'L']:
        is_with_use_case = st.checkbox('Incluye un ejemplo del mundo real')
    else:
        is_with_use_case = False

    return concept, explanation_type, explanation_length, is_with_use_case


def page_concept():
    st.header(Tools.CONCEPT_ILLUMINATOR)

    concept, explanation_type, explanation_length, is_with_use_case = ask_for_concept_inputs()

    if st.button('GO!'):
        query_llm = build_concept_query(concept, explanation_type, explanation_length, is_with_use_case)

        with st.spinner(SPINNER_TEXT):
            explanation = ask_gpt(
                user_message=query_llm,
                language_response=language_code_to_name[st.session_state.language_code]
            )

        st.markdown(explanation)

    # if st.button('SORPRÉNDEME!'):
    #     with st.spinner(SPINNER_TEXT_IMAGINE):
    #         explanation = ask_gpt(
    #             user_message=MESSAGE_RANDOM_CONCEPT,
    #             language_response=st.session_state.language_code,
    #         )
    #
    #     st.markdown(explanation)


def ask_for_exercise_inputs():
    topic = st.text_input('¿Sobre qué tema / concepto quieres el ejercicio?')

    col1, col2 = st.columns(2)
    difficulty_level = col1.radio('Nivel', options=['Básico', 'Intermediato', 'Experto'], index=0)

    return topic, difficulty_level


def build_puzzle_query(topic, difficulty_level):
    query_llm = f"Crea un ejercicio de código de dificultad {difficulty_level} sobre el tema '{topic}'. "
    query_llm += "Por favor, no escribas nada más que el ejercicio. "
    query_llm += "Al final, añadirás una línea extra con la sintaxis exacta: '--Solución--' seguida de la solución con una explicación. "

    return query_llm


def page_exercise():
    st.header(Tools.PUZZLE_BUILDER)
    topic, difficulty_level = ask_for_exercise_inputs()

    query_llm = build_puzzle_query(topic, difficulty_level)

    if st.button('GO!'):
        with st.spinner(SPINNER_TEXT_EXERCISE):
            response = ask_gpt(
                user_message=query_llm,
                language_response=language_code_to_name[st.session_state.language_code],
            )

            puzzle, st.session_state.solution = response.split("--Solución--")

        st.markdown(puzzle)

        with st.expander("Ver solución"):
            st.markdown(st.session_state.solution)


def page_dataset():
    st.header(Tools.DATASET_FINDER)
    st.subheader("Work in progress 🚧")


if __name__ == "__main__":
    main()
