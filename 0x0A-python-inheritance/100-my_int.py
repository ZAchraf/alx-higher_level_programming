#!/usr/bin/python3
"""MYINT, definig a class that inherit from int"""


class MyInt(int):
    """inverting operators == & !="""
    def __new__(clas, *args, **kwargs):
        """Creating a new inst"""
        return super(MyInt, clas).__new__(clas, *args, **kwargs)

    def __eq__(self, value):
        """changing != to =="""
        return int(self) != value

    def __ne__(self, value):
        """changing == to !="""
        return int(self) == value
