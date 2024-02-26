#!/usr/bin/python3
"""defining file-writing fun."""


def write_file(filename="", text=""):
    """writing string to a UTF8 text"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
