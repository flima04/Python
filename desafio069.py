contmaior = 0
conthomens = 0
contmulheres = 0

while True:
    idade = int(input('Qual a sua idade?'))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Qual o seu sexo (F ou M)?')).strip().upper()[0]
    if idade >= 18:
        contmaior += 1
    if sexo == 'M':
        conthomens += 1
    if sexo == 'F' and idade < 20:
        contmulheres += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar (S ou N)?')).strip().upper()[0]
    if resposta == 'N':
        break

print(f'O total de pessoas maiores de idade é: {contmaior}.')
print(f'O total de homens é: {conthomens}.')
print(f'O total de mulheres com menos de 20 anos é: {contmulheres}.')
