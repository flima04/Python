s = 0
lista = []

for r in range(1,7):
    n = int(input('Digite o {} valor: ' .format(r)))
    lista.append(n)
    if n % 2 == 0:
        s += n 

print('A soma dos numeros pares da sequencia {} é igual a {}.' .format(lista, s))