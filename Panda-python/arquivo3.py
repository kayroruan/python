#Criando um DataFrame e explorando dados

import pandas as pd
from datetime import date
from datetime import datetime as dt

listaNomes = "Kayro João Lucas Maria Caio".split()
listaCpf = "111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55".split()

dados = list(zip(listaNomes, listaCpf))
meuDf = pd.DataFrame(dados, columns=['nome', 'cpf'])


dataExtracao = date.today()
meuDf['dataExtracao'] = dataExtracao
meuDf['dataExtracao'] = meuDf['dataExtracao'].astype('datetime64[ns]')

print(meuDf)
print(meuDf.info())
