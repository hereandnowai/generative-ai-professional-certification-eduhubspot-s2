import os
from typing import TypedDict, NotRequired, Literal, cast
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END

load_dotenv()

model = init_chat_model(
    os.environ["MODEL"],
    model_provider="openrouter",
    temperature=0
)