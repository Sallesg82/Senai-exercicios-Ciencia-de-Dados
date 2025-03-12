# Exercício 4

#Solicite ao usuário que insira números. 
# O programa deve continuar até que um número negativo seja inserido. 
# No final, exiba o maior número informado.


num = int(input("Insira um número (Digite um número negativo para cancelar): "))

if num < 0:
    print("Nenhum número válido foi inserido.")

else:
    maior = num

    while True:
        num = int(input("Insira um número (Digite um número negativo para cancelar): "))

        if num < 0:
            break 

        if num > maior:
            maior = num

    print(f"O maior número informado foi: {maior}")