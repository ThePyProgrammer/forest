## shell
from forest._importable import LazyImport

tqdm = LazyImport("import tqdm", "PACKAGE: tqdm — A Fast Extensible Progress Bar for Python and CLI, derived from 'import tqdm', from https://github.com/tqdm/tqdm, Documentation: https://tqdm.github.io/")
sh = LazyImport("import sh", "PACKAGE: sh — a unique subprocess wrapper that maps your system programs to Python functions dynamically, derived from 'import sh', from https://github.com/amoffat/sh, Documentation: http://amoffat.github.io/sh/")
inspect = LazyImport("import inspect", "LIBRARY: inspect — Inspect live objects, derived from 'import inspect', part of The Python Standard Library")
