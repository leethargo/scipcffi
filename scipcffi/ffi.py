'''define the interface to the SCIP library'''

import cffi

_declarations = '''
enum SCIP_Retcode
{
   SCIP_OKAY               =   1,
   SCIP_ERROR              =   0,
   SCIP_NOMEMORY           =  -1,
   SCIP_READERROR          =  -2,
   SCIP_WRITEERROR         =  -3,
   SCIP_NOFILE             =  -4,
   SCIP_FILECREATEERROR    =  -5,
   SCIP_LPERROR            =  -6,
   SCIP_NOPROBLEM          =  -7,
   SCIP_INVALIDCALL        =  -8,
   SCIP_INVALIDDATA        =  -9,
   SCIP_INVALIDRESULT      = -10,
   SCIP_PLUGINNOTFOUND     = -11,
   SCIP_PARAMETERUNKNOWN   = -12,
   SCIP_PARAMETERWRONGTYPE = -13,
   SCIP_PARAMETERWRONGVAL  = -14,
   SCIP_KEYALREADYEXISTING = -15,
   SCIP_MAXDEPTHLEVEL      = -16,
   SCIP_BRANCHERROR        = -17
};
typedef enum SCIP_Retcode SCIP_RETCODE;

typedef ... SCIP;

SCIP_RETCODE SCIPcreate(SCIP** scip);
'''

_headers = '''
    #include <scip/scip.h>
'''

_libraries = [
    'gmp',
    'scipopt', # the important one
    'readline',
    'z',
]

ffi = cffi.FFI()
ffi.cdef(_declarations)
lib = ffi.verify(_headers, libraries=_libraries)
