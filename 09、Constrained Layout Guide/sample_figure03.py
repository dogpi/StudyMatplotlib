import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.gridspec as gridspec
import numpy as np

arr = np.arange(100).reshape((10, 10))
norm = mcolors.Normalize(vmin=0., vmax=100.)
# see note above: this makes all pcolormesh calls consistent:
pc_kwargs = {'rasterized': True, 'cmap': 'viridis', 'norm': norm}

fig, axs = plt.subplots(3, 3, figsize=(4, 4), constrained_layout=True)
for ax in axs.flat:
    im = ax.pcolormesh(arr, **pc_kwargs)
# axs[1:,][:,1] 子集1：第一行第二行的所有列--->子集1的所有行的第一列 行列从0开始
fig.colorbar(im, ax=axs[1:, ][:, 1], shrink=0.8)
# axs[:,-1] 所有行的最后一列
fig.colorbar(im, ax=axs[:, -1], shrink=0.6)

plt.show()