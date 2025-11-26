# LLM Benchmark Lab – Setup

This lab uses **local LLMs with Ollama**.  
Before running the `app.py` script, you **must** install Ollama, create a Python virtual environment using `virtualenv`, install dependencies, and pull the required models.

---

## 1. Install Ollama

Download and install Ollama from:

https://ollama.com/download

After installing, start the Ollama server in a terminal:

```bash
ollama serve
```

Leave this running while doing the lab.

---

## 2. Create and Activate a Virtual Environment (using virtualenv)

### Install virtualenv (if not installed):

```bash
pip install virtualenv
```

### Create the environment:

```bash
virtualenv venv
```

### Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

You should now see `(venv)` in your terminal.

---

## 3. Install Python Dependencies

Once the virtual environment is active, install all dependencies:

```bash
pip install -r requirements.txt
```

Your `requirements.txt` must include at least:

```
pandas
ollama
streamlit
```

Add others if your project requires them.

---

## 4. Pull the Required Models in Ollama

The app uses the following models:

```python
MODEL_NAMES = [
    "gemma3:latest",
    "cogito:3b",
]
```

Download them with:

```bash
ollama pull gemma3:latest
ollama pull cogito:3b
```

---

## 5. Run the Application

With the virtual environment active, start the Streamlit app:

```bash
streamlit run app.py
```

This will:

- Read sensor data
- Send it to the selected local LLMs
- Measure timing and output word counts
- Display results through the Streamlit interface

You're ready to start the lab. 🚀
