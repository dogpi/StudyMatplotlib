import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2,100)

plt.figure(num="lines")
plt.plot(x,x,label="liner")
plt.plot(x,x**2,label="quadratic")
plt.plot(x,x**3,label="cubic")

plt.title("simple plot")
plt.legend()
plt.show()


