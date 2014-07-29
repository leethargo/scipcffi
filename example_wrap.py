from scipcffi import SCIP

scip = SCIP()

x = scip.add_var('x')
y = scip.add_var('y', -1.0, 1.0)

xx = scip.get_var('x')
zz = scip.get_var('z')

assert x == xx

terms = [(x, 5.0), (y, -23.0)]
cons = scip.add_cons('foo', terms)
