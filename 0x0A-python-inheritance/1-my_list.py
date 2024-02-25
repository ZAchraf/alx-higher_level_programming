#!/usr/bin/python3
'''Module that contains MyList class.'''


class MyList(list):
    '''Customizing a subclass .'''
    def print_sorted(self):
        '''it will print a sorted list.'''
        print(sorted(self))
