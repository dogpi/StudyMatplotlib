import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.style.use("ggplot")
# print(mpl.get_configdir())
# 请注意，右边的样式将覆盖左边的样式已经定义的值
# plt.style.use(['dark_background', './presentation.mplstyle'])
data = np.random.random(50)
mpl.rcParams['lines.linewidth'] = 4
mpl.rcParams['lines.color'] = 'black'
# print(plt.style.available)
# mpl.rc('lines', linewidth=4, color='g')
plt.plot(data)

plt.show()