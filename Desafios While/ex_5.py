# 5. Escreva um programa que leia um número inteiro positivo e determine se ele é um
# quadrado perfeito (ou seja, se existe um número inteiro x tal que x² = n).

# Exemplo:

# Entrada: 49

# Cálculo: 7 × 7 = 49

# Saída: 49 é um quadrado perfeito


while True:
    num = int(input('Digite um número positivo: '))
    if num < 0:
        print('Número Inválido')
    else:
        break
    
# x ** 2 = num | num = raizquadrada de x
x = num ** 0.5
    
if x**2 == num:
    print('Ele é um quadrado perfeito')
else:
    print('Ele não é um quadrado perfeito')