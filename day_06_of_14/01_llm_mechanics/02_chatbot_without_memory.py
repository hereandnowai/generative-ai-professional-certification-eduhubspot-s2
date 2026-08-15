import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(base_url=os.environ["BASE_URL"], api_key=os.environ["OPENROUTER_API_KEY"])
MODEL = os.environ["MODEL"]

SYSTEM_PROMPT = "'You are a friendly assistant. Answer in one or two short sentences."

print("\nCaramel AI - The Chatbot")
print("Type 'quit' to exit.\n")
while True:
    user_input = input("You: ").strip()

    if not user_input:
        continue

    if user_input.lower() in {"quit", "exit"}:
        print("Goodbye!")
        break

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input}
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,  # type: ignore
        temperature=0
    )
    reply = response.choices[0].message.content

    print(f"Caramel AI: {reply}\n")


