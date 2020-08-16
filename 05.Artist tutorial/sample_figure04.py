import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import numpy as np
# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()
ax.plot(100*np.random.rand(20))

# tick显示格式
formatter = ticker.FormatStrFormatter('$%1.2f')
# 创建一个新的tick
ax.yaxis.set_major_formatter(formatter)

for tick in ax.yaxis.get_major_ticks():
    # 默认的label 在左边显示
    tick.label1.set_visible(False)
    # 右边显示的label
    tick.label2.set_visible(True)
    tick.label2.set_color('green')

plt.show()
