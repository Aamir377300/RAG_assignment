from pypdf import PdfReader

file_path = "/Users/aamirbelalkhan/Desktop/RAG/RAG_assignment/data/pdfs/investment_book.pdf"

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)

    text_store = ""

    for page in reader.pages:
        text_in_page = page.extract_text()
        # print(text_in_page)

        if text_in_page:
            text_store = text_store + text_in_page + "\n"

    cleaned_text = text_store.strip()

    # print(reader.pages)
    return cleaned_text

a = extract_text_from_pdf(file_path)
print(a[:5000])