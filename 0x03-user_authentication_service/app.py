#!/usr/bin/env python3
"""Simple Flask app"""
from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
auth = Auth()
app.url_map.strict_slashes = False


@app.route("/", methods=["GET"])
def index() -> str:
    """GET /
    Return:
        - The home page's payload.
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register() -> str:
    """POST /users
    Return:
        - Success creation, 201
        or
        - Failed creation, 400
    """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        auth.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 201
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
