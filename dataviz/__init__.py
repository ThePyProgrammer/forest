# web
from ._importable import LazyImport, _import_statements


## matlab
matplotlib = LazyImport("import matplotlib", "PACKAGE matplotlib — A comprehensive library for creating static, animated, and interactive visualizations in Python, derived from 'import matplotlib', from https://github.com/matplotlib/matplotlib, Documentation: https://matplotlib.org/contents.html")
mpl = LazyImport("import matplotlib as mpl", "PACKAGE mpl derived from matplotlib — A comprehensive library for creating static, animated, and interactive visualizations in Python, derived from 'import matplotlib as mpl', from https://github.com/matplotlib/matplotlib, Documentation: https://matplotlib.org/contents.html")
plt = LazyImport("import matplotlib.pyplot as plt", "SUBPACKAGE plt derived from matplotlib.pyplot — A comprehensive library for creating static, animated, and interactive visualizations in Python, derived from 'import matplotlib.pyplot as plt', from https://github.com/matplotlib/matplotlib, Documentation: https://matplotlib.org/api/index.html#the-pyplot-api")
pyplot = LazyImport("from matplotlib import pyplot", "SUBPACKAGE matplotlib.pyplot — A comprehensive library for creating static, animated, and interactive visualizations in Python, derived from 'from matplotlib import pyplot', from https://github.com/matplotlib/matplotlib, Documentation: https://matplotlib.org/api/index.html#the-pyplot-api")
pylab = LazyImport("import pylab", "PACKAGE pylab - A procedural interface to the Matplotlib object-oriented plotting library, derived from 'import pylab', from https://github.com/matplotlib/matplotlib, Documentation: https://scipy.github.io/old-wiki/pages/PyLab")
pl = LazyImport("import pylab as pl", "PACKAGE pylab - A procedural interface to the Matplotlib object-oriented plotting library, derived from 'import pylab as pl', from https://github.com/matplotlib/matplotlib, Documentation: https://scipy.github.io/old-wiki/pages/PyLab")

matkinter = LazyImport("import matkinter", "MODULE matkinter — A library for tkinter data visualizations, derived from 'import matkinter', self-created")


seaborn = LazyImport("import seaborn", "PACKAGE seaborn — A Python visualization library based on matplotlib, derived from 'import seaborn', from https://github.com/mwaskom/seaborn, Documentation: https://seaborn.pydata.org/")
sns = LazyImport("import seaborn as sns", "PACKAGE sns derived from seaborn — A Python visualization library based on matplotlib, derived from 'import seaborn as sns', from https://github.com/mwaskom/seaborn, Documentation: https://seaborn.pydata.org/")
eli5 = LazyImport("import eli5", "PACKAGE eli5 — A library for debugging/inspecting machine learning classifiers and explaining their predictions, derived from 'import eli5', from https://github.com/TeamHG-Memex/eli5/, Documentation: http://eli5.readthedocs.io/")
bokeh = LazyImport("import bokeh", "PACKAGE bokeh — Interactive Data Visualization in the browser, from Python, derived from 'import bokeh', from https://github.com/bokeh/bokeh, Documentation: https://docs.bokeh.org/en/latest/")

altair = LazyImport("import altair", "PACKAGE altair — Declarative statistical visualization library for Python, derived from 'import altair', from https://github.com/altair-viz/altair, Documentation: https://altair-viz.github.io/")
alt = LazyImport("import altair as alt", "PACKAGE alt derived from altair — Declarative statistical visualization library for Python, derived from 'import altair as alt', from https://github.com/altair-viz/altair, Documentation: https://altair-viz.github.io/")

pydot = LazyImport("import pydot", "PACKAGE pydot — Python interface to Graphviz's Dot language, derived from 'import pydot', from https://github.com/pydot/pydot")
pydot_ng = LazyImport("import pydot_ng", "PACKAGE pydot_ng — Python interface to Graphviz's Dot language, derived from 'import pydot_ng', from https://github.com/pydot/pydot-ng")


# plotlylib
from .plotlylib import *
