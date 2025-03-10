# Exercício 4

# O usuário deve digitar a senha correta (1234). Enquanto errar, o programa deve pedir novamente.

senha = 1423

verificador = int(input('Digite sua senha: '))

while verificador != senha:
    print('Senha incorreta! tente novamente.')
    verificador = int(input('Digite sua senha: '))
    
print('Senha correta! Bem-vindo.')