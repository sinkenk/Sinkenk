import os
from flask import Flask # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  
    app.run(host='0.0.0.0', port=port)
