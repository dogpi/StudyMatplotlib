import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

# 设置figure大小，单位英寸
plt.figure(figsize=(9, 3))

# 131:1行三列中的1列位置
plt.subplot(131)
# 条形图
plt.bar(names, values)
# 132:1行3列中的2列位置
plt.subplot(132)
# 散点图
plt.scatter(names, values)
# 133:1行三列中的3列位置
plt.subplot(133)
# 线状图
plt.plot(names, values)

# 将1行3列的figure重新划分为2行2列，并在第一个位置绘制新的图像，这将覆盖掉相应位置向的图像。
# 根据结果可以看出，覆盖掉了1行3列图像的前两个图像，由于新的图像大小没有与1行3列的第三张图有重叠，所以第3张图仍然存在。
plt.subplot(221)
plt.bar(names, values)

plt.suptitle('Categorical Plotting')
plt.show()