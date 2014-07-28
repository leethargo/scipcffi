from scipcffi.ffi import ffi, lib
from scipcffi import util

class SCIPException(Exception):
    pass

RC = util.make_enum([
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

_rc = {
     1: RC.SCIP_OKAY,
     0: RC.SCIP_ERROR,
    -1: RC.SCIP_NOMEMORY,
    -2: RC.SCIP_READERROR,
    -3: RC.SCIP_WRITEERROR,
    -4: RC.SCIP_NOFILE,
    -5: RC.SCIP_FILECREATEERROR,
    -6: RC.SCIP_LPERROR,
    -7: RC.SCIP_NOPROBLEM,
    -8: RC.SCIP_INVALIDCALL,
    -9: RC.SCIP_INVALIDDATA,
    10: RC.SCIP_INVALIDRESULT,
    11: RC.SCIP_PLUGINNOTFOUND,
    12: RC.SCIP_PARAMETERUNKNOWN,
    13: RC.SCIP_PARAMETERWRONGTYPE,
    14: RC.SCIP_PARAMETERWRONGVAL,
    15: RC.SCIP_KEYALREADYEXISTING,
    16: RC.SCIP_MAXDEPTHLEVEL,
    17: RC.SCIP_BRANCHERROR,
    }

def _call(rc):
    if rc != 1:
        raise SCIPException('%s' % _rc[rc])
    
class SCIP:
    def __init__(self):
        # TODO: work without double ptr?
        self._ptrptr = ffi.new('SCIP**')
        _call(lib.SCIPcreate(self._ptrptr))
        self._ptr = self._ptrptr[0]
        assert self._ptr != ffi.NULL

    def __del__(self):
        _call(lib.SCIPfree(self._ptrptr))

