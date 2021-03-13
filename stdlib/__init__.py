# stdlib
from forest._importable import LazyImport


## system
from .system import *

## io
from .iopy import *

## shell
from .shell import *

inspect = LazyImport("import inspect", "LIBRARY: inspect — Inspect live objects, derived from 'import inspect', part of The Python Standard Library")


### debugging
pdb = LazyImport("import pdb", "LIBRARY pdb — The Python Debugger, derived from 'import pdb', from The Python Standard Library")

### Windows
wincl = LazyImport('import win32com.client as wincl', "PACKAGE wincl derived from win32com.client — Python for Windows (pywin32) Extensions, derived from 'import win32com.client as wincl', from https://github.com/mhammond/pywin32, Documentation: http://timgolden.me.uk/pywin32-docs/contents.html")
