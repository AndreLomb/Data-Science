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

print('===Ex 3===')
#criar um array 2x2
mtz = np.array[[[0, 0], [0, 0]]]
print('Matriz original:\n', mtz)

linha_bomba = np.random.randint(0, 2)
coluna_bomba = np.random.randint(0, 2)
mtz[linha_bomba, coluna_bomba] = 1

jogadas_feitas = 0
max_jogadas = 3
posicoes_reveladas = [[False, False], [False, False]]

while jogadas_feitas < max_jogadas:
    print(f'\n--- Jogada {jogadas_feitas + 1} de {max_jogadas} ---')

    print('\nEscolha uma posição para revelar:')
    linha = input('insira a linha (0 ou 1): ')
    coluna = input('insira a coluna (0 ou 1): ')

    if linha not in ['0', '1'] or coluna not in ['0', '1']:
        print('apenas 0 ou 1')
        continue

    linha = int(linha)
    coluna = int(coluna)

    if posicoes_reveladas[linha][coluna]:
        print('posição já revelada')
        continue

    posicoes_reveladas[linha][coluna] = True
    jogadas_feitas += 1
    valor_revelado = matriz[linha][coluna]

    print(f'Posição [{linha}, {coluna}] revelada: {valor_revelado}')

    if valor_revelado == 1:
        print('Game Over! :( Try again!')
        break
    
    posicoes_seguras_encontradas = 0
    for i in range(2):
        for j in range(2):
            if matriz[i][j] == 0 and posicoes_reveladas[i][j]:
                posicoes_seguras_encontradas += 1

    if posicoes_seguras_encontradas == 3:
        print('Congratulations! You beat the game! :)')
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