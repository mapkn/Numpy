# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 11:05:07 2018

@author: patemi
"""

import numpy as np


#initialise an empty array
aa=np.empty((5,5))

#########################################
## Adding to existing array 

# Using append to add / combine
a = np.array([[1,2,3],[2,3,4]])
z = np.zeros((2,1), dtype=int)

y=np.append(a,z,axis=1)

##############################################
## Matrix mul/ np.dot

############################################

# matrix elements using tuple of lists
mat1=([1,2],[4,5])
mat2=([3,4],[4,4])


# Outputs are arrays
# using dot function
res=np.dot(mat1,mat2)
# using matmul function
res2=np.matmul(mat1,mat2)


# matrix elements converting list of tuples to numpy array
mat3=np.array(([1,2],[4,5]))
mat4=np.array(([3,4],[4,4]))

print(mat3.shape)
print(mat4.shape)

# Outputs are arrays, same as above
# using dot function
res3=np.dot(mat3,mat4)
# using matmul function
res4=np.matmul(mat3,mat4)


#################################
## TRANSPOSE (matrix)
################################

# Transpose will not work for mat1/mat2 as they are tuples
#mat1_T=mat1.transpose()
#mat2_T=mat2.transpose()

# Transpose will work for mat3/mat4 as they are arrays
mat3_T=mat3.transpose()
mat4_T=mat4.transpose()


# array of type float, size (3,)
x=np.array([2.644495330598511273e+00, 2.488047640305119046e+00, 2.461317155350413444e+01])

# Transpose works on this, but does nothing
x_T=x.transpose()

# Convert array to matrix type, size (1,3)
x_matrix=np.asmatrix(x)
# Transpose works on this, as expected, size (3,1)
x_matrix_T=x_matrix.transpose()


print(x_matrix.shape)
print(x_matrix_T.shape)


# matrix type
I1=np.matlib.identity(3)
 
# matmul : matrix product of two arrays
# Output is matrix type
output=np.matmul(np.asmatrix(np.array([1,2,3])),I1)


######################################

# Slicing arrays : take care with dimension of array
# and slicer

#####################################

list1=[[5,6],[7,8]]
list2=[5,6]

array1=np.array(list1)
array2=np.array(list2)

print(array1.shape)
print(array2.shape)

array1[:,0]
#array2[:,0]


# Size of an array

print(array1.size)