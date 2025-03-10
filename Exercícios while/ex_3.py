# Exercício 3

# Somar números até o usuário digitar 0. Peça números ao usuário e some-os até que ele digite 0.

soma = 0

num = float(input('Digite um número para somar (digite 0 para cancelar): '))

while num != 0:
  soma += num
  num = float(input('Digite um número para somar (digite 0 para cancelar): '))
  

print('Cancelado!')
print(f'A sua soma foi: {soma}')