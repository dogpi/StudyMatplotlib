import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,100)
y1 = 0.5 * x
y2 = x*x

plt.figure(num="坐标系")

plt.xlabel("x轴")
plt.ylabel("y轴")

ax = plt.gca()

ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")

ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")

ax.spines["bottom"].set_position(("data",0))
ax.spines["left"].set_position(("data",0))

plt.plot(x,y1,linestyle="--",label="0.5*x")
plt.plot(x,y2,label="x*x")

plt.legend()

plt.show()
