from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = "1.1.0"

@app.route("/")
def home():
    return "Welcome to Enterprise CI/CD Pipeline!"

@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    }), 200

@app.route("/version")
def version():
    return jsonify({
        "version": APP_VERSION
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)