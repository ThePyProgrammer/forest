# stdlib
from forest._importable import LazyImport

## system
from .system import *

## string
re = LazyImport("import re", "LIBRARY: re - regex operations, derived from 'import re', part of The Python Standard Library")


## io
io = LazyImport("import io", "LIBRARY: io — Core tools for working with streams, derived from 'import io', part of The Python Standard Library")
glob = LazyImport("import glob", "LIBRARY: glob — Unix style pathname pattern expansion, derived from 'import glob', part of The Python Standard Library")
Path = LazyImport("from pathlib import Path", "CLASS: pathlib.Path — represents concrete paths of the system’s path flavour, derived from 'from pathlib import Path', part of The Python Standard Library")
pathlib = LazyImport("import pathlib", "LIBRARY: pathlib — Object-oriented filesystem paths, derived from 'import pathlib', part of The Python Standard Library")
pickle = LazyImport("import pickle", "LIBRARY: pickle — Python object serialization, derived from 'import pickle', part of The Python Standard Library")


## shell
tqdm = LazyImport("import tqdm", "PACKAGE: tqdm — A Fast Extensible Progress Bar for Python and CLI, derived from 'import tqdm', from https://github.com/tqdm/tqdm, Documentation: https://tqdm.github.io/")
sh = LazyImport("import sh", "PACKAGE: sh — a unique subprocess wrapper that maps your system programs to Python functions dynamically, derived from 'import sh', from https://github.com/amoffat/sh, Documentation: http://amoffat.github.io/sh/")
inspect = LazyImport("import inspect", "LIBRARY: inspect — Inspect live objects, derived from 'import inspect', part of The Python Standard Library")
