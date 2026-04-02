import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rag_app.services.retriever import retrieve_relevant_chunks
from rag_app.services.generator import generate_answer


def main():
    # Step 1: question
    question = "what is diversification?"

    # Step 2: retrieve chunks
    chunks = retrieve_relevant_chunks(question, top_k=3)

    # Step 3: generate answer
    answer = generate_answer(question, chunks)

    # Step 4: print context
    print("\n--- Retrieved Context ---\n")
    for i, chunk in enumerate(chunks):
        print(f"{i+1}. {chunk[:100]}...\n")

    # Step 5: print answer
    print("\n--- Final Answer ---\n")
    print(answer)


if __name__ == "__main__":
    main()