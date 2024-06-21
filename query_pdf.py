import openai
from langchain import LangChain
 
# Configure your OpenAI API key
openai.api_key = 'your_openai_api_key'
 
class PDFQuery:
    def __init__(self, text):
        self.text = text
        self.chain = LangChain()
 
    def query(self, question):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Here is the PDF content:\n\n{self.text}\n\nQuestion: {question}\n\nAnswer:",
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()
 
# Example usage
pdf_text = extract_text_from_pdf('path_to_your_pdf.pdf')
pdf_query = PDFQuery(pdf_text)
answer = pdf_query.query("What is the main topic of this document?")
print(answer)
