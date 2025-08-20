from flask import Flask, request, jsonify, render_template
import cohere

app = Flask(__name__)
co = cohere.Client("1MKARbZfa1UhWBbJJs6q3WuGpdjS2E42q9HpsQrz")  # Replace with env var in production

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

if __name__ == '__main__':
    app.run(debug=True)