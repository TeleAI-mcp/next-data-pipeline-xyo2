# This file was copied from pallets/flask/src/flask/app.py
# Original source: https://github.com/pallets/flask/blob/main/src/flask/app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()