from scipcffi import SCIP

scip = SCIP()

x = scip.add_var('x', obj=2)
y = scip.add_var('y', -1, 1, obj=5)

xx = scip.get_var('x')
zz = scip.get_var('z')

assert x == xx

terms = [(x, 5), (y, 23)]
cons = scip.add_cons('foo', terms, lhs=17)

scip.solve()
