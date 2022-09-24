a = 0
b = 1
c = 0
count = 0


count = int(input('Digite um número: '))

while count <= 0:
    if count <= 0:
        print('Entrada inválida! Digite um numero inteiro maior que 0.')
    elif count > 0:
        print('A sequência para o(s) {} primeiro(s) termo(s) é:' .format(count))
if count == 1:
    print(a, end=' -> ')
    count -= 1
elif count == 2:
    print(a, end=' -> ')
    count -= 1
    print(b, end=' -> ')
    count -= 1

while count > 0:
    print('A sequência para o(s) {} primeiro(s) termo(s) é:' .format(count))
    print(a, end=' -> ')
    count -= 1
    print(b, end=' -> ')
    count -= 1
    while count > 0:
        c = a + b
        a = b
        b = c
        print(c, end=' -> ')
        count -= 1

print('ACABOU')
