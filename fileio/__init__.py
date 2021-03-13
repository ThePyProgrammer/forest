# file
from forest._importable import LazyImport


io = LazyImport("import io", "LIBRARY: io — Core tools for working with streams, derived from 'import io', part of The Python Standard Library")

fileinput = LazyImport("import fileinput", "LIBRARY fileinput — Iterate over lines from multiple input streams, derived from 'import fileinput', part of The Python Standard Library")

## misc
pickle = LazyImport("import pickle", "LIBRARY: pickle — Python object serialization, derived from 'import pickle', part of The Python Standard Library")

tablib = LazyImport("import tablib", "PACKAGE tablib — Python Module for Tabular Datasets in XLS, CSV, JSON, YAML, derived from 'import tablib', from https://github.com/jazzband/tablib, Documentation: https://tablib.readthedocs.io/")
difflib = LazyImport("import difflib", "LIBRARY difflib — Helpers for computing deltas, derived from 'import difflib', part of The Python Standard Library")


## loc
from .loc import *

## panda
from .panda import *

## excel
from .excel import *

## csv
csv = LazyImport("import csv", "LIBRARY csv — CSV File Reading and Writing, derived from 'import csv', part of The Python Standard Library")

## json
json = LazyImport("import json", "LIBRARY json — JSON encoder and decoder, derived from 'import json', from The Python Standard Library")

## sql
from ._sql import *

## xml
from .xml import *

## image
from .image import *

## human
from .human import *
