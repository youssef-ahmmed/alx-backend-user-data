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

        for excluded_path in excluded_paths:
            if (excluded_path.endswith('*')
                    and path.startswith(excluded_path[:-1])):
                return False

            if path == excluded_path:
                return False

        return True

        def authorization_header(self, request=None) -> str:
        """ Define the authorization header"""
        if not request:
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Check for the current user to require auth"""
        return None
