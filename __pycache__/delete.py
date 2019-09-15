# # bills = [12, 4, 5, 56, 7, 78, 8]

# for x, y in enumerate(bills, start=1):
#     print(x, y)
# print(type(enumerate(bills)))

# print(help(enumerate)) #help can only be used with classes
# print(emp1.__dict__)  # dict
# print(dir(a))         # dir(object) gives all the attributes that can be used with that object


# set1 = {1, 2, 3, 4, 4, 5, 5, 6}
# print(set1)

# a1 = [{1, 2, 3, 4, 4, 5, 5, 6}, {1, 2, 3, 4, 4, 5, 5, 6}]
# b = [a1[0], a1[1]]
# for x, y in enumerate(b):
#     print(x, y)

#
# -----------------------------------------------------------------------------

# for _ in int.__dict__.items():
#     print('----------------\n')
#     print(_)

# a1 = 5
# for _ in a1.__dir__().__class__():
#     print('******************\n')
#     print(_)
'''
import pandas as pd
import numpy as np

x = pd.Series(list(1, 2, 3))

# print(x)

y = pd.Series(list('rohit'))
# print(y)


t = pd.Series(list(set(x).intersection(set(y))))
print(t)


l = pd.Series(np.intersect1d(x.values, y.values))
print(l)
'''
# ______________________________________

#from matplotlib import pyplot as plt

import scikit_learn

'''
from sklearn.model_selection import train_test_split  # sklearm.cross_validation has been deprecated
from sklearn.linear_model import LinearRegression

from sklearn.preprocessing import imputation
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso, Ridge, ElasticNet
from sklearn.decomposition import PCA
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans, DBSCAN
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor
'''
