resultado = 1

n = int(input('Digite um número: '))

print('{}! =' .format(n), end=' ')

for r in range(n, 0, -1):
    resultado *= r
    if r != 1:
        print(r, end=' x ')
    else:
        print(r, end=' = ')

print(resultado)