import json
import os
import numpy as np
import faiss
from openai import OpenAI

EMBED_MODEL = "text-embedding-3-small"

embed_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def embed(text: str):
    response = embed_client.embeddings.create(
        model=EMBED_MODEL,
        input=text
    )
    return np.array(response.data[0].embedding, dtype="float32")

"""
faq.json is structured like:

{
    "mode1": [
        {"question": "...", "answer": "..."},
        ...
    ],
    "mode2": [...],
    "mode3": [...]
}
"""

with open("faq.json", "r", encoding="utf-8") as f:
    data = json.load(f)

all_vectors = []
metadata = []

for mode, entries in data.items():
    for entry in entries:
        q = entry["question"]
        a = entry["answer"]

        chunk_text = f"Q: {q}\nA: {a}"
        vec = embed(chunk_text)

        all_vectors.append(vec)
        metadata.append({
            "mode": mode,
            "question": q,
            "answer": a
        })

all_vectors = np.vstack(all_vectors).astype("float32")

dim = all_vectors.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(all_vectors)

faiss.write_index(index, "vectors.index")

with open("metadata.json", "w", encoding="utf-8") as f:
    json.dump(metadata, f, ensure_ascii=False, indent=2)