#!/usr/bin/env python3
""" template for an authentication system"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ define paths that require auth"""
        if not path or not excluded_paths:
            return True

        path = path if path.endswith('/') else path + '/'
        if path not in excluded_paths:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """ Define the authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Check for the current user to require auth"""
        return None
