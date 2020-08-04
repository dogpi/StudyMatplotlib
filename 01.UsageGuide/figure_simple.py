import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)
y = np.sin(x)
fig,ax = plt.subplots(num="sin")
ax.plot(x,y,marker="*",color=(1,0,0),linestyle="dashed")
ax.set_title("sin")
plt.show()