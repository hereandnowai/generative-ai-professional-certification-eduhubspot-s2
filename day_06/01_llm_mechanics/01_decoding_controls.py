# learning objectives:
# 1. temperature
# 2. token

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(base_url=os.environ["BASE_URL"], api_key=os.environ["OPENROUTER_API_KEY"])

MODEL = os.environ["MODEL"]

PROMPT = "Give a name for a new savings account product. Reply with just the name."

def generate(temperature: float, max_tokens: int = 20, stop=None) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": PROMPT}],
        temperature=temperature,
        top_p=1.0,
        max_tokens=max_tokens,
        stop=stop
    )
    return (response.choices[0].message.content or "").strip()

print("=== temperature 0.0 (run 3x - expect near-identical) ===")
for _ in range(3):
    print(generate(temperature=0.0))

print("\n=== temperature 1.0 (run 3x - expect some variation) ===")
for _ in range(3):
    print(generate(temperature=2.0))

print("\n=== max_tokens=1 (truncates the output) ===")
print(generate(temperature=0.7, max_tokens=1))


# temperature controls randomness in the output. Lower values (e.g., 0.0) make the model more deterministic,
# while higher values (e.g., 1.0) introduce more randomness and creativity.

# tokens control the length of the output. The max_tokens parameter sets the maximum number of tokens (words or word pieces) that the model can generate in its response.
# max_tokens=5 will truncate the output to a maximum of 5 tokens, which can be useful for generating concise responses or limiting the length of the output.