import numpy as np

ds = np.loadtxt('space.csv',
                dtype=str,
                delimiter=';',
                encoding='utf8')

#Apresente a porcentagem de missões que deram certo 
missions = ds[1:,7]

missions_sucess = np.char.find(missions, 'Success') >= 0

count_missions = missions_sucess.sum()

print(count_missions, 'missões deram certo\n')

#Qual a media de gastos de uma missão espacial se baseando em missões que possuam valores disponíveis (>0)?
mission_spending = ds[1:,6]

mission_spending_float = mission_spending.astype(float)

average_spending = mission_spending_float.mean()

print('A média de gastos foi de:', average_spending, '\n')

#Encontre quantas missões foram realizadas pelos Estados Unidos (EUA)
american_mission = ds[1:, 2]

is_american_mission = np.char.find(american_mission, 'USA') >= 0

number_missions = is_american_mission.sum()

print(number_missions, 'missões feitas pelos EUA', '\n')

#Encontre a missão mais cara da SpaceX



#Mostre o nome das empresas que já realizaram missões espaciais, juntamente com suas respectivas quantidades de missões (use o for no final para mostrar as informações)
