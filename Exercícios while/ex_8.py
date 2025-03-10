# Eercício 8

# Encontrando o maior número inserido pelo usuário. 
# Peça números ao usuário e, ao digitar 0, exiba o maior número inserido.

maior = 0
numero = int(input("Digite um número (ou 0 para sair): "))

while numero != 0:
    
    if numero > maior:
        maior = numero 
    
    if numero == 0:
        break 
    
    numero = int(input("Digite um número (ou 0 para sair): "))

if maior == 0:
    print("Nenhum número foi inserido.")
else:
    print(f"O maior número inserido foi: {maior}")