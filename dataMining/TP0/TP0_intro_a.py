#!/usr/bin/env python
# coding: utf-8

# 
# 
# ## <center> Python/Numpy Introduction (Not graded)
#  <center> Tuesday 02 March 2021
# 
#  <center> Frantzeska.Lavda@etu.unige.ch

# In[ ]:


# Create an 1d array from a list
import numpy as np

list1 = [0, 1, 2, 3, 4]
print(type(list1))
print('list1: ', list1)
arr1d = np.array(list1)

# Print the array and its type
print(type(arr1d))
print('arr1d: ', arr1d)

# ### Keep in mind: arrays are designed to handle vectorized operations while a python list is not!

# In[ ]:


# Add 2 to each element of list1. What do you observe?
list1 + 2

# In[ ]:


# Now Add 2 to each element of arr1d.
arr1d + 2

# In[ ]:


# Create a 2d array from a list of lists 
list2 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
arr2d = np.array(list2)
print(arr2d)

# Print its type
print(type(arr2d))

# In[ ]:


# Create a float, int, bool, str, object 2d array
arr2d_f = np.array(list2, dtype='float')
arr2d_f

# In[ ]:


# You can also convert an array to a different datatype using the astype method
# Convert arr2d_f to int
arr2d_f.astype('int')

# ### Keep in mind: A numpy array must have all items to be of the same data type, unlike lists!

# In[ ]:


# Shape, size, dimention, type
print('Shape: ', arr2d_f.shape)
print('Shape: ', arr2d_f.size)
print('Shape: ', arr2d_f.ndim)
print('Shape: ', arr2d_f.dtype)

# In[ ]:


# Create an 3d-dimensional NumPy array from nested Python lists.
list2 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]
arr3d = np.array(list2)
print(arr3d)
print(arr3d.dtype)
print((type(arr3d)))

# ### Creating arrays
# 
# #### There are several NumPy functions for creating arrays:
# 
# 
# <font color='blue'>numpy.array(a)</font>
# 	
#     Create n-dimensional NumPy array from sequence a
# 
# <font color='blue'>numpy.linspace(a,b,N)</font> 
#     
#     Create 1D NumPy array with N equally spaced values from a to b (inclusively)
# 
# <font color='blue'>numpy.arange(a,b,step)</font>
# 
# 	Create 1D NumPy array with values from a to b (exclusively) incremented by step
# 
# <font color='blue'>numpy.zeros(N)</font>
# 
# 	Create 1D NumPy array of zeros of length N
# 
# <font color='blue'>numpy.zeros((n,m))</font>
# 
# 	Create 2D NumPy array of zeros with n rows and  m columns
# 
# <font color='blue'>numpy.ones(N)</font>
# 
# 	Create 1D NumPy array of ones of length N
# 
# <font color='blue'>numpy.ones((n,m))</font>
# 
# 	Create 2D NumPy array of ones with n rows and m columns
# 
# <font color='blue'>numpy.eye(N)</font>
# 
# 	Create 2D NumPy array with  rows and  columns with ones on the diagonal (ie. the identity matrix of size N)

# In[ ]:


# Create a 1D NumPy array with 11 equally spaced values from 0 to 1:

x = np.linspace(0, 1, 11)
print(x)

# Create a 1D NumPy array with values from 0 to 20 (exclusively) incremented by 0.1:
y = np.arange(0, 1, 0.1)
print(y)

# In[ ]:


# Lower limit is 0 be default
print(np.arange(5))

# 0 to 9
print(np.arange(0, 10))

# 0 to 9 with step of 2
print(np.arange(0, 10, 2))

# 10 to 1, decreasing order
print(np.arange(10, 0, -1))

# Start at 1 and end at 50
np.linspace(start=1, stop=50, num=10, dtype=int)

# In[ ]:


# Create a 2D NumPy array of zeros with 2 rows and 5 columns:
zeros = np.zeros((2, 5))
print(zeros)

# Create the identity matrix of size 10:
I = np.eye(10)
print(I)

# ### Get  unique items and the counts

# In[ ]:


# Create random integers of size 10 between [0,10)
np.random.seed(100)
arr_rand = np.random.randint(0, 10, size=10)
print(arr_rand)

