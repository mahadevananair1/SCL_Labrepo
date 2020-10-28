import matplotlib.pyplot as plt
import random as ra

ra.seed(10)
y=[]
for i in range(100):
  y.append(int(10*ra.random()))
plt.hist(y,10)
plt.show()
