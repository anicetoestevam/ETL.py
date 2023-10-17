
Link do colab com permissão para comentar:

https://colab.research.google.com/drive/1BA4Kp7EVZ5Jx-YZMOxyhz_ckh3bn48Qw?usp=sharing

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ler_venda = pd.read_excel('/Prova+Excel.xlsx', sheet_name='Q1')['Venda']
ler_produto = pd.read_excel('/Prova+Excel.xlsx', sheet_name='Q1')['Produto']

ler_venda.plot()
plt.show()

data_frame = {
  "Venda": [ler_venda],
  "Produto": [ler_produto]
}

df = pd.DataFrame(data_frame)

display(df)

media_vendas = np.mean(ler_venda)
total_vendido = np.sum(ler_venda)
maior = max(ler_venda)
menor = min(ler_venda)

print("Maior valor vendido:", maior)
print("Menor valor vendido:", menor)
print("Total vendido:", total_vendido)
print("Média das vendas:", media_vendas)


