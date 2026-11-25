
from flask import Flask, jsonify
import os

app = Flask(__name__)

VERSION = os.environ.get("APP_VERSION", "2.0")


@app.route("/")
def home():
    return f"""
    <html>
    <head>
        <title>Automated CI/CD Pipeline</title>
    </head>
    <body style="font-family: Arial; text-align: center; padding: 50px;">
        <h1>Welcome to Automated CI/CD Pipeline!</h1>
        <h2>Application Version: {VERSION}</h2>
        <p>Successfully deployed using CI/CD.</p>
        <p>Powered by Flask, Docker and GitHub Actions.</p>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "version": VERSION
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
