'''define the interface to the SCIP library'''

import cffi

_declarations = '''
// enums
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

enum SCIP_Status
{
   SCIP_STATUS_UNKNOWN        =  0,
   SCIP_STATUS_USERINTERRUPT  =  1,
   SCIP_STATUS_NODELIMIT      =  2,
   SCIP_STATUS_TOTALNODELIMIT =  3,
   SCIP_STATUS_STALLNODELIMIT =  4,
   SCIP_STATUS_TIMELIMIT      =  5,
   SCIP_STATUS_MEMLIMIT       =  6,
   SCIP_STATUS_GAPLIMIT       =  7,
   SCIP_STATUS_SOLLIMIT       =  8,
   SCIP_STATUS_BESTSOLLIMIT   =  9,
   SCIP_STATUS_OPTIMAL        = 10,
   SCIP_STATUS_INFEASIBLE     = 11,
   SCIP_STATUS_UNBOUNDED      = 12,
   SCIP_STATUS_INFORUNBD      = 13
};
typedef enum SCIP_Status SCIP_STATUS;

enum SCIP_Objsense
{
   SCIP_OBJSENSE_MAXIMIZE = -1,
   SCIP_OBJSENSE_MINIMIZE =  1
};
typedef enum SCIP_Objsense SCIP_OBJSENSE;

enum SCIP_Vartype
{
   SCIP_VARTYPE_BINARY     = 0,
   SCIP_VARTYPE_INTEGER    = 1,
   SCIP_VARTYPE_IMPLINT    = 2,
   SCIP_VARTYPE_CONTINUOUS = 3
};
typedef enum SCIP_Vartype SCIP_VARTYPE;

// numeric types
typedef unsigned int SCIP_Bool;
typedef double SCIP_Real;

// (opaque) typedefs
typedef ... SCIP;
typedef ... SCIP_VAR;
typedef ... SCIP_CONS;
typedef ... SCIP_SOL;

// from scip.h
SCIP_RETCODE SCIPcreate(SCIP** scip);
SCIP_RETCODE SCIPfree(SCIP** scip);
SCIP_STATUS SCIPgetStatus(SCIP* scip);
SCIP_RETCODE SCIPcreateProbBasic(SCIP* scip, const char* name);
SCIP_RETCODE SCIPsetObjsense(SCIP* scip, SCIP_OBJSENSE objsense);
SCIP_RETCODE SCIPsolve(SCIP* scip);
SCIP_RETCODE SCIPfreeSolve(SCIP* scip, SCIP_Bool restart);
SCIP_Real SCIPgetSolVal(SCIP* scip, SCIP_SOL* sol, SCIP_VAR* var);

SCIP_RETCODE SCIPcreateVarBasic(
    SCIP* scip,
    SCIP_VAR** var,
    const char* name,
    SCIP_Real lb,
    SCIP_Real ub,
    SCIP_Real obj,
    SCIP_VARTYPE vartype);
SCIP_RETCODE SCIPcaptureVar(SCIP* scip, SCIP_VAR* var);
SCIP_RETCODE SCIPreleaseVar(SCIP* scip, SCIP_VAR** var);
SCIP_RETCODE SCIPaddVar(SCIP* scip, SCIP_VAR* var);
SCIP_VAR* SCIPfindVar(SCIP* scip, const char* name);

SCIP_RETCODE SCIPcaptureCons(SCIP* scip, SCIP_CONS* cons);
SCIP_RETCODE SCIPreleaseCons(SCIP* scip, SCIP_CONS** cons);
SCIP_RETCODE SCIPaddCons(SCIP* scip, SCIP_CONS* cons);
SCIP_RETCODE SCIPdelCons(SCIP* scip, SCIP_CONS* cons);
SCIP_CONS* SCIPfindCons(SCIP* scip, const char* name);

// from cons_linear.h
SCIP_RETCODE SCIPcreateConsBasicLinear(
    SCIP* scip,
    SCIP_CONS** cons,
    const char* name,
    int nvars,
    SCIP_VAR** vars,
    SCIP_Real* vals,
    SCIP_Real lhs,
    SCIP_Real rhs);

'''

_headers = '''
    #include <scip/scip.h>
    #include <scip/cons_linear.h>
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
