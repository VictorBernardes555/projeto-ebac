import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd

github_df = pd.read_csv('gasolina.csv', sep=',')
github_df


with sns.axes_style('whitegrid'):
  
  grafico = sns.lineplot(data=github_df, x="dia", y="venda", palette="pastel")
  grafico.set(title='Gasolina - Vendas por dia', xlabel='Dia - Julho/21', ylabel='Venda(R$)');
  plt.savefig("gasolina.png");