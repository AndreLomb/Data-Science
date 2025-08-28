import numpy as np

ds = np.loadtxt('space.csv',
                dtype=str,
                delimiter=';',
                encoding='utf8')

#Apresente a porcentagem de missões que deram certo 
missions = ds[1:,7]

total_missions = len(missions)

missions_sucess = np.char.find(missions, 'Success') >= 0

mission_sucess_total = missions_sucess.sum()

mission_mean = mission_sucess_total/total_missions

print(f"{mission_mean*100:.3f}% de missões bem sucedidas\n")

#Qual a media de gastos de uma missão espacial se baseando em missões que possuam valores disponíveis (>0)?
mission_spending = ds[1:,6].astype(float)

valid_spending = mission_spending[mission_spending > 0]

average_spending = valid_spending.mean()

print(f"Houve um gasto médio de {average_spending:.3f} milhões de $\n")

#Encontre quantas missões foram realizadas pelos Estados Unidos (EUA)
american_mission = ds[1:, 2]

is_american_mission = np.char.find(american_mission, 'USA') >= 0

number_missions = is_american_mission.sum()

print(number_missions, 'missões americanas', '\n')

#Encontre a missão mais cara da SpaceX
spacex_mission = ds[ds[:, 1] == 'SpaceX']
spacex_mission_cost = ds[1:, 6]

spacex_mission_cost_float = spacex_mission_cost.astype(float)

max_spacex_mission = spacex_mission[np.argmax(spacex_mission[:, 6].astype(float))]

spacex_name = max_spacex_mission[4]
spacex_cost = max_spacex_mission[6].astype(float)

print('A missão mais cara da SpaceX foi:\n', spacex_name, ';A qual custou ', spacex_cost, ' milhões de $\n')

#Mostre o nome das empresas que já realizaram missões espaciais, juntamente com suas respectivas quantidades de missões (use o for no final para mostrar as informações)

company_missions = ds[1:, 1]

company_sucess = np.unique(company_missions)

for missions_made in company_sucess:
    join = company_missions == missions_made
    num_missions = join.sum()
    print(f"{missions_made} - {num_missions} missão(ões) da empresa")
