#!/usr/bin/env python3
"""Implement basic auth for end points API"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ Basic auth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns base64 of Authorization header"""
        if not authorization_header or type(authorization_header) != str:
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]
