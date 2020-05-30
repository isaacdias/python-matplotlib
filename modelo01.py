
import matplotlib.pyplot as plt
import numpy as np

grupos = 11
homem = (51, 30, 50, 40, 20, 10, 30, 50, 40, 20, 30)
mulher = (5, 15, 25, 20, 30, 5, 15, 25, 20, 30, 35)
fig, ax = plt.subplots()
indice = np.arange(grupos)
bar_larg = 0.4
transp = 0.7
plt.bar(indice, mulher, bar_larg, color='#2E8B57', alpha=transp, label='Mulheres')
plt.bar(indice + bar_larg, homem, bar_larg, color='#FF6347', alpha=transp, label='Homens')

plt.title('Matrículas ensino básico Brasil')
plt.xticks(indice + bar_larg / 2, ('2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'))
plt.legend()
plt.tight_layout()
plt.xlabel('Anos')
plt.ylabel('Quantidade')
plt.show()