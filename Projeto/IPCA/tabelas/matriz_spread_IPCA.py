import pandas as pd
import seaborn as sns
import sys
from pathlib import Path
import dataframe_image as dfi



diretorio_projeto = Path(__file__).resolve().parent.parent
if str(diretorio_projeto) not in sys.path:
    sys.path.append(str(diretorio_projeto))

from intervalos.media_intervalos import media_intervalos_IPCA    

df_completo_media = media_intervalos_IPCA()
df_completo_media['DataReferencia'] = pd.to_datetime(df_completo_media['DataReferencia']).dt.strftime('%m/%Y')
df_erro = pd.DataFrame()


df_erro['DataReferencia'] = df_completo_media['DataReferencia']

df_erro['Erro_Mes_1'] = df_completo_media['Mes_1'] - df_completo_media['IPCA_Real']
df_erro['Erro_Mes_3'] = df_completo_media['Mes_3'] - df_completo_media['IPCA_Real']
df_erro['Erro_Mes_5'] = df_completo_media['Mes_5'] - df_completo_media['IPCA_Real']


print(df_erro)



tabela_erro = df_erro.copy()

tabela_erro = tabela_erro.rename(columns={
    'DataReferencia' : 'Mês inflação',
    'Erro_Mes_5': '5 Meses Antes',
    'Erro_Mes_3': '3 Meses Antes',
    'Erro_Mes_1': '1 Mês Antes'
})
tabela_erro.index.name = 'Mês inflação'


colunas_valores = ['5 Meses Antes', '3 Meses Antes', '1 Mês Antes']
tabela_erro = tabela_erro[['Mês inflação'] + colunas_valores]


tabela_estilizada = tabela_erro.style\
    .hide(axis='index')\
    .background_gradient(cmap='vlag', axis=None, vmin=-0.20, vmax=0.20, subset=colunas_valores)\
    .format("{:+.2f}", subset=colunas_valores)\
    .set_caption("Spread de Previsão do IPCA (Mercado vs Realidade)")\
    .set_table_styles([{
        'selector': 'caption',
        'props': [
            ('font-size', '18px'), 
            ('font-weight', 'bold'), 
            ('font-family', 'Arial, Helvetica, sans-serif'), 
            ('color', '#1C1C1C'), 
            ('margin-bottom', '15px')
        ]
    }, {
        'selector': 'th',
        'props': [
            ('background-color', '#1B3B6F'), 
            ('color', 'white'), 
            ('font-family', 'Arial, Helvetica, sans-serif'), 
            ('text-align', 'center'), 
            ('padding', '12px 25px'),
            ('border', '1px solid #8B9BB4') 
        ]
    }, {
        'selector': 'td',
        'props': [
            ('font-family', 'Arial, Helvetica, sans-serif'), 
            ('text-align', 'center'), 
            ('font-weight', 'bold'), 
            ('padding', '12px 25px'), 
            ('border', '1px solid #8B9BB4') 
        ]
    }, {
        'selector': 'td:first-child',
        'props': [
            ('background-color', '#2A4D87'), 
            ('color', 'white')               
        ]
    }])

dfi.export(tabela_estilizada, 'heatmap_ipca.png', dpi=300)

print("Matriz corrigida e exportada com sucesso!")