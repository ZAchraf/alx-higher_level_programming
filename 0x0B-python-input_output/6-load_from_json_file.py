#!/usr/bin/python3
"""dining JSON file-reading funct."""
import json


def load_from_json_file(filename):
    """python object from JSONfile."""
    with open(filename) as f:
        return json.load(f)
