
#trigonometric sin function

import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
      import matplotlib.pyplot as plt
x= np.arange(0, 10.01,0.01)	
si = np.sin(x)
co=np.cos(x) 
sih=np.sinh(x)
coh=np.cosh(x)	
f1 = InterpolatedUnivariateSpline(x, si)	
      dfdx = f1.derivative()	
plt.plot(x, dfdx(x))	
plt.show()	
dfdx2=dfdx.derivative()	
plt.plot(x, dfdx2(x))	
plt.show()

#trigonometric cos function
f1=InterpolatedUnivariateSpline(x,co)
dfdx=f1.derivative()
plt.plot(x,dfdx(x)) 
plt.show() 
dfdx2=dfdx.derivative() 
plt.plot(x, dfdx2(x)) 
plt.show()


#trigonometric sinh function

f1 = InterpolatedUnivariateSpline(x, sih) 
dfdx = f1.derivative()
plt.plot(x, dfdx(x)) 
plt.show() 
dfdx2=dfdx.derivative() 
plt.plot(x, dfdx2(x)) 
plt.show()

   #trigonometric cosh function
f1 = InterpolatedUnivariateSpline(x, coh) 
dfdx = f1.derivative()
plt.plot(x, dfdx(x)) 
plt.show() 
dfdx2=dfdx.derivative() 
plt.plot(x, dfdx2(x)) 
plt.show()


