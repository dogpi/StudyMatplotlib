import matplotlib.pyplot as plt

# figure1 两行1列
plt.figure(1)
plt.subplot(211)
plt.plot([1,2,3])
plt.subplot(212)
plt.plot([4,5,6])

# figure2
plt.figure(2)
plt.plot([4,5,6])

# 修改figure1中的第一幅图
plt.figure(1)
plt.subplot(211)
plt.title("Easy as 1,2,3")

# plt.clf()
# plt.cla()

plt.show()