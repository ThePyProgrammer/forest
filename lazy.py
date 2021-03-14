from ._importable import LazyImport, _import_statements


### Standard Library
from .stdlib import *


### File I/O
from .fileio import *


### STEM
from .stem import *


### Array
from .array import *


### String
from .string import *


### Functions
from .func import *


### Temporal
from .temporal import *


### Google
from .ggl import *


### Audio
from .audio import *


## Web
from .web import *


### Auto-complete
jedi = LazyImport("import jedi", "PACKAGE jedi — Awesome autocompletion, static analysis and refactoring library for Python, derived from 'import jedi', from https://github.com/davidhalter/jedi, Documentation: https://jedi.readthedocs.io/en/latest/")
setup_readline = LazyImport("from jedi.utils import setup_readline", "FUNCTION setup_readline — Function that sets up readline to use Jedi in a Python interactive shell, derived from 'from jedi.utils import setup_readline', from https://github.com/davidhalter/jedi, Documentation: https://jedi.readthedocs.io/en/latest/docs/usage.html")
readline = LazyImport("import readline", "LIBRARY readline — GNU readline interface, derived from 'import readline', from The Python Standard Library")
rlcompleter = LazyImport("import rlcompleter", "LIBRARY rlcompleter — Completion function for GNU readline, derived from 'import rlcompleter', from The Python Standard Library")


### GUI
from .gui import *


### Data Wrangling
dask = LazyImport("import dask", "PACKAGE dask — Parallel computing with task scheduling, derived from 'import dask', from https://github.com/dask/dask, Documentation: https://dask.org/")
dd = LazyImport("from dask import dataframe as dd", "SUBPACKAGE dd derived from dask.dataframe — Dataframes implementing the Pandas API, derived from 'from dask import dataframe as dd', from https://github.com/dask/dask, Documentation: https://dask.org/")
da = LazyImport("from dask import array as da", "SUBPACKAGE da derived from dask.array — Arrays implementing the Numpy API, derived from 'from dask import array as da', from https://github.com/dask/dask, Documentation: https://dask.org/")

from .apache import *

### Data Visualization and Plotting
from .dataviz import *


### Machine Learning
from .scikit import *

from .pytorch import *


creme = LazyImport("import creme")
Pipeline = LazyImport("from creme.compose import Pipeline")
preprocessing = LazyImport("from creme import preprocessing")
StandardScaler = LazyImport("from creme.preprocessing import StandardScaler")
KMeans = LazyImport("from creme.cluster import KMeans")
BernoulliNB = LazyImport("from creme.naive_bayes import BernoulliNB")
ComplementNB = LazyImport("from creme.naive_bayes import ComplementNB")
MultinomialNB = LazyImport("from creme.naive_bayes import MultinomialNB")
Gaussian = LazyImport("from creme.proba import Gaussian")
Multinomial = LazyImport("from creme.proba import Multinomial")
Accuracy = LazyImport("from creme.metrics import Accuracy")
F1 = LazyImport("from creme.metrics import F1")
Precision = LazyImport("from creme.metrics import Precision")
MAE = LazyImport("from creme.metrics import MAE")
Recall = LazyImport("from creme.metrics import Recall")
OneVsRestClassifier = LazyImport("from creme.multiclass import OneVsRestClassifier")
OneVsAllClassifier = LazyImport("from creme.multiclass import OneVsRestClassifier as OneVsAllClassifier")
LinearRegression = LazyImport("from creme.linear_model import LinearRegression")
progressive_val_score = LazyImport("from creme.model_selection import progressive_val_score")
KNeighborsRegressor = LazyImport("from creme.neighbors import KNeighborsRegressor")
SGD = LazyImport("from creme.optim import SGD")
Stochastic = LazyImport("from creme.optim import SGD as Stochastic")
SoftmaxRegression = LazyImport("from creme.linear_model import SoftmaxRegression")

Airline = LazyImport("from creme.datasets import Airline")
Phishing = LazyImport("from creme.datasets import Phishing")
ChickWeights = LazyImport("from creme.datasets import ChickWeights")
Elec2 = LazyImport("from creme.datasets import Elec2")
MovieLens100K = LazyImport("from creme.datasets import MovieLens100K")
HTTP = LazyImport("from crem.datasets import HTTP")
Higgs = LazyImport("from creme.datasets import Higgs")
Bikes = LazyImport("from creme.datasets import Bikes")
MaliciousURL = LazyImport("from creme.datasets import MaliciousURL")
ImageSegments = LazyImport("from creme.datasets import ImageSegments")
SMSSpam = LazyImport("from creme.datasets import SMSSpam")
SMTP = LazyImport("from creme.datasets import SMTP")
Taxis = LazyImport("from creme.datasets import Taxis")
TREC07 = LazyImport("from creme.datasets import TREC07")
TrumpApproval = LazyImport("from creme.datasets import TrumpApproval")


# Gradient Boosting Decision Tree
xgb = LazyImport("import xgboost as xgb")
lgb = LazyImport("import lightgbm as lgb")

# Deep Learning
tf = LazyImport("import tensorflow as tf")
tensorflow = LazyImport("import tensorflow")
keras = LazyImport("import keras")
tfkeras = LazyImport("import tensorflow.keras as tfkeras")


### OCR
opencv = LazyImport("import cv2 as opencv", "PACKAGE opencv derived from cv2 — Open Source Computer Vision Library, derived from 'import cv2 as opencv', from https://github.com/opencv/opencv, Documentation: https://docs.opencv.org/master/")
cv2 = LazyImport("import cv2", "PACKAGE cv2 — Open Source Computer Vision Library, derived from 'import cv2', from https://github.com/opencv/opencv, Documentation: https://docs.opencv.org/master/")
skimage = LazyImport("import skimage")


### NLP
nltk = LazyImport("import nltk")
gensim = LazyImport("import gensim")
spacy = LazyImport("import spacy")


### ------ Sentiment Analysis --------
tweepy = LazyImport("import tweepy")
TextBlob = LazyImport("from textblob import TextBlob")


### Quantum
qiskit = LazyImport("import qiskit")
cirq = LazyImport("import cirq")
openfermion = LazyImport("openfermion")
pyscf = LazyImport("import pyscf")
larq = LazyImport("import larq")
pyquil = LazyImport("import pyquil")
pennylane = LazyImport("import pennylane")
qml = LazyImport("import pennylane as qml")
quantum_forest = LazyImport("import quantum_forest")
deepchem = LazyImport("import deepchem")
dc = LazyImport("import deepchem as dc")
projectq = LazyImport("import projectq")
strawberryfields = LazyImport("import strawberryfields")
sf = LazyImport("import strawberryfields as sf")
ops = LazyImport("from strawberryfields import ops")
qibo = LazyImport("import qibo")
QFT = LazyImport("from qibo.models import QFT")



### Music Theory
mingus = LazyImport("import mingus")


pandas_profiling = LazyImport("import pandas_profiling")
pd.__on_import__(pandas_profiling)  # adds df.profile_report attribute to pd.DataFrame

eda = LazyImport("import edaviz as eda")
pd.__on_import__(eda)  # adds GUI to pd.DataFrame when IPython frontend can display it


##################################################
### dont make adjustments below this line ########
##################################################
def lazy_imports():
    return _import_statements(globals(), was_imported=False)


def active_imports():
    return _import_statements(globals(), was_imported=True)
