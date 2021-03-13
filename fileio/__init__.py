# file
from forest._importable import LazyImport


io = LazyImport("import io", "LIBRARY: io — Core tools for working with streams, derived from 'import io', part of The Python Standard Library")
fileinput = LazyImport("import fileinput", "LIBRARY fileinput — Iterate over lines from multiple input streams, derived from 'import fileinput', part of The Python Standard Library")


pickle = LazyImport("import pickle", "LIBRARY: pickle — Python object serialization, derived from 'import pickle', part of The Python Standard Library")

difflib = LazyImport("import difflib", "LIBRARY difflib — Helpers for computing deltas, derived from 'import difflib', part of The Python Standard Library")

tablib = LazyImport("import tablib", "PACKAGE tablib — Python Module for Tabular Datasets in XLS, CSV, JSON, YAML, derived from 'import tablib', from https://github.com/jazzband/tablib, Documentation: https://tablib.readthedocs.io/")
csv = LazyImport("import csv", "LIBRARY csv — CSV File Reading and Writing, derived from 'import csv', part of The Python Standard Library")


## loc
from .loc import *

## panda
from .panda import *

## excel
from .excel import *

## sql
sqlite3 = LazyImport("import sqlite3", "PACKAGE sqlite3 — An Embeddable SQL Database Engine, derived from 'import sqlite3', from http://www.sqlite.org/, Documentation: https://www.sqlite.org/docs.html")
mysql = LazyImport("import sqlite3 as mysql", "PACKAGE mysql derived from sqlite3 — An Embeddable SQL Database Engine, derived from 'import sqlite3 as mysql', from http://www.sqlite.org/, Documentation: https://www.sqlite.org/docs.html")
sql = LazyImport("import sqlite3 as sql", "PACKAGE sql derived from sqlite3 — An Embeddable SQL Database Engine, derived from 'import sqlite3 as sql', from http://www.sqlite.org/, Documentation: https://www.sqlite.org/docs.html")

## xml
from .xml import *

## image
Image = LazyImport("from PIL import Image")
PIL = LazyImport("import PIL")