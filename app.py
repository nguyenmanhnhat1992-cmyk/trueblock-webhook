from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8632327985:AAG6_J_JKlG3m5ST63R-z0gYNUE-QvS4gxw"
CHAT_ID = "-1003385973024"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.json
        print("DATA RECEIVED:", data, flush=True)

        message = data.get("comment")
        if not message:
            message = data.get("message", "No message")

        print("MESSAGE:", message, flush=True)

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message
        }

        r = requests.post(url, json=payload)
        print("TELEGRAM RESPONSE:", r.text, flush=True)

        return {"ok": True}

    except Exception as e:
        print("ERROR:", str(e), flush=True)
        return {"ok": False, "error": str(e)}

@app.route("/", methods=["GET"])
def home():
    return "TrueBlock Webhook is running!"
