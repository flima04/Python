soma = maior = menor = num = int(input('Digite um número: '))
cont = 1
resposta = str(input('Deseja continuar? S ou N?: '))


while resposta in 'Ss':
    num = int(input('Digite o próximo número: '))
    soma += num
    cont += 1
    if maior < num:
        maior = num
    elif menor > num:
        menor = num
    resposta = str(input('Deseja continuar? S ou N?: '))

print('Você saiu do laço.')
print('A média de todos os número é igual a {}.' .format(soma/cont))
print('O maior número digitado foi {}.' .format(maior))
print('O menor número digitado foi {}.' .format(menor))
