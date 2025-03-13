import openai
import config  # Make sure your OPENAI_API_KEY is stored in config.py

openai.api_key = config.OPENAI_API_KEY

def ask_ai(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": text}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print(ask_ai("What is the capital of France?"))
