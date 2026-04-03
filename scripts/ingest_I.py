from pypdf import PdfReader



def read_pdf_content(file_path):
    try:
        # Path ka use karke reader object banayein
        reader = PdfReader(file_path)
        
        # Pehle page ka text nikalne ka example
        first_page = reader.pages[0]
        return first_page.extract_text()
    
    except FileNotFoundError:
        return "Galti: File nahi mili. Path check karein."
    
my_path = "/Users/aamirbelalkhan/Desktop/RAG_Assignment/data/pdfs/investment_book.pdf"

content = read_pdf_content(my_path)

print(content)