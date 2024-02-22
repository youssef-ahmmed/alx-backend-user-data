#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from sqlalchemy.exc import NoResultFound

from db import DB
import uuid
from user import User


def _hash_password(password: str) -> bytes:
    """Hash password using bcrypt"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate random uuid"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Init object of a database"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register user with auth"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email=email,
                                     hashed_password=_hash_password(password))
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """Check if the login is valid"""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode("utf-8"),
                                  user.hashed_password)
        except NoResultFound:
            return False
