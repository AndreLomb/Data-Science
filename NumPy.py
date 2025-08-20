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
