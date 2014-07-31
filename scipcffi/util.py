TOL = 1e-6

def eq_float(x, y):
    return abs(x - y) <= TOL

def gt_float(x, y):
    return x + TOL > y

def ge_float(x, y):
    return x + TOL >= y

def lt_float(x, y):
    return x < y + TOL

def le_float(x, y):
    return x <= y + TOL
