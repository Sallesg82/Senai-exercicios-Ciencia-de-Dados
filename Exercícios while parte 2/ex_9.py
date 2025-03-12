# Exercício 9

# Implemente um sistema onde o usuário insere o código e a quantidade dos produtos desejados. 
# O programa deve calcular o valor total e permitir que o usuário finalize o pedido digitando 0.

total = 0


print("Opções de filmes disponíveis:")
print("1 - Duna 2 (COMPRE SE NÃO ASSISTIU AINDA, E SE ASSISTIU, ASSISTA DE NOVO), preço: 50,00")
print("2 - Emilia Pêraz (mesmo sendo 50 centavos, ainda está caro), preço: 0,50")
print("3 - Ainda Estou Aqui (Absolute Cinema), preço: 45,00")
print("Digite 0 quando quiser finalizar o pedido.")

while True:
    codigo = int(input("Insira o código do filme: "))
    
    if codigo == 0:
        break

    match codigo:
        case 1:
            nome = "Duna 2 (LISAN AL-GAIB)"
            print('Digite a quantidade')
            preco = 50.00
        case 2:
            nome = "Emilia Pêraz (Fuja desse filme)"
            print('Digite a quantidade')
            preco = 0.50
        case 3:
            nome = "Ainda Estou Aqui (Absolute Cinema)"
            print('Digite a quantidade')
            preco = 45.00
        case _:
            print("Código inválido! Tente novamente.")
            continue

    quantidade = int(input(f'Digite a quantidade de ingressos para "{nome}": '))
    if quantidade > 0:
        subtotal = preco * quantidade
        
        total += subtotal
        print(f'A quantidade de {quantidade} ingressos para "{nome}" foi adicionada ao pedido.')
    
    else:
        print("Quantidade inválida. Tente novamente.")

print(f'O total do pedido é de R$ {total}')
print('Obrigado por sua compra!')