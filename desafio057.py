# Uso do while começa aqui
# Programa que leia o sexo de uma pessoa e so aceite F ou M

sexo = str(input('Digite seu sexo (F/M).')).strip().upper()[0]


while sexo not in 'FM':
    sexo = str(input('Entrada inválida. Digite seu sexo (F/M).')).strip().upper()
if sexo == 'F':
    print('Usuário do sexo Feminino')
elif sexo == 'M':
    print('Usuário do sexo Masculino')
