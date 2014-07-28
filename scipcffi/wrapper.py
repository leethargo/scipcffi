from scipcffi.ffi import ffi, lib
from scipcffi import util

class SCIPException(Exception):
    pass

ReturnCode = util.make_enum([
    'SCIP_OKAY',
    'SCIP_ERROR',
    'SCIP_NOMEMORY',
    'SCIP_READERROR',
    'SCIP_WRITEERROR',
    'SCIP_NOFILE',
    'SCIP_FILECREATEERROR',
    'SCIP_LPERROR',
    'SCIP_NOPROBLEM',
    'SCIP_INVALIDCALL',
    'SCIP_INVALIDDATA',
    'SCIP_INVALIDRESULT',
    'SCIP_PLUGINNOTFOUND',
    'SCIP_PARAMETERUNKNOWN',
    'SCIP_PARAMETERWRONGTYPE',
    'SCIP_PARAMETERWRONGVAL',
    'SCIP_KEYALREADYEXISTING',
    'SCIP_MAXDEPTHLEVEL',
    'SCIP_BRANCHERROR',
    ])

_rc_rev = {
    lib.SCIP_OKAY: ReturnCode.SCIP_OKAY,
    lib.SCIP_ERROR: ReturnCode.SCIP_ERROR,
    lib.SCIP_NOMEMORY: ReturnCode.SCIP_NOMEMORY,
    lib.SCIP_READERROR: ReturnCode.SCIP_READERROR,
    lib.SCIP_WRITEERROR: ReturnCode.SCIP_WRITEERROR,
    lib.SCIP_NOFILE: ReturnCode.SCIP_NOFILE,
    lib.SCIP_FILECREATEERROR: ReturnCode.SCIP_FILECREATEERROR,
    lib.SCIP_LPERROR: ReturnCode.SCIP_LPERROR,
    lib.SCIP_NOPROBLEM: ReturnCode.SCIP_NOPROBLEM,
    lib.SCIP_INVALIDCALL: ReturnCode.SCIP_INVALIDCALL,
    lib.SCIP_INVALIDDATA: ReturnCode.SCIP_INVALIDDATA,
    lib.SCIP_INVALIDRESULT: ReturnCode.SCIP_INVALIDRESULT,
    lib.SCIP_PLUGINNOTFOUND: ReturnCode.SCIP_PLUGINNOTFOUND,
    lib.SCIP_PARAMETERUNKNOWN: ReturnCode.SCIP_PARAMETERUNKNOWN,
    lib.SCIP_PARAMETERWRONGTYPE: ReturnCode.SCIP_PARAMETERWRONGTYPE,
    lib.SCIP_PARAMETERWRONGVAL: ReturnCode.SCIP_PARAMETERWRONGVAL,
    lib.SCIP_KEYALREADYEXISTING: ReturnCode.SCIP_KEYALREADYEXISTING,
    lib.SCIP_MAXDEPTHLEVEL: ReturnCode.SCIP_MAXDEPTHLEVEL,
    lib.SCIP_BRANCHERROR: ReturnCode.SCIP_BRANCHERROR,
    }

VarType = util.make_enum([
    'BINARY',
    'INTEGER',
    'IMPLINT',
    'CONTINUOUS',
    ])

_vt = {
    VarType.BINARY: lib.SCIP_VARTYPE_BINARY,
    VarType.INTEGER: lib.SCIP_VARTYPE_INTEGER,
    VarType.IMPLINT: lib.SCIP_VARTYPE_IMPLINT,
    VarType.CONTINUOUS: lib.SCIP_VARTYPE_CONTINUOUS,
    }

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

        # always create a problem
        name = 'anon'.encode('utf8')
        _call(lib.SCIPcreateProbBasic(self._ptr, name))

    def __del__(self):
        _call(lib.SCIPfree(self._ptrptr))

    def add_var(self, name, lb=0.0, ub=float('inf'), obj=0.0,
                vartype=VarType.CONTINUOUS):
        # TODO: work without double ptr
        var_ptrptr = ffi.new('SCIP_VAR**')
        _call(lib.SCIPcreateVarBasic(
            self._ptr, var_ptrptr, name.encode('utf8'),
            lb, ub, obj, _vt[vartype]))
        return Var(self, var_ptrptr)

class Var:
    def __init__(self, scip, var_ptrptr):
        self.scip = scip
        self._ptrptr = var_ptrptr
        self._ptr = self._ptrptr[0]
        assert self._ptr != ffi.NULL
        _call(lib.SCIPcaptureVar(self.scip._ptr, self._ptr))

    def __del__(self):
        _call(lib.SCIPreleaseVar(self.scip._ptr, self._ptrptr))
