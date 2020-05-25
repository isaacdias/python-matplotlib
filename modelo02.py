import matplotlib.pyplot as plt
import numpy as np

brasil = [8, 9, 7, 8, 8, 9, 7, 8, 5, 10]
minas = [5, 10, 6, 8, 5, 10, 6, 8, 12, 3]
uberlandia = [8, 5, 7, 9, 5, 3, 16, 9, 10, 3]

barWidth = 0.25

plt.figure(figsize=(10,5))

r1 = np.arange(len(brasil))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

plt.bar(r1, brasil, color='#6ACACD', width=barWidth, label='Brasil')
plt.bar(r2, minas, color='#FFD700', width=barWidth, label='Minas Gerais')
plt.bar(r3, uberlandia, color='#6495ED', width=barWidth, label='Uberlândia')

plt.xlabel('Período')
bins = np.arange(5) - 0.5
plt.xticks([r + barWidth for r in range(len(brasil))], ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
plt.ylabel('Matrículas')
plt.title('Matrículas ensino médio')
plt.xlim([-1, 10])
plt.legend()
plt.show()