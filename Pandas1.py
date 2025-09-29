import numpy as np
import pandas as pd

indices = ['a','b', 'c']
valores = [1, 2, 3]
dic1 = {'a':10, 'b':20, 'c':30}
dic2 = {'a':10, 'b':20, 'd':40}

#CRIANDO E MOSTRANDO UMA SERIES
#series = pd.Series(data=valores, index=indices)
series = pd.Series(dic1)
series2 = pd.Series(dic2)
#print(series)
#print(type(series))
#print(series['a'])
#OPERAÇÕES ENTRE SERIES
#print(series + series2)
#print(series - series2)

print(series.add(series2, fill_value=0)) #fazendo soma COM VALOR PADRÃO
print(series.sub(series2, fill_value=0)) #fazendo subtração COM VALOR PADRÃO

#CONDICIONAIS NO PANDAS
print(series[series <= 20])

print('='*40)
print('PANDAS DATAFRAME')
np.random.seed(10)
df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [5,4])
)
print(df, '\n')
print('='*40)
#fazendo slicing com iloc(Padrão numpy - índices numéricos)
print(df.iloc[0:2, :])
#fazendo slicing com loc
print(df.loc[['A', 'B'], ['W', 'X', 'Y', 'Z']], '\n')
print(df.loc[['A', 'B'], ['W','Y']])
print('\n', df[['W', 'Y']])
