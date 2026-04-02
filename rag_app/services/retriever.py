# question likh jaye and this is gonna compare with the stored vector database

import json
import numpy as np
from rag_app.services.embeddings import generate_embedding


def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)

    return dot_product / (norm_vec1 * norm_vec2)


def retrieve_relevant_chunks(question, top_k=3):
    # Step 1: question → embedding
    question_vector = generate_embedding(question)

    # Step 2: load stored embeddings
    with open("data/vector_store/embeddings.json", "r") as f:
        data = json.load(f)
        # data = [chunks, their_embedding]

    results = []

    # Step 3: loop through stored data
    for item in data:
        chunk_text = item["text"] 
        chunk_vector = item["embedding"]

        # Step 4: similarity calculate
        score = cosine_similarity(question_vector, chunk_vector) # question_vector and chunk_vector kitne similar haiye us ke score 

        # result me dal do with the chunk_text and score(similarity)
        results.append((chunk_text, score))

    # Step 5: sort by similarity (descending) {hum bade wale chahte haiye due to they have high similarity so hum top 3 wale ko le lege to context jada bane ga}
    results.sort(key=lambda x: x[1], reverse=True)

    # Step 6: pick top_k
    top_chunks = results[:top_k]

    # Step 7: return only text
    return [chunk for chunk, score in top_chunks]