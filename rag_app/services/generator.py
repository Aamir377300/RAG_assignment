import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HUGGINGFACE_API_KEY")

API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-base"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}


def generate_answer(question, context_chunks):
    context = "\n".join(context_chunks)

    prompt = f"""
    Answer the question based only on the context below.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt}
    )

    # 🔥 DEBUG
    print("STATUS CODE:", response.status_code)
    print("RAW TEXT:", response.text[:200])

    # ❌ empty response handle
    if not response.text:
        return "Error: Empty response from API"

    # ❌ JSON parse safe
    try:
        result = response.json()
    except Exception:
        return f"Error: Non-JSON response → {response.text[:200]}"

    # ❌ API error
    if isinstance(result, dict) and "error" in result:
        return f"HuggingFace Error: {result['error']}"

    # ✅ success
    if isinstance(result, list) and "generated_text" in result[0]:
        return result[0]["generated_text"]

    return "Error: Unexpected response format"