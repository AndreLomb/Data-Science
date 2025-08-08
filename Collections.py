print("===Exercício 1===")
times = ["Botafogo", "Avaí", "Palmeiras", "Flamengo", "Boca Júniors"]

print("Os três primeiros colocados são:", times[0:3])
print("Os últimos são:", times[3:])
print("Em ordem:", sorted(times))
if "Barcelona" in times:
    print("O Barcelona se encontra na posição:", times.index("Barcelona") + 1)
else:
    print("Time não encontrado.")

print("===Exercício 2===")
loja1 = {'Xiaomi S3', 'Redmi Note 5', 'Samsung Galaxy', 'Motorola G2'}
loja2 = {'Samsung Galaxy', 'Motorola G2', 'Samsung-Haven2', 'Xiaomi S3'}

print(len(loja1), "são todos os celulares da loja 1.")
print("Modelos da loja 1:", loja1)
print(len(loja2), "são todos os celulares da loja 2.")
print("Modelos da loja 2:", loja2)

lojas = loja1 | loja2
print("Estes são todos os modelos disponíveis em ambas as lojas:", lojas)

iguais = loja1 & loja2
print("Estes são os modelos presentes em ambas:", iguais)

model = str(input("Qual modelo está procurando?"))
if model in lojas:
    lojas_disponiveis = []
    if model in loja1:
        lojas_disponiveis.append("Loja 1")
    if model in loja2:
        lojas_disponiveis.append("Loja 2")
    print("O modelo", model, "está disponível nestas lojas!")
    for loja in lojas_disponiveis:
        print("-", loja)
else:
    print("Celular indisponível.")

print("===Exercício 3===")
nome_aluno = str(input("Insira o nome do aluno."))
media = float(input("Insira a média do aluno."))

if media >= 50:
    print("AP")
else:
    print("RP")

dadosAluno = {'nome do aluno': nome_aluno, 'media': media}

print("Eis os dados do aluno:", dadosAluno)

print("===Exercício 4===")
nome = []
peso = []

for n in range(0, 3):
    nome_paciente = str(input("Nome do paciente:"))
    peso_paciente = float(input("Peso do paciente:"))

    nome.append(nome_paciente)
    peso.append(peso_paciente)

print("O paciente mais pesado é:", nome[peso.index(max(peso))])
print("O paciente mais leve é:", nome[peso.index(min(peso))])

print("===Exercício 5===")
lista_individuos = []
idades_sum = 0
menos_20 = 0
num = int(input("Quantas pessoas são? "))
for i in range(num):
    nome_individuo = str(input("Nome: "))
    idade_individuo = int(input("Idade: "))
    idades_sum += idade_individuo

    while True:
        sexo_individuo = str(input("Sexo(M ou F): "))
        if sexo_individuo in ['M', 'F']:
            break
        print("Digite M ou F apenas.")

    if sexo_individuo == 'F' and idade_individuo < 20:
        menos_20 += 1

    individuos = {'nome': nome_individuo,
                  'idade': idade_individuo,
                  'sexo': sexo_individuo}
    lista_individuos.append(individuos)

print(lista_individuos)
media_idades = idades_sum/num
print("Eis a média de idades: ", media_idades)
print("O número de mulheres com menos de 20 anos é:", menos_20)