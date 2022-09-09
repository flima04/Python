import random

aluno1 = input('Digite o nome do aluno 1')
aluno2 = input('Digite o nome do aluno 2')
aluno3 = input('Digite o nome do aluno 3')
aluno4 = input('Digite o nome do aluno 4')

list = [aluno1, aluno2, aluno3, aluno4] #para listas usa-se colchetes ao inves de parênteses!!!

random.shuffle(list)

print('A ordem dos alunos será:')
print(list)
