import PyPDF2
 
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extract_text()
    return text
 
# Example usage
pdf_path = 'path_to_your_pdf.pdf'
pdf_text = extract_text_from_pdf(pdf_path)
print(pdf_text)