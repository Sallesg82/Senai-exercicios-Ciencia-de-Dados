# Exercício 1 

# Solicite ao usuário um número inteiro positivo e exiba apenas os números pares de 2 até esse número.


num = int(input('Digite um número positivo: '))

if num <= 0:
    print('Número inválido')
else:
    contador = 2  
    while contador <= num:
        print(contador)
        contador += 2 