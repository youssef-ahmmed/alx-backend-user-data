#!/usr/bin/env python3
"""Implement session auth for end points API"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """SessionDBAuth class"""

    def create_session(self, user_id=None):
        """ Creates and stores new instance of UserSession
            and returns the Session ID"""
        session_id = super().create_session(user_id)

        user = UserSession(
            **{"session_id": session_id, "user_id": user_id}
        )
        user.save()

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Returns the User ID by requesting UserSession
            in the database based on session_id"""
        user_id = UserSession.search({"session_id": session_id})
        return user_id if user_id else None

    def destroy_session(self, request=None):
        """ Destroys the UserSession based on the Session ID
            from the request cookie"""
        if not request:
            return False

        session_id = self.session_cookie(request)
        if not session_id:
            return False

        user_session = self.user_id_by_session_id(session_id)
        if not user_session:
            return False

        user_session[0].remove()

        return True
