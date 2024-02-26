#!/usr/bin/python3
"""JSON-to-object funct."""
import json


def from_json_string(my_str):
    """Returning Python object rep of JSON str."""
    return json.loads(my_str)
