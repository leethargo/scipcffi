import scipcffi.ffi as s

scip_ptr = s.ffi.new('SCIP**')
rc = s.lib.SCIPcreate(scip_ptr)
assert rc == s.lib.SCIP_OKAY
scip = scip_ptr[0]

