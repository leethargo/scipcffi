from scipcffi import SCIP, Status

scip = SCIP()

x = scip.add_var('x', obj=2)
y = scip.add_var('y', -1, 1, obj=5)

xx = scip.get_var('x')
zz = scip.get_var('z')

assert x == xx

terms = [(x, 5), (y, 23)]
cons = scip.add_cons('foo', terms, lhs=25)

status = scip.solve()
assert status == Status.OPTIMAL

_x = scip.get_val(x)
_y = scip.get_val(y)

print('x: %f, y: %f' % (_x, _y))

assert x.val == _x
assert y.val == _y

print(str(x))
