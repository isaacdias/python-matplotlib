
import matplotlib.pyplot as plt
import numpy as np

grupos = 11
homem = (10, 30, 50, 40, 20, 10, 30, 50, 40, 20, 30)
mulher = (5, 15, 25, 20, 30, 5, 15, 25, 20, 30, 35)
fig, ax = plt.subplots()
indice = np.arange(grupos)
bar_larg = 0.4
transp = 0.7
plt.bar(indice, homem, bar_larg, alpha=transp, label='Homens')
plt.bar(indice + bar_larg, mulher, bar_larg, alpha=transp, label='Mulheres')

plt.title('Matrículas ensino básico Brasil')
plt.xticks(indice + bar_larg / 2, ('2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'))
plt.legend()
plt.tight_layout()
plt.xlabel('Anos')
plt.ylabel('Quantidade')
plt.show()