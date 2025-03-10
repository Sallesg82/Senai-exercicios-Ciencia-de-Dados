# Exercício 9

# Contar quantos números pares o usuário digitar. 
# O programa deve contar quantos números pares o usuário inseriu. O usuário para digitando -1.

pares = 0
numero = int(input("Digite um número (ou -1 para sair): "))

while numero != -1:
    
    if numero % 2 == 0:
        pares += 1
        
    if numero == -1:
        break
        
    numero = int(input("Digite um número (ou -1 para sair): "))

print(f"Quantidade de números pares adicinados: {pares}")
