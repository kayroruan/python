#Informação de dados listados

import pandas as pd

print("Dados gerais:")
serieDados = pd.Series([10.2, -1, None, "quinze", 23.4, "quinze"])
print("Qtd ", serieDados.shape)
print("Type ", serieDados.dtype)
print("Valor Unc? ", serieDados.is_unique)
print("Valor Nulo? ", serieDados.hasnans)
print("Qtd Valores ", serieDados.count())

print("Dados numéricos:")
serieDados2 = pd.Series([12, 24, 46, 74, 8, 9])
print("menor ", serieDados2.min())
print("maior ", serieDados2.max())
print("média ", serieDados2.mean())
print("desvio ", serieDados2.std())
print("mediana ", serieDados2.median())
print("resumo ", serieDados2.describe())