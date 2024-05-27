#!/usr/bin/env python3
""" Auth class
"""

from db import DB
from typing import TypeVar
from user import User
import bcrypt
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """
    _hash_password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    _generate_uuid.
    """
    return str(uuid4())


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()


