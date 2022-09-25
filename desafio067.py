#Tabuada com while
from time import sleep

while True:
    print('-=' * 10)
    print('------TABUADA------')
    print('-=' * 10)
    num = int(input('Digite um número: '))
    if num < 0:
        break
    for n in range(1,11):
        print(f'{num} x {n:2} = {num*n}')
    sleep(1)

print('-=' *5, 'FIM', '=-' *5)