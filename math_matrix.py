import numpy as np 
x = np.array([[1,2,3],[3,2,1],[1,0,-1]])
y = np.array([[-4,-3,2],[1,2,1],[2,4,2]]) 
# rank of x
print("rank of x: {}".format(np.linalg.matrix_rank(x)))
eigen_valuesX,eigen_vectorX= np.linalg.eig(x)
# print(w)
print("\nEIGEN VALUES OF X:\n{}".format(eigen_valuesX))
print("\nEIGEN VECTOR OF X:\n{}".format(eigen_vectorX))

# rank of y
print("rank of y : {}".format(np.linalg.matrix_rank(y)))
eigen_valuesY,eigen_vectorY= np.linalg.eig(y)
# print(w)
print("\nEIGEN VALUES OF Y:\n{}".format(eigen_valuesY))
print("\nEIGEN VECTOR OF Y:\n{}".format(eigen_vectorY))