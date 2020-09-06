import matplotlib.pyplot as plt
import numpy as np

# fig, ax = plt.subplots(constrained_layout=True)
# ax.plot(np.arange(10), label='This is a plot')
# ax.legend(loc='center left', bbox_to_anchor=(0.8, 0.5))

fig, axs = plt.subplots(1, 2, figsize=(4, 2), constrained_layout=True)
axs[0].plot(np.arange(10))
axs[1].plot(np.arange(10), label='This is a plot')
axs[1].legend(loc='center left', bbox_to_anchor=(0.8, 0.5))

plt.show()