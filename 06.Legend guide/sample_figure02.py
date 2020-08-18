import matplotlib.pyplot as plt
import matplotlib.lines as mlines

blue_line = mlines.Line2D([],[],color="blue",marker="*")
plt.legend(handles=[blue_line],bbox_to_anchor=(1,1),bbox_transform=plt.gcf().transFigure)

plt.show()