import json
import os

def store_embeddings(chunks, embeddings):
    data = []

    for chunk, vector in zip(chunks, embeddings):
        data.append({
            "text": chunk,
            "embedding": vector
        })

    # folder create if not exists
    os.makedirs("data/vector_store", exist_ok=True)

    with open("data/vector_store/embeddings.json", "w") as f:
        json.dump(data, f)