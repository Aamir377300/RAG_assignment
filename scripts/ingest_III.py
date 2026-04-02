import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rag_app.services.pdf_loader import extract_text_from_pdf
from rag_app.services.text_splitter import split_text_into_chunks
from rag_app.services.embeddings import generate_embedding
from rag_app.services.vector_store import store_embeddings

def main():
    pdf_path = "data/pdfs/investment_book.pdf"

    # Step 1: PDF → text
    text = extract_text_from_pdf(pdf_path)

    # Step 2: text → chunks
    chunks = split_text_into_chunks(text)

    embeddings = []

    # Step 3: generate embeddings
    for chunk in chunks:
        vector = generate_embedding(chunk)
        embeddings.append(vector)

    # Step 4: store
    store_embeddings(chunks, embeddings)

    # Step 5: print sample
    print("\n--- Sample Output ---\n")
    for i in range(2):
        print("Chunk:", chunks[i][:100])
        print("Vector (first 5 values):", embeddings[i][:5])
        print()
        

if __name__ == "__main__":
    main()