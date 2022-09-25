# par ou impar com while
from random import randint

print('-=-=-=VAMOS JOGAR PAR OU ÍMPAR?=-=-=-')

while True:
    numpc = randint(0,11)
    numuser = int(input('Digite um número de 0 a 10: '))
    opçãouser = str(input('Você quer par ou ímpar (P ou I)?')).upper().strip()[0]
    soma = numpc + numuser
    imparpar = ''
    descritivo = ''
    if soma % 2 == 0:
        imparpar = 'P'
        descritivo = 'PAR'
    else:
        imparpar = 'I'
        descritivo = 'ÍMPAR'
    resultado = ''
    if opçãouser == imparpar:
        resultado = 'VENCEU'
    else:
        resultado = 'PERDEU'
    print('-' * 40)
    print(f'Você jogou {numuser}, o PC {numpc}. Total de {soma}, um número {descritivo}.')
    print('-' * 40)
    print(f'VOCÊ {resultado}!')
    print('-=' * 20)
    if resultado == 'PERDEU':
        break
    else:
        print('Vamos jogar novamente?')
        print('-=' * 20)

print('------------FIM------------')