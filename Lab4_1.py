# To realize the functions 
# sin t, cos t, sinht and cosht for the vector 
# t = [0, 10] with increment 0.01. 

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,10.01,0.01)
a = np.sin(x)
b = np.cos(x)
c = np.sinh(x)
d = np.cosh(x)
plt.plot(x,a)
plt.show()
plt.plot(x,b)
plt.show()
plt.plot(x,c)
plt.show()
plt.plot(x,d)
plt.show()
