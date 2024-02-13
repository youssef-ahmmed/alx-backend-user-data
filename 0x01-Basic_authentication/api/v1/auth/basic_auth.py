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

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        """Returns the decoded value of a Base64 string"""
        if (not base64_authorization_header
                or type(base64_authorization_header) != str):
            return None

        try:
            return (base64.b64decode(base64_authorization_header)
                    .decode('utf-8'))
        except UnicodeDecodeError:
            return None
