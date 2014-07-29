from collections import namedtuple

def make_enum(items):
    return namedtuple('enum', items)._make(items)
