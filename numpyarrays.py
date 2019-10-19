# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 11:05:07 2018

@author: patemi
"""

# Good Reference for matrices in python
#http://eric.univ-lyon2.fr/~ricco/cours/slides/PH%20-%20en%20-%20matrices%20avec%20numpy.pdf


import numpy as np
import pandas as pd

# Creating empty numpy array
emptyarray=np.empty(1)


# Converts a list to a numpy array
x=np.array([2,3,1,0])

# Dot Product of two vectors/arrays
zz=np.dot(x,x)


# Multiply two lists with numpy
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])
print(a.shape)
print(b.shape)
c=a*b


# Single element indexing for 1-d array
print(a[0])



# Numpy arrays have fixed types. You can't change an int array to floats later
alpha=np.array([0,0,0])
alpha[0]=0.0001
print(alpha[0])
alpha=np.array([0,0,0], np.float)
alpha[0]=0.0001
print(alpha[0])



# Get indices where a given condition is true:
i=np.where(b==4)


# Element wise addition/subtraction in numpy
cc=a+b
cd=a-b


# Maxima by elements
d=np.maximum(a,b)


# Return a new array of given shape and type, without initializing entries.
e=np.empty(5,dtype=str)
e[0]='Mitul'


# Creates a numpy array of zeros 
y=np.zeros((2,3))

# Creatsr a numpy array with regularly inrementing values - incremenbs are specified
z=np.arange(10)
z1=np.arange(2,10)
z2=np.arange(2,10,0.5)
z3=np.arange(2,10,dtype=np.float)


# Create a numpy array with specified number of elements - increments are not specified
y2=np.linspace(1.,4.,6)


# Create a full array
y3=np.full((2,2),7)

# Create an array of random values
y3=np.random.random((2,2))



# Random dataframe
np.random.seed(5)
df = pd.DataFrame(np.random.randint(100, size=(100, 6)), 
                  columns=list('ABCDEF'), 
                  index=['R{}'.format(i) for i in range(100)])


# Convert a dataframe to a numpy array
dfarray=df.values
dfarray3=df.as_matrix()


# Reference the first row/column of an array
print(dfarray3[:,0])
print(dfarray3[0,:])


# For a great explanation of numpy array shapes see here
#https://stackoverflow.com/questions/22053050/difference-between-numpy-array-shape-r-1-and-r
aa = np.arange(12)
print(aa.shape)
bb=aa.reshape((3,4))


# iterating over the rows/columns of a numpy array
for column in bb.T:
    print(column)


for column in bb:
    print(column)


# Creating nupy array of 1s

v=np.ones((2,2))

# Iterating over a numpy array
# Take care if order matters!!!
#for x in np.nditer(dfarray):
    #print(x)
    

#  Finding the index of something in an array. 
# The result is a tuple with first all the row indices, then all the column indices

#  https://stackoverflow.com/questions/432112/is-there-a-numpy-function-to-return-the-first-index-of-something-in-an-array
itemindex = np.where(aa==5)


