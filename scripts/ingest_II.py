import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rag_app.services.pdf_loader import extract_text_from_pdf
from rag_app.services.text_splitter import split_text_into_chunks


def main():
    pdf_path = "data/pdfs/investment_book.pdf"

    text = extract_text_from_pdf(pdf_path)

    chunks = split_text_into_chunks(text)

    print(chunks[:5])


if __name__ == "__main__":
    main()