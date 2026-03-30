# MLOPS-Task05: Thinking Assistant: Local AI Implementation

## Summary
This task implements a specialized **Logical Thinking Assistant** designed to run entirely on a local machine. It leverages the **qwen:0.5b** model—a lightweight and fast LLM—served through the **Ollama** engine. The application provides a structured chat interface for users to receive step-by-step logical reasoning without relying on external cloud APIs.

---

## Task Structure
The task repository is organized to follow standard MLOps practices for local model serving:

* **`app/`**: Contains the core logic in `main.py`, which handles API requests and the GUI.
* **`requirements.txt`**: Defines the necessary environment, including `fastapi`, `gradio`, and `requests`.
* **`.gitignore`**: Configured to exclude sensitive files like `.env` and temporary cache data.
* **`README.md`**: Provides documentation and setup instructions.

---

## Task Description
The application acts as a "Universal Remote" that connects a user-friendly frontend to a powerful local model engine. 

* **Inference Engine**: **Ollama** functions as the high-performance background engine, managing model weights and serving a local API endpoint at `localhost:11434`.
* **Backend**: **FastAPI** is used to host the application and mount the interface for professional-grade serving.
* **Frontend**: A **Gradio** `ChatInterface` provides an interactive chat window with built-in conversation history, allowing the model to maintain context during logical drills.
* **Logic Specialization**: The assistant is programmed with a system role to ensure answers are concise, structured, and logical.

---

## How to Run

### 1. Set Up the Model Engine
Download and install **Ollama** from its official website. Once installed, pull the specialized model:
```bash
ollama pull qwen:0.5b
```

### 2. Install Dependencies
Ensure you have Python installed, then install the required libraries from the project root:
```bash
pip install -r requirements.txt
```

### 3. Launch the Application
Run the FastAPI server using **Uvicorn**:
```bash
uvicorn app.main:app --reload
```

### 4. Access the Assistant
Once the server is active, open your web browser and navigate to:
`http://127.0.0.1:8000`

You can now interact with your local AI, which is optimized for providing step-by-step logical explanations.
