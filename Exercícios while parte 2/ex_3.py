# Exercício 3

# Peça ao usuário que insira notas (valores numéricos). 
# A entrada deve continuar até que o usuário digite -1. Em seguida, exiba a média das notas.


soma = 0 
quantidade = 0 

while True:
    num = float(input("Digite uma nota (ou -1 para encerrar): ")) 

    
    if num == -1:
        break 

    soma += num 
    quantidade += 1



if quantidade > 0:
    media = soma / quantidade
    print(f"A média das notas é: {media}")
else:
    print("Nenhuma nota foi inserida.")
