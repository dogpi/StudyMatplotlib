import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

data = np.random.random(50)
with plt.style.context("dark_background"):
    plt.plot(np.sin(np.linspace(0,2*np.pi)),"r-o")

plt.show()
