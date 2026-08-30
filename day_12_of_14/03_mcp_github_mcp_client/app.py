import gradio as gr
import chatbot

demo = gr.ChatInterface(
    fn=chatbot.answer,
    title="MCP Client for GitHub",
    description="You can provide information about GitHub repositories, files, and user details. You can also create new repositories and update files in existing repositories.",
    examples=["Who am I on GitHub and how many public repositories do I have?",
              "What is the content of the README.md file in my my-project repository?"]
)
if __name__ == "__main__":
    demo.launch(theme=gr.themes.Soft())