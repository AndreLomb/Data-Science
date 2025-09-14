import numpy as np
import pandas as pd

print('='*40, 'Ex 1', '='*40)

seriesAno1 = {'Java': 16.25, 'C':16.04, 'Python':9.85}
seriesAno2 = {'C':16.21, 'Python':12.12, 'Java':11.68}

s1 = pd.Series(seriesAno1)
s2 = pd.Series(seriesAno2)

print(s1, '\n')
print(s2)

print('='*40, 'Ex 2', '='*40)
print("\nTotal que as 3 linguagens representam em cada ano:")
print(f"Ano 1: {s1.sum():.2f}% | Ano 2: {s2.sum():.2f}%")

print('='*40, 'Ex 3', '='*40)
var_series = s1 - s2
print("Eis a variação de cada linguagem:\n", var_series)

print('='*40, 'Ex 4', '='*40)
print("As linguagens que cresceram nos dois anos foram(foi): \n", var_series[var_series > 0])

print('='*40, 'Ex 5', '='*40)
series_growth = s2 + var_series*2
print("\nProjeção normal:", var_series)
print("A linguagem mais popular, após mais 2 anos, é:", series_growth.nlargest(1))

print('='*40, 'PARTE 2', '='*40)
#criando o dataframe
np.random.seed(10)
df = pd.DataFrame(
index=['A', 'B', 'C', 'D', 'E'],
columns=['W', 'X', 'Y', 'Z'],
data=np.random.randint(1, 50, [5, 4]))
#==========================================================
print('='*40, 'Ex 1', '='*40)
df_X = df['X']
df_X_less_30 = df.loc[df_X < 30, 'X'].mean()
print("\nMédia de elementos de X menores que 30.\n", df_X_less_30)
#==========================================================
print('='*40, 'Ex 2', '='*40)
#para a coluna D:
df_Dmean = df.loc['D'].mean()
print("Média D:", df_Dmean)
#para a coluna E:
df_lineE = df.loc['E'].sum()
print("Soma E:", df_lineE)
#==========================================================
print('='*40, 'Ex 3', '='*40)
slice_ACE_XY = df.loc[['A', 'C', 'E'], ['X', 'Y']]
print(slice_ACE_XY)
linesum_ACE_XY = slice_ACE_XY.sum(axis=1)
print("Soma por linha:\n", linesum_ACE_XY)
columnsum_ACE_XY = slice_ACE_XY.sum(axis=0)
print("Soma por coluna:\n", columnsum_ACE_XY)