salario = float(input('Informe seu salário.'))

if salario >= 1250:
    print('Seu salário terá um aumento de 10%. Seu novo salário será R${:.2f}' .format(salario+(salario*0.1)))
else:
    print('Seu salário terá um aumento de 15%. Seu novo salário será R${:.2f}' .format(salario+(salario*0.15)))

print('--Fim do Programa--')
