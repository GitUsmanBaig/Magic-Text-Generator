from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)
model = pipeline('text-generation', model='distilgpt2')

@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML page

@app.route('/generate', methods=['POST'])
def generate_text():
    prompt = request.json.get('prompt', '')
    response = model(prompt, max_length=50)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
