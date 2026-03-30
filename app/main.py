import gradio as gr
import requests
from fastapi import FastAPI

# Local Ollama API endpoint
URL = "http://localhost:11434/api/generate"

def generate_text(prompt: str):
    if not prompt:
        return "Please enter a prompt."

    # Specialization: Logical Thinking Assistant
    system_role = "You are a logical thinking assistant. Explain reasoning step-by-step."
    full_prompt = f"{system_role}\n\nUser: {prompt}\nAssistant:"

    # Data payload for the local engine
    data = {
        "model": "qwen:0.5b",
        "prompt": full_prompt,
        "stream": False
    }

    try:
        # Send request to the local engine
        response = requests.post(URL, json=data)
        response.raise_for_status()
        return response.json().get("response", "No response found.")
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Gradio GUI setup
gui = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(lines=3, label="User Prompt"),
    outputs=gr.Textbox(label="Assistant Response"),
    title="Local Thinking Assistant",
    description="A specialized AI assistant running locally with Ollama."
)

# FastAPI initialization and mount
app = FastAPI(title="Local AI API")
app = gr.mount_gradio_app(app, gui, path="/")
