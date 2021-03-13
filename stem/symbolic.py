## symbolic
from forest._importable import LazyImport

sympy = LazyImport("import sympy", "PACKAGE sympy — A computer algebra system written in pure Python, derived from 'import sympy', from https://github.com/sympy/sympy, Documentation: https://docs.sympy.org/dev/documentation-style-guide.html")
sp = LazyImport("import sympy as sp", "PACKAGE sp derived from sympy — A computer algebra system written in pure Python, derived from 'import sympy as sp', from https://github.com/sympy/sympy, Documentation: https://docs.sympy.org/dev/documentation-style-guide.html")
Symbol = LazyImport("from sympy import Symbol", "FUNCTION Symbol — A computer algebra system written in pure Python, derived from 'from sympy import Symbol', from https://github.com/sympy/sympy, Documentation: https://docs.sympy.org/dev/documentation-style-guide.html")
symbols = LazyImport("from sympy import symbols", "FUNCTION symbols — A computer algebra system written in pure Python, derived from 'from sympy import symbols', from https://github.com/sympy/sympy, Documentation: https://docs.sympy.org/dev/documentation-style-guide.html")