import pandas as pd


from expectativas_selic import df_expectativas_selic

def expectativas_intervalo_selic(meses, reuniao):

    df_expectativas_selic_= df_expectativas_selic[(df_expectativas_selic['Reuniao'] == reuniao)]
    ultima_atualizacao = df_expectativas_selic_['Data'].max()
    primeira_atualizacao_intervalo = ultima_atualizacao - pd.DateOffset(months=meses)
    df_expectativas_intervalo = df_expectativas_selic_[(df_expectativas_selic_['Data'] > primeira_atualizacao_intervalo)]

    return df_expectativas_intervalo
    

r1 = "R1/2026"

print("========================== 5 MESES")
df_R1_5_meses = expectativas_intervalo_selic(5,r1)
print(df_R1_5_meses)

print("========================== 3 MESES")
df_R1_3_meses = expectativas_intervalo_selic(3,r1)
print(df_R1_3_meses)

print("========================== 1 MESES")
df_R1_1_meses = expectativas_intervalo_selic(1,r1)
print(df_R1_1_meses)

