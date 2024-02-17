#!/usr/bin/env python3
"""Implement session auth for end points API"""
import uuid

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Session auth class"""

    user_id_by_session_id: dict = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create session id for a user"""
        if not user_id or type(user_id) != str:
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id
