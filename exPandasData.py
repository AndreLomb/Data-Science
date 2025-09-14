import numpy as np
import pandas as pd
dfPaises = pd.read_csv('paises.csv',
                       delimiter=';',
                       encoding='utf-8')

#calculando a população mundial
total_population = np.sum(dfPaises['Population'])
#fazendo um broadcasting para calcular a % da população de cada país
seriesPercPopulation = (dfPaises['Population']/total_population)*100
# adicionando uma nova coluna no Dataset contendo esta informação
# veja como é simples adicionar uma nova coluna no DataFrame
dfPaises['% Population'] = np.round(seriesPercPopulation, 3)
# salvando um novo arquivo com esta atualização
dfPaises.to_csv('paises_v2.csv', sep=';')