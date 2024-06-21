import PyPDF2
 
def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            text = ''
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                text += page.extract_text()
            return text
    except PyPDF2.utils.PdfReadError as e:
        print(f"Error reading PDF file: {e}")
        return None
    except FileNotFoundError:
        print(f"PDF file not found at: {pdf_path}")
        return None
