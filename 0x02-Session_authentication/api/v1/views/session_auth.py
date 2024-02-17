#!/usr/bin/env python3
""" Module for Session authentication view"""

from api.v1.views import app_views
from flask import jsonify, request, Response
from os import getenv

from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session() -> str:
    """ POST /api/v1/auth_session/login
    Return:

    """
    user_email = request.form.get("email")
    if not user_email:
        return jsonify({"error": "email missing"}), 400

    user_pwd = request.form.get("password")
    if not user_pwd:
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": user_email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    if not users[0].is_valid_password(user_pwd):
        return jsonify({"error": "wrong password"}), 401

    for user in users:
        if user.is_valid_password(user_pwd):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            session_name = getenv("SESSION_NAME")

            response = jsonify(user.to_json())
            response.set_cookie(session_name, session_id)
            return response

    return jsonify({"error": "wrong password"}), 401
