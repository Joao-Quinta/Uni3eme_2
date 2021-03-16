#!/usr/bin/env python
# coding: utf-8

# # TP1 Naive Bayes (OBLIGATORY)
# **individual work, deadline 29/03/2021 23:59**
# 
# In this TP you are going to implement the Naive Bayes (NB) algorithm for categorical (titanic) and continuous (iris) data using **Python 3**.
# 
# You are going to fill a few missing functions in the python script nb.py
# to implement the exercises that we ask. So first of all read and understand the given python script. To run your code you have to run the
# main TP1\_NB.ipynb notebook. Here you have to write
# only a short code (it is mentioned where) to run the NB algorithm. Parts of the code are given and it works if the missing functions in nb.py are correctly implemented.
# 
# For the categorical data you have to make the necessary modifications in the train_nb() and predict() functions functions in nb.py in order to work for both continuous and categorical data.
# 
# 
# 

# In[1]:


from __future__ import print_function
import random
import numpy as np

import matplotlib.pyplot as plt
# make figures appear inline
#get_ipython().run_line_magic('matplotlib', 'inline')


# for auto-reloading extenrnal modules
# see http://stackoverflow.com/questions/1907993/autoreload-of-modules-in-ipython
#get_ipython().run_line_magic('load_ext', 'autoreload')
#get_ipython().run_line_magic('autoreload', '2')


# ###  Import the iris data set

# In[2]:


from sklearn import datasets
from sklearn.utils import shuffle

def load_IRIS(test=True):
    iris = datasets.load_iris()
    X, y = shuffle(iris.data, iris.target, random_state= 1230)	
    if test:
        X_train = X[:100, :]
        y_train = y[:100]
        X_test = X[100:, :]
        y_test = y[100:]
        return X_train, y_train, X_test, y_test
    else:
        X = iris.data[:, :] 
        y = iris.target
        return X, y


# In[3]:


# Import the iris data set
X_train, y_train, X_test, y_test = load_IRIS(test=True)


# In[4]:


# As a sanity check, we print out the size of the training and test data.
print('Training data shape: ', X_train.shape)
print('Training labels shape: ', y_train.shape)
print('Test data shape: ', X_test.shape)
print('Test labels shape: ', y_test.shape)


# In[5]:


y_test


# ## Fill the missing parts in nb.py
# 

# In[7]:


from nb import train_nb, normal_distribution, predict


# ### Make sure that all the function work

# In[ ]:


print(normal_distribution(X_train, 0, 1).shape)


# In[ ]:


prior, mean, std = train_nb(X_train, y_train)
print('Prior: ', prior)
print('mean: ', mean)
print('std: ', std)
print('mean shape: ', mean.shape)
print('std shape: ', std.shape)


# In[ ]:


y_pred = predict(X_train, prior, mean, std)
print('Predicted label: ', y_pred)


# ### Train your model and compute train and test accuracy

# In[ ]:


from nb import NaiveBayes_cont


prior, mean, std = train_nb(X_train, y_train)


# In[ ]:


#compute the train accuracy:
y_train_pred = 
num_correct_train = 
accuracy_train = 
print('Train: Got %d / %d correct => accuracy: %f' % (num_correct_train, len(y_train), accuracy_train))


# In[ ]:


