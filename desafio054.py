from datetime import date

lista = []
maioridade = 0
menoridade = 0

for r in range(0,7):
    x = int(input('Digite o ano de nascimento'))
    lista.append(x)


for n in range (0,7):
    ano = lista[n]
    idade = date.today().year - ano
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1

print('Pelos meus calculos, {} pessoas já atingiram a maioridade.' .format(maioridade))
print('E {} pessoas ainda NÃO já atingiram a maioridade.' .format(menoridade))
