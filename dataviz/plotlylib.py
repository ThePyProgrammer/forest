# plotlylib
from ._importable import LazyImport, _import_statements


plotly = LazyImport("import plotly", "PACKAGE plotly — The interactive open-source browser-based graphing library for Python (includes Plotly Express), derived from 'import plotly', from https://github.com/plotly/plotly.py, Documentation: https://plotly.com/python/")
py = LazyImport("import plotly as py", "PACKAGE py derived from plotly — The interactive open-source browser-based graphing library for Python (includes Plotly Express), derived from 'import plotly as py', from https://github.com/plotly/plotly.py, Documentation: https://plotly.com/python/")
go = LazyImport("import plotly.graph_objs as go", "SUBPACKAGE go derived from plotly.graph_objs — Graph Objects, derived from 'import plotly.graph_objs as go', from https://github.com/plotly/plotly.py, Documentation: https://plotly.com/python/")
px = LazyImport("import plotly.express as px", "SUBPACKAGE px derived from plotly.express — Plotly Express, derived from 'import plotly.express as px', from https://github.com/plotly/plotly.py, Documentation: https://plotly.com/python/")
pio = LazyImport("import plotly.io as pio", "SUBPACKAGE pio derived from plotly.io — File IO for Plotly, derived from 'import plotly.io as pio', from https://github.com/plotly/plotly.py, Documentation: https://plotly.com/python/")
py1 = LazyImport("import plotly.plotly as py1", "SUBPACKAGE py1 derived from plotly.plotly — Plotly inbuilt subpackage, derived from 'import plotly.plotly as py1', from https://github.com/plotly/plotly.py, Documentation: https://plotly.com/python/")
plottools = LazyImport("from plotly import tools as plottools", "SUBPACKAGE plottools derived from plotly.tools — Tools for plotly, derived from 'import plotly.tools as plottools', from https://github.com/plotly/plotly.py, Documentation: https://plotly.com/python/")

dash = LazyImport("import dash", "PACKAGE dash — A Python framework for building analytical web applications, derived from 'import dash', from https://github.com/plotly/dash, Documentation: http://dash-docs.herokuapp.com/")
dhc = LazyImport("import dash_html_components as dhc", "SUBPACKAGE dhc derived from dash.dash_html_components — A Python framework for composing a HTML layout using Python structures, derived from 'import dash.dash_html_components as dhc', from https://github.com/plotly/dash, Documentation: http://dash-docs.herokuapp.com/dash-html-components")
dcc = LazyImport("import dash_core_components as dcc", "SUBPACKAGE dcc derived from dash.dash_core_components — A core set of components, derived from 'import dash.dash_core_components as dcc', from https://github.com/plotly/dash, Documentation: http://dash-docs.herokuapp.com/dash-core-components")
dbc = LazyImport("import dash_bootstrap_components as dbc", "SUBPACKAGE dbc derived from dash.dash_bootstrap_components_components — A Python framework for composing a HTML layout using Python structures, derived from 'import dash.dash_bootstrap_components as dbc', from https://github.com/plotly/dash, Documentation: https://dash-bootstrap-components.opensource.faculty.ai/")

cf = LazyImport("import cufflinks as cf", "PACKAGE cf derived from cufflinks — Productivity Tools for Plotly + Pandas, derived from 'import cufflinks as cf', from https://github.com/santosjorge/cufflinks")
cufflinks = LazyImport("import cufflinks", "PACKAGE cufflinks — Productivity Tools for Plotly + Pandas, derived from 'import cufflinks', from https://github.com/santosjorge/cufflinks")

