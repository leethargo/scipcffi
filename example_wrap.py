import scipcffi.wrapper as s

scip = s.SCIP()

x = scip.add_var('x')
y = scip.add_var('y', -1.0, 1.0)
