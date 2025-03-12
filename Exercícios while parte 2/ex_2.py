# Exercício 2

# Solicite ao usuário que insira uma senha e 
# continue pedindo até que ele insira a senha correta definida previamente.


senha = '1234'

aa = input('Digite a sua senha: ')

while aa != senha:
    print('Senha incorreta')
    aa = input('Digite a senha novamente: ')

print('Bem-vindo!')