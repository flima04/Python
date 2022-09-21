num = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA:'))
count = 1

print('Os 10 primeiros termos dessa PA são:')
while count <= 10:
    print(num, end=' -> ')
    num += razao
    count += 1
print('ACABOU')