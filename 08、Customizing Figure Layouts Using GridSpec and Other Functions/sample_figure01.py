import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# fig1, f1_axes = plt.subplots(ncols=2, nrows=2, constrained_layout=True)

# fig2 = plt.figure(constrained_layout=True)
# spec2 = gridspec.GridSpec(ncols=2,nrows=2,figure=fig2)
# f2_ax1 = fig2.add_subplot(spec2[0,0])
# f2_ax2 = fig2.add_subplot(spec2[0,1])
# f2_ax3 = fig2.add_subplot(spec2[1,0])
# f2_ax4 = fig2.add_subplot(spec2[1,1])

# fig3 = plt.figure(constrained_layout=True)
# gs = fig3.add_gridspec(3, 3)
# f3_ax1 = fig3.add_subplot(gs[0, :])
# f3_ax1.set_title('gs[0, :]')
# f3_ax2 = fig3.add_subplot(gs[1, :-1])
# f3_ax2.set_title('gs[1, :-1]')
# f3_ax3 = fig3.add_subplot(gs[1:, -1])
# f3_ax3.set_title('gs[1:, -1]')
# f3_ax4 = fig3.add_subplot(gs[-1, 0])
# f3_ax4.set_title('gs[-1, 0]')
# f3_ax5 = fig3.add_subplot(gs[-1, -2])
# f3_ax5.set_title('gs[-1, -2]')

# fig4 = plt.figure(constrained_layout=True)
# spec4 = fig4.add_gridspec(ncols=2, nrows=2)
# anno_opts = dict(xy=(0.5, 0.5), xycoords='axes fraction',
#                  va='center', ha='center')
#
# f4_ax1 = fig4.add_subplot(spec4[0, 0])
# f4_ax1.annotate('GridSpec[0, 0]', **anno_opts)
# fig4.add_subplot(spec4[0, 1]).annotate('GridSpec[0, 1:]', **anno_opts)
# fig4.add_subplot(spec4[1, 0]).annotate('GridSpec[1:, 0]', **anno_opts)
# fig4.add_subplot(spec4[1, 1]).annotate('GridSpec[1:, 1:]', **anno_opts)

# fig5 = plt.figure(constrained_layout=True)
# widths = [2, 3, 1.5]
# heights = [1, 3, 2]
# spec5 = fig5.add_gridspec(ncols=3, nrows=3, width_ratios=widths,
#                           height_ratios=heights)
# for row in range(3):
#     for col in range(3):
#         ax = fig5.add_subplot(spec5[row, col])
#         label = 'Width: {}\nHeight: {}'.format(widths[col], heights[row])
#         ax.annotate(label, (0.1, 0.5), xycoords='axes fraction', va='center')

# widths = [2, 3, 1.5]
# heights = [1, 3, 2]
# gs_kw = dict(width_ratios=widths, height_ratios=heights)
# fig6, f6_axes = plt.subplots(ncols=3, nrows=3, constrained_layout=True,
#         gridspec_kw=gs_kw)
# for r, row in enumerate(f6_axes):
#     for c, ax in enumerate(row):
#         label = 'Width: {}\nHeight: {}'.format(widths[c], heights[r])
#         ax.annotate(label, (0.1, 0.5), xycoords='axes fraction', va='center')

# fig7, f7_axs = plt.subplots(ncols=3, nrows=3)
# gs = f7_axs[1, 2].get_gridspec()
# # remove the underlying axes
# for ax in f7_axs[1:, -1]:
#     ax.remove()
# axbig = fig7.add_subplot(gs[1:, -1])
# axbig.annotate('Big Axes \nGridSpec[1:, -1]', (0.1, 0.5),
#                xycoords='axes fraction', va='center')
# fig7.tight_layout()

# fig8 = plt.figure(constrained_layout=False)
# gs1 = fig8.add_gridspec(nrows=3, ncols=3, left=0.05, right=0.48, wspace=0.05)
# f8_ax1 = fig8.add_subplot(gs1[:-1, :])
# f8_ax2 = fig8.add_subplot(gs1[-1, :-1])
# f8_ax3 = fig8.add_subplot(gs1[-1, -1])

# fig9 = plt.figure(constrained_layout=False)
# gs1 = fig9.add_gridspec(nrows=3, ncols=3, left=0.05, right=0.48,
#                         wspace=0.05)
# f9_ax1 = fig9.add_subplot(gs1[:-1, :])
# f9_ax2 = fig9.add_subplot(gs1[-1, :-1])
# f9_ax3 = fig9.add_subplot(gs1[-1, -1])
#
# gs2 = fig9.add_gridspec(nrows=3, ncols=3, left=0.55, right=0.98,
#                         hspace=0.05)
# f9_ax4 = fig9.add_subplot(gs2[:, :-1])
# f9_ax5 = fig9.add_subplot(gs2[:-1, -1])
# f9_ax6 = fig9.add_subplot(gs2[-1, -1])

fig10 = plt.figure(constrained_layout=True)
gs0 = fig10.add_gridspec(1, 2)

gs00 = gs0[0].subgridspec(2, 3)
gs01 = gs0[1].subgridspec(3, 2)

for a in range(2):
    for b in range(3):
        fig10.add_subplot(gs00[a, b])
        fig10.add_subplot(gs01[b, a])

plt.show()

