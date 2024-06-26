import os
from flask import Flask, render_template, request, jsonify
from extract_text import extract_text_from_pdf
from query_pdf import PDFQuery
 
app = Flask(__name__)
 
# Load OpenAI API Key from environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')
 
# Initialize variables
pdf_path = os.path.join(os.path.dirname(__file__), 'path_to_your_pdf.pdf')
pdf_text = None
pdf_query = None
 
# Function to load and extract text from PDF
def load_pdf_text():
    global pdf_text, pdf_query
    pdf_text = extract_text_from_pdf(pdf_path)
    pdf_query = PDFQuery(pdf_text, openai_api_key)
 
# Route to render index.html
@app.route('/')
def home():
    # Ensure pdf_text and pdf_query are initialized before rendering template
    if pdf_text is None:
        load_pdf_text()
    return render_template('index.html')
 
# Route for chatbot API endpoint
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')
    # Ensure pdf_query is initialized before querying
    if pdf_query is None:
        load_pdf_text()
    bot_response = pdf_query.query(user_message)
    return jsonify({"response": bot_response})
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)