import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
men_means = [4572346, 4573805, 4530484, 4459572, 4415051, 4257878, 4258888, 4117158, 3990009, 3858296]
women_means = [3786301, 3828024, 3847458, 3854476, 3886329, 3818272, 3874152, 3813226, 3719920, 3607595]

x = np.arange(len(labels))  # the label locations
width = 0.48  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means,  width, color='#8B0000', label='Mulheres')
rects2 = ax.bar(x + width/2, women_means, width, color='#2F4F4F', label='Homens')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Matriculas (Milhão)')
ax.set_title('Alunos Ension Médio - Brasil')
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