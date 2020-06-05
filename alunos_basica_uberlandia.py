import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
men_means = [68.995, 70.333, 70.362, 70.683, 70.545, 70.191, 71.696, 72.810, 74.532, 74.200]
women_means = [70.197, 71.384, 71.439, 71.993, 72.750, 72.089, 73.705, 74.873, 76.701, 75.243]

x = np.arange(len(labels))  # the label locations
width = 0.45  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means,  width, color='#8B0000', label='Mulheres')
rects2 = ax.bar(x + width/2, women_means, width, color='#2F4F4F', label='Homens')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Matriculas (Milhão)')
ax.set_title('Alunos Séries da Educação Básica - Uberlândia MG ')
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