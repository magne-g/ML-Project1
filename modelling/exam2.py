import hashlib
import os
import time
import warnings
from matplotlib import pyplot as py
from datetime import date
from pylatex import Document, Table, Tabular, LongTable, MultiColumn, Subsection, Subsubsection, FlushLeft, Figure, \
    SubFigure
from sklearn import tree
import numpy as np
import pandas as pd
import seaborn as sns
import math
import matplotlib.colors
from scipy.stats import randint as sp_randint
from scipy.stats import rv_continuous
from scipy.stats import rv_discrete
import sklearn.utils.testing as test
from IPython.core.interactiveshell import InteractiveShell
from matplotlib import pyplot as plt
from sklearn import metrics as metrics, preprocessing
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import AdaBoostRegressor, BaggingRegressor, GradientBoostingRegressor, RandomForestRegressor, \
    ExtraTreesRegressor, RandomForestClassifier
from sklearn.externals.six import StringIO
from sklearn.kernel_ridge import KernelRidge
from sklearn.linear_model import BayesianRidge, Lasso
from sklearn.model_selection import cross_val_score, GridSearchCV, KFold, learning_curve, train_test_split, \
    validation_curve, cross_val_predict, RandomizedSearchCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA, SparsePCA
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from graphviz import Source


#Preprocess this dataset in the simplest possible way so that the re-
#sponse can be perfectly predicted using just one single test of the form
#z < c, where c is a constant and z is a new feature generated by your preprocessing.

#Use gini impurity heuristics as in Random Forest to construct #just one
#binary decision tree that perfectly classifies the credit in #this data set.
#Clearly explain all calculations.

from sklearn.tree import _tree
from sklearn.tree import _splitter
def tree_to_code(tree, splitter, feature_names):
    tree_ = tree.tree_
    splitter_ = splitter
    print(splitter_)
    print(tree_.impurity)
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    print("def tree({}):".format(", ".join(feature_names)))

    def recurse(node, depth):
        indent = "  " * depth

        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            print("{}if {} <= {}:".format(indent, name, threshold))

            recurse(tree_.children_left[node], depth + 1)
            print("{}else:  # if {} > {}".format(indent, name, threshold))
            recurse(tree_.children_right[node], depth + 1)
        else:
            print("{}return {}".format(indent, tree_.value[node]))

    recurse(0, 1)

def gini(array):
    """Calculate the Gini coefficient of a numpy array."""
    # based on bottom eq:
    # http://www.statsdirect.com/help/generatedimages/equations/equation154.svg
    # from:
    # http://www.statsdirect.com/help/default.htm#nonparametric_methods/gini.htm
    # All values are treated equally, arrays must be 1d:
    array = array.flatten()
    if np.amin(array) < 0:
        # Values cannot be negative:
        array -= np.amin(array)
    # Values cannot be 0:
    array += 0.0000001
    # Values must be sorted:
    array = np.sort(array)
    # Index per array element:
    index = np.arange(1,array.shape[0]+1)
    # Number of array elements:
    n = array.shape[0]
    # Gini coefficient:
    return ((np.sum((2 * index - n - 1) * array)) / (n * np.sum(array)))




X = pd.read_csv('../credit.csv')

print(gini(X['credit'].values.astype(np.ndarray)))
print(gini(X['unemployed'].values.astype(np.ndarray)))
print(gini(X['married'].values.astype(np.ndarray)))
print(gini(X['age'].values.astype(np.ndarray)))
eq = 'fraq{'



#print(X)L


#print(X.to_latex(longtable=True))


print(X.sort_values(by=['credit']).to_latex(longtable=True))

y = X['credit']
X = X.drop(columns=['credit'])
c = RandomForestClassifier(max_depth=2, n_estimators=3, max_features=1, bootstrap=False)






rf = c.fit(X, y)




p = c.predict(X)
print(p)

print("Accuracy Score:")
print(metrics.balanced_accuracy_score(y, p))


t = rf.estimators_[0]
graph = Source(export_graphviz(t, out_file=None, feature_names=['age', 'married', 'unemployed']))
graph.format = 'png'
graph.render('dt1', view=True)
time.sleep(1)
tree_to_code(t, t.splitter, feature_names=['age', 'married', 'unemployed'])

t = rf.estimators_[1]
graph = Source(export_graphviz(t, out_file=None, feature_names=['age', 'married', 'unemployed']))
graph.format = 'png'
graph.render('dt2', view=True)
time.sleep(1)
tree_to_code(t, t.splitter, feature_names=['age', 'married', 'unemployed'])

t = rf.estimators_[2]
graph = Source(export_graphviz(t, out_file=None, feature_names=['age', 'married', 'unemployed']))
graph.format = 'png'
graph.render('dt3', view=True)
time.sleep(1)
tree_to_code(t, t.splitter, feature_names=['age', 'married', 'unemployed'])


