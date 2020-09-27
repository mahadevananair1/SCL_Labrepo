
# Impoting Numpy library
import numpy as np 

# Initialising arrays
x = np.array([[1,2,3],[3,2,1],[1,0,-1]])
y = np.array([[-4,-3,2],[1,2,1],[2,4,2]]) 

# Printing rank of x
print("rank of x: {}".format(np.linalg.matrix_rank(x)))

# Storing and Finding eigen vector and value of X Using eig function of Numpy
eigen_valuesX,eigen_vectorX= np.linalg.eig(x)

# Printing eigen value and vector of X
print("\nEIGEN VALUES OF X:\n{}".format(eigen_valuesX))
print("\nEIGEN VECTOR OF X:\n{}".format(eigen_vectorX))

# Printing rank of y
print("rank of y : {}".format(np.linalg.matrix_rank(y)))

# Storing and Finding eigen vector and value of Y Using eig function of Numpy
eigen_valuesY,eigen_vectorY= np.linalg.eig(y)

# Printing eigen value and vector of Y
print("\nEIGEN VALUES OF Y:\n{}".format(eigen_valuesY))
print("\nEIGEN VECTOR OF Y:\n{}".format(eigen_vectorY))