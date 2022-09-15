num = int(input('Digite um número inteiro.'))

print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal''')

opção = int(input('Sua opção é: '))

if opção == 1:
    print('O número {} convertido para binário é igual a: {}' .format(num, bin(num)))
elif opção == 2:
    print('O número {} convertido para octal é igual a: {}' .format(num, oct(num)))
elif opção == 3:
    print('O número {} convertido para hexadecimal é igual a: {}' .format(num, hex(num)))
else:
    print('Digite uma opção válida!')
