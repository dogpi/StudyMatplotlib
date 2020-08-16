import matplotlib.pyplot as plt
import matplotlib.lines as lines

fig = plt.figure()

l1 = lines.Line2D([0,1],[0,1],transform=fig.transFigure,figure=fig)
l2 = lines.Line2D([0,1],[1,0],transform=fig.transFigure,figure=fig)

fig.lines.extend([l1,l2])


# 创建一个Axes
ax = fig.add_subplot(111)
#获取创建的Axes的patch
rect = ax.patch
# 通过patch设置属性
rect.set_facecolor('green')

for label in ax.get_xticklabels():
    label.set_color("orange")

axis = ax.xaxis
print(axis.get_ticklocs())
print(axis.get_ticklabels())
print(axis.get_ticklines())

plt.show()
