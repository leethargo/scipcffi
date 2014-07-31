from collections import namedtuple

from scipcffi.ffi import lib


class SCIPException(Exception):
    pass


def make_enum(items, prefix=''):
    class Enum(namedtuple('enum', items)):
        to_scip = {i:getattr(lib, prefix + i)  for i in items}
        from_scip = {getattr(lib, prefix + i):i  for i in items}

    return Enum._make(items)


ReturnCode = make_enum([
    'OKAY',
    'ERROR',
    'NOMEMORY',
    'READERROR',
    'WRITEERROR',
    'NOFILE',
    'FILECREATEERROR',
    'LPERROR',
    'NOPROBLEM',
    'INVALIDCALL',
    'INVALIDDATA',
    'INVALIDRESULT',
    'PLUGINNOTFOUND',
    'PARAMETERUNKNOWN',
    'PARAMETERWRONGTYPE',
    'PARAMETERWRONGVAL',
    'KEYALREADYEXISTING',
    'MAXDEPTHLEVEL',
    'BRANCHERROR',
], prefix='SCIP_')


Status = make_enum([
    'UNKNOWN',
    'USERINTERRUPT',
    'NODELIMIT',
    'TOTALNODELIMIT',
    'STALLNODELIMIT',
    'TIMELIMIT',
    'MEMLIMIT',
    'GAPLIMIT',
    'SOLLIMIT',
    'BESTSOLLIMIT',
    'OPTIMAL',
    'INFEASIBLE',
    'UNBOUNDED',
    'INFORUNBD',
], prefix='SCIP_STATUS_')


VarType = make_enum([
    'BINARY',
    'INTEGER',
    'IMPLINT',
    'CONTINUOUS',
], prefix='SCIP_VARTYPE_')


ObjSense = make_enum([
    'MAXIMIZE',
    'MINIMIZE',
], prefix='SCIP_OBJSENSE_')
