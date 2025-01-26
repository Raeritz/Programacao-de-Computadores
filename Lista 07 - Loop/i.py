# Ler o número de jogos
n = int(input())

# Inicializar o contador de vitórias
vitorias = 0

# Processar cada jogo
for x in range(n):
    carro = int(input())
    
    # O jogador sempre escolhe a porta 1 e sempre troca
    # Verificar se o carro está atrás da porta que sobra após a troca
    if carro != 1:
        # Se o carro está na porta 2 ou 3, a troca resulta em vitória
        vitorias += 1

# Imprimir o total de vitórias
print(vitorias)


n = int(input())
vitorias = 0

# Processar cada jogo
for x in range(n):
    carro = int(input())
    if carro != 1:
        vitorias += 1
print(vitorias)