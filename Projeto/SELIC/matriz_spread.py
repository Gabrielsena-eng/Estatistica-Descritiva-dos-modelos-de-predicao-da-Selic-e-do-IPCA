import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from openpyxl.workbook import Workbook
import sys
from pathlib import Path

# (Subindo de 'tabela_de_periodos.py' -> 'resumos' -> 'Projeto' -> Raiz)
RAIZ_PROJETO = Path(__file__).resolve().parent.parent

if str(RAIZ_PROJETO) not in sys.path:
    sys.path.append(str(RAIZ_PROJETO))

# Adiciona também a pasta 'Projeto' para buscas internas
PASTA_PROJETO = RAIZ_PROJETO / "Projeto"
if str(PASTA_PROJETO) not in sys.path:
    sys.path.append(str(PASTA_PROJETO))


from tabelas.tabela_de_periodos import df_completo

df_completo['Erro_Previsao'] = df_completo['Media'] - df_completo['Selic_Real']

tabela_erro = df_completo.pivot_table(
    index='Reuniao', 
    columns='Mes_Expectativa', 
    values='Erro_Previsao'
)

# 3. Força a ordem cronológica exata das colunas
tabela_erro = tabela_erro[['Mes_5', 'Mes_3', 'Mes_1']]

# 4. Aplica a estilização nativa do Pandas (Formatação Condicional)
# Vermelho = superestimou, Azul = subestimou.
tabela_estilizada = tabela_erro.style\
    .background_gradient(cmap='vlag', axis=None, vmin=-2, vmax=2)\
    .format("{:+.2f}")\
    .set_caption("Spread de Previsão da Selic (Mercado vs Realidade)")\
    .set_table_styles([{
        'selector': 'caption',
        'props': [('font-size', '16px'), ('font-weight', 'bold'), ('color', '#1C1C1C'), ('margin-bottom', '10px')]
    }, {
        'selector': 'th',
        'props': [('background-color', '#1B3B6F'), ('color', 'white'), ('text-align', 'center'), ('padding', '10px')]
    }, {
        'selector': 'td',
        'props': [('text-align', 'center'), ('font-weight', 'bold'), ('padding', '10px'), ('border', '1px solid white')]
    }])

with open('matriz_erro.html', 'w', encoding='utf-8') as f:
    f.write(tabela_estilizada.to_html())

tabela_estilizada.to_excel('matriz_erro.xlsx', engine='openpyxl')
