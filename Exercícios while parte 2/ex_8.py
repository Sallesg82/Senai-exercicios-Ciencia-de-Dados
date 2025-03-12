# Exercício 8

# Implemente um sistema de caixa registradora onde o usuário insere valores dos produtos. 
# A entrada de 0 indica o fim da compra. Exiba o total da compra, peça o valor pago e exiba o troco. 
# Após isso, o programa deve reiniciar para um novo cliente.


while True:
    total = 0
    
    while True:
        valor = float(input("coloque o valor do produto (ou 0 para finalizar a compra): "))
        
        if valor == 0:
            break
        
        
        elif valor < 0:
            print("Valor inválido.")
        else:
            total += valor
            print(f"Produto adicionado: R$ {valor}")

    print(f"Total da compra: R$ {total}")
    
    while True:
        valor_pago = float(input("Digite o valor pago pelo cliente: "))
        
        if valor_pago < total:
            print("Valor pago insuficiente. Por favor, insira um valor maior ou igual ao total da compra.")
        else:
            troco = valor_pago - total
            print(f"Troco a ser devolvido: R$ {troco}")
            break

 
    novo_cliente = input("Deseja continuar? (s/n): ").strip().lower()
    
    if novo_cliente != 'n':
        print("Sistema encerrado. Obrigado!")
        break
