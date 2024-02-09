#!/usr/bin/env python3
"""Regex-ing"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Returns the log message obfuscated"""
    return re.sub(r'(\w+)=([^{}]+)'.format(separator),
                  lambda match: '{}={}'.format(match.group(1), redaction)
                  if match.group(1) in fields
                  else '{}={}'.format(match.group(1), match.group(2)), message)
