import os
from flask import Flask, request, jsonify

# Load environment variables (e.g., API keys)
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "✅ Bot is running on Render!"

# Webhook endpoint - WhatsApp will POST messages here later
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("📩 Incoming data:", data)  # Debug log

    # ---- Step 1: Extract user message ----
    user_message = data.get("message", "")

    # ---- Step 2: (Future) Convert audio -> text (STT) ----
    # Example placeholder
    # text = speech_to_text(audio_file)

    # ---- Step 3: (Future) Generate reply using Gemini/OpenAI ----
    # reply_text = generate_reply(text)

    # ---- Step 4: (Future) Convert reply -> audio (TTS) ----
    # audio_file = text_to_speech(reply_text)

    # ---- Step 5: Respond (currently just echo text) ----
    reply = f"Echo: {user_message}"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
  
