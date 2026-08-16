# import necessary libraries
from dotenv import load_dotenv
import os
import urllib.request
from langchain.chat_models import init_chat_model
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage, AIMessage
from system_prompt import SYSTEM_PROMPT

# load environment variables from .env file
load_dotenv()

# set the model to be used for the chatbot
MODEL = os.environ["MODEL_LOCAL"]

# initialize the chat model with the specified model and provider
llm = init_chat_model(model=MODEL, model_provider="ollama", temperature=0)

# define the path to the document and the URL to download it from
DOCUMENT_URL = "https://raw.githubusercontent.com/hereandnowai/genai-and-prompt-engineering-eduhubspot-s1/refs/heads/main/day-6-of-14/6-chatbot-with-text/profile-rr.md"
DOCUMENT_PATH = os.path.join(os.path.dirname(__file__), "profile-rr.md")

# download the document if it does not exist
def download_document(url, file_path):
    if os.path.exists(file_path):
        return
    with urllib.request.urlopen(url, timeout=10) as response:
        content = response.read().decode("utf-8")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

download_document(DOCUMENT_URL, DOCUMENT_PATH)

# load the document from the specified file path
def load_text_context(file_path):
    if not os.path.exists(file_path):
        return f"Warning: {file_path} not found. Proceeding without the document context."
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

document_context = load_text_context(DOCUMENT_PATH)
knowledge_base = f"{SYSTEM_PROMPT}\n\nProvide answers to the user's questions only from this document {document_context}"

messages: list[BaseMessage] = [SystemMessage(content=knowledge_base)]

def get_streaming_response(user_input):
    global messages
    messages.append(HumanMessage(content=user_input))

    full_response = ""
    for chunk in llm.stream(messages):
        content = chunk.content
        if isinstance(content, str) and content:
            full_response += content
            yield ("response", content)

    messages.append(AIMessage(content=full_response))