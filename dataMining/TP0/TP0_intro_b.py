#!/usr/bin/env python
# coding: utf-8

# ## <center> Playing with the data sets (Not graded)
#  <center> Tuesday 02 March 2021
# 
#  <center> Frantzeska.Lavda@etu.unige.ch

# In[ ]:


import numpy as np
#from scipy.misc import imread
#from imageio import imread
from sklearn import datasets
from sklearn.utils import shuffle


# ## Iris data set. 
# 
# The iris data set contains descriptions of plants belonging to one of three categories of the iris plant : Iris-setosa, Iris-versicolor, Iris-virginica. The description of a plant is given by the four continuous attributes : sepal-length, sepal-width, petal-length, petal-width
# 
# 

# In[ ]:


def load_IRIS(test=True):
    iris = datasets.load_iris()
    X, y = shuffle(iris.data, iris.target, random_state= 400)
    if test:
        X_train = X[:100, :]
        y_train = y[:100]
        X_test = X[100:, :]
        y_test = y[100:]
        return X_train, y_train, X_test, y_test
    else:
        X = iris.data
        y = iris.target
        return X, y


# In[ ]:


# load the iris data set
x_iris, y_iris = load_IRIS(test=False)

# chech the shape of the data anf target
print('Data shape:', x_iris.shape)
print('Target shape:', y_iris.shape)


# ### For each continuous attribute f compute:
# - the mean and the variance of each column, mean(f), var(f)
# - the conditional mean and variance of each column, mean(f | target), var(f | target)

# In[ ]:





# ### Visualize the distributions of the continuous attributes using histograms

# In[ ]:


import matplotlib.pyplot as plt


# ### Visualize the distributions of the continuous attributes conditioned on the type of the iris plant using histograms

# In[ ]:





# ## Titanic data set
#  This dataset provides information on the fate of
# passengers on the fatal maiden voyage of the ocean liner ’Titanic’, summarized
# according to economic status (class), sex, age and survival. The target attribute
# is result ∈ {mort, surv} which indicates whether the passenger survived or not.
# 
# - Class    : crew = 0, first = 1, second = 2, third = 3
# - Age      : adult = 0, child = 1
# - Sex      : female = 0, male = 1
# - Survived : no = 0, yes = 1.

# In[ ]:


import csv

# Loading the titanic data set and transform it into an array.
with open('titanic.csv', newline='') as csvfile: titanic = list(csv.reader(csvfile))
 
print('Name of each column:\n', np.array(titanic)[0, :], '\n')

# Delete the header containing the name of each feature
titanic = np.array(titanic)[1:, :]

# shuffle the data
np.random.shuffle(titanic)

# print 10 first lines of dataset
print('10 first lines of dataset:\n', titanic[0:10, :], '\n')


# In[ ]:


# split data and target
x_titanic = titanic[:,0:3]
y_titanic = titanic[:,3]

# shapes

print('Dataset shape:', titanic.shape)
print('x shape:', x_titanic.shape)
print('target shape:', y_titanic.shape)


# ### For each discrete attribute f :
# - find the levels of each attribute/ column 
# - compute the number of data of each level
# 
# hint: use np.unique

# In[ ]:




