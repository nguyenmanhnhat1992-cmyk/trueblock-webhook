from flask import Flask, request
import requests

app = Flask(__name__)

# =========================
# TELEGRAM CONFIG
# =========================
BOT_TOKEN = "8632327985:AAG6_J_JKlG3m5ST63R-z0gYNUE-QvS4gxw"
CHAT_ID = "-1003385973024"

# =========================
# WEBHOOK
# =========================
@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.json

        # Ưu tiên đọc comment (script mới)
        message = data.get("comment")

        # fallback nếu dùng script cũ
        if not message:
            message = data.get("message", "No message")

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        payload = {
            "chat_id": CHAT_ID,
            "text": message
        }

        requests.post(url, json=payload)
        return {"ok": True}

    except Exception as e:
        return {"ok": False, "error": str(e)}

# =========================
# HOME
# =========================
@app.route("/", methods=["GET"])
def home():
    return "TrueBlock Webhook is running!"