import numpy as np
import scipy.linalg

A = np.array([[-7,-5,3], [-1,-8,2]])            # [[First Row] ,[Second row]]
print(f'The Matrix A is')
print(A)

B = np.array([[1],[2],[3]])
print('\nThe column vector B =')
print(B)
'''
C = np.zeros((3,2))
print('\n The 3x2 zero matrix =')
print(C)

Id = np.identity(3)
print('\nThe identity matrix is =')
print(id)

el = Id[:,[0]]
print('\nThe First coordinate Vector e_1 = ')
print(el)

D = np.transpose(A)                 # rows becomes the columns and the columns become the rows
# D = A.T                           # This is eqivalent to the above line
print('\nThe Tranpose of A is =')
print(D)

E = 3*A
print('\nScalar Multiplication by 3 =')
print(E)'''

#  ApB = A + B                      # This doens't work but they should be the same size
#  ApB = 
print('\nSum of A and B = ')
# print(ApB)

#C = np.add
# This isn't done I'll finish it later