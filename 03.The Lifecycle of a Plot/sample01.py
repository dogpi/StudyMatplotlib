import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# 数据
data = {
    'Barton LLC': 109438.50,
    'Frami, Hills and Schmidt': 103569.59,
    'Fritsch, Russel and Anderson': 112214.71,
    'Jerde-Hilpert': 112591.43,
    'Keeling LLC': 100934.30,
    'Koepp Ltd': 103660.54,
    'Kulas Inc': 137351.96,
    'Trantow-Barrows': 123381.38,
    'White-Trantow': 135841.99,
    'Will LLC': 104437.60
}

# key
group_names = list(data.keys())
# values
group_data = list(data.values())
# values 的平均值
group_mean = np.mean(group_data)

# 可使用的样式
# ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic',
# 'dark_background', 'fast', 'fivethirtyeight', 'ggplot',
# 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind',
# 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid',
# 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook',
# 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk',
# 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']
print(plt.style.available)

# 使用样式
plt.style.use('fivethirtyeight')

# 创建Figure对象
# 返回值 fig是一个Figure对象，ax是Axes对象的数组，这里我们只生成1个Axes。
# 可通过nrows= ncols= 来控制生成的Axes的个数，默认情况下nrows=1, ncols=1。因此只生成1个Axes。
fig,ax = plt.subplots(num="barh")

# 绘制条形图
ax.barh(group_names,group_data)



plt.show()