import os

from flask import Flask, jsonify

app = Flask(__name__)

# # Load DB connection info from environment variables
# DB_HOST = os.getenv("POSTGRES_HOST", "db")
# DB_NAME = os.getenv("POSTGRES_DB", "testdb")
# DB_USER = os.getenv("POSTGRES_USER", "postgres")
# DB_PASS = os.getenv("POSTGRES_PASSWORD", "example")
# DB_PORT = os.getenv("POSTGRES_PORT", "5432")

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "success",
        "message": "Python Flask app v9 openshift running successfully!"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
