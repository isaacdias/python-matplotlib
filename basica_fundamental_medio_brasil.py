import matplotlib.pyplot as plt
import numpy as np


brasil = [51.549899,  50.972619, 50.545050, 50.042448, 49.771371, 48.796512, 48.817479, 48.608093, 48.455867, 47.874246]
minas = [31.148207, 30.490476, 29.826627, 29.187602, 28.571512, 27.931210, 27.691478, 27.348080, 27.183970, 26.923730]
uberlandia = [8.358647, 8.401829, 8.377942, 8.314048, 8.301380, 8.076150, 8.133040, 7.930384, 7.709929, 7.465891]

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
plt.title('Matrículas da Educação Básica, segundo a Região Geográfica de 2010 a 2019')
plt.xlim([-1, 10])
plt.legend()
plt.show()


#[31148.207, 30490.476, 29826.627, 29187.602, 28571.512, 27931.210, 27691.478, 27348.080, 27183.970, 26923.730]
#8358647, 8401829, 8377942, 8314048, 8301380, 8076150, 8133040, 7930384, 7709929, 7465891

