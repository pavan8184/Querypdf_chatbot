from flask import Flask, render_template, request, jsonify
import openai
from extract_text import extract_text_from_pdf
from query_pdf import PDFQuery
 
app = Flask(__name__)
 
# Configure your OpenAI API key
openai.api_key = 'your_openai_api_key'
 
# Load and extract text from your PDF
pdf_text = extract_text_from_pdf('path_to_your_pdf.pdf')
pdf_query = PDFQuery(pdf_text)
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')
    bot_response = pdf_query.query(user_message)
    return jsonify({"response": bot_response})
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
