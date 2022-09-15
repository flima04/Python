import random

lista = ['pedra', 'papel', 'tesoura']
print('-='*10)
print('VAMOS JOGAR JOKENPÔ?')
print('-='*10)

jogador = str(input('Você escolhe Pedra, Papel ou Tesoura?')).lower()
pc = random.choice(lista)

if pc == 'pedra' and jogador == 'papel':
    print('Eu escolhi Pedra, mas Papel embrulha Pedra. Você venceu!')
elif pc == 'pedra' and jogador == 'tesoura':
    print('Eu escolhi Pedra, e Pedra esmaga Tesoura. Eu venci!')
elif pc == 'papel' and jogador == 'pedra':
    print('Eu escolhi Papel, e Papel embrulha Pedra. Eu venci!')
elif pc == 'papel' and jogador == 'tesoura':
    print('Eu escolhi Papel, e Tesoura corta Papel. Você venceu!')
elif pc == 'tesoura' and jogador == 'pedra':
    print('Eu escolhi Tesoura, e Pedra esmaga Tesoura. Você venceu!')
elif pc == 'tesoura' and jogador == 'papel':
    print('Eu escolhi Tesoura, e Tesoura corta Papel. Eu Venci!')
