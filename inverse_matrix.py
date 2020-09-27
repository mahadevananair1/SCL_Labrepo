# Import necesssary library
import numpy as np 
# Initialising 2D matrices
x = np.array([[1,3,3],[1,4,3],[1,3,4]]) 

# Inverse function of numpy
y = np.linalg.inv(x) 
print (y)

# Verification of inverse matrix
# print(np.matmul(x,y))