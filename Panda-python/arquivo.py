#Criação de Séries com Pandas

import pandas as pd

pd.Series(data=5)

listaNomes = "Kayro João Lucas Maria Caio".split()

pd.Series(listaNomes)

dados = {
    'nome1' : 'Kayro',
    'nome2' : 'João',
    'nome3' : 'Lucas',
    'nome4' : 'Maria',
    'nome5' : 'Caio',
}

pd.Series(dados)