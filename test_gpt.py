from gpt import ask_gpt


def test_ask_gpt():
    message = "Hola"
    print("asking gpt...")
    response = ask_gpt(message)
    print(response)


if __name__ == "__main__":
    test_ask_gpt()
