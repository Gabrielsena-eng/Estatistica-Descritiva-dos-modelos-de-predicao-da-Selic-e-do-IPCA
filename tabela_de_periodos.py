import pandas as pd

from expecativa_selic_intervalo import expectativas_intervalo_selic
from Indices.selic import df_selic_resumo


df_para_merge = df_selic_resumo[['Reuniao', 'Selic_Real']]

def compilar_dados_selic(Quantidade_reuniao):
  lista_dfs = []
  for i in range(1, Quantidade_reuniao + 1):
    reuniao = f"R{i}/2026"
    
    for j in range(1, 6, 2):
      df_temp = expectativas_intervalo_selic(j, reuniao, 15)
      df_temp['Mes_Expectativa'] = f"Mes_{j}"

      lista_dfs.append(df_temp)


    
  df_central = pd.concat(lista_dfs, ignore_index=True)
  df_merge = pd.merge(df_central, df_para_merge, on="Reuniao", how="left")
  df_merge = df_merge[['Reuniao', 'Media', 'Mes_Expectativa', 'Selic_Real']]
  return df_merge

df_completo = compilar_dados_selic(5)
print(df_completo)


def tabela_resumo_tempo_selic (Quantidade_reuniao):
    dados = []
    

    for i in range(1, Quantidade_reuniao + 2):
     reuniao = f"R{i}/2026"
     linha = {'Reuniao': reuniao}
     

     for j in range(1, 6, 2):
       media =  "{:.2f}".format(expectativas_intervalo_selic(j, reuniao, 1)['Media'].mean())
       linha[f'Mes_{j}'] = media

     dados.append(linha)


    df_merge = pd.merge(pd.DataFrame(dados), df_para_merge, on='Reuniao', how='inner')
    df_merge = df_merge[['Reuniao', 'Selic_Real', 'Mes_1', 'Mes_3', 'Mes_5' ]]
    return df_merge

