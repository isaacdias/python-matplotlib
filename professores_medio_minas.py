import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
men_means = [37.422, 38.629, 37.413, 39.391, 40.051, 39.789, 40.652, 39.438, 38.873, 36.770]
women_means = [17.657, 18.200, 18.400, 19.588, 20.239, 20.254, 21.136, 21.624, 21.856, 22.125]

x = np.arange(len(labels))  # the label locations
width = 0.48  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means,  width, color='#8B0000', label='Mulheres')
rects2 = ax.bar(x + width/2, women_means, width, color='#2F4F4F', label='Homens')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Matriculas')
ax.set_title('MInas Gerais - Ensino Médio ')
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