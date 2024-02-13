#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv

from api.v1.auth.auth import Auth
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
auth_type = getenv("AUTH_TYPE")

if auth_type == "auth":
    auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def handle_auth() -> None:
    """Handle authorization before sending requests"""
    if not auth:
        return

    excluded_list = ['/api/v1/status/', '/api/v1/unauthorized/',
                     '/api/v1/forbidden/']
    require_auth = auth.require_auth(request.path, excluded_list)
    if not require_auth:
        return

    auth_header = auth.authorization_header(request)
    if not auth_header:
        abort(401)

    curr_user = auth.current_user(request)
    if not curr_user:
        abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
