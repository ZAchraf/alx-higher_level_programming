#!/usr/bin/python3
"""defining JSON file-writing funct."""
import json


def save_to_json_file(my_obj, filename):
    """Writing an object using JSON rep"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
