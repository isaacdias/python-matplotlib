import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
men_means = [789.752, 753.237, 709.173, 689.564, 688.777, 675.847, 673.175, 677.647, 670.964, 649.936]
women_means = [670.500, 658.844, 658.048, 652.839, 640.700, 617.814, 585.545, 555.337, 545.505, 544.400]

x = np.arange(len(labels))  # the label locations
width = 0.48  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means,  width, color='#00BFFF', label='Anos Iniciais')
rects2 = ax.bar(x + width/2, women_means, width, color='#C71585', label='Anos Finais')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Matriculas')
ax.set_title('Mulheres Ensino fundamental - Minas Gerais')
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