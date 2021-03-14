# forest

**By Prannaya Gupta**

A library based on [pyforest](https://github.com/8080labs/pyforest) to auto-import every library imaginable. It also adds functionality for Machine Learning and Data Science.

## The basics of forest

Based around pyforest, forest utilises many tools from the library.

```python
>>> from forest import *
>>> arr = np.linspace(-math.pi, np.pi)
>>> os.mkdir("test")
>>> _ = sys.stdout.write("I am ThePyProgrammer")
I am ThePyProgrammer
>>> x, y = symbols("x y")
>>> (x + 6)**2 + (y - 6)**2
(x + 6)**2 + (y - 6)**2
>>> for i in gsearch("ThePyProgrammer", tld="co.in", num=10, stop=10, pause=2):
	pprint(i)

'https://github.com/ThePyProgrammer'
'https://github.com/ThePyProgrammer/PXChallenge'
'https://pypi.org/user/ThePyProgrammer/'
'https://githubmemory.com/@ThePyProgrammer'
'https://githubmemory.com/repo/ThePyProgrammer/GaitMonitoringForParkinsonsDiseasePatients/activity?page=2'
'https://twitter.com/thepycoder'
'https://www.xinruishi.com/ThePyProgrammer/shabdkosh/pulls'
'https://www.gitmemory.com/thepycoder'
'https://www.fiverr.com/thepycoder/design-and-build-applications'
'https://www.deviantart.com/thepycoder/gallery/all'
>>> x = np.random.rand(50)
>>> plt.plot(arr, x)
[<matplotlib.lines.Line2D object at 0x000001EDD32F6FD0>]
>>> plt.show()

```





## Documentation

This library still uses the LazyForest class used in pyforest, but allows users to add documentation.

```python
>>> from forest import *
>>> sklearn
PACKAGE sklearn — Machine learning in Python, derived from 'import sklearn', from https://github.com/scikit-learn/scikit-learn, Documentation: https://scikit-learn.org/stable/modules/classes.html
>>> np
PACKAGE np — np-altered NumPy for more functionality, derived from 'import np', from https://github.com/k7hoven/np
>>> numpy
PACKAGE numpy — The fundamental package for scientific computing with Python, derived from 'import numpy', from https://github.com/numpy/numpy, Documentation: https://numpy.org/doc
>>> pd
PACKAGE pd derived from pandas — powerful Python data analysis toolkit, derived from 'import pandas as pd', from https://github.com/pandas-dev/pandas, Documentation: https://pandas.pydata.org/pandas-docs/stable/
>>> plt
SUBPACKAGE plt derived from matplotlib.pyplot — A comprehensive library for creating static, animated, and interactive visualizations in Python, derived from 'import matplotlib.pyplot as plt', from https://github.com/matplotlib/matplotlib, Documentation: https://matplotlib.org/api/index.html#the-pyplot-api
>>> sns
PACKAGE sns derived from seaborn — A Python visualization library based on matplotlib, derived from 'import seaborn as sns', from https://github.com/mwaskom/seaborn, Documentation: https://seaborn.pydata.org/
>>> opencv
PACKAGE opencv derived from cv2 — Open Source Computer Vision Library, derived from 'import cv2 as opencv', from https://github.com/opencv/opencv, Documentation: https://docs.opencv.org/master/
```

