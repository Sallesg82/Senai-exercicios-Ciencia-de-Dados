# 4. Escreva um programa que leia um número inteiro positivo e determine se ele é um número
# perfeito. Um número perfeito é aquele cuja soma dos seus divisores próprios (excluindo ele
# mesmo) é igual ao próprio número.

# Exemplo:


# Entrada: 28

# Cálculo: 1 + 2 + 4 + 7 + 14 = 28

# Saída: 28 é um número perfeito


while True:
    num = int(input('Digite um número positivo: '))
    if num < 0:
        print('Número Inválido')
    else:
        break
    
soma = 0

for perfeito in range(1, num):
    if num % perfeito == 0:
        soma += perfeito
    
    
if soma == num:
    print('O número é perfeito')
else:
    print('O número não é perfeito')