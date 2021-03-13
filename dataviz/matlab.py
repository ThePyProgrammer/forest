# matlab
from ._importable import LazyImport, _import_statements


matplotlib = LazyImport("import matplotlib", "PACKAGE matplotlib — A comprehensive library for creating static, animated, and interactive visualizations in Python, derived from 'import matplotlib', from https://github.com/matplotlib/matplotlib, Documentation: https://matplotlib.org/contents.html")
mpl = LazyImport("import matplotlib as mpl", "PACKAGE mpl derived from matplotlib — A comprehensive library for creating static, animated, and interactive visualizations in Python, derived from 'import matplotlib as mpl', from https://github.com/matplotlib/matplotlib, Documentation: https://matplotlib.org/contents.html")
plt = LazyImport("import matplotlib.pyplot as plt", "SUBPACKAGE plt derived from matplotlib.pyplot — A comprehensive library for creating static, animated, and interactive visualizations in Python, derived from 'import matplotlib.pyplot as plt', from https://github.com/matplotlib/matplotlib, Documentation: https://matplotlib.org/api/index.html#the-pyplot-api")
pyplot = LazyImport("from matplotlib import pyplot", "SUBPACKAGE matplotlib.pyplot — A comprehensive library for creating static, animated, and interactive visualizations in Python, derived from 'from matplotlib import pyplot', from https://github.com/matplotlib/matplotlib, Documentation: https://matplotlib.org/api/index.html#the-pyplot-api")
pylab = LazyImport("import pylab", "PACKAGE pylab - A procedural interface to the Matplotlib object-oriented plotting library, derived from 'import pylab', from https://github.com/matplotlib/matplotlib, Documentation: https://scipy.github.io/old-wiki/pages/PyLab")
pl = LazyImport("import pylab as pl", "PACKAGE pylab - A procedural interface to the Matplotlib object-oriented plotting library, derived from 'import pylab as pl', from https://github.com/matplotlib/matplotlib, Documentation: https://scipy.github.io/old-wiki/pages/PyLab")

matkinter = LazyImport("import matkinter", "MODULE matkinter — A library for tkinter data visualizations, derived from 'import matkinter', self-created")


seaborn = LazyImport("import seaborn", "PACKAGE seaborn — A Python visualization library based on matplotlib, derived from 'import seaborn', from https://github.com/mwaskom/seaborn, Documentation: https://seaborn.pydata.org/")
sns = LazyImport("import seaborn as sns", "PACKAGE sns derived from seaborn — A Python visualization library based on matplotlib, derived from 'import seaborn as sns', from https://github.com/mwaskom/seaborn, Documentation: https://seaborn.pydata.org/")
