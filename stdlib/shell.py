## shell
from forest._importable import LazyImport

tqdm = LazyImport("import tqdm", "PACKAGE: tqdm — A Fast Extensible Progress Bar for Python and CLI, derived from 'import tqdm', from https://github.com/tqdm/tqdm, Documentation: https://tqdm.github.io/")
sh = LazyImport("import sh", "PACKAGE: sh — a unique subprocess wrapper that maps your system programs to Python functions dynamically, derived from 'import sh', from https://github.com/amoffat/sh, Documentation: http://amoffat.github.io/sh/")
shell = LazyImport('from shell import shell', "FUNCTION shell.shell — Shortcut function to quickly run a command, derived from 'from shell import shell', from https://github.com/toastdriven/shell, Documentation: https://shell.readthedocs.io/en/latest/shell_api.html#module-shell")
Shell = LazyImport('from shell import Shell', "CLASS shell.Shell — Class to run multiple commands and extend the behaviour, derived from 'from shell import Shell', from https://github.com/toastdriven/shell, Documentation: https://shell.readthedocs.io/en/latest/shell_api.html#module-shell")
