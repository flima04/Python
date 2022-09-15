s = 0

for n in range(1, 501):
    if n % 3 == 0:
        s += n

print('A soma de todos os numeros impares multiplos de 3, de 1 até 500 é {}.' .format(s))