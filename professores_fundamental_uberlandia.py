import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
men_means = [3373, 3413, 3382, 3667, 3629, 3709, 3724, 3670, 3886, 3826]
women_means = [602, 628, 622, 466, 460, 499, 554, 509, 569, 590]

x = np.arange(len(labels))  # the label locations
width = 0.48  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means,  width, color='#8B0000', label='Mulheres')
rects2 = ax.bar(x + width/2, women_means, width, color='#2F4F4F', label='Homens')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Matriculas')
ax.set_title('Uberlândia MG - Ensino Fundamental ')
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