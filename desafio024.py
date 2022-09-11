# Mostrar se uma cidade começa com Santo

cidade = str(input('Digite o nome da sua cidade.')).strip()

cidade = cidade.title()

print('O nome na sua cidade começa com "Santo"?')
print('Santo' in cidade[:5])
