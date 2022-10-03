pares = []
impares = []
lista = []
for r in range(0,7):
    num = int(input('Digite o {}º valor: ' .format(r+1)))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    if r == 6:
        sorted(pares)
        sorted(impares)
        lista.append(pares[:])
        lista.append(impares[:])
print('-=' * 30)
print(f'Os números pares digitados foram {lista[0]}.')
print(f'Os números ímpares digitados foram {lista[1]}.')