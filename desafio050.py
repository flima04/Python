s = 0

for r in range(0,6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        s += n

print('A somo dos numeros pares dessa sequencia é igual a {}.' .format(s))