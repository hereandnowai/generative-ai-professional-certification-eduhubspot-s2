import asyncio, os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()
model = os.environ["MODEL"]
TOKEN = os.environ["GITHUB_PERSONAL_ACCESS_TOKEN"]
SERVERS = {"github": {"url": "https://api.githubcopilot.com/mcp/",
                      "transport": "streamable_http",
                      "headers": {"Authorization": f"Bearer {TOKEN}"}}}
ALLOWED = {"get_me", "search_repositories", "get_file_contents",
           "create_repository", "create_or_update_file"}

async def answer(message: str, history: list | None = None) -> str:
    tools = [t for t in await MultiServerMCPClient(SERVERS).get_tools() if t.name in ALLOWED]
    agent = create_agent(
        init_chat_model(model=model, model_provider="openrouter"),
        tools=tools,
        system_prompt="You are a GitHub Copilot Assistant. You can provide information about GitHub repositories, files, and user details. You can also create new repositories and update files in existing repositories.")
    result = await agent.ainvoke({"messages": [{"role": "user", "content": message}]})
    return result["messages"][-1].content

if __name__ == "__main__":
    print(asyncio.run(answer("Who am I on GitHub and how many public repositories do I have?")))