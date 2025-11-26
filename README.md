# LLM Benchmark Lab – Setup

This lab uses **local LLMs with Ollama**.  
Before running the benchmark script, you **must** install Ollama, create a Python virtual environment using `virtualenv`, install dependencies, and pull the required models.

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

Once the virtual environment is active, install all required libraries:

```bash
pip install -r requirements.txt
```

Your `requirements.txt` must include at least:

```
pandas
ollama
```

Add other dependencies if needed.

---

## 4. Pull the Required Models in Ollama

The benchmark script uses these models:

```python
MODEL_NAMES = [
    # "qwen3:4b",
    "gemma3:latest",  # 4B
    "cogito:3b",
]
```

Download them with:

```bash
ollama pull gemma3:latest
ollama pull cogito:3b
# optional if you later enable it:
# ollama pull qwen3:4b
```

---

## 5. Run the Benchmark Script

When the virtual environment is active and models are installed, run:

```bash
python benchmark_ollama_models.py
```

This will:

- Call each model with the same questions and sensor data  
- Measure how long each model takes  
- Count how many words each model actually generated  
- Save the results into a CSV file for inspection  

You're ready to start the lab. 🚀
