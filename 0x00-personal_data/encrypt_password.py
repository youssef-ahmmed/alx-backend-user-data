#!/usr/bin/env python3
"""Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hash password"""
    password_bytes = password.encode('utf-8')
    return bcrypt.hashpw(password_bytes, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if the given password is valid"""
    password_bytes = password.encode('utf-8')
    return bcrypt.hashpw(password_bytes, hashed_password) == hashed_password
