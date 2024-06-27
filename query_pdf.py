import openai
 
class PDFQuery:
    def __init__(self, pdf_text, openai_api_key):
        self.pdf_text = pdf_text
        self.openai_api_key = openai_api_key
        openai.api_key = openai_api_key
 
    def query(self, user_message):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message},
                {"role": "assistant", "content": self.pdf_text}
            ]
        )
        return response['choices'][0]['message']['content']