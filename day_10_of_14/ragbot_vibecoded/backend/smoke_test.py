from pathlib import Path
import os

from dotenv import load_dotenv
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings,
)

TEXT_MODEL = "gemma-4-31b-it"
EMBEDDING_MODEL = "gemini-embedding-2"
BACKEND_DIR = Path(__file__).resolve().parent
ENV_FILE = BACKEND_DIR / ".env"


def main() -> None:
    if not ENV_FILE.exists():
        raise RuntimeError(
            "backend/.env was not found. Create it from .env.example and add "
            "GOOGLE_API_KEY before running the smoke test."
        )

    load_dotenv(dotenv_path=ENV_FILE)
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY is missing from backend/.env.")

    chat_model = ChatGoogleGenerativeAI(
        model=TEXT_MODEL,
        temperature=0,
        api_key=api_key,
    )
    embedding_model = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        api_key=api_key,
    )

    response = chat_model.invoke("Reply with exactly: Caramel AI smoke test passed")
    vector = embedding_model.embed_query("Caramel AI smoke test")

    print(f"Text model ({TEXT_MODEL}) response: {response.content}")
    print(f"Embedding model ({EMBEDDING_MODEL}) vector length: {len(vector)}")
    print("Smoke test passed.")


if __name__ == "__main__":
    main()
