# Exercício 5

# Solicite ao usuário números indefinidamente. 
# O programa deve parar quando o usuário digitar um número igual ao anterior. 
# Em seguida, exiba quantos números foram inseridos.


while True:
    num = int(input("Digte um numero: "))
    num2 = int(input("Digte um numero: "))
    if num == num2:
        print('Os numeros sao iguais')
        break