import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
men_means = [31.148207, 30.490476, 29.826627, 29.187602, 28.571512, 27.931210, 27.691478, 27.348080, 27.183970,26.923730]

x = np.arange(len(labels))  # the label locations
width = 0.60  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/20, men_means, width, color='#0000FF', label='Brasil')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Matrículas (Em milhões)')
ax.set_title('Matrículas do ensino fundamental, segundo a Região Geográfica de 2010 a 2019')
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

fig.tight_layout()

plt.show()