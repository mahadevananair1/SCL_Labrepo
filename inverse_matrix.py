import numpy as np 
x = np.array([[1,3,3],[1,4,3],[1,3,4]]) 
y = np.linalg.inv(x) 
print (y)

# todo verification of inverse matrix
print(np.matmul(x,y))