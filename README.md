# AI-ChatBot-Advance
# 🧠 Command DG Chatbot

A multimodal, voice-enabled AI chatbot built with Flask, Tailwind CSS, and Cohere. Supports text, voice, and image-based queries with intelligent mode switching (Friendly Chat, Deep Thinking, Research).

---

## 🚀 Features

- 💬 Text-based chat powered by Cohere's `command-r-plus` model
- 🎙️ Voice input using Web Speech API
- 🔊 Voice output with mute/unmute toggle and persistent state
- 🧠 Mode selector: Friendly, Deep Thinking, Research
- 🖼 Image upload with OCR (via Tesseract) for visual understanding
- 📋 Auto-formatting of long responses into bullet points

---

## 🛠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/command-dg-chatbot.git
cd command-dg-chatbot

pip install flask cohere pillow pytesseract

 Install Tesseract OCR Engine
Windows
- Download from UB Mannheim builds
- Add install path (e.g., C:\Program Files\Tesseract-OCR) to your system's PATH
- Or specify manually in app.py:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

python app.py
