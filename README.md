# LLM Benchmark Lab – Setup

This lab uses **local LLMs with Ollama**.  
Before running the benchmark script, you **must** install Ollama and pull the required models.

---

## 1. Install Ollama

Download and install Ollama from:

https://ollama.com/download

After installing, start the Ollama server in a terminal:

```bash
ollama serve
```

Leave this running while you do the lab.

---

## 2. Pull the Required Models

The Python script uses the following models:

```python
MODEL_NAMES = [
    # "qwen3:4b",
    "gemma3:latest",  # 4B
    "cogito:3b",
]
```

You must download them first:

```bash
ollama pull gemma3:latest
ollama pull cogito:3b
# optional if you uncomment it later:
# ollama pull qwen3:4b
```

---

## 3. Run the Benchmark Script

Make sure you have Python and the required libraries (for example: `pandas`, `ollama`):

```bash
pip install pandas ollama
```

Then run the benchmark script from the folder where it is saved:

```bash
python benchmark_ollama_models.py
```

This will:

- Call each model with the same questions and sensor data  
- Measure how long each model takes  
- Count how many words each model actually generated  
- Save the results to a CSV file for you to inspect.
