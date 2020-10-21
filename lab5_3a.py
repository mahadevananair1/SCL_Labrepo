import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dx/dt
def f(x,t):
    dxdt = -1/3*x 
    return dxdt

# initial condition
x0 = 5

# time points
t = np.linspace(0,10)

# solve ODE
y = odeint(f,x0,t)

# plot results
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('x(t)')
plt.show()