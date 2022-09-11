frase = ('Curso em vídeo Python')

len(frase)  # comprimento da string

frase.count('o')  # contagem de caracteres específicos

frase.count('o', 0, 13)  # contagem com fatiamento

frase.find('deo')  # achar a posição do texto ou parte dele

frase.replace('Python', 'Android', 1)  # substitui caracteres na string

frase.upper()

frase.lower()

frase.capitalize()  # so o primeiro caracter da string fica maiusculo

frase.title()  # todas as palavras tem a inicial capitalizada

frase.strip()  # tira espaços excedentes, usado para formularios quando se coloca espaço por engano

frase.rstrip()  # tira espaços do lado direito

frase.lstrip()  # tira espaços do lado esquerdo

frase.split()  # separa as palavras de uma string em novos itens

Curso-em-video-python.join(frase)

# FATIAMENTO

frase[0:14]  # seleciona um intervalo de caracteres

frase[0:14:2]  # intervalo + quantidade de caracteres a saltar

frase[9::3]  # A partir do 9 até o final + quantidade de caracteres a saltar
