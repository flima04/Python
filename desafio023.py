# Ler um numero e mostra as unidades, dezenas, centenas e milhares.
num = int(input('Digite um número de 0 a 9999'))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10


print('Unidade(s): {}' .format(u))
print('Dezena(s): {}' .format(d))
print('Centena(s): {}' .format(c))
print('Milhar(es): {}' .format(m))
