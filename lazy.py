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
sklearn = LazyImport("import sklearn", "PACKAGE sklearn — Machine learning in Python, derived from 'import sklearn', from https://github.com/scikit-learn/scikit-learn, Documentation: https://scikit-learn.org/stable/modules/classes.html")
OneHotEncoder = LazyImport("from sklearn.preprocessing import OneHotEncoder", "CLASS sklearn.preprocessing.OneHotEncoder — Encode categorical features as a one-hot numeric array, derived from 'from sklearn.preprocessing import OneHotEncoder', from https://github.com/scikit-learn/scikit-learn, Documentation: https://scikit-learn.org/stable/modules/classes.html")
# , "CLASS sklearn. — , derived from 'from sklearn. import ', from https://github.com/scikit-learn/scikit-learn, Documentation: https://scikit-learn.org/stable/modules/classes.html")
train_test_split = LazyImport("from sklearn.model_selection import train_test_split" , "FUNCTION sklearn.model_selection.train_test_split — Split arrays or matrices into random train and test subsets, derived from 'from sklearn.model_selection import train_test_split', from https://github.com/scikit-learn/scikit-learn, Documentation: https://scikit-learn.org/stable/modules/classes.html")
cross_val_score = LazyImport("from sklearn.model_selection import cross_val_score" , "FUNCTION sklearn.model_selection.cross_val_score — Evaluate a score by cross validation, derived from 'from sklearn.model_selection import cross_val_score', from https://github.com/scikit-learn/scikit-learn, Documentation: https://scikit-learn.org/stable/modules/classes.html")
StratifiedKFold = LazyImport("from sklearn.model_selection import StratifiedKFold" , "CLASS sklearn.model_selection.StratifiedKFold — Stratified K-Folds cross-validator, derived from 'from sklearn.model_selection import StratifiedKFold', from https://github.com/scikit-learn/scikit-learn, Documentation: https://scikit-learn.org/stable/modules/classes.html")
LogisticRegression = LazyImport("from sklearn.linear_model import LogisticRegression")
DecisionTreeClassifier = LazyImport("from sklearn.tree import DecisionTreeClassifier")
KNeighborsClassifier = LazyImport("from sklearn.neighbours import KNeighborsClassifier")
LinearDiscriminantAnalysis = LazyImport("from sklearn.discriminant_analysis import LinearDiscriminantAnalysis")
GaussianNB = LazyImport("from sklearn.naive_bayes import GaussianNB")
classification_report = LazyImport("from sklearn.metrics import classification_report")
confusion_matrix = LazyImport("from sklearn.metrics import confusion_matrix")
accuracy_score = LazyImport("from sklearn.metrics import accuracy_score")
make_scorer = LazyImport("from sklearn.metrics import make_scorer")
TSNE = LazyImport("from sklearn.manifold import TSNE")
svm = LazyImport("from sklearn import svm")
SVC = LazyImport("from sklearn.svm import SVC")
make_pipeline = LazyImport("from sklearn.pipeline import make_pipeline")
GradientBoostingClassifier = LazyImport("from sklearn.ensemble import GradientBoostingClassifier")
GradientBoostingRegressor = LazyImport("from sklearn.ensemble import GradientBoostingRegressor")
RandomForestClassifier = LazyImport("from sklearn.ensemble import RandomForestClassifier")
RandomForestRegressor = LazyImport("from sklearn.ensemble import RandomForestRegressor")
TfidfVectorizer = LazyImport("from sklearn.feature_extraction.text import TfidfVectorizer")
datasets = LazyImport("from sklearn import datasets")
load_iris = LazyImport("from sklearn.datasets import load_iris")
Iris = LazyImport("from sklearn.datasets import load_iris as Iris")
load_diabetes = LazyImport("from sklearn.datasets import load_diabetes")
Diabetes = LazyImport("from sklearn.datasets import load_diabetes as Diabetes")
load_digits = LazyImport("from sklearn.datasets import load_digits")
Digits = LazyImport("from sklearn.datasets import load_digits as Digits")
load_boston = LazyImport("from sklearn.datasets import load_boston")
Boston = LazyImport("from sklearn.datasets import load_boston as Boston")
load_breast_cancer = LazyImport("from sklearn.datasets import load_breast_cancer")
BreastCancer = LazyImport("from sklearn.datasets import load_breast_cancer as BreastCancer")




make_biclusters = LazyImport("from sklearn.datasets import make_biclusters")
make_blobs = LazyImport("from sklearn.datasets import make_blobs")
make_checkerboard = LazyImport("from sklearn.datasets import make_checkerboard")
make_circles = LazyImport("from sklearn.datasets import make_circles")
make_classification = LazyImport("from sklearn.datasets import make_classification")
make_regression = LazyImport("from sklearn.datasets import make_regression")

#diabetes = load_diabetes()
#digits = load_digits()
#iris = load_iris()
#iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)
#diabetes_df = pd.DataFrame(diabetes.data, columns = diabetes.feature_names)


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

eli5 = LazyImport("import eli5", "PACKAGE eli5 — A library for debugging/inspecting machine learning classifiers and explaining their predictions, derived from 'import eli5', from https://github.com/TeamHG-Memex/eli5/, Documentation: http://eli5.readthedocs.io/")

torch = LazyImport("import torch")
tc = LazyImport("import tensor_comprehensions as tc")

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


# NLP
nltk = LazyImport("import nltk")
gensim = LazyImport("import gensim")
spacy = LazyImport("import spacy")


# ------ Sentiment Analysis --------
tweepy = LazyImport("import tweepy")
TextBlob = LazyImport("from textblob import TextBlob")


# Quantum
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
