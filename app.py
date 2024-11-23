from flask import Flask, request, jsonify, send_from_directory, render_template
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize the Flask app
app = Flask(__name__)

# Load the model and tokenizer
MODEL_NAME = "sachinoholic/my_T5_finetuned_model"  # Hugging Face pre-trained model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

# Route for home page
@app.route("/")
def index():
    return render_template('index.html')

# Route for favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Route for summarization
@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        # Parse the input JSON
        data = request.json
        if "text" not in data or not data["text"].strip():
            return jsonify({"error": "Invalid input: 'text' field is required."}), 400

        # Tokenize and generate the summary
        text = data['text']
        logging.info(f"Input text: {text}")
        inputs = tokenizer.encode(data['text'], return_tensors="pt", truncation=True, max_length=1024)
        logging.info(f"Inputs: {inputs}")
        outputs = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        logging.info(f"Outputs: {outputs}")
        summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Return the summary as JSON
        return jsonify({"summary": summary})
    except Exception as e:
        logging.exception(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
