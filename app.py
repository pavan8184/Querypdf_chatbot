import os
from flask import Flask, render_template, request, jsonify
from extract_text_from_pdf import extract_text_from_pdf
from query_pdf import PDFQuery
 
app = Flask(__name__)
 
# Load OpenAI API Key from environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')
 
# Path to the PDF file relative to the application directory
pdf_path = os.path.join(os.path.dirname(__file__), 'path_to_your_pdf.pdf')
 
# Load and extract text from your PDF
pdf_text = extract_text_from_pdf(pdf_path)
pdf_query = PDFQuery(pdf_text, openai_api_key)
 
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
