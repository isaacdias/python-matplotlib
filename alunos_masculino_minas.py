import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
men_means = [864.199, 819.127, 769.311, 743.392, 736.977, 719.936, 714.581, 717.254, 710.028, 687.871]
women_means = [712.892, 698.361, 694.471, 689.900, 679.458, 658.068, 629.947, 599.161, 584.986, 578.887]

x = np.arange(len(labels))  # the label locations
width = 0.48  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means,  width, color='#2E8B57', label='Anos Iniciais')
rects2 = ax.bar(x + width/2, women_means, width, color='#FF6347', label='Anos Finais')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Matriculas')
ax.set_title('Homens Ensino Fundamental - Minas Gerais')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()