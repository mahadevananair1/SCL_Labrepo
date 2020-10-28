import matplotlib.pyplot as pl
import numpy as np

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)

y = np.cos(x)
y1 = np.sin(x)

#cos plot
pl.stem(x,y,'b', markerfmt='bo')
# sin plot
pl.stem(x, y1,'g', markerfmt='go')
pl.show()
