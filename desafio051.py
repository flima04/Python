num = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('Os 10 primeiros termos dessa PA são:')

for r in range(0, 10):
    print(num, end=' -> ')
    num += razao
print('ACABOU')
