# To realize 
# the function f(t) = 4t^2+ 3 
# and plot it for the vector t = [-5 5] with increment 0.01 

import numpy as np
import matplotlib.pyplot as plt
t=np.arange(-5,5.01,0.01)
y=(4*t*t)+3
plt.plot(t,y)
plt.show()
