lista = []

for r in range(0,5):
    peso = float(input('Digite o peso em kg.'))
    lista.append(peso)

print('O maior peso foi {}.' .format(max(lista)))
print('O menor peso foi {}.' .format(min(lista)))