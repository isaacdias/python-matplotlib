import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
men_means = [182.870, 183.566, 182.387, 186.184, 187.806, 189.121, 189.349, 188.614, 189.292, 184.647]
women_means = [34.561, 35.561, 36.011, 37.329, 38.282, 38.361, 39.084, 39.204, 39.521, 39.283]

x = np.arange(len(labels))  # the label locations
width = 0.48  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means,  width, color='#8B0000', label='Mulheres')
rects2 = ax.bar(x + width/2, women_means, width, color='#2F4F4F', label='Homens')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Matriculas')
ax.set_title('Minas - Séries da Educação Básica ')
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











