# scikit
from ._importable import LazyImport, _import_statements


sklearn = LazyImport("import sklearn", "PACKAGE sklearn — Machine learning in Python, derived from 'import sklearn', from https://github.com/scikit-learn/scikit-learn, Documentation: https://scikit-learn.org/stable/modules/classes.html")


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


OneHotEncoder = LazyImport("from sklearn.preprocessing import OneHotEncoder", "CLASS sklearn.preprocessing.OneHotEncoder — Encode categorical features as a one-hot numeric array, derived from 'from sklearn.preprocessing import OneHotEncoder', from https://github.com/scikit-learn/scikit-learn, Documentation: https://scikit-learn.org/stable/modules/classes.html")


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

# , "CLASS sklearn. — , derived from 'from sklearn. import ', from https://github.com/scikit-learn/scikit-learn, Documentation: https://scikit-learn.org/stable/modules/classes.html")

eli5 = LazyImport("import eli5", "PACKAGE eli5 — A library for debugging/inspecting machine learning classifiers and explaining their predictions, derived from 'import eli5', from https://github.com/TeamHG-Memex/eli5/, Documentation: http://eli5.readthedocs.io/")
