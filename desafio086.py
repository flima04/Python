linha0 = []
linha1 = []
linha2 = []

for r in range(0,3):
    linha0.append(int(input(f'Digite um número para [0,{r}]: ')))
for r in range(0,3):
    linha1.append(int(input(f'Digite um número para [1,{r}]: ')))
for r in range(0,3):
    linha2.append(int(input(f'Digite um número para [2,{r}]: ')))
print('-=' *30)
print(f'[ {linha0[0]} ] [ {linha0[1]} ] [ {linha0[2]} ]')
print(f'[ {linha1[0]} ] [ {linha1[1]} ] [ {linha1[2]} ]')
print(f'[ {linha2[0]} ] [ {linha2[1]} ] [ {linha2[2]} ]')
