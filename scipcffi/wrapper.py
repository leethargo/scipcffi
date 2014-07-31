from scipcffi.ffi import ffi, lib
from scipcffi.types import Status, VarType

CODEC = 'ascii'


def _call(rc):
    if rc != lib.SCIP_OKAY:
        raise SCIPException('%s' % _rc_rev[rc])

class SCIP:
    def __init__(self):
        # TODO: work without double ptr?
        self._ptrptr = ffi.new('SCIP**')
        _call(lib.SCIPcreate(self._ptrptr))
        self._ptr = self._ptrptr[0]
        assert self._ptr != ffi.NULL

        # initialize, like in SCIPrunShell
        _call(lib.SCIPincludeDefaultPlugins(self._ptr))

        # always create a problem
        name = 'anon'.encode(CODEC)
        _call(lib.SCIPcreateProbBasic(self._ptr, name))

    def __del__(self):
        _call(lib.SCIPfree(self._ptrptr))
        self._ptr = ffi.NULL

    def add_var(self, name, lb=0.0, ub=float('inf'), obj=0.0,
                vartype=VarType.CONTINUOUS):
        # TODO: work without double ptr
        var_ptrptr = ffi.new('SCIP_VAR**')
        _call(lib.SCIPcreateVarBasic(
            self._ptr, var_ptrptr, name.encode(CODEC),
            lb, ub, obj, VarType.to_scip[vartype]))
        var_ptr = var_ptrptr[0]
        assert var_ptr != ffi.NULL
        _call(lib.SCIPaddVar(self._ptr, var_ptr))
        return Var(self, var_ptr)

    def get_var(self, name):
        var_ptr = lib.SCIPfindVar(self._ptr, name.encode(CODEC))
        if var_ptr == ffi.NULL:
            return None
        else:
            return Var(self, var_ptr)

    def add_cons(self, name, terms, lhs=0.0, rhs=float('inf')):
        # TODO: work without double ptr
        cons_ptrptr = ffi.new('SCIP_CONS**')
        vars = ffi.new('SCIP_VAR*[]', [v._ptr for (v,c) in terms])
        vals = ffi.new('SCIP_Real[]', [c for (v,c) in terms])
        _call(lib.SCIPcreateConsBasicLinear(
            self._ptr, cons_ptrptr, name.encode(CODEC),
            len(terms), vars, vals, lhs, rhs))
        cons_ptr = cons_ptrptr[0]
        assert cons_ptr != ffi.NULL
        _call(lib.SCIPaddCons(self._ptr, cons_ptr))
        return Cons(self, cons_ptr)

    def solve(self):
        _call(lib.SCIPsolve(self._ptr))
        _status = lib.SCIPgetStatus(self._ptr)
        return Status.from_scip[_status]

    def get_val(self, var):
        return lib.SCIPgetSolVal(self._ptr, ffi.NULL, var._ptr)


class Var:
    def __init__(self, scip, var_ptr):
        self._scip = scip
        self._ptr = var_ptr
        assert self._ptr != ffi.NULL

    def __eq__(self, other):
        return isinstance(other, Var) and self._ptr == other._ptr

    @property
    def val(self):
        return self._scip.get_val(self)

    @property
    def name(self):
        _name = ffi.string(lib.SCIPvarGetName(self._ptr))
        return _name.decode(CODEC)

    def __str__(self):
        return self.name


class Cons:
    def __init__(self, scip, cons_ptr):
        self._scip = scip
        self._ptr = cons_ptr
        assert self._ptr != ffi.NULL

    def __eq__(self, other):
        return isinstance(other, Cons) and self._ptr == other._ptr
