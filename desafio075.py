# ler 4 valores, colocar em tupla, quantas vezes aparece 9, a primeira posiçao do 3 e quais foram os numeros pares
sequencia = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')), int(input('Digite mais um numero: ')), int(input('Digite o ultimo numero: ')))
countpares = 0
for c in sequencia:
    if c % 2 == 0:
        countpares += 1

print('Você digitou os valores', sequencia)
print(f'O valor 9 apareceu {sequencia.count(9)} vez(es).')
if 3 in sequencia:
    print(f'O valor 3 apareceu na {sequencia.index(3) + 1}ª posição.')
else:
    print('Não foram digitados valores "3".')
print (f'Os valores pares digitados foram iguais a {countpares}.')
