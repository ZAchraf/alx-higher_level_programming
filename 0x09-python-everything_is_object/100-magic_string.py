#!/usr/bin/python3
def magic_string():
    magic_string.numb = getattr(magic_string, 'numb', 0) + 1
    return ", ".join(["BestSchool" for i in range(magic_string.numb)])