# In[ ]:


# Get the unique items and their counts
uniqs, counts = np.unique(arr_rand, return_counts=True)
print("Unique items : ", uniqs)
print("Counts       : ", counts)

# ### Extract specific items from an array

# In[ ]:


# Create a 2 x 4 2D NumPy array of random samples:
rand2d = np.random.rand(2, 4)
print(rand2d)

# In[ ]:


# Access the entry at 2nd row and 3rd column 
rand2d[1, 2]

# In[ ]:


# Access the 1st elemrn (top left entry)
rand2d[0, 0]

# In[ ]:


# Access the last element (bottom right entry) in the array
rand2d[-1, -1]

# In[ ]:


# Access the last row 
print(rand2d[1, :])
print(rand2d[-1, :])

# In[ ]:


# Access the 3rd column 
print(rand2d[:, 2])
print(rand2d[:, -2])

# In[ ]:


# Select the subarray of the 2 rows , and 2nd and 3rd columns 
sub_rand2d = rand2d[:, 1:3]
sub_rand2d

# In[ ]:


# reshape rand2d from 2 x 4 to 4 x 2
print(rand2d)
print('rand2d shape: ', rand2d.shape)

rand2d_b = rand2d.reshape(4, 2)
print(rand2d_b)
print('rand2d_b shape: ', rand2d_b.shape)

# ### Compute mean, var, min, max, sum

# In[ ]:


# ToDO compute the mean, minimum and maximum value of rand2d using for loop


# In[ ]:


# using numpy
# mean, max and min 
print("Mean value is: ", np.mean(rand2d))
print("Max value is: ", np.max(rand2d))
print("Min value is: ", np.min(rand2d))
print("Var value is: ", np.var(rand2d))

# In[ ]:


# Row wise and column wise mean
print("Column wise Mean: ", np.mean(rand2d, axis=0))
print("Row wise Mean: ", np.mean(rand2d, axis=1))

# In[ ]:


# Row wise and column wise min
print("Column wise minimum: ", np.amin(rand2d, axis=0))
print("Row wise minimum: ", np.amin(rand2d, axis=1))

# In[ ]:


# Sum of the columns
print(np.sum(rand2d, axis=0))
# Sum of the rows
print(np.sum(rand2d, axis=1))

# ### Basic Operations
# 

# In[ ]:


# 1d array

a = np.array([20, 30, 40, 50])
b = np.arange(4)
c = a - b
print('a: ', a)
print('b: ', b)

print('a - b: ', c)
d = a - b
print('a + b: ', d)
b_sq = b ** 2
print('b square: ', b_sq)
print('a<35: ', a < 35)

# In[ ]:


# 2d array
A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
# elementwise product
print('elementwise product:', A * B)
# matrix product1
print('matrix product1:', A @ B)
# matrix product2
print('matrix product2:', A.dot(B))

# ### While, for loop, list comprehension, function ..

# Define a sequence of numbers,
# 
# $$x_n=n^2+1$$
# 
# for integers $n=0,1,2,…,N$. * prints out $x_n$ for $n=0,1,…,20$ using a while loop. * store all the $x_n$ values
# computed above using a while loop in a list (using a while loop). Print the entire list (as one object) * reapet
# using for loop * make the code shorter using a list comprehension * Write a function called compute_x, which takes
# as input $n$, for computing an element in the sequence $x_n=n^2+1$. Call the function for $n=4$ and write out the
# result.
# 
# 

# In[ ]:


# prints out $x_n$ for $n=0,1,…,20$ using a while loop.

n = 0
while n <= 20:
    x_n = n ** 2 + 1
    print(x_n)
    n = n + 1

# In[ ]:


# store all the $x_n$ values computed above using a while loop in a list (using a while loop). Print the entire list (as one object)
n = 0
x = []  # the x_n values
while n <= 20:
    x.append(n ** 2 + 1)
    n = n + 1
print(x)

# In[ ]:


# reapet using for loop
x = []
for n in range(21):
    x.append(n ** 2 + 1)
print(x)

# In[ ]:


