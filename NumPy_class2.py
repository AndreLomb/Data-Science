import numpy as np
ds = np.loadtxt('space.csv', 
                delimiter=';', 
                dtype=str, 
                encoding='utf-8')
#print(ds)

#colunas do dataset
#print(ds[0, :])

#calculando a média de gastos das missões
print(ds[0, :])

#slicing para extrair a coluna custo
ds_cost = ds[:, 6]

print('\n', 'Custo médio de cada missão:', ds_cost[1:]) #[1:] para ignorar o cabeçalho (printa strings)

#transformando em float
ds_cost_float = ds_cost[1:].astype(float)
print('\n', 'Custo médio de cada missão (float):', ds_cost_float)
print('\n', 'Custo médio das três primeiras missões(float)', ds_cost_float[0:4]) 
#[0:4] para pegar as três primeiras missões
#média de custo das missões
print('\n', ds_cost_float.mean())