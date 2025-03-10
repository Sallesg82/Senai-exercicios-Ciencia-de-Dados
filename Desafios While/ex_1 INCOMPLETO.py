#1. Escreva um programa que leia um número N e imprima todos os termos da sequência de
#Fibonacci até que o maior termo seja menor ou igual a N.

#Exemplo:
     
#Entrada: 20

#Saída: 0 1 1 2 3 5 8 13

num = int(input('Digite um número: '))
num1 = 0
num2 = 1

proxNum = num2  
contador = 1

while contador <= num:
    print(proxNum)
    contador += 1
    num1, num2 = num2, proxNum
    proxNum = num1 + num2
    if proxNum > num:
        break
print()

#VOLTE AQUI