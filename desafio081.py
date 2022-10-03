lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    opção = str(input('Deseja continuar (S ou N)? ')).strip().upper()[0]
    if opção in 'N':
        break
print('-=' * 40)
print(f'Você digitou {len(lista)} elemento(s).')
lista.sort(reverse=True)
print(f'Os valores em ordem descrecente são {lista}.')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 NÃO faz parte da lista!')
