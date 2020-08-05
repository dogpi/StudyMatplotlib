from matplotlib.ticker import NullFormatter
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19940101)

y = np.random.normal(loc=0.5,scale=0.4,size=1000)
y = y[(y>0)&(y<1)]
y.sort()

x = np.arange(len(y))

plt.figure()

plt.subplot(221)
plt.plot(x,y)
plt.yscale("linear")
plt.title("linear")
plt.grid(True)

plt.subplot(222)
plt.plot(x,y)
plt.yscale("log")
plt.title("log")
plt.grid(True)

plt.subplot(223)
plt.plot(x,y-y.mean())
plt.yscale("symlog",linthreshy=0.01)
plt.title("symlog")
plt.grid(True)

plt.subplot(224)
plt.plot(x,y)
plt.yscale("logit")
plt.title("logit")
plt.grid(True)


#将y轴的短刻度标签格式化为空字符串“NullFormatter”，以避免使用太多标签妨碍轴。
plt.gca().yaxis.set_minor_formatter(NullFormatter())
# 调整subplots的布局，因为logit可能占用更多的空间，因为tick标签更长
plt.subplots_adjust(top=0.92,bottom=0.08,left=0.10,right=0.95,hspace=0.25,wspace=0.35)

plt.show()


