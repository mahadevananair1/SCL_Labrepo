# Solve the system of equations 2x + y + z = 4, x + 3y + 2z = 5, x = 6
import numpy as np
from matplotlib import pyplot as plt


q=np.array([[2,1,1],[1,3,2],[1,0,0]])
w=np.array([4,5,6])
x = np.linalg.solve(q, w)

print(x)
# plt.plot(x)
# #Showing what we plotted
# plt.show()
