

import time
import json
import pandas as pd
import ollama

MODEL_NAMES = [
    # "qwen3:4b",
    "gemma3:latest", # 4b
    "cogito:3b",
]

FORCED_WORD_COUNT = 30

SYSTEM_PROMPT = (
    "You are a robotics/IoT assistant. "
    f"Your answer MUST be exactly {FORCED_WORD_COUNT} words."
)

QUESTIONS = [
    "Describe what this sensor data represents.",
    "Is anything unusual visible in the readings?",
    "Give one likely reason for rising temperature.",
    "Give one rule for triggering an alert.",
]

SENSOR_DATA = [
    {"time": "2025-11-19T10:00:00", "temperature": 24.5, "humidity": 56.2},
    {"time": "2025-11-19T10:01:00", "temperature": 25.1, "humidity": 55.0},
    {"time": "2025-11-19T10:02:00", "temperature": 26.0, "humidity": 54.7},
    {"time": "2025-11-19T10:03:00", "temperature": 27.3, "humidity": 53.9},
]

# --------------------------------------------------------------------
# 2) BENCHMARK LOOP
# --------------------------------------------------------------------


rows = []
sensor_json = json.dumps(SENSOR_DATA, indent=2)

for model_name in MODEL_NAMES:
    print(f"\n=== MODEL: {model_name} ===")

    for question in QUESTIONS:

        user_msg = (
            "Sensor readings (JSON):\n"
            f"{sensor_json}\n\n"
            f"QUESTION: {question}\n"
            f"Your answer MUST BE EXACTLY {FORCED_WORD_COUNT} WORDS."
        )

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": user_msg},
        ]

        start = time.perf_counter()
        resp = ollama.chat(model=model_name, messages=messages)
        end = time.perf_counter()

        answer = resp["message"]["content"].strip()
        elapsed = round(end - start, 3)
        actual_word_count = len(answer.split())

        print(f"- {question[:40]}...  time={elapsed}s  words={actual_word_count}")

        rows.append({
            "model": model_name,
            "question": question,
            "forced_words": FORCED_WORD_COUNT,
            "actual_words": actual_word_count,
            "time_s": elapsed,
            "answer": answer
        })

# --------------------------------------------------------------------
# 3) SAVE RESULTS
# --------------------------------------------------------------------

df = pd.DataFrame(rows)

print("\n=== BENCHMARK TABLE ===")
print(df[["model", "question", "time_s", "forced_words", "actual_words"]])

df.to_csv("benchmark.csv", index=False)

print("\nSaved results to benchmark.csv!")