from typing import List
from config import OPENAI_KEY
from openai import OpenAI

client = OpenAI(api_key=OPENAI_KEY)


def ask_gpt(system_role: str, user_messages: List[str]):
    messages = [{"role": "system", "content": system_role}]

    for user_message in user_messages:
        messages.append({"role": "user", "content": user_message})

    response_gpt = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )

    response_text = response_gpt['choices'][0]['message']["content"]

    return response_text
