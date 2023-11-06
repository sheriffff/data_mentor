from openai import OpenAI

from config import OPENAI_KEY, GPT_ROLE

client = OpenAI(api_key=OPENAI_KEY)


def ask_gpt(user_message: str, language_response: str = "ENG"):
    user_message = user_message + f"\nPlease provide your answer in the following language: {language_response}."

    messages = [
        {"role": "system", "content": GPT_ROLE},
        {"role": "user", "content": user_message},
    ]

    response_gpt = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )

    response_text = response_gpt.choices[0].message.content

    return response_text
