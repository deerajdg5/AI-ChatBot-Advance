from flask import Flask, request, jsonify, render_template
import cohere
from PIL import Image
import pytesseract
import io

app = Flask(__name__)
co = cohere.Client("1MKARbZfa1UhWBbJJs6q3WuGpdjS2E42q9HpsQrz")

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Unified Chat API with Mode Support
@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('prompt')
    mode = request.json.get('mode', 'friendly')

    # Mode-based prompt augmentation
    if mode == 'deep':
        system_prompt = "You are a thoughtful assistant who reflects deeply before answering. Provide nuanced, well-reasoned responses."
    elif mode == 'research':
        system_prompt = "You are a research assistant. Provide factual, well-cited, and informative answers."
    else:
        system_prompt = "You are a friendly chatbot. Keep responses casual, warm, and engaging."

    try:
        response = co.chat(
            model="command-r-plus",
            message=user_input,
            temperature=0.7,
            preamble=system_prompt,
            chat_history=[],
            connectors=[],
            prompt_truncation='AUTO'
        )
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Image Upload and OCR
@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    try:
        image = Image.open(file.stream).convert('RGB')

        # OCR: Extract text from image
        extracted_text = pytesseract.image_to_string(image)

        if extracted_text.strip():
            reply = f"I found this text in the image:\n\n{extracted_text.strip()}"
        else:
            reply = "I couldn't find any readable text in the image. Try a clearer photo or zoomed-in section."

        return jsonify({'response': reply})

    except Exception as e:
        return jsonify({'error': f'Failed to process image: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)