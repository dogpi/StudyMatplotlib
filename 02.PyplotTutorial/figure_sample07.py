import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6.5,6.5))
plt.plot([1,2,3],[4,5,6])
#         左下角坐标点
plt.axes([0,0.1,0.8,0.8])
plt.show()