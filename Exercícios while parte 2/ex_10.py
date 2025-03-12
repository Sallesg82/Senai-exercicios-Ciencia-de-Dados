# Exercício 10

# Implemente um sistema de votação onde o usuário pode votar em candidatos (1 a 4), nulo (5) ou branco (6). 
# O programa deve exibir o total de votos de cada tipo e a porcentagem de votos nulos e brancos. 
# A entrada 0 encerra a votação.


podpah = 1
flowpodcast = 2
inteigenciaLimitada = 3
monarkTalks = 4

nulo = 5
branco = 6

votoa = 0
votob = 0
votoc = 0
votod = 0

nulo_votos = 0
branco_votos = 0

total_votos = 0

print('Vote aqui num podcast para a presidência: ')
print('Podpah = 1, Flowpodcast = 2, Inteligência Limitada = 3, Monark Talks = 4')
print('Caso queira votar nulo, vote 5, caso queira votar branco, vote 6.')

while True:
    voto = int(input("Digite seu voto: "))

    match voto:
        case 1:
            votoa += 1
            print(f'Seu voto foi ao: Podpah')
        case 2:
            votob += 1
            print(f'Seu voto foi ao: Flowpodcast')
        case 3:
            votoc += 1
            print(f'Seu voto foi ao: Inteligencia Limitada')
        case 4:
            votod += 1
            print(f'Seu voto foi ao: Monark Talks')
        case 5:
            nulo_votos += 1
            print("Voto anulado.")
        case 6:
            branco_votos += 1
            print("Voto em branco registrado.")
        case 0:
            print("Votação encerrada.")
            break
        case _:
            print("Voto inválido, foi anulado.")
            nulo_votos += 1

    total_votos += 1

print("--- RESULTADO DA VOTAÇÃO ---")
        
print(f'Podpah teve {votoa} votos.')
print(f'FlowPodcast teve {votob} votos.')
print(f'Inteligência Limitada teve {votoc} votos.')
print(f'Monark Talks teve {votod} votos.')

print(f"Votos nulos: {nulo_votos} votos")
print(f"Votos brancos: {branco_votos} votos")


vencedor = ""
maior_voto = 0

match True:
    case _ if votoa > maior_voto:
        maior_voto = votoa
        vencedor = "Podpah"
    case _ if votob > maior_voto:
        maior_voto = votob
        vencedor = "Flow Podcast"
    case _ if votoc > maior_voto:
        maior_voto = votoc
        vencedor = "Inteligência Limitada"
    case _ if votod > maior_voto:
        maior_voto = votod
        vencedor = "Monark Talks"

print(f"O vencedor da eleição foi: {vencedor}!")
