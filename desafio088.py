import random
n = int(input('Quantos jogos você quer gerar? '))
apostas = []
print('-=' *5, f'SORTEANDO {n} JOGOS', '=-' * 5)
for r in range(0,n):
    palpites = random.sample(range(1,61), 6)
    apostas.append(palpites[:])
    print(f'Jogo {r+1}: ', palpites)
print('-=' *7, 'BOA SORTE', '=-' * 7)