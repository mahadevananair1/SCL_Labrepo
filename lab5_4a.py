import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def f(U, t):
    # Here U is a vector such that y=U[0] and z=U[1]. This function should return [y', z']
    return [U[1], -1000*U[1] - 1000000000*U[0]]
U0 = [0, 5000]
t = np.arange(0, 0.01,0.00005)
Us = odeint(f, U0, t)
xs = Us[:,0]
plt.xlabel("x")
plt.ylabel("y")
plt.plot(t,xs);