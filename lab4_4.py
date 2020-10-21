# To compute the integral of f(t) in the limit -2 to 2 where f(t) = 4t^2+ 3. 


import numpy as np
import scipy.integrate as gra
t=np.arange(-5,5.01,0.01)
def f(t):
  return(4*t**2+3)
ans=gra.quad(f,-2,2)
print(ans)
