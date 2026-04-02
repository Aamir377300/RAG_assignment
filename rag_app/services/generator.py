import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HUGGINGFACE_API_KEY")
API_URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

SYSTEM_PROMPT = """You are a precise question-answering assistant with strict integrity rules.

RULES:
1. Answer ONLY using information explicitly stated in the provided context.
2. Do NOT add any information, facts, or explanations that are not present in the context.
3. Do NOT use your general knowledge or training data to fill gaps.
4. If the context does not contain enough information to answer the question, respond with exactly: "The provided context does not contain enough information to answer this question."
5. Quote or closely paraphrase the source text. Do not invent details.
6. Keep your answer concise and grounded in the context."""


def generate_answer(question, context_chunks):
    if not context_chunks:
        return "No relevant context was retrieved to answer this question."

    # Number each chunk so the model can reference them
    numbered_context = "\n\n".join(
        f"[Chunk {i+1}]: {chunk}" for i, chunk in enumerate(context_chunks)
    )

    payload = {
        "model": "meta-llama/Llama-3.1-8B-Instruct:cerebras",
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": (
                    f"Context:\n{numbered_context}\n\n"
                    f"Question: {question}\n\n"
                    f"Answer strictly based on the context above:"
                )
            }
        ],
        "max_tokens": 300,
        "temperature": 0.1  # low temperature = more deterministic, less hallucination
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        result = response.json()

        if "error" in result:
            return f"API Error: {result['error']}"

        return result["choices"][0]["message"]["content"].strip()

    except Exception as e:
        return f"Error: {e}"
