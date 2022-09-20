from datetime import date

maioridade = 0
menoridade = 0

for r in range(1,8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: ' .format(r)))
    idade = date.today().year - ano
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1

print('Pelos meus calculos, {} pessoas já atingiram a maioridade.' .format(maioridade))
print('E {} pessoas ainda NÃO já atingiram a maioridade.' .format(menoridade))
