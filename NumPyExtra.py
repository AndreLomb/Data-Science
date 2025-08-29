import numpy as np

ds = np.loadtxt('paises.csv',delimiter=';',dtype=str,encoding='utf-8')

#1) Faça um slicing no dataset para mostrar apenas o País (Country), Região (Region), População (Population) e Area (Area (sq. mi.)) dos países contidos nele;

country = ds[1:, 0]
region = ds[1:, 1]
pop = ds[1:, 2]
area = ds[1:, 3]

print('===Ex1===')

print('Países\n', country)
print('\nregion\n', region)
print('\npop\n', pop)
print('\narea\n', area)

print('===EX2===')

#2) Conte e em seguida mostre quais são as diferentes Regiões do planeta segundo este dataset;

region_unique = np.unique(region)
print('O dataset possui', len(region_unique), 'regiões')
#3) Mostre qual a taxa média de alfabetização (Literacy (%)) do planeta segundo este dataset;
print('===Ex3===')
alfabet = ds[1:, 9].astype(float)
print(f"A média de alfabetização mundial é de: {alfabet.mean():.3f}")

#4) Conte quantas regiões são da América do Norte (NORTHERN AMERICA) segundo este dataset;
print('===Ex4===')
region_america = np.char.find(region, 'NORTHERN AMERICA') >= 0
print(region_america.sum(), 'é o numero de regiões que pertencem à américa do norte.')

#5) Encontre qual país da América do Sul e Caribe (LATIN AMER. & CARIB) possui a maior renda per capita (GDP ($ per capita));
print('===Ex5===')
gdp = ds[1:, 8].astype(float)

latam_gdp_max = gdp[region == 'LATIN AMER. & CARIB    ']

latam_country = country[np.argmax(latam_gdp_max)]
print(latam_country, 'é o maior GDP da da região LATIN AMER. & CARIB;', latam_gdp_max.max(), 'é o seu gdp')