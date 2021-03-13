## tensoralg
from forest._importable import LazyImport

theano = LazyImport("import theano", "PACKAGE theano — a Python library that allows you to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently, derived from 'import theano', from https://github.com/Theano/Theano")
tensor = LazyImport("from theano import tensor")