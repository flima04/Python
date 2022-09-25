# Caixa eletronico

valor = int(input('Digite o valor a ser sacado: '))
cedulas50 = cedulas20 = cedulas10 = cedulas1 = 0


resto50 = valor % 50
cedulas50 = (valor - resto50) / 50
resto20 = resto50 % 20
cedulas20 = (resto50 - resto20) / 20
resto10 = resto20 % 10
cedulas10 = (resto20 - resto10) / 10
cedulas1 = resto10

if cedulas50 != 0:
    print(f'Total de {cedulas50} cedulas de R$50,00.')
if cedulas20 != 0:
    print(f'Total de {cedulas20} cedulas de R$20,00.')
if cedulas10 != 0:
    print(f'Total de {cedulas10} cedulas de R$10,00.')
if cedulas1 != 0:
    print(f'Total de {cedulas1} cedulas de R$1,00.')