## io
from forest._importable import LazyImport

io = LazyImport("import io", "LIBRARY: io — Core tools for working with streams, derived from 'import io', part of The Python Standard Library")

glob = LazyImport("import glob", "LIBRARY: glob — Unix style pathname pattern expansion, derived from 'import glob', part of The Python Standard Library")
Path = LazyImport("from pathlib import Path", "CLASS: pathlib.Path — represents concrete paths of the system’s path flavour, derived from 'from pathlib import Path', part of The Python Standard Library")
pathlib = LazyImport("import pathlib", "LIBRARY: pathlib — Object-oriented filesystem paths, derived from 'import pathlib', part of The Python Standard Library")

pickle = LazyImport("import pickle", "LIBRARY: pickle — Python object serialization, derived from 'import pickle', part of The Python Standard Library")

difflib = LazyImport("import difflib", "LIBRARY difflib — Helpers for computing deltas, derived from 'import difflib', part of The Python Standard Library")
tablib = LazyImport("import tablib", "PACKAGE tablib — Python Module for Tabular Datasets in XLS, CSV, JSON, YAML, derived from 'import tablib', from https://github.com/jazzband/tablib, Documentation: https://tablib.readthedocs.io/")
csv = LazyImport("import csv", "LIBRARY csv — CSV File Reading and Writing, derived from 'import csv', part of The Python Standard Library")

fileinput = LazyImport("import fileinput", "LIBRARY fileinput — Iterate over lines from multiple input streams, derived from 'import fileinput', part of The Python Standard Library")
