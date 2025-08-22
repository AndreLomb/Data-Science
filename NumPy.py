import numpy as np

print('===Ex 1===')

arr1 = np.ones(8)
arr2 = np.random.randint(0, 9, 8)
arr3 = arr1 + arr2

print(arr1)
print(arr2)

if arr3.sum() > 40:
    matriz = arr3.reshape(4, 2)
    print('Eis a nova matriz linha: \n', matriz)
else:
    matriz = arr3.reshape(2, 4)
    print('Eis a nova matriz coluna: \n', matriz)

print('===Ex 2===')

arrEven = np.arange(0, 51, 2)
arrEven2 = np.arange(100, 50, -2) 

arr_concat = np.concatenate((arrEven, arrEven2))

print('Array concatenado:', arr_concat)

arr_order = np.sort(arr_concat)

print('Array ordenado:', arr_order)

print('===Ex 2===')
# criar um array 2x2
mtz = np.zeros(4).reshape(2, 2)
print('Matriz original:\n', mtz)

linha_bomba = np.random.randint(0, 2)
coluna_bomba = np.random.randint(0, 2)

mtz[linha_bomba, coluna_bomba] = 1

visivel = np.array([['?', '?'], ['?', '?']])

attempts = 0
max_attempts = 3

for tentativa in range(max_attempts):
    print(f'\nTentativa {tentativa + 1}/{max_attempts}===')
    print(visivel)

    l = int(input('Insira a linha(0-1): '))
    c = int(input('Insira a coluna(0-1): '))

    if visivel[l, c] != '?':
        print('position revealed already!!')
        continue

    if l == linha_bomba and c == coluna_bomba:
        visivel[l, c] = 'X'
        print('Game Over! :( Try again!')
        break
    else:
        visivel[l, c] = '0'
        print('safe')
        attempts += 1

    print('\nCampo atual:')
    print(visivel)

    if attempts == max_attempts or visivel[l, c] == 'X':
        print('You win! :)')
        break   

print('=== Ex 3 ===')
arr  = np.arange(0, 50, 2)
mtz_any = arr.reshape(5, 5)
# arr = np.arange(0, 18, 3)
# mtz_any = arr.reshape(2, 5)
# "O vetor é par"
#mostrar as linhas e colunas da matriz
print('Array original:\n', arr)
print('Matriz feita:\n', mtz_any)

print('Linhas:', mtz_any.shape[0])
print('Colunas:', mtz_any.shape[1])

linhas = mtz_any.shape[0]
colunas = mtz_any.shape[1]

multi = linhas * colunas
print('linhas * colunas:', multi)

if multi % 2 == 0:
    print('O vetor é par')
elif multi % 2 != 0:
    print('O vetor é impar')
    
print('=== Ex 4 ===')    
seed_rand = np.random.seed(10)
arr_4x4 = np.random.randint(1, 51, 16)
mtz_4x4 = arr_4x4.reshape(4, 4)
print('matriz:\n', mtz_4x4)

#media de cada linha da matriz 4x4
media_linhas = np.mean(mtz_4x4, axis=1)
print('\nMédia de cada linha:', media_linhas)

#media de cada coluna da matriz 4x4
media_colunas = np.mean(mtz_4x4, axis=0)
print('\nMedia de cada coluna:', media_colunas)

print('\nMaior número da média de linhas:', media_linhas.max())

print('\nMaior número da média colunas:', media_colunas.max())

valores, contagens = np.unique(mtz_4x4, return_counts=True)

print(f"\nc) Contagem de aparições:")
for valor, count in zip(valores, contagens):
    print(f"Número {valor}: aparece {count} vez(es)")

numeros_2_vezes = valores[contagens == 2]
print(f"\nNúmeros que aparecem 2 vezes: {numeros_2_vezes}")