# string
from forest._importable import LazyImport

textwrap = LazyImport("import textwrap", "LIBRARY: textwrap — Text wrapping and filling, derived from 'import textwrap', part of The Python Standard Library")
stringprep = LazyImport("import stringprep", "LIBRARY: stringprep — Internet String Preparation, derived from 'import stringprep', part of The Python Standard Library")
reprlib = LazyImport("import reprlib", "LIBRARY: reprlib — Alternate repr() implementation, derived from 'import reprlib', part of The Python Standard Library")

## regex
re = LazyImport("import re", "LIBRARY: re - regex operations, derived from 'import re', part of The Python Standard Library")

## unicode
ucd = LazyImport("import unicodedata as ucd", "LIBRARY ucd derived from unicodedata — Unicode Database, derived from 'import unicodedata as ucd', part of The Python Standard Library")
unicodedata = LazyImport("import unicodedata", "LIBRARY unicodedata — Unicode Database, derived from 'import unicodedata', part of The Python Standard Library")
