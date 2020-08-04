import matplotlib.pyplot as plt
import numpy as np

# 从0开始，到5.0，步长为0.2
t = np.arange(0.,5.,0.2)

plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.show()