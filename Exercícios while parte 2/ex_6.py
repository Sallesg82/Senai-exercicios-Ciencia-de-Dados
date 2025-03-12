# Exercício 6

# Solicite ao usuário uma nota entre 0 e 10. 
# Caso o valor seja inválido, peça novamente até que o usuário informe um valor válido.


num = int(input('Digite um número de 0 a 10: '))

while num > 10 or num < 0:
    print('Número incorreto.')
    num = int(input('Digite um número de 0 a 10: '))

print(f'Seu número é {num}')