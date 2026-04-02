import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rag_app.services.pdf_loader import extract_text_from_pdf
from rag_app.services.text_splitter import split_text_into_chunks


def main():
    # Step 1: PDF path
    pdf_path = "data/pdfs/investment_book.pdf"

    # Step 2: Load PDF → text
    text = extract_text_from_pdf(pdf_path)

    # Step 3: Split text → chunks
    chunks = split_text_into_chunks(text)

    # Step 4: Print preview
    print(chunks[:5])
    # print("\n--- First 5 Chunks ---\n")
    # for i, chunk in enumerate(chunks[:5]):
    #     print(f"Chunk {i+1}:\n{chunk}\n")


if __name__ == "__main__":
    main()