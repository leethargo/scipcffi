from scipcffi import SCIP

scip = SCIP()

x = scip.add_var('x')
y = scip.add_var('y', -1.0, 1.0)

xx = scip.get_var('x')
zz = scip.get_var('z')

assert x == xx

