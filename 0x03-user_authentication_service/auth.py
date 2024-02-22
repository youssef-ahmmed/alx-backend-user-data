#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from sqlalchemy.exc import NoResultFound

from db import DB, User


def _hash_password(password: str) -> bytes:
    """Hash password using bcrypt"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self) -> None:
        """Init object of a database"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register user with auth"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email,
                                     _hash_password(password).decode("utf-8"))
        raise ValueError(f"User {email} already exists")
