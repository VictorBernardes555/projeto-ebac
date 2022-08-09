import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd

github_df = pd.read_csv('gasolina.csv', sep=',')
github_df


with sns.axes_style('whitegrid'):
  
  grafico = sns.lineplot(data=github_df, x="dia", y="venda", palette="pastel")
  grafico.set(title='Vendas por dia', xlabel='Dia', ylabel='Venda');
  plt.savefig("gasolina.png");