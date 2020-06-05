import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
men_means = [7979918, 7803781, 7652237, 7553783, 7539595, 7434623, 7384382, 7332464, 7271059, 7206384]
women_means = [7056371, 6914019, 6734737, 6539400, 6256443, 6057779, 5992016, 5871426, 5874441, 5825569]

x = np.arange(len(labels))  # the label locations
width = 0.48  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means,  width, color='#00BFFF', label='Anos Iniciais')
rects2 = ax.bar(x + width/2, women_means, width, color='#C71585', label='Anos Finais')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Matriculas (Milhão)')
ax.set_title('Mulheres Ensino fundamental - Brasil')
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