#compute the test accuracy:
y_test_pred = 
num_correct_test = 
accuracy_test = (
print('Test: Got %d / %d correct => accuracy: %f' % (num_correct_test, len(y_test), accuracy_test))


# ## Comment your results

# 

# ## Visualization
# ## Decision surface
# Visualize, study, and **discuss the decision surfaces that NB algorithm produces for the iris data set**.
# 
# 
# * To do so, you will work only in two attributes(training and testing).
# 
#      * Testing will be done on an artificially generated dataset that covers in a regular manner all possible values for the two chosen attributes. To do so we need to divide the space into a grid by discretizing the space  into $n$ values between the minimum and maximum value of an attribute. Each of these values must be compared with the $n$ discrete values of the second attribute. The resulting array will be of shape ($n$ * $n$, 2)
#      
#      * Using your training set classify your test instances and visualize the results of the classification

# In[ ]:


# Load the Iris data.
# Cleaning up variables to prevent loading data multiple times (which may cause memory issues)
try:
   del X_train, y_train
   del X_test, y_test
   print('Clear previously loaded data.')
except:
   pass

X_train, y_train = load_IRIS(test=False)

# As a sanity check, we print out the size of the training and test data.
# we use all the data as training
print('Training data shape: ', X_train.shape)
print('Training labels shape: ', y_train.shape)


# In[ ]:


axes_labels = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']

# For our visualisation we will only keep the two first attributs.
# You can choose 2 attribus here
attribut_1 = 1
attribut_2 = 3

X_train_2_features = np.array([X_train[:,attribut_1], X_train[:,attribut_2]]).T
axes_label_1 = axes_labels[attribut_1]
axes_label_2 = axes_labels[attribut_2]

# and the test set will be the matrix (n*n, 2) where n is the number of values taken between
# the min and the max of each attribute
n = 150

X_test = np.zeros((n*n, 2))
tmp = np.linspace(np.min(X_train_2_features[:, 0])-0.1, np.max(X_train_2_features[:, 0])+0.1, n)
X_test[:,0] = np.repeat(tmp, n)

tmp = np.linspace(np.min(X_train_2_features[:, 1])-0.1, np.max(X_train_2_features[:, 1])+0.1, n)
X_test[:,1] = np.tile(tmp, n)


print('Training data shape: ', X_train_2_features.shape)
print('Testing data shape: ', X_test.shape)


# In[ ]:


# train

from nb import NaiveBayes_cont

nb = NaiveBayes_cont()

prior, mean, std = train_nb(X_train_2_features, y_train)

# test
y_test_pred = predict(X_test, log_prior, mean_std)

print('Predicted data shape : ', y_test_pred.shape)


# In[ ]:


# plot the decision surface
colors_surfaces = ['#88E2EA', '#FFE1BB', '#D4F3CD']
colors_points = ['blue', 'red', 'green']

plt.rcParams['figure.figsize'] = (20.0, 16.0)
plt.clf()
fig = plt.figure() 

for n_class in range(3):
    x_train_attri_1 = X_train_2_features[y_train == n_class, 0]
    x_train_attri_2 = X_train_2_features[y_train == n_class, 1]
        
    x_test_attri_1 = X_test[y_test_pred == n_class, 0]
    x_test_attri_2 = X_test[y_test_pred == n_class, 1]
        
    ax = fig.add_subplot(2,3,1+i)  
    ax.set_title("K = ")
    ax.scatter(x_test_attri_1, x_test_attri_2, s=15, color=colors_surfaces[n_class])
    ax.scatter(x_train_attri_1, x_train_attri_2, s=15, color=colors_points[n_class])
    ax.set_xlabel(axes_label_1)
    ax.set_ylabel(axes_label_2)

        
# each color represent a class of the problem

# don't take care of the warning


# # NB for catedorical data

# In[ ]:


import numpy as np
import csv


# ### Import titanic dataset

# In[ ]:


with open('titanic.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile))
 
#We suppose that the first line is an indication on the meaning of each
#attribute so we can remove it.
del data[0]
 
#Randomizing the data (we use numpy)
data = np.array(data)
np.random.shuffle(data)
data.tolist()
 
#Splitting the set (2/3 for the training set / 1/3 for the test set)
split_value = int(len(data) / 3)
X_data = data[:,0:3]
y_data = data[:,3]


# In[ ]:


# As a sanity check, we print out the size of the data and the first line.

print('Data shape:', data.shape)
print('X_data shape:', X_data.shape)
print('y_data shape:', y_data.shape)
print('Data 1st line:', data[0])
print('X_data 1st line:', X_data[0])
print('y_data 1st line:', y_data[0])


# In[ ]:


X_train = X_data[:2*split_value]
y_train = y_data[:2*split_value]

X_test = X_data[2*split_value:]
y_test = y_data[2*split_value:]


# In[ ]:


# As a sanity check, we print out the size of the training and test data and the first line.

print('X_train shape:', X_train.shape)
print('y_train shape:', y_train.shape)
print('X_test shape:', X_test.shape)
print('y_test shape:', y_test.shape)


print('X_train 1st line:', X_train[0])
print('y_train 1st line:', y_train[0])


# ### NB for vategorical data
# 
# - Implement the NB algorithm for categorical data in (nb.py). 
# Do that using the train_nb() and predict() functions, **making the necessary modifications in order to work for both continuous and categorical data**.
#  
# - Compute the classification accuracy of the titanic data set (test data) and comment

# In[ ]:


# dont forget to import your functions


# In[ ]:





# In[ ]:





# In[ ]:




