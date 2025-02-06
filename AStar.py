import heapq

# Define uma classe No para representar os nós do labirinto
class No:
    def __init__(self, x, y, pai=None):
        self.x = x
        self.y = y
        self.pai = pai
        self.g = 0  # Custo real g(n)
        self.h = 0  # Heurística h(n)
    
    def __lt__(self, outro):
        # Comparação para heapq (baseada no custo total f(n) = g(n) + h(n))
        return (self.g + self.h) < (outro.g + outro.h)

# Função de heurística (distância de Manhattan)
def calcular_heuristica(no, objetivo):
    return abs(no.x - objetivo.x) + abs(no.y - objetivo.y)

# Função para encontrar o caminho usando o algoritmo A*
def encontrar_caminho(labirinto, origem, destino):
    linhas, colunas = len(labirinto), len(labirinto[0])
    lista_aberta = []
    heapq.heapify(lista_aberta)
    lista_fechada = set()

    # Inicializa o nó de origem
    no_origem = No(origem[0], origem[1])
    no_destino = No(destino[0], destino[1])
    heapq.heappush(lista_aberta, no_origem)

    while lista_aberta:
        # Seleciona o nó com o menor valor de f(n)
        no_atual = heapq.heappop(lista_aberta)

        # Verifica se chegou ao destino
        if (no_atual.x, no_atual.y) == (no_destino.x, no_destino.y):
            # Reconstrói o caminho
            caminho = []
            custo_total = 0
            while no_atual:
                caminho.append((no_atual.x, no_atual.y))
                no_atual = no_atual.pai
                custo_total += 1

            # Crie uma matriz de resultado com o caminho
            matriz_resultado = [list(linha) for linha in labirinto]
            for x, y in caminho:
                if matriz_resultado[x][y] not in ('P', 'D'):
                    matriz_resultado[x][y] = '.'

            # Imprima a matriz de resultado
            for linha in matriz_resultado:
                print(' '.join(linha))
            
            print(f"Custo Total do Caminho: {(custo_total) -1}")
            return caminho[::-1]
        
        # Gera os vizinhos
        vizinhos = [(no_atual.x - 1, no_atual.y), (no_atual.x + 1, no_atual.y),
                    (no_atual.x, no_atual.y - 1), (no_atual.x, no_atual.y + 1)]
        
        for (nx, ny) in vizinhos:
            if 0 <= nx < linhas and 0 <= ny < colunas and labirinto[nx][ny] != '0' and (nx, ny) not in lista_fechada:
                novo_no = No(nx, ny, no_atual)
                novo_no.g = no_atual.g + 1  # Custo uniforme de movimento
                novo_no.h = calcular_heuristica(novo_no, no_destino)
                heapq.heappush(lista_aberta, novo_no)
                lista_fechada.add((nx, ny))
    
    print("Caminho não encontrado.")
    return None  # Caminho não encontrado

# Matriz do Primeiro labirinto
 
labirinto = [
    ['1', '0', '1', '0', '1'],
    ['0', '1', '1', '1', '1'],
    ['1', '0', '1', '0', '1'],
    ['0', '1', '1', '1', '1'],
    ['P', '1', '0', '1', 'D']
]

# Matriz do Segundo labirinto

labirinto2 = [
    ['P', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
    ['1', '0', '1', '1', '1', '0', '1', '1', '1', '0'],
    ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
    ['1', '1', '1', '1', '1', '0', '1', '0', '1', '0'],
    ['1', '0', '0', '1', '0', '1', '1', '1', '1', '0'],
    ['1', '0', '1', '1', '1', '0', '1', '0', '1', '0'],
    ['1', '0', '1', '0', '1', '1', '1', '0', '1', '0'],
    ['1', '1', '1', '1', '1', '0', '1', '0', '1', '0'],
    ['1', '0', '0', '1', '1', '0', '1', '1', '1', '0'],
    ['1', '0', '1', '1', '1', '0', '0', '0', '1', 'D']
]

# Primeiro labirinto

# Encontre as coordenadas do nó de partida ('P') e do nó de destino ('D')
for linha in range(len(labirinto)):
    for coluna in range(len(labirinto[linha])):
        if labirinto[linha][coluna] == 'P':
            origem = (linha, coluna)
        elif labirinto[linha][coluna] == 'D':
            destino = (linha, coluna)

# Encontre o caminho e imprima a matriz com o caminho
print('\nNo primeoro labirinto:')

caminho = encontrar_caminho(labirinto, origem, destino)

print("\nCaminho percorrido no primeiro labirinto é:")
print(caminho)


# Segundo labirinto


for linha in range(len(labirinto2)):
    for coluna in range(len(labirinto2[linha])):
        if labirinto2[linha][coluna] == 'P':
            origem = (linha, coluna)
        elif labirinto2[linha][coluna] == 'D':
            destino = (linha, coluna)

print("\nNo segundo labirinto:")

caminho2 = encontrar_caminho(labirinto2, origem, destino)

print("\nCaminho percorrido no segundo labirinto é:")
print(caminho2)