# make the code shorter using a list comprehension
x = [n ** 2 + 1 for n in range(21)]
print(x)


# In[ ]:


# Write  function
def compute_x(n):
    return n ** 2 + 1


print(compute_x(3))

# ###  Vectorization
# 
# #### Vectorization is a powerful ability within NumPy to express operations as occurring on entire arrays rather
# than their individual elements.
# 
# #### Count the number of even and odd numbers from a series of numbers using for loop.
# 

# In[ ]:


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
    if not x % 2:
        count_even += 1
    else:
        count_odd += 1
print("Number of even numbers :", count_even)
print("Number of odd numbers :", count_odd)

# In[ ]:


# compact syntax
print("Total evens: ", len([i for i in numbers if (i % 2 == 0)]))
print("Total odds: ", len([i for i in numbers if (i % 2 != 0)]))

# #### Find the index of 5th repetition of number 1 in x using
#  * for loop
#  * without for loop using np.where

# In[ ]:


x = np.array([1, 2, 1, 1, 3, 4, 3, 1, 1, 2, 1, 1, 2])
n = 5

# Solution 1: for loop 
# [i for i, v in enumerate(x) if v == 1][n-1]
# print('solution 1:', x)
count = 0
for i, v in enumerate(x):
    if v == 1:
        count += 1
        if count == 5:
            print('Sol 1: ', i)

# Solution 2: for loop List comprehension
print('Sol 2:', [i for i, v in enumerate(x) if v == 1][n - 1])

# Solution 3: Numpy version
print('Sol 3: ', np.where(x == 1)[0][n - 1])

# ### Measure the efficiency of vectorization
# 
# Measure the CPU time required by computing sin(x), where x is an array of 1M elements, using scalar computing with
# a loop (function sin_func) and vectorized computing using the sin function from numpy.

# In[ ]:


import numpy as np

n = 1000000
x = np.linspace(0, 1, n + 1)


def sin_func(x):
    r = np.zeros_like(x)  # result
    for i in range(len(x)):
        r[i] = np.sin(x[i])
    return r


# In[ ]:


get_ipython().run_line_magic('timeit', 'y = sin_func(x)')

# In[ ]:


get_ipython().run_line_magic('timeit', 'y = np.sin(x)')

# ### Understanding np.where

# In[ ]:


x = np.arange(9.).reshape(3, 3)
x

# In[ ]:


np.where(x > 5)

# In[ ]:


x[np.where(x > 3.0)]

# In[ ]:


np.where(x < 5, x, -1)

# ### Plot histograms

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, facecolor='blue')

plt.xlabel('x')

plt.show()


# ### Exercise 1
# The cosine function has the following infinite product representation
# 
# $$\cos x = \prod_{k=1}^{\infty}(1 - \frac{4 x^2}{\pi (2k -1)^2})$$
# 
# Write a function called cos_product which takes input parameters x and returns the Nth partial product
# 
# $$\prod_{k=1}^{\infty}(1 - \frac{4 x^2}{\pi (2k -1)^2})$$
# 

# In[ ]:


def cos_product(x, N):
    "Compute the product \\prod_{k=1}^N (1 - 4x^2/(pi^2 (2k - 1)^2)."

    ####### ADD YOUR CODE


# Verify your function using values for which you know the result. For example, $\cos(0) = 1$ , $\cos(\pi) = -1$ 

# In[ ]:


cos_product(0, 10)

# In[ ]:


cos_product(np.pi, 1000)

# ### Exercise 2 Write a function called count_transitions_for which takes 1 inputx x, a 1-dimensional vector of True
# and False and count the number of “False to True” transitions in the sequence with a for loop and a function called
# count_transitions without a for loop.

# In[ ]:


np.random.seed(444)
vect1 = np.random.choice([False, True], size=100000)
vect1


# In[ ]:


def count_transitions_for(x):
    count = 0

    ###### ADD YOUR CODE

    return count


# In[ ]:


count_transitions_for(vect1)


# In[ ]:


def count_transitions_for(x):
    ###### ADD YOUR CODE
    ###### hint: chech np.count_nonzero

    return count


# In[ ]:


count_transitions(vect1)

# In[ ]:
