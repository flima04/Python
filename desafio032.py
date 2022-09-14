ano = int(input('Digite um ano e direi se ele pe bissexto.'))

if ano%2==0 and ano%100!=0 or ano%400==0:
    print('Ano Bissexto')
else:
    print('Ano Não Bissexto')