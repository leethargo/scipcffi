import pytest

from scipcffi import SCIP, Status
from scipcffi.util import eq_float

def test_created_and_delete():
    '''SCIP solvers can be created and deleted'''
    scip = SCIP()
    del scip


def test_get_vars():
    '''vars can be found by name'''
    scip = SCIP()
    x = scip.add_var('x')
    y = scip.add_var('y')
    assert x != y
    
    assert scip.get_var('x') == x
    assert scip.get_var('z') is None


def test_solve():
    '''test all steps from model building to solution values'''
    scip = SCIP()

    # build simple model
    x = scip.add_var('x', obj=1)
    y = scip.add_var('y', obj=2)
    cons = scip.add_cons('c', [(x, 1), (y, 1)], lhs=1)
    
    # solve
    status = scip.solve()
    assert status == Status.OPTIMAL

    # compare (unique) values from optimal solution
    assert eq_float(x.val, 1.0)
    assert eq_float(y.val, 0.0)
