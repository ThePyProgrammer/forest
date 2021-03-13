## numalg
from forest._importable import LazyImport

numpy = LazyImport("import numpy", "PACKAGE numpy — The fundamental package for scientific computing with Python, derived from 'import numpy', from https://github.com/numpy/numpy, Documentation: https://numpy.org/doc")
la = LazyImport("import numpy.linalg as la", "PACKAGE la derived from numpy.linalg — Linear Algebra for Python and primarily NumPy, derived from 'import numpy.linalg as la', from https://github.com/numpy/numpy, Documentation: https://numpy.org/doc/1.18/reference/routines.linalg.html")
np = LazyImport("import np", "PACKAGE np — np-altered NumPy for more functionality, derived from 'import np', from https://github.com/k7hoven/np")
