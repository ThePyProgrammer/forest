# array
from forest._importable import LazyImport


collections = LazyImport("import collections", "LIBRARY: collections — Container datatypes, derived from 'import collections', part of The Python Standard Library")
itertools = LazyImport("import itertools", "LIBRARY: itertools — Functions creating iterators for efficient looping, derived from 'import itertools', part of The Python Standard Library")
arr = LazyImport("from array import array as arr", "CLASS arr derived from array.array — a base array, derived from 'from array import array as arr', part of The Python Standard Library")
array_funcs = LazyImport("import array as array_funcs", "LIBRARY: array_funcs derived from array — Efficient arrays of numeric values, derived from 'import array as array_funcs', part of The Python Standard Library")

bisect = LazyImport("import bisect", "LIBRARY: bisect — Array bisection algorithm, derived from 'import bisect', part of The Python Standard Library")
bisect_right = LazyImport("from bisect import bisect_right", "FUNCTION bisect_right(a, x, lo=0, hi=len(a)) — Locates the insertion point for x in a to maintain sorted order which comes before any existing entries of x in a, derived from 'from bisect import bisect_right', part of The Python Standard Library")
bisect_left = LazyImport("from bisect import bisect_left", "FUNCTION bisect_left(a, x, lo=0, hi=len(a)) — Locates the insertion point for x in a to maintain sorted order which comes before any existing entries of x in a, derived from 'from bisect import bisect_left', part of The Python Standard Library")
