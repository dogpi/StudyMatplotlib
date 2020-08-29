import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.gridspec as gridspec
import numpy as np

arr = np.arange(100).reshape((10, 10))
norm = mcolors.Normalize(vmin=0., vmax=100.)
# see note above: this makes all pcolormesh calls consistent:
pc_kwargs = {'rasterized': True, 'cmap': 'viridis', 'norm': norm}

# fig, axs = plt.subplots(3, 1, figsize=(4, 4), constrained_layout=True)
# for ax in axs[:2]:
#     im = ax.pcolormesh(arr, **pc_kwargs)
# axs[:2]为列表
# fig.colorbar(im, ax=axs[:2], shrink=0.6)
# im = axs[2].pcolormesh(arr, **pc_kwargs)
# axs[2]为非列表
# fig.colorbar(im, ax=axs[2], shrink=0.6)

fig, axs = plt.subplots(3, 1, figsize=(4, 4), constrained_layout=True)
for ax in axs[:2]:
    im = ax.pcolormesh(arr, **pc_kwargs)
# axs[:2]为列表
fig.colorbar(im, ax=axs[:2], shrink=0.6)
im = axs[2].pcolormesh(arr, **pc_kwargs)
# [axs[2]]为列表
fig.colorbar(im, ax=[axs[2]], shrink=0.6)

plt.show()