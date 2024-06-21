import openai
from extract_text import extract_text_from_pdf
 
class PDFQuery:
    def __init__(self, text, api_key):
        self.text = text
        self.api_key = api_key
 
    def query(self, question):
        openai.api_key = self.api_key
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Here is the PDF content:\n\n{self.text}\n\nQuestion: {question}\n\nAnswer:",
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()
 
# Example usage (not needed when integrated with Flask)
if __name__ == '__main__':
    pdf_text = extract_text_from_pdf('path_to_your_pdf.pdf')
    pdf_query = PDFQuery(pdf_text, 'your_openai_api_key')
    answer = pdf_query.query("What is the main topic of this document?")
    print(answer)
