idadesoma = 0
maioridadehomem = 0
homemvelho = ''
totalmulher20 = 0


for r in range(1, 5):
    print('---- {}ª PESSOA ----' .format(r))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (F/M)')).strip()
    idadesoma += idade
    if r == 1 and sexo in ('Mm'):
        maioridadehomem = idade
        homemvelho = nome
    elif sexo in ('Mm') and idade > maioridadehomem:
        maioridadehomem = idade
        homemvelho = nome
    elif sexo in ('Ff') and idade < 20:
        totalmulher20 += 1


idademedia = idadesoma/4
print('A média de idade do grupo é igual a: {}.' .format(idademedia))
print('O homem mais velho se chama {}.' .format(homemvelho))
print('O total de mulher com menos de 20 anos é igual a: {}.' .format(totalmulher20))
