#!/usr/bin/env python3
"""Regex-ing"""
import logging
import re
from typing import Tuple, List

PII_FIELDS: Tuple = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns the log message obfuscated"""
    return re.sub(r'(\w+)=([^{}]+)'.format(separator),
                  lambda match: '{}={}'.format(match.group(1), redaction)
                  if match.group(1) in fields
                  else '{}={}'.format(match.group(1), match.group(2)), message)


def get_logger() -> logging.Logger:
    """Get logger with specific configs"""
    logger = logging.getLogger("user_data")
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(RedactingFormatter(PII_FIELDS))

    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Call super formatter"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format log record"""
        msg = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
