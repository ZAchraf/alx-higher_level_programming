#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        v = fct(*args)
        return v
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
