import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

from selic import extrair_dados_expectativa_selic
from dolar import extrair_dados_dolar

df_cambio_dolar = extrair_dados_dolar()
df_expectativas_selic = extrair_dados_expectativa_selic(10000)


#juntar os df's utilizando o merge

df_mesclado = pd.merge(df_cambio_dolar, df_expectativas_selic, on='Data', how='left')
df_mesclado = df_mesclado.ffill()
print(df_mesclado)

df_modelo = df_mesclado.dropna(subset=['Media', 'cotacaoVenda'])


Y = df_modelo['cotacaoVenda']
X = df_modelo['Media']
X = sm.add_constant(X)
modelo = sm.OLS(Y, X).fit()

print(modelo.summary())

plt.figure(figsize=(10, 6)) 
plt.scatter(df_modelo['Media'], df_modelo['cotacaoVenda'], alpha=0.5, color='blue', label='Dados Reais')


Y_predito = modelo.predict(X)
plt.plot(df_modelo['Media'], Y_predito, color='red', linewidth=2, label='Linha de Regressão OLS')


plt.title('Impacto da Expectativa Selic na Cotação do Dólar', fontsize=14)
plt.xlabel('Expectativa Selic (%)', fontsize=12)
plt.ylabel('Cotação Dólar (R$)', fontsize=12)

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()


