#!/usr/bin/python3
'''inherits_from method. Defining an inherited class-checking Fun'''


def inherits_from(obj, a_class):
    '''it will check if an object is inhereted instancce of a classs'''
    return isinstance(obj, a_class) and type(obj) != a_class
