resposta = 0

while resposta != 5:
    num1 = int(input('Digite o primero número'))
    num2 = int(input('Digite o segundo número'))
    print('''O que você deseja fazer com os números?
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    resposta = int(input('Escolha uma das opções acima. '))
    if resposta == 1:
        print('A soma dos números é igual a : ', num1 + num2)
    elif resposta == 2:
        print('A multiplicação dos números é igual a : ', num1 * num2)
    elif resposta == 3:
        print('O maior número é: ', max(num1, num2))
    elif resposta == 4:
        print('Entre com novos números a seguir')
    elif resposta == 5:
        break
    else:
        print('Digite uma opção válida.')

print('--FIM DO PROGRAMA--')