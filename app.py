from flask import Flask
from datetime import datetime
import os, pytz

app = Flask(__name__)

@app.route("/")
def home():
    time = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime("%H:%M:%S")
    info = str(os.environ.get("HOSTNAME"))

    return f'[{time}] SRV said that: {info}'

if __name__ == '__main__':
    app.run()