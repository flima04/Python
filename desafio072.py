# Tuplas: criar uma tupla com numeros por extenso e ao ler um numero no teclado mostrar por extenso.


extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número de 0 a 20: '))
    while n not in range(0,21):
        n = int(input('Digite um número VÁLIDO de 0 a 20: '))
    print('Você digitou', extenso[n])
    resposta = str(input('Deseja continuar (S ou N)?')).strip().upper()[0]
    if resposta in 'N':
        break
print('---ACABOU---')