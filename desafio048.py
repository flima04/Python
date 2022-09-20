s = 0
conta = 0

for n in range(1, 501, 2):
    if n % 3 == 0:
        s += n
        conta += 1

print('A soma de todos os {} numeros impares multiplos de 3, de 1 até 500 é {}.' .format(conta,s))