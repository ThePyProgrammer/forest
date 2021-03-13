# web
from ._importable import LazyImport, _import_statements

# matlab
from .matlab import *


# misc
bokeh = LazyImport("import bokeh", "PACKAGE bokeh — Interactive Data Visualization in the browser, from Python, derived from 'import bokeh', from https://github.com/bokeh/bokeh, Documentation: https://docs.bokeh.org/en/latest/")

altair = LazyImport("import altair", "PACKAGE altair — Declarative statistical visualization library for Python, derived from 'import altair', from https://github.com/altair-viz/altair, Documentation: https://altair-viz.github.io/")
alt = LazyImport("import altair as alt", "PACKAGE alt derived from altair — Declarative statistical visualization library for Python, derived from 'import altair as alt', from https://github.com/altair-viz/altair, Documentation: https://altair-viz.github.io/")

pydot = LazyImport("import pydot", "PACKAGE pydot — Python interface to Graphviz's Dot language, derived from 'import pydot', from https://github.com/pydot/pydot")
pydot_ng = LazyImport("import pydot_ng", "PACKAGE pydot_ng — Python interface to Graphviz's Dot language, derived from 'import pydot_ng', from https://github.com/pydot/pydot-ng")


# plotlylib
from .plotlylib import *
