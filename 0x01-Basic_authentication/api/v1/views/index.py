#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, Response
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> Response:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {'users': User.count()}
    return jsonify(stats)


@app_views.route('/unauthorized', strict_slashes=False)
def unauthorized() -> str:
    """ Get /api/v1/unauthorized
    Return:
        - raising 401 status error
    """
    return abort(401)


@app_views.route('/forbidden', strict_slashes=False)
def forbidden() -> str:
    """ Get /api/v1/unauthorized
    Return:
        - raising 403 status error
    """
    return abort(403)
