# Exercício 7

# Adivinhe o número secreto (de 1 a 10). O usuário deve tentar adivinhar um número até acertar. 
# (Declare um valor e receba outro)

numeroSecreto = 4

resp = int(input("Digite um número de 1 a 10 para ver se você consegue adivinhar um número: "))

while resp != numeroSecreto:
    if resp > 10  or resp < 1:
        print('Ei, é entre 1 a 10!')
        resp = int(input("Digite um número de 1 a 10 para ver se você consegue adivinhar um número: "))
        
    else:
        print('Número incorreto tente novamente.')
        resp = int(input("Digite um número de 1 a 10 para ver se você consegue adivinhar um número: "))
    
print('Parabéns, você conseguiu!')