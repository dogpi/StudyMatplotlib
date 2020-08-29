import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.gridspec as gridspec
import numpy as np


plt.rcParams['savefig.facecolor'] = "0.8"
plt.rcParams['figure.figsize'] = 4.5, 4.


def example_plot(ax, fontsize=12, nodec=False):
    ax.plot([1, 2])

    ax.locator_params(nbins=3)
    if not nodec:
        ax.set_xlabel('x-label', fontsize=fontsize)
        ax.set_ylabel('y-label', fontsize=fontsize)
        ax.set_title('Title', fontsize=fontsize)
    else:
        ax.set_xticklabels('')
        ax.set_yticklabels('')


# fig, ax = plt.subplots(constrained_layout=False)
# fig, ax = plt.subplots(constrained_layout=True)
# example_plot(ax, fontsize=24)

# fig, axs = plt.subplots(2,2,constrained_layout=False)
# for ax in axs.flat:
#     example_plot(ax, fontsize=24)

fig, axs = plt.subplots(2,2,constrained_layout=True)
for ax in axs.flat:
    example_plot(ax, fontsize=24)

plt.show()