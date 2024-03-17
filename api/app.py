import time

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def post_payload():
    if request.method == 'POST':
        payload = request.json
        time.sleep(0.1)
        return jsonify(payload), 200


@app.route('/')
def hello():
    return 'API is up and running!', 200


if __name__ == '__main__':
    app.run(debug=True)
