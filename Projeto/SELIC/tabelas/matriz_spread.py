import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from openpyxl.workbook import Workbook
import sys
from pathlib import Path


RAIZ_PROJETO = Path(__file__).resolve().parent.parent.parent

if str(RAIZ_PROJETO) not in sys.path:
    sys.path.append(str(RAIZ_PROJETO))


PASTA_PROJETO = RAIZ_PROJETO / "Projeto"
if str(PASTA_PROJETO) not in sys.path:
    sys.path.append(str(PASTA_PROJETO))


from tabela_de_periodos import df_completo_media

df_erro = pd.DataFrame()

df_erro['Reuniao'] = df_completo_media['Reuniao']

df_erro['Erro_Mes_1'] = df_completo_media['Mes_1'] - df_completo_media['Selic_Real']
df_erro['Erro_Mes_3'] = df_completo_media['Mes_3'] - df_completo_media['Selic_Real']
df_erro['Erro_Mes_5'] = df_completo_media['Mes_5'] - df_completo_media['Selic_Real']

print(df_erro)



tabela_erro = df_erro.copy()

tabela_erro = tabela_erro.rename(columns={
    'Reuniao' : 'Reunião',
    'Erro_Mes_5': '5 Meses Antes',
    'Erro_Mes_3': '3 Meses Antes',
    'Erro_Mes_1': '1 Mês Antes'
})
tabela_erro.index.name = 'Reunião'


colunas_valores = ['5 Meses Antes', '3 Meses Antes', '1 Mês Antes']
tabela_erro = tabela_erro[['Reunião'] + colunas_valores]


tabela_estilizada = tabela_erro.style\
    .hide(axis='index')\
    .background_gradient(cmap='vlag', axis=None, vmin=-1, vmax=1, subset=colunas_valores)\
    .format("{:+.2f}", subset=colunas_valores)\
    .set_caption("Spread de Previsão da Selic (Mercado vs Realidade)")\
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

with open('matriz_erro_selic.html', 'w', encoding='utf-8') as f:
    f.write(tabela_estilizada.to_html())

print("Matriz corrigida e exportada com sucesso!")