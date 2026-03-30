import gradio as gr
import requests
from fastapi import FastAPI

URL = "http://localhost:11434/api/chat"

def chat_logic(message, history):
    if not message:
        return "Please enter a message."

    # Specialization: Logical Thinking Assistant
    system_role = "You are a logical thinking assistant. Give short, step-by-step answers."
    
    # Construct the message list for the Chat API
    messages = [{"role": "system", "content": system_role}]
    
    # Add previous conversation history
    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})
    
    # Add the current user message
    messages.append({"role": "user", "content": message})

    # Data payload for the Chat API [cite: 113-114, 116]
    data = {
        "model": "qwen:0.5b",
        "messages": messages,
        "stream": False,
        "options": {
            "num_predict": 200,  # Limit response length to prevent infinite loops
            "temperature": 0.7
        }
    }

    try:
        # Send request to the local engine
        response = requests.post(URL, json=data, timeout=30)
        response.raise_for_status()
        
        # Parse the Chat API response format 
        result = response.json()
        return result['message']['content']
        
    except requests.exceptions.Timeout:
        return "Error: The model took too long to respond. Try a shorter prompt."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Chat Interface setup
gui = gr.ChatInterface(
    fn=chat_logic,
    title="Thinking Assistant",
    description="An LLM running locally via Ollama.",
    theme=gr.themes.Soft(),
    examples=["Explain why the sky is blue in 3 steps.", "If all cats are animals and Leo is a cat, what is Leo?"],
)

# FastAPI initialization
app = FastAPI(title="Local AI API")
app = gr.mount_gradio_app(app, gui, path="/")
