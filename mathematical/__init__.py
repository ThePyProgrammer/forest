# mathematical
from forest._importable import LazyImport

## basic math
math = LazyImport("import math", "LIBRARY: math — Mathematical functions, derived from 'import math', part of The Python Standard Library")

## complex math
cmath = LazyImport("import cmath", "LIBRARY: cmath — Mathematical functions for complex numbers, derived from 'import cmath', part of The Python Standard Library")

## statistics
statistics = LazyImport("import statistics", "LIBRARY: statistics — Mathematical statistics functions, derived from 'import statistics', part of The Python Standard Library")

## random
from .rand import *

## oop
from .oop import *

## symbols
sympy = LazyImport("import sympy", "PACKAGE sympy — A computer algebra system written in pure Python, derived from 'import sympy', from https://github.com/sympy/sympy, Documentation: https://docs.sympy.org/dev/documentation-style-guide.html")
sp = LazyImport("import sympy as sp", "PACKAGE sp derived from sympy — A computer algebra system written in pure Python, derived from 'import sympy as sp', from https://github.com/sympy/sympy, Documentation: https://docs.sympy.org/dev/documentation-style-guide.html")
