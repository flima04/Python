nota1 = float(input('Digite a primeira nota'))
nota2 = float(input('Digite a segunda nota'))

media = (nota1 + nota2)/2

if media < 5:
    print('Média abaixo de 5.0. REPROVADO')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('Média acima de 7.0. APROVADO')
