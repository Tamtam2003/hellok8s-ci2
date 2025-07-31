from flask import Flask
import os

app = Flask(__name__)

username = os.environ.get('APP_USERNAME', 'Anonymous')

@app.route('/')
def home():
    return f"Welcome, {username}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
