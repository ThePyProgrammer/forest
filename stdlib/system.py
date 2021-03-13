## system
from forest._importable import LazyImport

sys = LazyImport("import sys", "LIBRARY: sys — System-specific parameters and functions, derived from 'import sys', part of The Python Standard Library")
system = LazyImport("import sys as system", "LIBRARY: sys — System-specific parameters and functions, derived from 'import sys', part of The Python Standard Library")
System = LazyImport("import sys as System", "LIBRARY: sys — System-specific parameters and functions, derived from 'import sys', part of The Python Standard Library")
os = LazyImport("import os", "LIBRARY: os — Miscellaneous operating system interfaces, derived from 'import os', part of The Python Standard Library")
stat = LazyImport("import stat", "LIBRARY: stat — Interpreting os.stat(), os.fstat() and os.lstat() results, derived from 'import stat', part of The Python Standard Library")
subprocess = LazyImport("import subprocess", "LIBRARY: subprocess — Subprocess management, derived from 'import subprocess', part of The Python Standard Library")
