
print("===Exercício 1===")
nome1 = input("Meu nome é: ")
print(nome1)
print("Tudo maiúsculo:", nome1.upper())
print("Tudo minúsculo:", nome1.lower())
print("Tem", len(nome1), "letras")
print(nome1.replace('Rocha', 'do Inatel'))

print("===Exercício 2===")
numero = int(input("Qual tabuáda quer ver?"))
comeco = int(input("Escolha o começo da tabuada."))
final = int(input("Escolha o final da tabuada"))

for num in range(comeco, final + 1):
    c = num
    res = numero * c
    print(numero, " * ", c, " = ", res)

print("===Exercício 3===")
sexo = str(input("Qual seu sexo? (M ou F) "))

if sexo == 'M':
    print("Masculino")
elif sexo == 'F':
    print("Feminino")
else:
    print("Sexo inválido")

print("===Exercício 4===")
distance = int(input("Qual foi a distancia percorrida?(Km) "))

if 200 >= distance > 0:
    result = 0.50*distance
    print(result, "pago por viagem curta")
elif distance > 200:
    result = 0.45*distance
    print(result, "pago por viagem intercontinental")

print("===Exercício 5===")

numero = int(input("Digite um número entre 1000 e 9999:"))

while 1000 <= numero <= 9999:
    option = int(input("Escolha(1 a 4):"))
    string_numero = str(numero)
    if option == 1:
        print("Eis a unidade:", string_numero[3])
    elif option == 2:
        print("Eis a dezena:", string_numero[2])
    elif option == 3:
        print("Eis a centena:", string_numero[1])
    elif option == 4:
        print("Eis o milhar:", string_numero[0])
    else: break

print("===Exercício 6===")
import math

numero = float(input("Digite um número decimal:"))
print(f"{numero:.2f}")

print(f"{math.sqrt(numero):.2f} é a raiz do número.")

print(f"{math.ceil(numero)} é a função teto.")

print(f"{math.floor(numero)} é a função chão.")

print(f"{math.trunc(numero)} é a parte inteira.")