import matplotlib.pyplot as plt
import numpy as np
# fig = plt.figure("hello figure")
# fig.suptitle("No axes on this figure")

fig, ax_lst = plt.subplots(2,2,num="hello figure")
fig.suptitle("2x2 axes")
ax_lst[0][0].set_title("first")
ax_lst[0][0].set_xlim(10)
ax_lst[0][0].set_ylim(20)
ax_lst[0][0].set_xlabel("x")
ax_lst[0][0].set_ylabel("y")
ax_lst[0][1].set_title("second")
ax_lst[1][0].set_title("third")
ax_lst[1][1].set_title("fourth")
plt.show()