# Exercício 10

# Apenas aceitar números negativos. 
# O programa deve continuar pedindo um número até o usuário digitar um número positivo.


num = int(input('Digite um número negativo: '))

while num > 0:
    print('número inválido, digite um número negativo')
    num = int(input('Digite um número negativo: '))
print(':)')