import pytest

from scipcffi import SCIP

def test_created_and_delete():
    '''SCIP solvers can be created and deleted'''
    scip = SCIP()
    del scip
