#!/usr/bin/python3
"""defining file-appending fun."""


def append_write(filename="", text=""):
    """writing string to a UTF8 text"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
