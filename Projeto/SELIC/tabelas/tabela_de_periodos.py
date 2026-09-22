import pandas as pd
import sys
from pathlib import Path
import dataframe_image as dfi

RAIZ_PROJETO = Path(__file__).resolve().parent.parent.parent

if str(RAIZ_PROJETO) not in sys.path:
    sys.path.append(str(RAIZ_PROJETO))

PASTA_PROJETO = RAIZ_PROJETO / "Projeto"
if str(PASTA_PROJETO) not in sys.path:
    sys.path.append(str(PASTA_PROJETO))


from SELIC.expectativas.expecativa_selic_intervalo import expectativas_intervalo_selic
from Indices.selic import df_selic_resumo  

df_para_merge = df_selic_resumo[['Reuniao', 'Selic_Real']]
print(df_para_merge)

def compilar_dados_selic(Quantidade_reuniao):
  lista_dfs = []
  for i in range(1, Quantidade_reuniao + 1):
    reuniao = f"R{i}/2026"
    
    for j in range(1, 6, 2):
      df_temp = expectativas_intervalo_selic(j, reuniao, 7)
      df_temp['Mes_Expectativa'] = f"Mes_{j}"

      lista_dfs.append(df_temp)


    
  df_central = pd.concat(lista_dfs, ignore_index=True)
  df_merge = pd.merge(df_central, df_para_merge, on="Reuniao", how="left")
  df_merge = df_merge[['Reuniao', 'Media', 'Mes_Expectativa', 'Selic_Real', 'Data']]
  return df_merge

df_completo = compilar_dados_selic(5)




def tabela_resumo_tempo_selic (Quantidade_reuniao):
    dados = []
    

    for i in range(1, Quantidade_reuniao + 1):
     reuniao = f"R{i}/2026"
     linha = {'Reuniao': reuniao}
     

     for j in range(1, 6, 2):
       media =  "{:.2f}".format(expectativas_intervalo_selic(j, reuniao, 7)['Media'].mean())
       linha[f'Mes_{j}'] = float(media)
       

     dados.append(linha)


    df_merge = pd.merge(pd.DataFrame(dados), df_para_merge, on='Reuniao', how='inner')
    df_merge = df_merge[['Reuniao', 'Selic_Real', 'Mes_1', 'Mes_3', 'Mes_5' ]]

    
    return df_merge

df_completo_media = tabela_resumo_tempo_selic(6)
dfi.export(df_completo_media, "tabela_media_SELIC.png")

