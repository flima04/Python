soma = 0
resposta = int(input('Digite um número inteiro para que eu vá somando ao montante ou digite 999 para sair e exibir o resultado: '))

while resposta != 999:
    soma += resposta
    resposta = int(input('Digite o próximo número ou digite 999 para sair: '))

print('Você saiu do laço. A soma de todos os números digitados é igual a {}' .format(soma))