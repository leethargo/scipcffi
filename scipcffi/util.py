from collections import namedtuple

def make_enum(items):
    return namedtuple('anon', items)._make(items)
