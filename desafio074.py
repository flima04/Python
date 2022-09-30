# gerar 5 valores aleatorios e colocar numa tupla, mostrar a listagem, indicar o menor e o maior
from random import randint

sequencia = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram:', sequencia)
print('O menor valor foi ', min(sequencia))
print('O maior valor foi ', max(sequencia))
