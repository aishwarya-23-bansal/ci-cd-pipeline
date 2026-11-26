
from flask import Flask, jsonify
import os

app = Flask(__name__)

VERSION = os.environ.get("APP_VERSION", "3.0")


@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Automated CI/CD Pipeline</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #101827;
                color: white;
                text-align: center;
                padding: 40px 20px;
            }}
            h1 {{ color: #38bdf8; }}
            .version {{
                color: #4ade80;
                font-size: 22px;
            }}
            .dashboard {{
                max-width: 650px;
                margin: 30px auto;
                background: #1e293b;
                padding: 25px;
                border-radius: 15px;
            }}
            .stage {{
                background: #334155;
                padding: 15px;
                margin: 12px 0;
                border-radius: 8px;
                display: flex;
                justify-content: space-between;
            }}
            .success {{ color: #4ade80; }}
            .footer {{ color: #94a3b8; margin-top: 30px; }}
        </style>
    </head>
    <body>
        <h1>Automated CI/CD Pipeline</h1>
        <p class="version">Application Version: {VERSION}</p>
        <p>Continuous Integration and Continuous Deployment</p>

        <div class="dashboard">
            <h2>Pipeline Dashboard</h2>

            <div class="stage">
                <span>Code Push to GitHub</span>
                <span class="success">✓ Success</span>
            </div>
            <div class="stage">
                <span>Automated Testing (Pytest)</span>
                <span class="success">✓ Passed</span>
            </div>
            <div class="stage">
                <span>Docker Image Build</span>
                <span class="success">✓ Success</span>
            </div>
            <div class="stage">
                <span>Docker Hub Publishing</span>
                <span class="success">✓ Success</span>
            </div>
            <div class="stage">
                <span>Cloud Deployment</span>
                <span class="success">✓ Deployed</span>
            </div>
            <p class="footer">
                Powered by Flask | Docker | GitHub Actions | Render
            </p>
        </div>
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
