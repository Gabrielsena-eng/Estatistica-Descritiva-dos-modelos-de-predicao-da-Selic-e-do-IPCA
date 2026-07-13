import pandas as pd
import matplotlib.pyplot as plt
from dados import extrair_dados_expectativa_selic
from dolar import extrair_dados_dolar

df_cambio_dolar = extrair_dados_dolar()
df_expectativas_selic = extrair_dados_expectativa_selic(10000)


