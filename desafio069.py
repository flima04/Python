sexo = ''
idade = 0
resposta = 'S'

contmaior = 0
conthomens = 0
contmulheres = 0

while resposta == 'S':
    sexo = str(input('Qual o seu sexo (F ou M)?')).strip().upper()[0]
    idade = int(input('Qual a sua idade?'))
    print(sexo, idade)
    if idade >= 18:
        contmaior += 1
    elif sexo == 'M':
        conthomens += 1
    elif sexo == 'F' and idade < 20:
        contmulheres += 1
    resposta = str(input('Deseja continuar (S ou N)?')).strip().upper()[0]

print(f'O total de pessoas maiores de idade é: {contmaior}.')
print(f'O total de homens é: {conthomens}.')
print(f'O total de mulheres com menos de 20 anos é: {contmulheres}.')
