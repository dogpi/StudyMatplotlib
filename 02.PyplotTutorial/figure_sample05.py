import matplotlib.pyplot as plt
import numpy as np

y1 = np.arange(0,10,2)
x1 = np.arange(0,5)

y2 = np.arange(0,20,4)
x2 = np.arange(0,5)

lines = plt.plot(x1,y1,x2,y2)
plt.setp(lines)
plt.show()