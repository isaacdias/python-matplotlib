import matplotlib.pyplot as plt
import numpy as np


brasil = [4985864, 4932285, 4842066, 4783117, 4746926, 4624599, 4658750, 4624409, 4576150, 4364668]
minas = [3037343, 2929569, 2831003, 2775695, 2745912, 2671665, 2603248, 2549399, 2511483, 2461094]
uberlandia = [836390, 861022, 848983, 821588, 763666, 787359, 835089, 842697, 821349, 751103]

barWidth = 0.25

plt.figure(figsize=(10,5))

r1 = np.arange(len(brasil))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

plt.bar(r1, brasil, color='#0000FF', width=barWidth, label='Educação Básica')
plt.bar(r2, minas, color='#006400', width=barWidth, label='Ensino fundamental')
plt.bar(r3, uberlandia, color='#D2691E', width=barWidth, label='Ensino médio')

plt.xlabel('Período')
bins = np.arange(5) - 0.5
plt.xticks([r + barWidth for r in range(len(brasil))], ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
plt.ylabel('Matrículas')
plt.title('Matrículas por etapa de ensino, segundo a região de Minas Gerais de 2010 a 2019')
plt.xlim([-1, 10])
plt.legend()
plt.show()


#[31148.207, 30490.476, 29826.627, 29187.602, 28571.512, 27931.210, 27691.478, 27348.080, 27183.970, 26923.730]
#8358647, 8401829, 8377942, 8314048, 8301380, 8076150, 8133040, 7930384, 7709929, 7465891

