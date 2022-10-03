lista = []

for r in range(0,5):
    lista.append(int(input('Digite um numero: ')))
    if r == 0:
        maior = menor = lista[r]
    else:
        if lista[r] > maior:
            maior = lista[r]
        if lista[r] < menor:
            menor = lista[r]

print(f'O maior número digitado foi {maior}, que se encontra nas posições ', end='')
for p, v in enumerate(lista):
    if v == maior:
        print(f'{p}... ', end='')
print()
print(f'O menor número digitado foi {menor}, que se encontra nas posiçoes ', end='')
for p, v in enumerate(lista):
    if v == menor:
        print(f'{p}... ', end='')