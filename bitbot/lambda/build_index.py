import json
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

BOT_MODE = "sleeper_site"
client = OpenAI()

dataset = []
with open("faq.json", "r") as f:
    data = json.load(f)
    for q, v in data[BOT_MODE]["questions"].items():
        dataset.append({
            "text": f"Q: {q}\nA: {v['answer']}"
        })

embeddings = []
for item in dataset:
    resp = client.embeddings.create(
        input=item["text"],
        model="text-embedding-3-small"
    )
    embeddings.append(resp.data[0].embedding)

np.savez(
    "faq_index.npz",
    texts=[d["text"] for d in dataset],
    embeddings=np.array(embeddings, dtype=np.float32)
)
