# Use general integration tool to compute the integral of the 
# function (e^(-t))Sin(3t) from 0 to 2*pi.
#  Execute the program and upload the results.


import numpy as np
import scipy.integrate as gra
def f(x):
  return (np.exp(-x)*np.sin(3*x))
x = np.arange(-5,5.01,0.01)
ans=gra.quad(f,0,2*np.pi)
print(ans)
