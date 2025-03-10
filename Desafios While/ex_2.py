# 2. Escreva um programa que leia um número inteiro positivo e determine se ele é um
# palíndromo (ou seja, se lido de trás para frente continua igual).

# Exemplo:

# Entrada: 1221

# Saída: 1221 é um número palíndromo

while True:
    num = int(input('Digite um número positivo: '))
    if num < 0:
        print('Número Inválido')
    else:
        break

mun = str(num)[::-1]

if str(num) == mun:
    print('É um número palíndromo')
else:
    print('Não é um número palíndromo')