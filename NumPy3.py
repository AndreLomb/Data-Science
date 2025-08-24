import numpy as np

ds = np.loadtxt('space.csv',
                dtype=str,
                delimiter=';',
                encoding='utf8')

#Apresente a porcentagem de missões que deram certo 
ds_sucess = ds[:,7]
print(ds_sucess[1:])

count = 0;

for n in ds_sucess:
    if 'Success' in ds_sucess:
        count += 1;

print(count, 'missões deram certo')


#Qual a media de gastos de uma missão especial se baseando em missões que possuam valores disponíveis (>0)?
ds = ds[:,6]
ds_cost = ds[1:]
ds_cost_float = ds_cost.astype(float)

ds_cost_viavel = ds_cost_float[ds_cost_float>0]

print('Custo médio das expedições viáveis:', ds_cost_viavel.mean())