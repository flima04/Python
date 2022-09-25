maisde1000 = total = 0
maisbaratopreço = 0
maisbaratonome = ''

while True:
    nome = str(input('Digite o nome do produto: ')).strip().upper()
    preço = float(input('Digite o valor do produto'))
    total += preço
    if maisbaratopreço == 0:
        maisbaratonome = nome
        maisbaratopreço = preço
    if maisbaratopreço > preço:
        maisbaratonome = nome
        maisbaratopreço = preço
    if preço >= 1000:
        maisde1000 += 1
    resposta = str(input('Deseja continuar (S ou N)?')).upper().strip()[0]
    if resposta == 'N':
        break

print(f'O total das compras é igual a R${total:.2f}, o produto mais barato é {maisbaratonome} e {maisde1000} produtos custam mais de R$1000,00 reais')
    
