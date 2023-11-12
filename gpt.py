from openai import OpenAI

from config import OPENAI_KEY, GPT_ROLE, GPT_MODEL

client = OpenAI(api_key=OPENAI_KEY)


def ask_gpt(user_message: str, language_response: str = "español"):
    # user_message = user_message + f"\nPorfavor, da tu respuesta en la lengua: {language_response}."

    messages = [
        {"role": "system", "content": GPT_ROLE},
        {"role": "user", "content": user_message},
    ]

    response_gpt = client.chat.completions.create(
        model=GPT_MODEL,
        messages=messages,
    )

    response_text = response_gpt.choices[0].message.content

    return response_text
