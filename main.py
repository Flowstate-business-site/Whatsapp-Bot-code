import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

# This endpoint will receive audio/text messages
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Incoming data:", data)  # debug log

    # Example: If the incoming message is text
    user_message = data.get("message", "")

    # For now, just echo back
    reply = f"You said: {user_message}"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
