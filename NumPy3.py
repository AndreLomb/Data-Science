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
    if 'Success' in n:
        count += 1;

print(count, 'missões deram certo')

#Qual a media de gastos de uma missão espacial se baseando em missões que possuam valores disponíveis (>0)?
#*Correto, talvez
ds2 = ds[:,6]
ds_cost = ds2[1:]
ds_cost_float = ds_cost.astype(float)

ds_cost_viavel = ds_cost_float[ds_cost_float>0]

print('\nCusto médio das expedições viáveis:', ds_cost_viavel.mean(), '\n')

#Encontre qual foi a missão mais cara realizada pelos Estados Unidos (EUA)
#!!refazer
dsUSA = ds[:,1]
dsUSAMission = ds[:,4]
dsUSACost = ds[:,6]

condUSA = dsUSA == 'USA'

#!!PROBLEMA AQUI
condUSACost = dsUSACost[1:][condUSA[1:]].astype(float)
maxUSACost = condUSACost.max()
usaIndex = maxUSACost.argmax()

usaMissionName = dsUSAMission[1:][condUSA[1:]][usaIndex]

#print('Missão mais cara dos EUA:', usaMissionName, 'de custo:', maxUSACost)

#Encontre a missão mais cara da SpaceX
dsCompanyName = ds[:,1]
dsCompanyCost = ds[:,6]
dsMissionName = ds[:,4]

condSpaceX = dsCompanyName == 'SpaceX'

#!!PROBLEMA AQUI
condCostSpaceX = dsCompanyCost[1:][condSpaceX[1:]].astype(float)
maxCostSpace = condCostSpaceX.max()
costIndex = maxCostSpace.argmax()

missionName = dsMissionName[1:][condSpaceX[1:]][costIndex]

#print('Missão mais cara:', missionName, 'de custo:' ,maxCostSpace)

#Mostre o nome das empresas que já realizaram missões espaciais, juntamente com suas respectivas quantidades de missões (use o for no final para mostrar as informações)
#*nome, quantidade, status