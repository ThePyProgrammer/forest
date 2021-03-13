## file
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

pandas = LazyImport("import pandas", "PACKAGE pandas — powerful Python data analysis toolkit, derived from 'import pandas', from https://github.com/pandas-dev/pandas, Documentation: https://pandas.pydata.org/pandas-docs/stable/")
pd = LazyImport("import pandas as pd", "PACKAGE pd derived from pandas — powerful Python data analysis toolkit, derived from 'import pandas as pd', from https://github.com/pandas-dev/pandas, Documentation: https://pandas.pydata.org/pandas-docs/stable/")
read_csv = LazyImport("from pandas import read_csv", "FUNCTION pandas.read_csv — Read a comma-separated values (csv) file into DataFrame, derived from 'from pandas import read_csv', from https://github.com/pandas-dev/pandas, Documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html")

pandas_datareader = LazyImport("import pandas_datareader", "PACKAGE pandas_datareader — Extract data from a wide range of Internet sources into a pandas DataFrame, derived from 'import pandas_datareader', from https://github.com/pydata/pandas-datareader, Documentation: https://pydata.github.io/pandas-datareader/stable/index.html")
pd_dr = LazyImport("import pandas_datareader as pd_dr", "PACKAGE pd_dr derived from pandas_datareader — Extract data from a wide range of Internet sources into a pandas DataFrame, derived from 'import pandas_datareader as pd_dr', from https://github.com/pydata/pandas-datareader, Documentation: https://pydata.github.io/pandas-datareader/stable/index.html")
pdr = LazyImport("import pandas_datareader as pdr", "PACKAGE pdr derived from pandas_datareader — Extract data from a wide range of Internet sources into a pandas DataFrame, derived from 'import pandas_datareader as pdr', from https://github.com/pydata/pandas-datareader, Documentation: https://pydata.github.io/pandas-datareader/stable/index.html")
DataReader = LazyImport("from pandas_datareader.data import DataReader", "Class DataReader — reading data from a wide range of Internet sources, derived from 'from pandas_datareader.data import DataReader', from https://github.com/pydata/pandas-datareader, Documentation: https://pydata.github.io/pandas-datareader/stable/index.html")
